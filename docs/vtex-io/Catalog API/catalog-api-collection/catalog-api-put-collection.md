---
title: "Update Collection"
slug: "catalog-api-put-collection"
excerpt: "Updates a previously Collection"
hidden: false
createdAt: "2020-04-16T15:43:24.310Z"
updatedAt: "2020-04-24T14:36:52.487Z"
---
## Request object has the following properties:

| Attribute  | Type    | Description                                |
| ---------- | ------- | ------------------------------------------ |
| Name       | string  | Collection Name                            |
| Searchable | boolean | Whether the Collection is searchale or not |
| Highlight  | boolean | If the Collection is highlighted or not    |
| DateFrom   | string  | Initial value date for the Collection      |
| DateTo     | string  | Final value date for the Collection        |

## Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"Name\": \"Test\",\n    \"Searchable\": false,\n    \"Highlight\": false,\n    \"DateFrom\": \"2017-09-27T10:47:00\",\n    \"DateTo\": \"2027-09-27T10:47:00\"\n}",
      "language": "json"
    }
  ]
}
[/block]
## Response body has the following properties:

| Attribute  | Type    | Description                                |
| ---------- | ------- | ------------------------------------------ |
| Name       | string  | Collection Name                            |
| Searchable | boolean | Whether the Collection is searchale or not |
| Highlight  | boolean | If the Collection is highlighted or not    |
| DateFrom   | string  | Initial value date for the Collection      |
| DateTo     | string  | Final value date for the Collection        |

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"Name\": \"Test\",\n    \"Searchable\": false,\n    \"Highlight\": false,\n    \"DateFrom\": \"2017-09-27T10:47:00\",\n    \"DateTo\": \"2027-09-27T10:47:00\"\n}",
      "language": "json"
    }
  ]
}
[/block]