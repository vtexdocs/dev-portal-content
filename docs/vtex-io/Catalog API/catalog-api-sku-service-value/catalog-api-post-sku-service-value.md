---
title: "Create SKU Service Value"
slug: "catalog-api-post-sku-service-value"
excerpt: "Creates an SKU Service Value for an existing SKU Service Type"
hidden: false
createdAt: "2020-06-08T19:47:12.380Z"
updatedAt: "2020-06-19T16:35:18.800Z"
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
      "code": "{\n    \"SkuServiceTypeId\": 2,\n    \"Name\": \"Teste ServiceValue API\",\n    \"Value\": 10.5,\n    \"Cost\": 10.5\n}",
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
      "code": "{\n    \"Id\": 2,\n    \"SkuServiceTypeId\": 2,\n    \"Name\": \"Teste ServiceValue API\",\n    \"Value\": 10.5,\n    \"Cost\": 10.5\n}",
      "language": "json"
    }
  ]
}
[/block]