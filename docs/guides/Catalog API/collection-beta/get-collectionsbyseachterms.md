---
title: "Get Collections by search terms"
slug: "get-collectionsbyseachterms"
excerpt: "Retrieves a list of collections matching a filter."
hidden: false
createdAt: "2020-12-21T16:28:05.316Z"
updatedAt: "2022-05-20T22:23:44.260Z"
---
## Response body has the following properties:

| Attribute     | Type    | Description                                    |
| ------------- | ------- | ---------------------------------------------- |
| `items` | array of objects | Object with general information about the Collections |
| `id` | integer | Collection's ID|
| `name` | string | Collection's Name|
| `searchable` | boolean | Option making the collection searchable in the store|
| `highlight` | boolean | Option if you want the collection to highlight specific products using a tag|
| `dateFrom` | string | Collection start date and time. If a future date and time are set, the collection will have a scheduled status|
| `dateTo` | string | Collection end date and time|
| `totalSku` | integer | Total of SKUs on the Collection|
| `totalProducts` | integer | Total of Products on the Collection |
| `type` | string | Type of the Collection. It can be `Manual`, `Automatic` and `Hybrid`|
| `lastModifiedBy` | string | Last user that modified the Collection|
| `paging` | object | General information about the paging of the Collection dashboard |
| `page` | integer | Page number of the Collection dashboard|
| `perPage` | integer | Quantity of Collections per page|
| `total` | integer | Total of Collections|
| `pages` | integer | Total number of pages|


## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"items\": [\n        {\n            \"id\": 2758,\n            \"name\": \"Coleção Verão\",\n            \"searchable\": false,\n            \"highlight\": false,\n            \"dateFrom\": \"2020-03-04T19:17:00\",\n            \"dateTo\": \"2069-03-04T19:17:00\",\n            \"totalSku\": 12,\n            \"totalProducts\": 12,\n            \"type\": \"Manual\",\n            \"lastModifiedBy\": null\n        },\n        {\n            \"id\": 6206,\n            \"name\": \"Coleção Primavera Verão\",\n            \"searchable\": false,\n            \"highlight\": true,\n            \"dateFrom\": \"2020-06-06T14:40:00\",\n            \"dateTo\": \"2069-06-14T14:40:00\",\n            \"totalSku\": 12,\n            \"totalProducts\": 12,\n            \"type\": \"Manual\",\n            \"lastModifiedBy\": null\n        },\n        {\n            \"id\": 7140,\n            \"name\": \"Coleção Verão\",\n            \"searchable\": false,\n            \"highlight\": false,\n            \"dateFrom\": \"2020-06-18T21:01:00\",\n            \"dateTo\": \"2069-06-18T21:01:00\",\n            \"totalSku\": 4,\n            \"totalProducts\": 4,\n            \"type\": \"Manual\",\n            \"lastModifiedBy\": null\n        },\n        {\n            \"id\": 7149,\n            \"name\": \"Coleção Primavera Verão\",\n            \"searchable\": true,\n            \"highlight\": true,\n            \"dateFrom\": \"2020-06-18T21:33:00\",\n            \"dateTo\": \"2069-06-18T21:33:00\",\n            \"totalSku\": 22,\n            \"totalProducts\": 22,\n            \"type\": \"Manual\",\n            \"lastModifiedBy\": null\n        },\n        {\n            \"id\": 8052,\n            \"name\": \"Coleção Vera Verão\",\n            \"searchable\": false,\n            \"highlight\": false,\n            \"dateFrom\": \"2020-06-29T19:40:00\",\n            \"dateTo\": \"2069-06-29T19:40:00\",\n            \"totalSku\": 10,\n            \"totalProducts\": 10,\n            \"type\": \"Manual\",\n            \"lastModifiedBy\": null\n        },\n        {\n            \"id\": 8054,\n            \"name\": \"Coleção de Verão - 2021\",\n            \"searchable\": false,\n            \"highlight\": false,\n            \"dateFrom\": \"2020-06-29T19:51:00\",\n            \"dateTo\": \"2069-06-29T19:51:00\",\n            \"totalSku\": 7,\n            \"totalProducts\": 7,\n            \"type\": \"Manual\",\n            \"lastModifiedBy\": null\n        },\n        {\n            \"id\": 10118,\n            \"name\": \"Coleção Verão\",\n            \"searchable\": false,\n            \"highlight\": false,\n            \"dateFrom\": \"2020-09-30T19:48:00\",\n            \"dateTo\": \"2069-09-30T19:48:00\",\n            \"totalSku\": 12,\n            \"totalProducts\": 12,\n            \"type\": \"Manual\",\n            \"lastModifiedBy\": null\n        },\n        {\n            \"id\": 10765,\n            \"name\": \"Coleção Verão?\",\n            \"searchable\": false,\n            \"highlight\": false,\n            \"dateFrom\": \"2020-11-11T16:41:00\",\n            \"dateTo\": \"2069-11-11T16:41:00\",\n            \"totalSku\": 5,\n            \"totalProducts\": 5,\n            \"type\": \"Manual\",\n            \"lastModifiedBy\": null\n        }\n    ],\n    \"paging\": {\n        \"page\": 1,\n        \"perPage\": 20,\n        \"total\": 8,\n        \"pages\": 1\n    }\n}",
      "language": "json"
    }
  ]
}
[/block]