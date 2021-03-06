---
slug: "update-on-search-resolver-api-response"
title: "Update on search-resolver@0.x API response"
createdAt: 2022-01-14T19:33:53.734Z
hidden: true
type: "improved"
---

For stores using `search-resolver@0.x`  and the native search,  [VTEX Search GraphQL](https://github.com/vtex-apps/search-graphql) attribute `AvailableQuantity`  will not return the exact quantity of products anymore. Instead, it will return binary results with `0` for products without stock and `10000` for products with stock.
[block:callout]
{
  "type": "warning",
  "body": "This update does not apply to customers using the `search-resolver@1.x`."
}
[/block]
## Response before the update
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f62b7f6-Screenshot_1.png",
        "Screenshot_1.png",
        1136,
        724,
        "#f1f0f2"
      ],
      "caption": ""
    }
  ]
}
[/block]
## Response after the update
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/dd1a88b-Screenshot_3.png",
        "Screenshot_3.png",
        1155,
        828,
        "#f1f1f2"
      ],
      "caption": ""
    }
  ]
}
[/block]