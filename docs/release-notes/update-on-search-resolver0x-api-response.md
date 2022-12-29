---
slug: "update-on-search-resolver0x-api-response"
title: "Update on search-resolver@0.x API response"
createdAt: 2022-02-21T17:00:00.000Z
hidden: false
type: "improved"
---

For stores using `search-resolver@0.x`  and the native search, [VTEX Search GraphQL](https://github.com/vtex-apps/search-graphql) attribute `AvailableQuantity`  will not return the exact quantity of products anymore. Instead, this field will always return `null`.

For further information, check our [announcement](https://help.vtex.com/en/announcements/search-resolve-hides-number-product-stock--7Ah6ou3RCoNmMeedZaBeJS).

> ⚠️ This update does not apply to customers using the `search-resolver@1.x`.

## Response before the update

![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/update-on-search-resolver0x-api-response-0.png)

## Response after the update

![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/update-on-search-resolver0x-api-response-1.png)
