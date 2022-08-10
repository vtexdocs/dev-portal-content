---
title: "Get SKU Attachment by SKU ID"
slug: "get_api-catalog-pvt-stockkeepingunit-skuid-attachment"
excerpt: "Retrives an existing SKU Attachment from a SKU by its ID"
hidden: false
createdAt: "2021-02-03T22:11:32.897Z"
updatedAt: "2021-02-04T15:28:03.498Z"
---
## Response body has the following properties:

| Attribute    | Type    | Description                                                    |
| ------------ | ------- | -------------------------------------------------------------- |
| Id           | integer | SKU Attachment ID: Identifier of SKU association to Attachment |
| AttachmentId | integer | Attachment ID                                                  |
| SkuId        | integer | Unique identifier of an SKU                                    |

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "[\n    {\n        \"Id\": 31,\n        \"AttachmentId\": 1,\n        \"SkuId\": 7\n    }\n]",
      "language": "json"
    }
  ]
}
[/block]