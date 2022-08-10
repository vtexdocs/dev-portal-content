---
title: "Update SKU Service"
slug: "catalog-api-put-sku-service"
excerpt: "Updates an SKU Service from an SKU"
hidden: false
createdAt: "2020-06-22T17:51:32.924Z"
updatedAt: "2020-07-06T16:10:44.622Z"
---
## Request body has the following properties:

| Attribute | Type    | Description                                                         |
| --------- | ------- | ------------------------------------------------------------------- |
| Name      | string  | SKU Service Name. Maximum of 50 characters                          |
| Text      | string  | Internal description for the SKU Service. Maximum of 100 characters |
| IsActive  | boolean | If the SKU Service is active or not                                 |

## Request body example:

[block:code]
{
  "codes": [
    {
      "code": "{\n    \"Name\": \"name\",\n    \"Text\": \"text\",\n    \"IsActive\": false\n}",
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


## Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"Id\": 1,\n    \"SkuServiceTypeId\": 1,\n    \"SkuServiceValueId\": 1,\n    \"SkuId\": 1,\n    \"Name\": \"name\",\n    \"Text\": \"text\",\n    \"IsActive\": false\n}",
      "language": "json"
    }
  ]
}
[/block]