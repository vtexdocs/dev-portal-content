---
title: "Get SubCollection"
slug: "catalog-api-get-subcollection"
excerpt: "Gets information about a SubCollection"
hidden: false
createdAt: "2020-04-16T15:43:24.310Z"
updatedAt: "2020-05-20T17:23:17.818Z"
---
## Response body has the following properties:

| Attribute    | Type    | Description                                                                                                                           |
| ------------ | ------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Id | integer | SubCollection ID                                                                                                                      |
| CollectionId | integer | Collection ID                                                                                                                      |
| Name         | string  | SubCollection Name                                                                                                                    |
| Type         | string  | Either “Exclusive” (all the products contained in it will not be used) or “Inclusive” (all the products contained in it will be used) |
| PreSale      | boolean | Defines PreSale date                                                                                                                  |
| Release      | boolean | Defines Release date                                                                                                                  |

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"Id\": 13,\n    \"CollectionId\": 149,\n    \"Name\": \"Test\",\n    \"Type\": \"Exclusive\",\n    \"PreSale\": true,\n    \"Release\": false\n}",
      "language": "json"
    }
  ]
}
[/block]