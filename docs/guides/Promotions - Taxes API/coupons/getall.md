---
title: "Get all coupons"
slug: "getall"
excerpt: "Retrives all coupons from an account."
hidden: false
createdAt: "2021-11-09T19:16:40.460Z"
updatedAt: "2021-11-12T20:10:41.970Z"
---
## Response object has the following properties:
[block:parameters]
{
  "data": {
    "h-0": "Attribute",
    "h-1": "Type",
    "0-0": "`lastModifiedUtc`",
    "1-0": "`utmSource`",
    "0-1": "string",
    "1-1": "string",
    "2-0": "`utmCampaign`",
    "2-1": "string",
    "3-0": "`couponCode`",
    "3-1": "string",
    "4-0": "`isArchived`",
    "4-1": "boolean",
    "5-0": "`maxItemsPerClient`",
    "5-1": "integer",
    "6-0": "`expirationIntervalPerUse`",
    "6-1": "string",
    "h-2": "Description",
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