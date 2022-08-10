---
title: "Get coupon by coupon code"
slug: "getbycouponcode"
excerpt: "Retrieves a specific coupon by its coupon code"
hidden: false
createdAt: "2019-12-30T04:15:05.270Z"
updatedAt: "2020-07-14T18:35:29.316Z"
---
## Response object has the following properties:
[block:parameters]
{
  "data": {
    "h-2": "Description",
    "h-1": "Type",
    "h-0": "Attribute",
    "0-0": "`lastModifiedUtc`",
    "0-1": "string",
    "1-0": "`utmSource`",
    "1-1": "string",
    "2-0": "`utmCampaign`",
    "3-0": "`couponCode`",
    "4-0": "`isArchived`",
    "5-0": "`maxItemsPerClient`",
    "6-0": "`expirationIntervalPerUse`",
    "2-1": "string",
    "3-1": "string",
    "4-1": "boolean",
    "5-1": "integer",
    "6-1": "string",
    "0-2": "When the Coupon was last modified",
    "1-2": "Coupon UTM Source",
    "2-2": "Coupon UTM Campaign",
    "3-2": "Coupon Code",
    "4-2": "Field that archive or unarchive a Coupon",
    "5-2": "The customer may purchase up a number of products, using this coupon in one or more purchases",
    "6-2": "Renew each coupon usage after a number of days"
  },
  "cols": 3,
  "rows": 7
}
[/block]
## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"lastModifiedUtc\": \"2020-07-14T18:19:32.6614635Z\",\n    \"utmSource\": \"cupom3\",\n    \"couponCode\": \"ctest\",\n    \"isArchived\": false,\n    \"maxItemsPerClient\": 1,\n    \"expirationIntervalPerUse\": \"00:00:00\"\n}",
      "language": "json"
    }
  ]
}
[/block]