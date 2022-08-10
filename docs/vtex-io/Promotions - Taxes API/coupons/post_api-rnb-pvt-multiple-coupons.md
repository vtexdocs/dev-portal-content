---
title: "Create multiple coupons"
slug: "post_api-rnb-pvt-multiple-coupons"
excerpt: "Creates multiple coupons with different coupon codes"
hidden: false
createdAt: "2020-06-22T17:51:08.201Z"
updatedAt: "2020-09-30T15:55:43.489Z"
---
## Request body has the following properties:

| Attribute                | Type    | Description                                             |
| ------------------------ | ------- | ------------------------------------------------------- |
| quantity                 | integer | Quantity of coupons created                             |
| couponConfiguration      | object  | Object that contains all coupon configuration           |
| utmSource                | string  | utmSource code                                          |
| utmCampaign              | string  | utmCampaign code                                        |
| couponCode               | string  | couponCode                                              |
| maxItemsPerClient        | integer | Maximum itens per client that the coupon can be applied |
| expirationIntervalPerUse | string  | Coupon expiration interval per use                     |

## Request body example:

[block:code]
{
  "codes": [
    {
      "code": "[\n    {\n        \"quantity\": 1,\n        \"couponConfiguration\": {\n            \"utmSource\": \"cupom1\",\n            \"utmCampaign\": null,\n            \"couponCode\": \"test1\",\n            \"isArchived\": false,\n            \"maxItemsPerClient\": 10,\n            \"expirationIntervalPerUse\": \"00:00:00\"\n        }\n    },\n    {\n        \"quantity\": 1,\n        \"couponConfiguration\": {\n            \"utmSource\": \"cupom2\",\n            \"utmCampaign\": null,\n            \"couponCode\": \"test2\",\n            \"isArchived\": false,\n            \"maxItemsPerClient\": 5,\n            \"expirationIntervalPerUse\": \"00:10:00\"\n        }\n    }\n]",
      "language": "json"
    }
  ]
}
[/block]
## Response body has the following properties:
| Attribute                | Type    | Description                                             |
| ------------------------ | ------- | ------------------------------------------------------- |
| coupons | array of strings | Array with all coupons names                             |

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "[\n    \"test\"\n]",
      "language": "json"
    }
  ]
}
[/block]