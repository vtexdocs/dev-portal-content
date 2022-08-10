---
title: "Associate SKU Service"
slug: "catalog-api-post-sku-service"
excerpt: "Associates an SKU Service to an SKU"
hidden: false
createdAt: "2020-06-08T19:47:12.373Z"
updatedAt: "2020-06-19T16:21:53.058Z"
---
## Request body has the following properties:

| Attribute         | Type    | Description                                                         |
| ----------------- | ------- | ------------------------------------------------------------------- |
| SkuServiceTypeId  | integer | SKU Service Type ID                                                 |
| SkuServiceValueId | integer | SKU Service Value ID                                                |
| SkuId             | integer | SKU ID                                                              |
| Name              | string  | SKU Service Name. Maximum of 50 characters                          |
| Text              | string  | Internal description for the SKU Service. Maximum of 100 characters |
| IsActive          | boolean | If the SKU Service is active or not                                 |

## Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"SkuServiceTypeId\": 2,\n    \"SkuServiceValueId\": 1,\n    \"SkuId\": 1,\n    \"Name\": \"Nome teste\",\n    \"Text\": \"texto teste\",\n    \"IsActive\": true\n}\n",
      "language": "json"
    }
  ]
}
[/block]
## Response body has the following properties:

| Attribute         | Type    | Description                              |
| ----------------- | ------- | ---------------------------------------- |
| Id                | integer | SKU Service ID                           |
| SkuServiceTypeId  | integer | SKU Service Type ID                      |
| SkuServiceValueId | integer | SKU Service Value ID                     |
| SkuId             | integer | SKU ID                                   |
| Name              | string  | SKU Service Name                         |
| Text              | string  | Internal description for the SKU Service |
| IsActive          | boolean | If the SKU Service is active or not      |

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"Id\": 2,\n    \"SkuServiceTypeId\": 1,\n    \"SkuServiceValueId\": 1,\n    \"SkuId\": 7,\n    \"Name\": \"Nome teste\",\n    \"Text\": \"texto teste\",\n    \"IsActive\": true\n}\n",
      "language": "json"
    }
  ]
}
[/block]