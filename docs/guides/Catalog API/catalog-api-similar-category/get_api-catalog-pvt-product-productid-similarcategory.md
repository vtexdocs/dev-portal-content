---
title: "Get Similar Product Category"
slug: "get_api-catalog-pvt-product-productid-similarcategory"
excerpt: "Retrieves Similar Categories from a Product."
hidden: false
createdAt: "2020-12-03T19:43:36.930Z"
updatedAt: "2022-05-20T22:23:43.174Z"
---
## Response body has the following properties:

| Attribute       | Type    | Description     |
| --------------- | ------- | --------------- |
| ProductId | integer | Product ID      |
| CategoryId | integer | Similar Category ID |

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "[\n    {\n        \"ProductId\": 1,\n        \"CategoryId\": 1\n    },\n    {\n        \"ProductId\": 1,\n        \"CategoryId\": 20\n    }\n]",
      "language": "json"
    }
  ]
}
[/block]