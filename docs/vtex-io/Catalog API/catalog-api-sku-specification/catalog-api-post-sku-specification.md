---
title: "Associate SKU Specification"
slug: "catalog-api-post-sku-specification"
excerpt: "Associates a previously defined Specification to an SKU"
hidden: false
createdAt: "2020-03-10T13:42:06.197Z"
updatedAt: "2021-03-11T15:21:14.957Z"
---
## Request body has the following properties:

| Attribute    | Type    | Description   |
| ------------ | ------- | ------------- |
| FieldId      | integer | Field ID      |
| FieldValueId | integer | Fied Value ID |


## Request body example
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"FieldId\": 65,\n    \"FieldValueId\": 138\n}",
      "language": "json"
    }
  ]
}
[/block]

## Response has the following properties:

| Attribute    | Type    | Description                                |
| ------------ | ------- | ------------------------------------------ |
| Id           | integer | Specifications association ID with the SKU |
| SkuId        | integer | SKU ID                                     |
| FieldId      | integer | Field ID                                   |
| FieldValueId | integer | Fied Value ID                              |
| Text         | string  | Value inside the Field ID                  |


## Response body example
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"Id\": 730,\n    \"SkuId\": 31,\n    \"FieldId\": 65,\n    \"FieldValueId\": 138,\n    \"Text\": \"Muito Dinheiro\"\n}",
      "language": "json"
    }
  ]
}
[/block]