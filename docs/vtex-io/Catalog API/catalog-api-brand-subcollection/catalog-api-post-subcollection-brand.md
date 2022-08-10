---
title: "Associate SubCollection to Brand"
slug: "catalog-api-post-subcollection-brand"
excerpt: "Associates a SubCollection to a single Brand"
hidden: false
createdAt: "2020-04-16T15:43:24.310Z"
updatedAt: "2020-07-02T14:58:51.390Z"
---
## Request object has the following properties:

| Attribute | Type    | Description |
| --------- | ------- | ----------- |
| BrandId   | integer | Brand ID    |

## Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"BrandId\": 2000004\n}",
      "language": "json"
    }
  ]
}
[/block]
## Response body has the following properties:

| Attribute       | Type    | Description      |
| --------------- | ------- | ---------------- |
| SubCollectionId | integer | SubCollection ID |
| BrandId         | integer | Brand ID         |

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"SubCollectionId\": 13,\n    \"BrandId\": 2000004\n}",
      "language": "json"
    }
  ]
}
[/block]