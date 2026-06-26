---
title: "Using payment policies"
slug: "using-payment-policies"
hidden: false
createdAt: "2026-06-08T00:00:00.000Z"
updatedAt: "2026-06-08T00:00:00.000Z"
excerpt: "Create and test payment policies to control payment method eligibility by item collection and delivery state."
---

Payment policies allow merchants to control which payment methods are available in Checkout based on purchase context, such as item collection and shipping state. They complement payment conditions: conditions define how a payment method is configured, including installments, interest, and affiliation, while policies define whether a configured payment method is displayed for each cart item.

> ⚠️ This feature is in closed beta, meaning only specific customers can access it now. If you want to implement it in the future, contact [our Support](https://support.vtex.com/hc/en-us/).

> ℹ️ VTEX is developing a Payment Policies version with support for agents or LLM models and additional purchase context variables. In the current version, use the API and the `collectionIds` and `shippingState` variables described in this guide.

## Before you begin

Make sure you have:

- A VTEX account enabled for payment policies. Contact [VTEX Support](https://support.vtex.com/hc/en-us/) or your VTEX representative to request enablement.
- API credentials with the required [permissions](https://help.vtex.com/docs/tutorials/license-manager-resources):
  - `ManageStore` to create, update, disable, and delete policy rules.
  - `ViewPayments` to list policy rules and test payment system availability.
- Numeric IDs of the payment systems you want to manage. You can retrieve them with `GET https://{accountName}.vtexpayments.com.br/api/pvt/payment-systems`.
- Catalog collections created and associated with the SKUs that should be affected by the policies.

## How payment policies work

Each policy rule has a JSONLogic expression, an action, a priority, and a list of payment systems. When Checkout evaluates the cart, the rule is evaluated for each item separately.

Available context variables:

| Variable        | Type              | Description                                                |
| --------------- | ----------------- | ---------------------------------------------------------- |
| `collectionIds` | Array of integers | Collections that the item belongs to.      |
| `shippingState` | String            | Delivery state code, such as `NY` or `CA`. |

Available actions:

| Action    | Behavior                                                                |
| --------- | ----------------------------------------------------------------------- |
| `Exclude` | Removes the listed payment systems from matching items. |
| `Include` | Restricts matching items to the listed payment systems. |

Rules are evaluated in priority order. Lower `priority` values have higher precedence. If an `Include` rule and an `Exclude` rule have the same priority for the same payment system, `Exclude` takes precedence.

Payment systems not mentioned in any policy rule are always returned. Payment systems mentioned in a rule are returned normally when the rule condition is not met.

## API reference

For endpoint contracts, base URLs, request parameters, and response schemas, see the [Payment Policies API reference](https://github.com/vtex/openapi-schemas/blob/ed57245faeabbc5351666be92eb6e8e8c1929e66/VTEX%20-%20Payment%20Policies%20API.json).

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
        { "==": [{ "var": "shippingState" }, "NY"] }
      ]
    },
    "enabled": true,
    "priority": 90,
    "action": "Exclude",
    "paymentSystems": [2]
  }'
```

Rule fields:

| Field            | Type              | Description                                                                                                   |
| ---------------- | ----------------- | ------------------------------------------------------------------------------------------------------------- |
| `name`           | String            | Rule name used to identify the policy.                                                        |
| `expression`     | Object            | JSONLogic condition. The rule fires when this expression evaluates to `true`. |
| `enabled`        | Boolean           | Whether the rule is active. Disabled rules are ignored.                       |
| `priority`       | Integer           | Rule priority from `0` to `999`. Lower values have higher precedence.         |
| `action`         | String            | `Exclude` or `Include`.                                                                       |
| `paymentSystems` | Array of integers | Payment system IDs affected by the rule.                                                      |

The `expression` field is validated when the rule is saved. Each expression can have up to 500 operators.

## Step 3 - Manage policy rules

Use the following endpoints to manage policy rules:

| Operation             | Endpoint                                              |
| --------------------- | ----------------------------------------------------- |
| Create rule           | `POST {baseUrl}/policy-rules?an={accountName}`        |
| List rules            | `GET {baseUrl}/policy-rules?an={accountName}`         |
| Get rule by ID        | `GET {baseUrl}/policy-rules/{id}?an={accountName}`    |
| Replace rule          | `PUT {baseUrl}/policy-rules/{id}?an={accountName}`    |
| Partially update rule | `PATCH {baseUrl}/policy-rules/{id}?an={accountName}`  |
| Delete rule           | `DELETE {baseUrl}/policy-rules/{id}?an={accountName}` |

To disable a rule without deleting it, send a partial update:

```bash
curl --request PATCH \
  --url "https://pcs.vtexcommercestable.com.br/api/payment-configuration-service/policy-rules/{id}?an={accountName}" \
  --header "Content-Type: application/json" \
  --header "X-VTEX-API-AppKey: {appKey}" \
  --header "X-VTEX-API-AppToken: {appToken}" \
  --data '{
    "enabled": false
  }'
```

## Step 4 - Test the policy with the search endpoint

Use the search endpoint to validate policy behavior before testing the full Checkout flow. The request receives item context and returns payment system assignments by item.

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
  "paymentSystemAssignments": [
    {
      "paymentSystem": 1,
      "itemIds": ["sku-01"]
    },
    {
      "paymentSystem": 4,
      "itemIds": ["sku-01"]
    }
  ]
}
```

In this example, payment system `2` must not appear in `paymentSystemAssignments` for `sku-01`, because the item belongs to collection `139` and the delivery state is `NY`.

## Step 5 - Validate the policy in Checkout

After validating the rule with the search endpoint, test the behavior in Checkout:

1. Create a cart with [Get current or create a new cart](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/orderForm) endpoint.
2. Add an item from the collection configured in the policy rule.
3. Add a delivery address with the state configured in the policy rule.
4. Inspect `paymentData.availableAssociations` in the `orderForm` response.

Example:

```json
{
  "paymentData": {
    "availableAssociations": {
      "2": ["sku-002"],
      "4": ["sku-001", "sku-002"]
    }
  }
}
```

In this example, payment system `2` is available for `sku-002`, but not for `sku-001`. This means the policy filtered payment system `2` only for the item that matched the rule.

During payment authorization, VTEX revalidates whether the selected payment system complies with active policies. If a buyer or integration attempts to use a payment system that isn't allowed by an active policy, the authorization is rejected.

## Test scenarios

Use the following scenarios to validate a policy setup:

| Scenario                                                                                                | Expected result                                                                   |
| ------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Item belongs to the configured collection and delivery state matches the policy.        | The excluded payment system is absent for that item.              |
| Item doesn't belong to the configured collection and delivery state matches the policy. | The rule doesn't fire and the payment system remains available.   |
| Item belongs to the configured collection and delivery state doesn't match the policy.  | The rule doesn't fire and the payment system remains available.   |
| Cart has two items, one matching the policy and one not matching it.                    | The payment system is filtered only for the matching item.        |
| Matching `Include` rule.                                                                | Only the listed payment systems are available for matching items. |
| Matching `Include` and `Exclude` rules with different priorities.                       | The rule with the lower priority value takes precedence.          |
| Two matching `Exclude` rules for the same item.                                         | Both exclusions apply.                                            |
| Rule has `enabled` set to `false`.                                                      | The rule is ignored.                                              |

## Troubleshooting

| Symptom                                                                                        | Likely cause                                                                                                               | What to check                                                                                                          |
| ---------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Policy rules were created, but Checkout is not filtering payment systems.      | The feature isn't enabled for the account.                                                                 | Confirm the account enablement with VTEX Support or your VTEX representative.                          |
| `POST /policy-rules` returns `401` or `403`.                                   | API credentials do not have `ManageStore`.                                                                 | Review the permissions assigned to the app key and app token.                                          |
| `GET /policy-rules` or `POST /search` returns `401` or `403`.                  | API credentials do not have `ViewPayments`.                                                                | Review the permissions assigned to the app key and app token.                                          |
| The rule was created, but the search result did not change.                    | The rule is disabled, the expression doesn't match the test item, or the wrong payment system ID was used. | Check `enabled`, `collectionIds`, `shippingState`, and `paymentSystems` with `GET /policy-rules/{id}`. |
| The expression is rejected with `400`.                                         | Invalid JSONLogic syntax or too many operators.                                                            | Validate the JSONLogic object and keep the expression under 500 operators.                             |
| The search endpoint returns the expected result, but the `orderForm` does not. | Checkout isn't using the payment policies contract for the account.                                        | Confirm the account enablement and test with a fresh `orderForm`.                                      |
