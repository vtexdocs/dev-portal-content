---
title: "Create / Edit Price or Fixed Price"
slug: "put_prices-itemid"
excerpt: "Creates or updates an SKU Price or Fixed Price. The Fixed Price is an optional price of the SKU for a specific Trade Policy with a specific Minimum Quantity to be activated"
hidden: false
createdAt: "2020-02-27T01:32:48.932Z"
updatedAt: "2020-05-21T23:54:18.732Z"
---
The property "basePrice" is the base selling price of the SKU. The property "fixedPrices" is an array where each item is a `Fixed Price`. When fetching a Price, if a valid Fixed Price is not found, the price will fallback to the `Base Price`.

know more about [Prices in VTEX Help] (https://help.vtex.com/en/tutorial/prices-v2)
[block:callout]
{
  "type": "info",
  "body": "In the same Create/Edit Price request, you may optionally set a list price. Additionally, you may set either a cost price or a markup value. By defining either one of them, the other will be calculated to conform to the formula `basePrice = costPrice * (1 + markup)`."
}
[/block]
## Request body has the following properties:
[block:parameters]
{
  "data": {
    "h-0": "Attribute",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "`costPrice`",
    "2-0": "`basePrice`",
    "0-1": "integer",
    "2-1": "integer",
    "0-2": "SKU Cost Price",
    "2-2": "SKU Selling Base Price",
    "4-0": "`fixedPrices`",
    "4-1": "array of objects",
    "5-0": "`tradePolicyId`",
    "6-0": "`value`",
    "7-0": "`listPrice`",
    "8-0": "`minQuantity`",
    "9-0": "`dateRange`",
    "10-0": "`from`",
    "11-0": "`to`",
    "11-1": "string",
    "10-1": "string",
    "5-1": "string",
    "9-1": "object",
    "6-1": "float",
    "7-1": "integer",
    "8-1": "integer",
    "8-2": "Minimum quantity of the SKU",
    "4-2": "Fixed Price",
    "5-2": "Trade Policy ID",
    "6-2": "Price",
    "7-2": "SKU List Fixed Price",
    "9-2": "Trade Policy Fixed Price Validity Period Object",
    "10-2": "Validity start Date",
    "11-2": "Validity end Date",
    "1-0": "`markup`",
    "1-1": "integer",
    "3-0": "`listPrice`",
    "3-1": "integer",
    "3-2": "SKU List Price",
    "1-2": "Price Markup"
  },
  "cols": 3,
  "rows": 12
}
[/block]
## Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"markup\": 30,\n    \"basePrice\": 100,\n    \"listPrice\": 12,\n    \"fixedPrices\": [\n        {\n            \"tradePolicyId\": \"1\",\n            \"value\": 2.99,\n            \"listPrice\": 1,\n            \"minQuantity\": 1,\n            \"dateRange\": {\n                \"from\": \"2020-05-21T22:00:00Z\",\n                \"to\": \"2020-05-28T22:00:00Z\"\n            }\n        },\n        {\n            \"tradePolicyId\": \"1\",\n            \"value\": 0.49,\n            \"listPrice\": null,\n            \"minQuantity\": 2\n        }\n    ]\n}",
      "language": "json"
    }
  ]
}
[/block]