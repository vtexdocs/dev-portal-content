---
title: "Associate SubCollection to SKU"
slug: "catalog-api-post-subcollection-sku"
excerpt: "Associates a SubCollection to a single SKU"
hidden: false
createdAt: "2020-04-16T15:43:24.310Z"
updatedAt: "2020-07-02T14:58:51.462Z"
---
## Request object has the following properties:

| Attribute | Type    | Description                 |
| --------- | ------- | --------------------------- |
| SkuId     | integer | Unique identifier of an SKU |

## Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"SkuId\": 7\n}",
      "language": "json"
    }
  ]
}
[/block]
## Response object has the following properties:

| Attribute       | Type    | Description                 |
| --------------- | ------- | --------------------------- |
| SubCollectionId | integer | SubCollection ID            |
| SkuId           | integer | Unique identifier of an SKU |

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"SubCollectionId\": 13,\n    \"SkuId\": 7\n}",
      "language": "json"
    }
  ]
}
[/block]