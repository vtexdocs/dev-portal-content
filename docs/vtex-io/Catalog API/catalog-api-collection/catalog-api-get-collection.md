---
title: "Get Collection"
slug: "catalog-api-get-collection"
excerpt: "Gets general information of a Collection"
hidden: false
createdAt: "2020-04-16T15:43:24.310Z"
updatedAt: "2020-04-24T14:27:58.274Z"
---
## Response body has the following properties:

| Attribute     | Type    | Description                                    |
| ------------- | ------- | ---------------------------------------------- |
| Id            | integer | Collection ID                                  |
| Name          | string  | Collection Name                                |
| Description   | string  | Collection description                         |
| Searchable    | boolean | Whether the Collection is searchale or not     |
| Highlight     | string  | If the Collection is highlighted or not        |
| DateFrom      | string  | Initial value date for the Collection          |
| DateTo        | string  | Final value date for the Collection            |
| TotalProducts | integer | Amount of products contained on the Collection |

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"Id\": 149,\n    \"Name\": \"Marketplace\",\n    \"Description\": null,\n    \"Searchable\": true,\n    \"Highlight\": true,\n    \"DateFrom\": \"2020-02-14T11:26:00\",\n    \"DateTo\": \"2070-02-14T11:26:00\",\n    \"TotalProducts\": 0\n}",
      "language": "json"
    }
  ]
}
[/block]