---
title: "Copy All Files from an SKU to other SKU"
slug: "put_api-catalog-pvt-stockkeepingunit-copy-skuidfrom-skuidto-file"
excerpt: "Copy all existing files from an SKU to other SKU"
hidden: false
createdAt: "2020-11-09T21:04:25.933Z"
updatedAt: "2020-11-10T15:27:23.435Z"
---
## Response body has the following properties:
[block:parameters]
{
  "data": {
    "h-0": "Attribute",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "Id",
    "1-0": "SkuId",
    "2-0": "IsMain",
    "3-0": "Label",
    "0-2": "Unique identifier of the Image",
    "0-1": "integer",
    "1-1": "integer",
    "2-1": "boolean",
    "3-1": "string",
    "1-2": "Unique identifier of an SKU",
    "2-2": "Tells if the Image is the Main Image of the SKU",
    "3-2": "Image Label"
  },
  "cols": 3,
  "rows": 4
}
[/block]
## Response body examples:
[block:code]
{
  "codes": [
    {
      "code": "[\n    {\n        \"Id\": 549,\n        \"SkuId\": 8,\n        \"IsMain\": true,\n        \"Label\": \"frents\"\n    }\n]",
      "language": "json"
    }
  ]
}
[/block]