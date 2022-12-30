---
title: "Get price association by ID"
slug: "get_-v-custom-prices-rules-priceassociationid"
excerpt: "Retrieves price association for a shopping scenario by its ID"
hidden: false
createdAt: "2020-09-04T15:44:57.990Z"
updatedAt: "2022-02-03T13:16:58.094Z"
---
## Response body has the following properties:

[block:parameters]
{
  "data": {
    "h-0": "Attribute",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "`id`",
    "1-0": "`orderType`",
    "2-0": "`state`",
    "3-0": "`pricetable`",
    "4-0": "`email`",
    "0-1": "integer",
    "0-2": "Price association ID",
    "1-1": "string",
    "2-1": "string",
    "4-1": "string",
    "3-1": "string",
    "1-2": "Order type",
    "2-2": "Delivery location",
    "3-2": "Name of the Price Table associated with the scenario",
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