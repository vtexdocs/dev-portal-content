---
title: "Update SubCollection"
slug: "catalog-api-put-subcollection"
excerpt: "Updates a previously SubCollection"
hidden: false
createdAt: "2020-04-16T15:43:24.310Z"
updatedAt: "2020-04-24T15:52:27.501Z"
---
## Request object has the following properties:

| Attribute    | Type    | Description                                                                                                                           |
| ------------ | ------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| CollectionId | integer | SubCollection ID                                                                                                                      |
| Name         | string  | SubCollection Name                                                                                                                    |
| Type         | string  | Either “Exclusive” (all the products contained in it will not be used) or “Inclusive” (all the products contained in it will be used) |
| PreSale      | boolean | Defines PreSale date                                                                                                                  |
| Release      | boolean | Defines Release date                                                                                                                  |

## Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"CollectionId\": 149,\n    \"Name\": \"Test\",\n    \"Type\": \"Exclusive\",\n    \"PreSale\": true,\n    \"Release\": false\n}",
      "language": "json"
    }
  ]
}
[/block]
## Response body has the following properties:

| Attribute    | Type    | Description                                                                                                                           |
| ------------ | ------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| CollectionId | integer | SubCollection ID                                                                                                                      |
| Name         | string  | SubCollection Name                                                                                                                    |
| Type         | string  | Either “Exclusive” (all the products contained in it will not be used) or “Inclusive” (all the products contained in it will be used) |
| PreSale      | boolean | Defines PreSale date                                                                                                                  |
| Release      | boolean | Defines Release date                                                                                                                  |

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"CollectionId\": 149,\n    \"Name\": \"Test\",\n    \"Type\": \"Exclusive\",\n    \"PreSale\": true,\n    \"Release\": false\n}",
      "language": "json"
    }
  ]
}
[/block]