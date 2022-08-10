---
title: "Get Subcollection's SKUs"
slug: "catalog-api-get-subcollection-sku"
excerpt: "Retrieves all SKUs from a Subcollection"
hidden: false
createdAt: "2020-05-21T01:19:03.828Z"
updatedAt: "2020-05-21T21:03:06.475Z"
---
## Response body has the following properties:
[block:parameters]
{
  "data": {
    "h-0": "Attribute",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "`Page`",
    "0-1": "integer",
    "0-2": "Page number",
    "1-1": "integer",
    "2-1": "integer",
    "3-1": "integer",
    "4-1": "array of objects",
    "5-1": "integer",
    "6-1": "integer",
    "6-0": "`SkuId`",
    "5-0": "`SubCollectionId`",
    "4-0": "`Data`",
    "3-0": "`TotalPage`",
    "2-0": "`TotalRows`",
    "1-0": "`Size`",
    "1-2": "Number of items in a page",
    "2-2": "Total rows of the page",
    "3-2": "Total page number",
    "4-2": "Informations about the Subcollection",
    "5-2": "SubCollection ID",
    "6-2": "SKU ID"
  },
  "cols": 3,
  "rows": 7
}
[/block]
## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"Page\": 1,\n    \"Size\": 2,\n    \"TotalRows\": 2,\n    \"TotalPage\": 1,\n    \"Data\": [\n        {\n            \"SubCollectionId\": 12,\n            \"SkuId\": 2\n        },\n        {\n            \"SubCollectionId\": 12,\n            \"SkuId\": 7\n        }\n    ]\n}",
      "language": "json"
    }
  ]
}
[/block]