---
title: "Access Control List"
slug: "access-control-list"
hidden: false
createdAt: "2022-01-24T14:17:40.173Z"
updatedAt: "2024-02-23T07:19:43.562Z"
---

By default, all VTEX stores are configured to display all available products during every navigation session. The Access Control List feature allows you to create a list of users that can or cannot access specific products in the store.

## Creating a specification

To configure the Access Control List, you must first create one of the following product specifications either through [Catalog API](https://developers.vtex.com/docs/guides/product-specifications) or on [VTEX Admin](https://help.vtex.com/en/tutorial/adding-specifications-or-product-fields--tutorials_106) and set their values, which represent groups of customers that can be set on Master Data. All values for both specifications must be separated by `;` (i.e.: `1;2;3`).

| Specification name | Example values | Description |
|-|-|-|
|`_blocklist`| `1;2;3` | Blocklist: Restricts product visibility based on the defined navigation values. |
|`_allowlist` | `1;2;3` | Allowlist: Enables product visibility based on the defined navigation values. |

>⚠️ Do not set both specifications at the same time for the same product, otherwise the product will not be displayed in any scenario. Read [Behavior](#behavior) for more information.

After creating the product specification, Intelligent Search automatically triggers a reindexing process to update the values in the search database.

## Defining segmented navigation

To define segmented navigation, you must configure the `accesscontrollist` facet on the [`vtex-segment`](https://developers.vtex.com/docs/guides/vtex-io-documentation-segmenting-the-search-result) app. For example, `acesscontrollist:1` can define navigation for a customer, where a certain product will not be displayed in the search results.

```graphql
query {
  productSearch(
      selectedFacets: [
        {key: "trade-policy", value: "1"},
        {key: "accesscontrollist", value: "1"}
        ]
    )
  {
    products {
      productId,
      productName
    }
  }
}
```

### Behavior

Wherever the `accesscontrollist` facet is present, `_blocklist` and `_allowlist` can be applied to each product and result in one of the following scenarios:

| `_blocklist` | `_allowlist` | Result |
|-|-|-|
| Empty value or nonexistent specification | Empty value or nonexistent specification | The product will always be visible. |
| Defined value | Empty value or nonexistent specification | The product will be visible unless the `accesscontrollist` value is included in `_blocklist`. |
| Empty value or nonexistent specification | Defined value | The product will be visible only if the `accesscontrollist` value is included in `_allowlist`. |
| Defined value | Defined value | The product will not be visible to anyone. This is an invalid scenario. |