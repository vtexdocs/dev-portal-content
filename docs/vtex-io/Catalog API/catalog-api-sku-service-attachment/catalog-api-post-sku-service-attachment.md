---
title: "Associate SKU Service Attachment"
slug: "catalog-api-post-sku-service-attachment"
excerpt: "Associates an Attachment for an existing SKU Service Type"
hidden: false
createdAt: "2020-06-08T19:47:12.376Z"
updatedAt: "2020-06-19T16:25:26.310Z"
---
## Request body has the following properties:

| Attribute        | Type    | Description         |
| ---------------- | ------- | ------------------- |
| AttachmentId     | integer | Attachment ID       |
| SkuServiceTypeId | integer | SKU Service Type ID |

## Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"AttachmentId\": 1,\n    \"SkuServiceTypeId\": 1\n}",
      "language": "json"
    }
  ]
}
[/block]

## Response body has the following properties:

| Attribute        | Type    | Description                 |
| ---------------- | ------- | --------------------------- |
| Id               | integer | SKU Service Type Attachment |
| AttachmentId     | integer | Attachment ID               |
| SkuServiceTypeId | integer | SKU Service Type ID         |

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"Id\": 1,\n    \"AttachmentId\": 1,\n    \"SkuServiceTypeId\": 1\n}",
      "language": "json"
    }
  ]
}
[/block]