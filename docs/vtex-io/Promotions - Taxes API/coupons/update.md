---
title: "Update coupon"
slug: "update"
excerpt: "Update a specific coupon"
hidden: false
createdAt: "2019-12-30T04:15:05.270Z"
updatedAt: "2020-07-14T18:42:29.724Z"
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
      "code": "{\n    \"lastModifiedUtc\": \"2020-01-08T20:06:06.37289Z\",\n    \"utmSource\": \"cupom3\",\n    \"couponCode\": \"ctest-01e0ueos8zq95rt\",\n    \"isArchived\": true,\n    \"maxItemsPerClient\": 1,\n    \"expirationIntervalPerUse\": \"00:00:00\"\n}",
      "language": "json"
    }
  ]
}
[/block]