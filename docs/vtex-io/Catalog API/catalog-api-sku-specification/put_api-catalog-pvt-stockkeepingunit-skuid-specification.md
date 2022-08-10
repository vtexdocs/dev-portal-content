---
title: "Update SKU Specification"
slug: "put_api-catalog-pvt-stockkeepingunit-skuid-specification"
excerpt: "Updates an existing Specification on an existing SKU. This endpoint only updates the `FieldValueId`"
hidden: false
createdAt: "2020-10-22T21:59:16.168Z"
updatedAt: "2020-10-23T14:17:17.182Z"
---
[block:callout]
{
  "type": "warning",
  "body": "This endpoint is a little more complicated than the others. If you having some trouble, check [our guide](https://developers.vtex.com/vtex-developer-docs/docs/using-the-catalog-api-to-update-an-sku-specification)."
}
[/block]
## Request body has the following properties:
[block:parameters]
{
  "data": {
    "h-0": "Attribute",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "Id",
    "0-1": "integer",
    "0-2": "Specification and SKU association unique identifier. This field cannot be updated",
    "1-0": "SkuId",
    "1-1": "integer",
    "1-2": "SKU unique identifier. This field cannot be updated",
    "2-0": "FieldId",
    "2-1": "integer",
    "3-1": "integer",
    "4-1": "string",
    "2-2": "Specification unique identifier. This field cannot be updated",
    "3-0": "FieldValueId",
    "3-2": "Specification value unique identifier. This field can only be updated with other values of the same `FieldId`",
    "4-0": "Text",
    "4-2": "Specification Value Name. This field is automatically updated if the `FieldValue` is updated. Otherwise, the value cannot be modified"
  },
  "cols": 3,
  "rows": 5
}
[/block]
## Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"Id\": 65,\n  \"SkuId\": 21,\n  \"FieldId\": 32,\n  \"FieldValueId\": 131,\n  \"Text\": \"Red\"\n}",
      "language": "json"
    }
  ]
}
[/block]
## Response body has the following properties:
[block:parameters]
{
  "data": {
    "h-0": "Attribute",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "Id",
    "0-1": "integer",
    "1-1": "integer",
    "3-1": "integer",
    "2-1": "integer",
    "4-1": "string",
    "0-2": "Specification and SKU association unique identifier. This field cannot be updated",
    "1-0": "SkuId",
    "1-2": "SKU unique identifier. This field cannot be updated",
    "2-0": "FieldId",
    "3-0": "FieldValueId",
    "4-0": "Text",
    "2-2": "Specification unique identifier. This field cannot be updated",
    "3-2": "Specification value unique identifier. This field can only be updated with other values of the same `FieldId`",
    "4-2": "Specification Value Name. This field is automatically updated if the `FieldValue` is updated. Otherwise, the value cannot be modified"
  },
  "cols": 3,
  "rows": 5
}
[/block]
## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"Id\": 65,\n  \"SkuId\": 21,\n  \"FieldId\": 32,\n  \"FieldValueId\": 132,\n  \"Text\": \"Blue\"\n}",
      "language": "json"
    }
  ]
}
[/block]