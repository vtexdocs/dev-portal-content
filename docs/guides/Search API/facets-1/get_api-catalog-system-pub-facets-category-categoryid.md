---
title: "Get Category Facets"
slug: "get_api-catalog-system-pub-facets-category-categoryid"
excerpt: "Retrieves the names and IDs of the categories facets."
hidden: false
createdAt: "2021-08-31T18:21:42.987Z"
updatedAt: "2021-10-13T16:37:29.820Z"
---
[block:callout]
{
  "type": "warning",
  "body": "This endpoint returns a maximum of 50 items per response, so the difference between `_from` and `_to` should not exceed this number. It is also important to highlight that the result order is descending, from the highest product ID to the lowest."
}
[/block]
## Response body has the following properties

| Attribute | Type    | Description            |
|-----------|---------|------------------------|
| Name      | string  | Category's facet name. |
| Id        | integer | Facet ID.              |

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "[\n\t[\n    {\n      \"Name\":\"Tamanho Global\",\n      \"Id\":45\n\t\t},\n\t\t{\n      \"Name\":\"Percentuals\",\n      \"Id\":25\n\t\t}\n\t]\n]",
      "language": "json"
    }
  ]
}
[/block]