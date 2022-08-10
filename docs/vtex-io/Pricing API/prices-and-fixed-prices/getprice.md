---
title: "Get Price"
slug: "getprice"
excerpt: "Retrieves price data by SKU Id It is possible that on the property fixedPrices exists a list of specific prices for Trade Policies and Minimium Quantities of the SKU. Fixed Prices may also be scheduled"
hidden: false
createdAt: "2019-12-30T17:39:05.877Z"
updatedAt: "2020-02-27T17:22:30.503Z"
---
know more about [Prices in VTEX Help] (https://help.vtex.com/en/tutorial/prices-v2)
[block:parameters]
{
  "data": {
    "h-0": "Attribute",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "`itemId`",
    "0-1": "string",
    "1-0": "`listPrice`",
    "1-1": "integer",
    "2-0": "`costPrice`",
    "2-1": "integer",
    "3-0": "`markup`",
    "3-1": "integer",
    "4-0": "`basePrice`",
    "4-1": "integer",
    "5-0": "`fixedPrices`",
    "5-1": "object",
    "6-0": "`tradePolicyId`",
    "7-0": "`value`",
    "8-0": "`listPrice`",
    "9-0": "`minQuantity`",
    "10-0": "`dateRange`",
    "11-0": "`from`",
    "12-0": "`to`",
    "6-1": "string",
    "7-1": "integer",
    "9-1": "integer",
    "10-1": "object",
    "11-1": "string",
    "12-1": "string",
    "0-2": "SKU ID",
    "1-2": "List Price",
    "2-2": "Cost Price",
    "3-2": "Price Markup",
    "4-2": "Base Price",
    "5-2": "Fixed Prices",
    "6-2": "Trade Policy ID Fixed Price",
    "7-2": "Value",
    "8-1": "integer",
    "8-2": "List Price",
    "9-2": "Minimum Quantity",
    "10-2": "DateRange for schedule fixed price",
    "11-2": "Price Begin Date",
    "12-2": "Price End Date"
  },
  "cols": 3,
  "rows": 13
}
[/block]