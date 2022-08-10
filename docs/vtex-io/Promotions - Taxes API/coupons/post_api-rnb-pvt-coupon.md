---
title: "Create coupon"
slug: "post_api-rnb-pvt-coupon"
excerpt: "Create a new coupon"
hidden: false
createdAt: "2020-02-13T10:33:31.285Z"
updatedAt: "2020-07-14T18:20:29.420Z"
---
## Request body has the following properties:

| Attribute                | Type    | Description                                             |
| ------------------------ | ------- | ------------------------------------------------------- |
| utmSource                | string  | utmSource code                                          |
| utmCampaign              | string  | utmCampaign code                                        |
| couponCode               | string  | couponCode                                              |
| maxItemsPerClient        | integer | Maximum items per client that the coupon can be applied |
| expirationIntervalPerUse | string  | Coupon expiration interval per use                     |

## Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"utmSource\": \"cupom3\",\n  \"utmCampaign\": null,\n  \"couponCode\": \"ctest\",\n  \"isArchived\": false,\n  \"maxItemsPerClient\": 1,\n  \"expirationIntervalPerUse\": \"00:00:00\"\n}",
      "language": "json"
    }
  ]
}
[/block]
## Response body has the following properties:

| Attribute                | Type    | Description                                             |
| ------------------------ | ------- | ------------------------------------------------------- |
| lastModifiedUtc        | string  | Date and time of the last modification |
| utmSource                | string  | utmSource code                                          |
| utmCampaign              | string  | utmCampaign code                                        |
| couponCode               | string  | couponCode                                              |
| maxItemsPerClient        | integer | Maximum items per client that the coupon can be applied |
| expirationIntervalPerUse | string  | Coupon expiration interval per use                     |

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