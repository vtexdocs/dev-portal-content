---
slug: "update-on-search-resolver-api-response"
title: "Update on search-resolver@0.x API response"
createdAt: 2022-01-14T19:33:53.734Z
hidden: true
type: "improved"
---

For stores using `search-resolver@0.x`  and the native search,  [VTEX Search GraphQL](https://github.com/vtex-apps/search-graphql) attribute `AvailableQuantity`  will not return the exact quantity of products anymore. Instead, it will return binary results with `0` for products without stock and `10000` for products with stock.

> ⚠️ This update does not apply to customers using the `search-resolver@1.x`.

## Response before the update

![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/update-on-search-resolver-api-response-0.png)

## Response after the update

![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/update-on-search-resolver-api-response-1.png)
