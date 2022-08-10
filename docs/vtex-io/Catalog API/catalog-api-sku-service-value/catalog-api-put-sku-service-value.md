---
title: "Update SKU Service Value"
slug: "catalog-api-put-sku-service-value"
excerpt: "Updates an existing SKU Service Value"
hidden: false
createdAt: "2020-06-08T19:47:12.378Z"
updatedAt: "2020-06-19T16:30:37.621Z"
---
## Request body has the following properties:

| Attribute        | Type    | Description                                       |
| ---------------- | ------- | ------------------------------------------------- |
| SkuServiceTypeId | integer | SKU Service Type ID                               |
| Name             | string  | SKU Service Value name. Maximum of 100 characters |
| Value            | float   | SKU Service Value value                           |
| Cost             | float   | SKU Service Value cost                            |

## Request body example:

[block:code]
{
  "codes": [
    {
      "code": "{\n    \"SkuServiceTypeId\": 527,\n    \"Name\": \"Nome teste ServiceValue\",\n    \"Value\": 10.4,\n    \"Cost\": 10.4\n}",
      "language": "json"
    }
  ]
}
[/block]
## Response body has the following properties:

| Attribute        | Type    | Description             |
| ---------------- | ------- | ----------------------- |
| Id               | integer | SKU Service Value ID    |
| SkuServiceTypeId | integer | SKU Service Type ID     |
| Name             | string  | SKU Service Value Name  |
| Value            | float   | SKU Service Value value |
| Cost             | float   | SKU Service Value cost  |

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"Id\": 1,\n    \"SkuServiceTypeId\": 1,\n    \"Name\": \"Nome teste ServiceValue\",\n    \"Value\": 10.4,\n    \"Cost\": 10.4\n}",
      "language": "json"
    }
  ]
}
[/block]