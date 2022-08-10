---
title: "Associate SKU Attachment"
slug: "catalog-api-post-sku-attachment"
excerpt: "Associates an existing SKU to an existing Attachment"
hidden: false
createdAt: "2020-04-16T15:43:24.310Z"
updatedAt: "2020-04-22T15:25:15.665Z"
---
## Request body has the following properties:

| Attribute    | Type    | Description                 |
| ------------ | ------- | --------------------------- |
| AttachmentId | integer | Attachment ID               |
| SkuId        | integer | Unique identifier of an SKU |

## Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"AttachmentId\": 1,\n    \"SkuId\": 1622\n}",
      "language": "json"
    }
  ]
}
[/block]
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
      "code": "{\n    \"Id\": 31,\n    \"AttachmentId\": 1,\n    \"SkuId\": 7\n}",
      "language": "json"
    }
  ]
}
[/block]