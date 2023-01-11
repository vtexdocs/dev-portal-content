---
title: "Add marketing data to the cart"
slug: "add-marketing-data-to-the-cart"
hidden: true
createdAt: "2022-11-23T19:24:49.778Z"
updatedAt: "2022-11-28T18:28:17.413Z"
---
The shopping cart is where the information on the products chosen by the customer while browsing a store is gathered. This data may include item prices, shipping value, payment, and delivery methods, among others.

This guide will describe how to add marketing data information to the shopping cart by the API. For more information about UTMs, access [What are utm_source, utm_campaign, and utm_medium](https://help.vtex.com/tutorial/what-are-utm-source-utm-campaign-and-utm-medium).

## Getting shopping cart information

The first step is to get the `orderFormId` of the shopping cart you want to add the marketing data information to. For more information, access the [Get cart information by ID](https://developers.vtex.com/vtex-rest-api/docs/get-cart-information-by-id) guide.

## Adding marketing data to the shopping cart

To add marketing data to the shopping cart, you need to use the [Add marketing data](https://developers.vtex.com/vtex-rest-api/reference/addmarketingdata) endpoint. In this request, you must send the `orderFormId` through the URL address, as shown in the example below:

`https://{accountName}.{environment.com.br}/api/checkout/pub/orderForm/ede846222cd44046ba6c638442c3505a/attachments/marketingData`

Additionally, you need to send the request body containing the following marketing data information:

- `coupon`: coupon code to be applied to the cart. Use the [cart simulation](https://developers.vtex.com/vtex-rest-api/reference/orderform#orderformsimulation) request to check which coupons can be applied before placing the order.
- `marketingTags`: marketing tags.
- `utmSource`: source of the traffic (e.g. Facebook, Google).
- `utmMedium`: advertising or marketing media (e.g. banner, cpc).
- `utmCampaign`: campaign name (e.g. Christmas, launch, promo01).
- `utmiPage`: utmi_page (internal utm).
- `utmiPart`: utmi_part (internal utm).
- `utmiCampaign`: utmi_campaign (internal utm).

See a request body example below:
[block:code]
{
  "codes": [
    {
      "code": "{\n     \"coupon\": \"free-shipping\",\n     \"marketingTags\": [\n          \"tag1\",\n          \"tag2\"\n     ],\n     \"utmSource\": \"Facebook\",\n     \"utmMedium\": \"CPC\",\n     \"utmCampaign\": \"Black friday\",\n     \"utmiPage\": \"utmi_page-example\",\n     \"utmiPart\": \"utmi_part-example\",\n     \"utmiCampaign\": \"utmi_campaign-example\"\n}",
      "language": "json"
    }
  ]
}
[/block]
After sending the request, the endpoint will return the response body containing the client preferences information in the shopping cart, as shown in the example below:
[block:code]
{
  "codes": [
    {
      "code": "...\n\"marketingData\": {\n        \"utmSource\": \"Facebook\",\n        \"utmMedium\": \"CPC\",\n        \"utmCampaign\": \"Black friday\",\n        \"utmipage\": \"utmi_page-example\",\n        \"utmiPart\": \"utmi_part-exmaple\",\n        \"utmiCampaign\": \"utmi_campaign-example\",\n        \"coupon\": \"free-shipping\",\n        \"marketingTags\": [\n            \"tag1\",\n            \"tag2\"\n        ]\n    }\n...",
      "language": "json"
    }
  ]
}
[/block]

> ℹ️️ For more information about the meaning of each of the fields available in the shopping cart, access the [orderForm](https://developers.vtex.com/vtex-rest-api/reference/orderform-fields) overview.

## Error codes

The following errors may appear as a message in the response body.

### 200 - OK

Despite the code `200` (which indicates the success of the request), if the item `coupon` code sent is incorrect or unavailable, the following message will appear.
[block:code]
{
  "codes": [
    {
      "code": "...\n\"messages\": [\n        {\n            \"code\": \"couponNotFound\",\n            \"text\": \"Coupon 34324 invalid\",\n            \"status\": \"warning\",\n            \"fields\": {}\n        }\n    ]\n...",
      "language": "json"
    }
  ]
}
[/block]
### 400 - Bad Request

- **Message error example (code ORD002)**: `"Invalid order form"`. The `orderFormId` information is not valid.
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"fields\": {},\n    \"error\": {\n        \"code\": \"ORD002\",\n        \"message\": \"Invalid order form\",\n        \"exception\": null\n    },\n    \"operationId\": \"5d9f54e6-7db4-46d6-bca9-deeb278b8b98\"\n}",
      "language": "json"
    }
  ]
}
[/block]
### 404 - Not Found

- `Message error example: "The requested URL was not found on the server"`: check that the URL data is correct.
[block:code]
{
  "codes": [
    {
      "code": "<body>\n\t<h1>404 Not Found</h1>\n\t<p>The requested URL was not found on this server.</p>\n</body>",
      "language": "json"
    }
  ]
}
[/block]