---
title: "Using payment policies"
slug: "using-payment-policies"
hidden: false
createdAt: "2026-07-07T00:00:00.000Z"
updatedAt: "2026-11-12T00:00:00.000Z"
excerpt: "Create and test payment policies to control payment method eligibility by item collection and delivery state."
---

> ⚠️ This feature is in closed beta, meaning only specific customers can access it now. If you want to implement it in the future, contact [our Support](https://support.vtex.com/hc/en-us/).

Payment policies allow merchants to control which payment methods are available in Checkout based on purchase context, such as item collection and shipping state. They complement payment conditions: conditions define how a payment method is configured, including installments, interest, and affiliation, while policies define whether a configured payment method is displayed for each cart item.

> ℹ️ VTEX is developing a Payment Policies version with support for agents or LLM models and additional purchase context variables. In the current version, use the API and the `collectionIds`, `seller`, and `shippingData.state` variables described in this guide.

## Before you begin

Make sure you have:

- A VTEX account enabled for payment policies. Contact [VTEX Support](https://support.vtex.com/hc/en-us/) or your VTEX representative to request enablement.
- Payment connectors configured with the Partial processing mode for [post-purchase payment operations](https://help.vtex.com/docs/tutorials/post-purchase-payment-operations). Payment policies currently work only with this mode. To learn how to request it, see [Partial mode: New flow in post-purchase payment operations](https://help.vtex.com/announcements/2026-07-14-partial-mode-new-flow-in-post-purchase-payment-operations).
- API credentials with the required [permissions](https://help.vtex.com/docs/tutorials/license-manager-resources):
  - `ManageStore` to create, update, and delete policy rules.
  - `ViewPayments` to list policy rules and test payment system availability.
- Numeric IDs of the payment systems you want to manage. You can retrieve them with `GET https://{accountName}.vtexpayments.com.br/api/pvt/payment-systems`.
- Catalog collections created and associated with the SKUs that should be affected by the policies.

## How payment policies work

Each policy rule has a JSONLogic expression, an action, a priority, and a list of payment systems. When Checkout evaluates the cart, the rule is evaluated for each item separately.

### Context variables

| Variable | Type | Description |
| --- | --- | --- |
| `collectionIds` | Array of integers | Collections that the item belongs to. An empty, null, or missing list produces the same result. |
| `seller` | String | Seller that fulfills the item. An empty or whitespace-only value is treated as not sent. |
| `shippingData.state` | String | Delivery state code, such as `NY` or `CA`. An empty or whitespace-only value is treated as not sent. |

> ⚠️ Variable names aren't validated when you save a rule. Any other name, such as `shippingState`, is treated as a missing field. In this case, comparisons using `==` and `in` with that field return `false`, while comparisons using `!=` return `true`. Check the variable names before saving a rule.

### Operators

| Operator | Usage rules |
| --- | --- |
| `and`, `or` | Every operand must be a condition (object). Literal values are rejected. |
| `in` | Requires two operands. Each operand is a value, a list, or `{"var": "path"}`. When the second operand is a list, the type and value must match: `"139"` isn't in `[139]`. |
| `==` | Requires two operands. Each operand is `{"var": "path"}`, a non-empty string other than `"null"`, or an integer. Booleans, decimals, and lists are rejected. A number is equal to the string of the same number: `"1" == 1` is `true`. |
| `!=` | Same rules as `==`. Returns the opposite result. |
| `!` | Negates exactly one condition: `{"!": {...}}` or `{"!": [{...}]}`. Literal values and a standalone `var` are rejected. |
| `var` | Field path as a string. Use a dot to access nested fields, such as `shippingData.state`. Default values aren't supported. |

Any other operator, such as `===`, `!==`, `!!`, `>`, `<`, `>=`, `<=`, `if`, or arithmetic operators, is rejected with status `422`. To request support for other JSONLogic operators, contact [VTEX Support](https://support.vtex.com/hc/en-us/).

There's no `not in` operator. To check that a value isn't in a list, use `{"!": {"in": [...]}}`.

Each expression can have up to 500 operators. The `and`, `or`, `!`, `in`, `==`, and `!=` operators count toward this limit. The `var` operator doesn't count.

### Negation and missing fields

When an item doesn't have a field used by a comparison:

- `in` and `==` return `false`.
- `!=` returns `true`.
- `!` negates the result of its child condition. Negating a missing-field `==` or `in` comparison returns `true`, and negating a missing-field `!=` comparison returns `false`.

This means negated conditions also match items without the field. For example, `{"!": {"in": [{"var": "seller"}, ["seller-a", "seller-b"]]}}` matches items with other sellers and items without a seller. To require the field, combine the condition with `and`: `{"and": [{"var": "seller"}, {"!": {...}}]}`.

Similarly, `{"!": {"in": [139, {"var": "collectionIds"}]}}` matches items outside collection `139` and items without any collection. With an `Exclude` action, a product that isn't assigned to the eligible collection loses the payment system.

### Actions and priority

| Action | Behavior |
| --- | --- |
| `Exclude` | Removes the listed payment systems from matching items. |
| `Include` | Restricts matching items to the listed payment systems. |

All active rules that match an item are applied. Rules are applied in ascending priority order, and the order doesn't change the result. `Exclude` removes payment systems from the allowed set; `Include` only filters what remains and can't restore systems removed by an `Exclude` rule. When both actions match the same item, exclusion therefore prevails over inclusion: the item keeps the payment systems listed in the `Include` rule, minus those listed in the `Exclude` rule.

Disabled rules are ignored. Payment systems not mentioned in any policy rule are always returned. Payment systems mentioned in a rule are returned normally when the rule condition isn't met.

## API reference

For endpoint contracts, base URLs, request parameters, and response schemas, see the [Payment Policies API reference](https://developers.vtex.com/docs/api-reference/payment-policies-api).

The examples below use the stable environment and require the `an` query parameter with the account name.

## Step 1 - Get payment system IDs

Before creating a policy rule, get the numeric IDs of the payment systems configured in your account:

```bash
curl --request GET \
  --url "https://{accountName}.vtexpayments.com.br/api/pvt/payment-systems" \
  --header "X-VTEX-API-AppKey: {appKey}" \
  --header "X-VTEX-API-AppToken: {appToken}"
```

Use these IDs in the `paymentSystems` array when creating policy rules.

## Step 2 - Create a policy rule

The following example excludes payment system `2` for items in collection `139` when the delivery state is `NY`.

```bash
curl --request POST \
  --url "https://pcs.vtexcommercestable.com.br/api/payment-configuration-service/policy-rules?an={accountName}" \
  --header "Content-Type: application/json" \
  --header "X-VTEX-API-AppKey: {appKey}" \
  --header "X-VTEX-API-AppToken: {appToken}" \
  --data '{
    "name": "Exclude payment system 2 for collection 139 in NY",
    "expression": {
      "and": [
        { "in": [139, { "var": "collectionIds" }] },
        { "==": [{ "var": "shippingData.state" }, "NY"] }
      ]
    },
    "enabled": true,
    "priority": 90,
    "action": "Exclude",
    "paymentSystems": [2]
  }'
```

Rule fields:

| Field | Type | Description |
| --- | --- | --- |
| `name` | String | Rule name used to identify the policy. |
| `expression` | Object | JSONLogic condition. The rule fires when this expression evaluates to `true`. |
| `enabled` | Boolean | Whether the rule is active. Disabled rules are ignored. |
| `priority` | Integer | Rule priority from `0` to `999`. Rules are applied in ascending priority order, and the order doesn't change the result. |
| `action` | String | `Exclude` or `Include`. Values are case-sensitive. |
| `paymentSystems` | Array of integers | Payment system IDs affected by the rule. Must contain at least one ID. |

The `expression` field is validated when the rule is saved. Each expression can have up to 500 operators, including `!` and `!=`. Variable names aren't validated, so check them before saving the rule.

## Step 3 - Manage policy rules

Use the following endpoints to manage policy rules:

| Operation | Endpoint |
| --- | --- |
| Create rule | `POST {baseUrl}/policy-rules?an={accountName}` |
| List rules | `GET {baseUrl}/policy-rules?an={accountName}` |
| Get rule by ID | `GET {baseUrl}/policy-rules/{id}?an={accountName}` |
| Replace rule | `PUT {baseUrl}/policy-rules/{id}?an={accountName}` |
| Delete rule | `DELETE {baseUrl}/policy-rules/{id}?an={accountName}` |

To update a rule without deleting it, replace the existing rule with a new version:

```bash
curl --request PUT \
  --url "https://pcs.vtexcommercestable.com.br/api/payment-configuration-service/policy-rules/{id}?an={accountName}" \
  --header "Content-Type: application/json" \
  --header "X-VTEX-API-AppKey: {appKey}" \
  --header "X-VTEX-API-AppToken: {appToken}" \
  --data '{
    "name": "Exclude payment system 5 for collection 139 in NY",
    "expression": {
      "and": [
        { "in": [139, { "var": "collectionIds" }] },
        { "==": [{ "var": "shippingData.state" }, "NY"] }
      ]
    },
    "enabled": true,
    "priority": 90,
    "action": "Exclude",
    "paymentSystems": [5]
  }'
```

## Step 4 - Test the policy with the search endpoint

Use the search endpoint to validate policy behavior before testing the full Checkout flow. Send the cart line items (and optionally `salesChannel` and `paymentSystemIds`) in the request body. Each item accepts `id`, `collectionIds`, `seller`, and `shippingData.state`, and only `id` is required. The response returns, for each item ID, the payment system IDs still allowed after active policy rules are applied (`paymentSystemAssignments`), plus the corresponding payment system metadata (`paymentSystemDefinitions`).

```bash
curl --request POST \
  --url "https://{accountName}.vtexpayments.com.br/api/pvt/payment-systems/search?an={accountName}" \
  --header "Content-Type: application/json" \
  --header "X-VTEX-API-AppKey: {appKey}" \
  --header "X-VTEX-API-AppToken: {appToken}" \
  --data '{
    "items": [
      {
        "id": "sku-01",
        "collectionIds": [139],
        "shippingData": {
          "state": "NY"
        }
      }
    ]
  }'
```

Expected response pattern:

```json
{
  "paymentSystemAssignments": {
    "sku-01": [1, 4]
  },
  "paymentSystemDefinitions": [
    {
      "id": 1,
      "name": "Debit Card",
      "groupName": "debitCard"
    },
    {
      "id": 4,
      "name": "Mastercard",
      "groupName": "creditCard"
    }
  ]
}
```

In this example, payment system `2` must not appear in `paymentSystemAssignments` for `sku-01`, because the item belongs to collection `139` and the delivery state is `NY`.

Consider the following when reading the response:

- Payment system IDs in `paymentSystemAssignments` are sorted in ascending order.
- Items without any allowed payment system don't appear in `paymentSystemAssignments`.
- Items without `id` are ignored.
- `paymentSystemDefinitions` lists only the payment systems that appear in `paymentSystemAssignments`.
- Send one entry per SKU. If the same SKU is sent more than once, the response returns a single entry for it.

## Step 5 - Validate the policy in Checkout

After validating the rule with the search endpoint, test the behavior in Checkout:

1. Create a cart with [Get current or create a new cart](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/orderForm) endpoint.
2. Add an item from the collection configured in the policy rule.
3. Add a delivery address with the state configured in the policy rule.
4. Inspect `paymentData.availableAssociations` in the `orderForm` response.

In the `availableAssociations` object, each key is a cart item (SKU) ID, and each value lists the IDs of the payment systems allowed for that item.

Example:

```json
{
  "paymentData": {
    "availableAssociations": {
      "sku-001": ["4"],
      "sku-002": ["2", "4"]
    }
  }
}
```

In this example, `sku-002` can be paid with payment systems `2` and `4`, while `sku-001` can only be paid with payment system `4`. This means the policy filtered payment system `2` only for the item that matched the rule.

> ℹ️ This field follows the same structure as `paymentSystemAssignments` in the [search endpoint](#step-4---test-the-policy-with-the-search-endpoint) response. The only difference is that payment system IDs are returned as strings in the `orderForm` (for example, `"4"`) and as integers in the search endpoint response (for example, `4`).

During payment authorization, VTEX revalidates whether the selected payment system complies with active policies. If a buyer or integration attempts to use a payment system that isn't allowed by an active policy, the authorization is rejected.

## Rule examples

The following examples show common policy rules.

### Exclude a payment system from items outside an eligible collection

This rule removes payment system `45` from items that aren't in collection `139`, including items without any collection.

```json
{
  "name": "Exclude EBT for non-eligible items",
  "expression": { "!": { "in": [139, { "var": "collectionIds" }] } },
  "enabled": true,
  "priority": 100,
  "action": "Exclude",
  "paymentSystems": [45]
}
```

### Combine collection and delivery state

This expression matches items in collection `139` delivered to `NY`.

```json
{
  "and": [
    { "in": [139, { "var": "collectionIds" }] },
    { "==": [{ "var": "shippingData.state" }, "NY"] }
  ]
}
```

### Match multiple collections

This expression matches items in collection `10` or collection `11`.

```json
{
  "or": [
    { "in": [10, { "var": "collectionIds" }] },
    { "in": [11, { "var": "collectionIds" }] }
  ]
}
```

### Exclude a list of sellers without matching items without a seller

This expression matches items whose seller isn't `seller-a` or `seller-b`. The first condition requires the `seller` field, so items without a seller don't match.

```json
{
  "and": [
    { "var": "seller" },
    { "!": { "in": [{ "var": "seller" }, ["seller-a", "seller-b"]] } }
  ]
}
```

### Best practices

- Use the numeric collection ID. The string `"139"` doesn't match the collection `139`.
- Write lists as arrays, not as comma-separated strings.
- Prefer `Exclude` rules.
- Use `!` with the eligible collection so that items not assigned to the collection lose the payment system.
- Require the field with `and` when a negation shouldn't apply to items without that field.
- Check variable names. An incorrect name is accepted when saving and is treated as a missing field, so `!=` comparisons and negated `==` or `in` comparisons match all items.
- Test the rule with the [search endpoint](#step-4---test-the-policy-with-the-search-endpoint) before relying on it in Checkout.

## Test scenarios

Use the following scenarios to validate a policy setup with the [search endpoint](#step-4---test-the-policy-with-the-search-endpoint): create the rule, send the item, and check `paymentSystemAssignments`. Unless stated otherwise, each rule has `action` set to `Exclude`, `paymentSystems` set to `[2]`, and `enabled` set to `true`.

Expressions used in the scenarios:

| Name | Expression |
| --- | --- |
| R1 | `{"in": [139, {"var": "collectionIds"}]}` |
| R2 | `{"!": {"in": [139, {"var": "collectionIds"}]}}` |
| R3 | `{"!": {"in": [{"var": "seller"}, ["seller-a", "seller-b"]]}}` |
| R4 | `{"and": [{"var": "seller"}, {"!": {"in": [{"var": "seller"}, ["seller-a", "seller-b"]]}}]}` |
| R5 | `{"!=": [{"var": "shippingData.state"}, "TX"]}` |

| Scenario | Rule | Item sent | Expected result |
| --- | --- | --- | --- |
| Item in the collection. | R1 | `"collectionIds": [139]` | Payment system `2` doesn't appear for the item. |
| Item outside the collection. | R1 | `"collectionIds": [12]` | Payment system `2` remains available. |
| Item without a collection. | R1 | No `collectionIds` | Payment system `2` remains available. |
| Collection ID written as a string. | R1 with `"139"` instead of `139` | `"collectionIds": [139]` | Payment system `2` remains available because the rule doesn't apply. |
| Negation, item in the collection. | R2 | `"collectionIds": [139]` | Payment system `2` remains available. |
| Negation, item outside the collection. | R2 | `"collectionIds": [12]` | Payment system `2` doesn't appear for the item. |
| Negation, item without a collection. | R2 | No `collectionIds` | Payment system `2` doesn't appear for the item. |
| Seller in the negated list. | R3 | `"seller": "seller-a"` | Payment system `2` remains available. |
| Seller outside the negated list. | R3 | `"seller": "seller-c"` | Payment system `2` doesn't appear for the item. |
| Item without a seller, simple negation. | R3 | No `seller` | Payment system `2` doesn't appear for the item. |
| Item without a seller, negation that requires the field. | R4 | No `seller` | Payment system `2` remains available. |
| Different delivery state. | R5 | `"shippingData": {"state": "NY"}` | Payment system `2` doesn't appear for the item. |
| Same delivery state. | R5 | `"shippingData": {"state": "TX"}` | Payment system `2` remains available. |
| Item without a delivery state. | R5 | No `shippingData` | Payment system `2` doesn't appear for the item. |
| Two items in the cart. | R1 | `sku-01` with `[139]` and `sku-02` with `[12]` | Payment system `2` is removed only from `sku-01`. |
| Matching `Include` rule. | R1 with `Include` and `[2, 4]` | `"collectionIds": [139]` | Only payment systems `2` and `4` are available for the item. |
| Matching `Include` and `Exclude` rules. | R1 with `Exclude` and `[2]`, and R1 with `Include` and `[2, 4]` | `"collectionIds": [139]` | Only payment system `4` is available for the item, regardless of the priority of each rule. |
| Two matching `Exclude` rules for the same item. | R1 with `[2]` and R1 with `[4]` | `"collectionIds": [139]` | Payment systems `2` and `4` don't appear for the item. |
| Disabled rule. | R1 with `enabled` set to `false` | `"collectionIds": [139]` | Payment system `2` remains available. |
| Incorrect variable name. | `{"!=": [{"var": "shippingState"}, "TX"]}` | Any item | Payment system `2` is removed from all items, including items delivered to `TX`. |

> ℹ️ An item without any allowed payment system doesn't appear in `paymentSystemAssignments`.

## Troubleshooting

| Symptom | Likely cause | What to check |
| --- | --- | --- |
| Policy rules were created, but Checkout is not filtering payment systems. | The feature isn't enabled for the account. | Confirm the account enablement with VTEX Support or your VTEX representative. |
| `POST /policy-rules` returns `401` or `403`. | API credentials do not have `ManageStore`. | Review the permissions assigned to the app key and app token. |
| `GET /policy-rules` or `POST /search` returns `401` or `403`. | API credentials do not have `ViewPayments`. | Review the permissions assigned to the app key and app token. |
| The rule was created, but the search result did not change. | The rule is disabled, the expression doesn't match the test item, or the wrong payment system ID was used. | Check `enabled`, `collectionIds`, `seller`, `shippingData.state`, and `paymentSystems` with `GET /policy-rules/{id}`. |
| A rule never applies, or a rule applies to all items. | The expression uses a variable name that doesn't exist, such as `shippingState`. | Use only `collectionIds`, `seller`, and `shippingData.state`. See [Context variables](#context-variables). |
| The rule is rejected with `400`. | The request body is missing `expression`, `enabled`, `priority`, or `action`, or `action` has a value other than `Include` or `Exclude`. | Send all required fields and use `Include` or `Exclude` with this exact capitalization. |
| The expression is rejected with `422`. | Invalid JSONLogic syntax, an unsupported operator, or more than 500 operators. | Validate the JSONLogic object against the [supported operators](#operators) and keep the expression within 500 operators. See [Error messages](#error-messages). |
| The search endpoint returns the expected result, but the `orderForm` does not. | Checkout isn't using the payment policies contract for the account. | Confirm the account enablement and test with a fresh `orderForm`. |

### Error messages

Policy rule endpoints return errors in the [Problem Details](https://www.rfc-editor.org/info/rfc9457/) format, with the `type`, `title`, `status`, `detail`, and `instance` fields. The following table lists the `detail` values. Errors returned by the expression validator may include additional parameter information at the end of the message.

| Status | When | `detail` |
| --- | --- | --- |
| `400` | The request body is missing `expression`, `enabled`, `priority`, or `action`. Messages for all missing fields are returned together. | `Expression is required. enabled is required. priority is required. action is required.` |
| `400` | `action` has a different capitalization or value. | `action must be Include or Exclude.` |
| `422` | The expression uses an unsupported operator. | `Unsupported expression: JSONLogic operator "!==" is not supported.` |
| `422` | An operator object has more than one key. | `Unsupported expression: operator object must contain exactly one property, found "!=", "foo".` |
| `422` | `==`, `!=`, or `in` doesn't have exactly two operands. | `Unsupported expression: "!=" must have exactly two operands.` |
| `422` | `!` negates a literal value or a standalone `var`. | `Unsupported expression: "!" must negate exactly one condition, not a literal or a bare var.` |
| `422` | `and` or `or` has a literal value as an operand. | `Unsupported expression: every operand of "and" must be a condition, not a literal.` |
| `422` | `==` or `!=` has a boolean or decimal operand. | `Unsupported expression: inside "==", each operand must be {"var":"path"}, a non-empty string other than "null", or an integer.` |
| `422` | `==`, `!=`, or `in` has `null` or `"null"` as an operand. | `Unsupported expression: null is not allowed as a literal inside "==", "!=" or "in", neither as JSON null nor as the string "null".` |
| `422` | `==`, `!=`, or `in` has an empty or whitespace-only string as an operand. | `Unsupported expression: an empty or whitespace string is not allowed as a literal inside "==", "!=" or "in".` |
| `422` | `var` has a default value. | `Unsupported expression: inside "in", {"var": ...} must be a single string path (default values are not supported).` |
| `422` | The expression has more than 500 operators. | `Expression exceeds maximum conditionals (500). Found: 501.` |
| `422` | `priority` is outside the `0` to `999` range. A blank `name` or an empty `paymentSystems` list also returns `422`. | `Priority must be between 0 and 999.` |
| `404` | The rule doesn't exist. | `Policy rule with ID '...' was not found.` |
| `409` | The same rule was updated by concurrent requests. | `Version mismatch; re-read the rule and retry.` |

> ℹ️ The search endpoint returns `400`, `403`, and `408` errors as plain text, not in the Problem Details format.
