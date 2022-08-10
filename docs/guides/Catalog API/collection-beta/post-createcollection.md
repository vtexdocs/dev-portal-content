---
title: "Create Collection"
slug: "post-createcollection"
excerpt: "Creates a new collection."
hidden: false
createdAt: "2020-12-21T16:28:05.315Z"
updatedAt: "2022-05-20T22:23:44.221Z"
---
## Request body has the following properties:

| Attribute     | Type    | Description                                    |
| ------------- | ------- | ---------------------------------------------- |
| `name` | string | Collection's Name|
| `searchable` | boolean | Option making the collection searchable in the store|
| `highlight` | boolean | Option if you want the collection to highlight specific products using a tag|
| `dateFrom` | string | Collection start date and time. If a future date and time are set, the collection will have a scheduled status|
| `dateTo` | string | Collection end date and time|
| `description` | string | Collection's description for internal use, with the collection's details. It will not be used for search engines|


## Request body example:

[block:code]
{
  "codes": [
    {
      "code": "{\n    \"name\": \"My Collection\",\n    \"searchable\": true,\n    \"highlight\": true,\n    \"dateFrom\": \"2020-12-11 16:00:00\",\n    \"dateTo\": \"2020-12-12 16:00:00\",\n    \"description\": \"Just a simple collection.\"\n}",
      "language": "json"
    }
  ]
}
[/block]
## Response body has the following properties:

| Attribute     | Type    | Description                                    |
| ------------- | ------- | ---------------------------------------------- |
| `id` | integer | Collection's ID|
| `name` | string | Collection's Name|
| `searchable` | boolean | Option making the collection searchable in the store|
| `highlight` | boolean | Option if you want the collection to highlight specific products using a tag|
| `dateFrom` | string | Collection start date and time. If a future date and time are set, the collection will have a scheduled status|
| `dateTo` | string | Collection end date and time|
| `description` | string | Collection's description for internal use, with the collection's details. It will not be used for search engines|
| `totalProducts` | integer | Total of Products on the Collection |
| `type` | string | Type of the Collection. It can be `Manual`, `Automatic` and `Hybrid`|


## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"Id\": 10854,\n    \"Name\": \"My Collection\",\n    \"Description\": \"Just a simple collection.\",\n    \"Searchable\": true,\n    \"Highlight\": true,\n    \"DateFrom\": \"2020-12-11T16:00:00\",\n    \"DateTo\": \"2020-12-12T16:00:00\",\n    \"TotalProducts\": 0,\n    \"Type\": \"Manual\"\n}",
      "language": "json"
    }
  ]
}
[/block]