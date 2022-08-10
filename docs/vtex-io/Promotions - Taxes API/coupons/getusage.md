---
title: "Get coupon usage"
slug: "getusage"
excerpt: "Retrieves coupon usage"
hidden: false
createdAt: "2019-12-30T04:15:05.270Z"
updatedAt: "2020-07-14T20:01:54.888Z"
---
## Response body has the following properties:
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
## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"hostName\": \"store\",\n    \"couponCode\": \"coupon\",\n    \"profileUsages\": {\n        \"683bb572-f175-41f9-a2dd-56a24a555640\": {\n            \"orderUsage\": [],\n            \"usageDateUtc\":\"\"\n        }\n    }\n}",
      "language": "json"
    }
  ]
}
[/block]