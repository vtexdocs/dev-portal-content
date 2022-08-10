---
title: "Associate SubCollection to Category"
slug: "catalog-api-post-subcollection-category"
excerpt: "Associates a SubCollection to a single Category"
hidden: false
createdAt: "2020-04-16T15:43:24.310Z"
updatedAt: "2020-07-02T14:58:51.304Z"
---
## Request object has the following properties:

| Attribute  | Type    | Description |
| ---------- | ------- | ----------- |
| CategoryId | integer | Category ID |

## Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"CategoryId\": 4\n}",
      "language": "json"
    }
  ]
}
[/block]
## Response body has the following properties:

| Attribute       | Type    | Description      |
| --------------- | ------- | ---------------- |
| SubCollectionId | integer | SubCollection ID |
| CategoryId      | integer | Category ID      |

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"SubCollectionId\": 13,\n    \"CategoryId\": 4\n}",
      "language": "json"
    }
  ]
}
[/block]