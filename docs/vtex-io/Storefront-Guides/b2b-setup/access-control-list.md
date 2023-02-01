---
title: "Access Control List"
slug: "access-control-list"
hidden: false
createdAt: "2022-01-24T14:17:40.173Z"
updatedAt: "2022-01-24T14:19:43.562Z"
---
By default, all the stores are configured to show all the products for all navigations. The Access Control List feature allows you to create a list of users that can access specific products on the store.
 
To configure the Access Control List, you must create a product specification on the catalog called `_blocklist` with navigation values separated by `;`(i.e.: `1;2;3`). This specification restricts the product visibility according to these navigation values.

> ℹ️ After creating the product specification, you must reindex the Intelligent Search to update the values on the search database.

To define segmented navigation, you must configure the `accesscontrollist` facet on the [`vtex-segment`](https://developers.vtex.com/docs/guides/vtex-io-documentation-segmenting-the-search-result) app. For example, `acesscontrollist:1` can define navigation for a client, where a certain product will not be displayed in the search result.
 
 
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