---
title: "Update price association by ID"
slug: "put_-v-custom-prices-rules-priceassociationid"
excerpt: "Updates a price association for a shopping scenario by its ID"
hidden: false
createdAt: "2020-09-04T15:44:57.991Z"
updatedAt: "2022-02-03T13:17:50.526Z"
---
## Request body has the following properties:

[block:parameters]
{
  "data": {
    "h-0": "Attribute",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "`id`",
    "0-1": "integer",
    "0-2": "Price association ID",
    "1-0": "`orderType`",
    "1-1": "string",
    "1-2": "Order type",
    "2-0": "`state`",
    "2-1": "string",
    "2-2": "Delivery location",
    "3-0": "`pricetable`",
    "3-1": "string",
    "3-2": "Name of the Price Table associated with the scenario",
    "4-0": "`email`",
    "4-1": "string",
    "4-2": "User's email"
  },
  "cols": 3,
  "rows": 5
}
[/block]
## Request body example:

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"id\":1,\n  \"orderType\": \"Resale\",\n  \"state\": \"ES\",\n  \"pricetable\": \"pricetable1\",\n  \"email\": \"email@email.com\"\n}",
      "language": "json"
    }
  ]
}
[/block]
## Response body has the following properties:

[block:parameters]
{
  "data": {
    "h-0": "Attribute",
    "h-1": "Type",
    "0-0": "`id`",
    "0-1": "integer",
    "0-2": "Price association ID",
    "h-2": "Description",
    "1-0": "`orderType`",
    "1-1": "string",
    "1-2": "Order type",
    "2-0": "`state`",
    "2-1": "string",
    "2-2": "Delivery location",
    "3-0": "`pricetable`",
    "3-1": "string",
    "3-2": "Name of the Price Table associated with the scenario",
    "4-0": "`email`",
    "4-1": "string",
    "4-2": "User's email"
  },
  "cols": 3,
  "rows": 5
}
[/block]
## Response body example:

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"id\":1,\n  \"orderType\": \"Resale\",\n  \"state\": \"ES\",\n  \"pricetable\": \"pricetable1\",\n  \"email\": \"email@email.com\"\n}",
      "language": "json"
    }
  ]
}
[/block]