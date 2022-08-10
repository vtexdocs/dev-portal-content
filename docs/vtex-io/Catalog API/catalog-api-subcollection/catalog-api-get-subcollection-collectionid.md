---
title: "Get Subcollection by Collection ID"
slug: "catalog-api-get-subcollection-collectionid"
excerpt: "Retrieves all Subcollections by its Collection ID"
hidden: false
createdAt: "2020-05-20T01:33:18.040Z"
updatedAt: "2020-05-20T20:43:08.228Z"
---
## Response body has the following properties:
[block:parameters]
{
  "data": {
    "h-0": "Attribute",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "`Id`",
    "1-0": "`CollectionId`",
    "2-0": "`Name`",
    "3-0": "`Type`",
    "4-0": "`PreSale`",
    "5-0": "`Release`",
    "0-1": "integer",
    "0-2": "SubCollection ID",
    "1-1": "integer",
    "1-2": "Collection ID",
    "2-1": "string",
    "2-2": "SubCollection Name",
    "3-1": "string",
    "3-2": "Either “Exclusive” (all the products contained in it will not be used) or “Inclusive” (all the products contained in it will be used)",
    "4-1": "boolean",
    "5-1": "boolean",
    "4-2": "Defines PreSale date",
    "5-2": "Defines Release date"
  },
  "cols": 3,
  "rows": 6
}
[/block]
## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "[\n    {\n        \"Id\": 12,\n        \"CollectionId\": 149,\n        \"Name\": \"Subcollection\",\n        \"Type\": \"Inclusive\",\n        \"PreSale\": false,\n        \"Release\": true\n    },\n    {\n        \"Id\": 13,\n        \"CollectionId\": 149,\n        \"Name\": \"Test\",\n        \"Type\": \"Exclusive\",\n        \"PreSale\": true,\n        \"Release\": false\n    },\n    {\n        \"Id\": 14,\n        \"CollectionId\": 149,\n        \"Name\": \"asdfghj\",\n        \"Type\": \"Inclusive\",\n        \"PreSale\": false,\n        \"Release\": false\n    }\n]",
      "language": "json"
    }
  ]
}
[/block]