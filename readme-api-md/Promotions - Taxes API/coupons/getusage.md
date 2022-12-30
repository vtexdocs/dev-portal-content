---
title: "Get coupon usage"
slug: "getusage"
excerpt: "Retrieves information about the coupon usage."
hidden: false
createdAt: "2021-11-09T19:16:40.461Z"
updatedAt: "2021-11-12T20:10:42.006Z"
---
## Response object has the following properties:
[block:parameters]
{
  "data": {
    "h-0": "Attribute",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "`hostName`",
    "0-1": "string",
    "0-2": "Account name",
    "1-0": "`couponCode`",
    "1-1": "string",
    "1-2": "Coupon Code",
    "2-0": "`profileUsages`",
    "2-1": "object",
    "3-0": "`orderId`",
    "3-1": "string",
    "4-0": "`usageDateUtc`",
    "4-1": "string",
    "3-2": "Order ID",
    "4-2": "Order usage date (UTC)",
    "2-2": "Coupon usage Information"
  },
  "cols": 3,
  "rows": 5
}
[/block]