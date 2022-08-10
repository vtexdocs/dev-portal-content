---
title: "Get SKU Specifications"
slug: "catalog-api-get-sku-specification"
excerpt: "Retrieves general information about an SKU Specification"
hidden: false
createdAt: "2020-04-16T15:43:24.310Z"
updatedAt: "2020-04-22T14:58:37.097Z"
---
## Response body has the following properties:

| Attribute    | Type    | Description                                       |
| ------------ | ------- | ------------------------------------------------- |
| Id           | integer | Unique identifier of the Specification on the SKU |
| SkuId        | integer | Unique identifier of an SKU                       |
| FieldId      | integer | Field ID                                          |
| FieldValueId | integer | Field ID Value                                    |
| Text         | string  | Text contained inside the Specification           |


## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "[\n    {\n        \"Id\": 427,\n        \"SkuId\": 7,\n        \"FieldId\": 32,\n        \"FieldValueId\": 131,\n        \"Text\": \"500g\"\n    },\n    {\n        \"Id\": 428,\n        \"SkuId\": 7,\n        \"FieldId\": 40,\n        \"FieldValueId\": 133,\n        \"Text\": \"A\"\n    }\n]",
      "language": "json"
    }
  ]
}
[/block]