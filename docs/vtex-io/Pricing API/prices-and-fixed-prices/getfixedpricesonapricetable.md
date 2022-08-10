---
title: "Get Fixed Prices on a price table"
slug: "getfixedpricesonapricetable"
excerpt: "Gets all Fixed Prices on a price table (or trade policy)"
hidden: false
createdAt: "2019-12-30T17:39:05.877Z"
updatedAt: "2020-02-27T16:56:10.648Z"
---
## Request object has the following properties:
[block:parameters]
{
  "data": {
    "h-0": "Attribute",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "`itemId`",
    "1-0": "`priceTableId`",
    "0-1": "integer",
    "1-1": "string",
    "0-2": "SKU ID",
    "1-2": "Price Table ID"
  },
  "cols": 3,
  "rows": 2
}
[/block]
## Response object has the following properties:
[block:parameters]
{
  "data": {
    "0-0": "`tradePolicyId`",
    "h-0": "Attribute",
    "h-1": "Type",
    "h-2": "Description",
    "0-1": "string",
    "1-0": "`value`",
    "1-1": "integer",
    "2-0": "`listPrice`",
    "2-1": "integer",
    "3-0": "`minQuantity`",
    "3-1": "integer",
    "4-0": "`dateRange`",
    "4-1": "object",
    "5-0": "`from`",
    "6-0": "`to`",
    "5-1": "string",
    "6-1": "string",
    "0-2": "Trade Policy ID",
    "1-2": "Price Value",
    "2-2": "List Price",
    "3-2": "Minimum Quantity",
    "4-2": "DateRange for schedule fixed price",
    "5-2": "Price begin date",
    "6-2": "Price end date"
  },
  "cols": 3,
  "rows": 7
}
[/block]