---
title: "Coupon Massive Generation"
slug: "massivegeneration"
excerpt: "Coupon massive generation"
hidden: false
createdAt: "2019-12-30T04:15:05.270Z"
updatedAt: "2020-04-02T20:34:03.285Z"
---
## Request object has the following properties:

| Attribute                  | Type    |  Description                                                                                  |
|----------------------------|---------|-----------------------------------------------------------------------------------------------|
| `utmSource`                | string  | Coupon UTM Source                                                                             |
| `utmCampaign`              | string  | Coupon UTM Campaign                                                                           |
| `couponCode`               | string  | Coupon Code                                                                                   |
| `isArchived`               | boolean | Field that archive or unarchive a Coupon                                                      |
| `maxItemsPerClient`        | integer | The customer may purchase up a number of products, using this coupon in one or more purchases |
| `expirationIntervalPerUse` | string  | Renew each coupon usage after a number of days                                                |

## Request body example
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"utmSource\": \"cupom\",\n  \"utmCampaign\": null,\n  \"couponCode\": \"ctest\",\n  \"isArchived\": false,\n  \"maxItemsPerClient\": 1,\n  \"expirationIntervalPerUse\": \"00:00:00\"\n}",
      "language": "json"
    }
  ]
}
[/block]
## Response object has the following properties:
| Attribute                  | Type    |  Description                                                                                  |
|----------------------------|---------|-----------------------------------------------------------------------------------------------|
| `coupon`                | string  | Generated Coupons                                                                            |

## Response body
[block:code]
{
  "codes": [
    {
      "code": "[\n    \"ctest-wzcp5lwt7yz1s7n\",\n    \"ctest-rb6smoassp2xe71\",\n    \"ctest-vpw84ag9tfi8khv\",\n    \"ctest-ne26wgmidp5ctht\",\n    \"ctest-127ng0ox09tho5l\",\n    \"ctest-qsowch8c8s7jipo\",\n    \"ctest-6acbsst6zpss75l\",\n    \"ctest-0bksc2tzh5ai946\",\n    \"ctest-4jjx8u2rrqj4ck9\",\n    \"ctest-hxiox1isdp6padl\"\n]",
      "language": "json"
    }
  ]
}
[/block]