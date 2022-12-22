---
title: "Add coupons to the cart"
slug: "add-coupons-to-the-cart"
hidden: false
createdAt: "2022-11-01T15:10:30.654Z"
updatedAt: "2022-11-17T13:00:19.482Z"
---
The shopping cart is where the information on the products chosen by the customer while browsing a store is gathered. This data may include item prices, shipping value, payment, and delivery methods, among others.

This guide will describe how to add coupons to the shopping cart by the API.
>ℹ️ Before adding the coupon code to the cart, call the [Get all coupons](https://developers.vtex.com/vtex-rest-api/reference/getall) endpoint to confirm that it is active in your store. If necessary, you can [create a new coupon](https://developers.vtex.com/vtex-rest-api/docs/creating-and-managing-coupons-with-promotions-api).

## Getting shopping cart information

The first step is to get the `orderFormId` of the shopping cart information that you want to obtain information about the number of installments. For more information, access the [Get cart information by ID](https://developers.vtex.com/vtex-rest-api/docs/get-cart-information-by-id) guide.

## Adding coupons to the cart

To add coupons to the shopping cart, you must use the [Add coupons to the cart](https://developers.vtex.com/vtex-rest-api/reference/addcoupons) endpoint. In this request, the `ordeFormId` of the shopping cart must be sent through the URL request, as shown by the example below:

`https://{accountname}.{environment.com.br}/api/checkout/pub/orderForm/36a1646105f243e1a9012c9156315644b/coupons`

Additionally, you need to send the request body containing the coupon code to be applied to the shopping cart:
[block:code]
{
  "codes": [
    {
      "code": "{\n     \"text\": \"summersale30\"\n}",
      "language": "json"
    }
  ]
}
[/block]
After sending the request, the endpoint will return the response body containing the coupon information, as shown in the example below:
[block:code]
{
  "codes": [
    {
      "code": "...\n\"marketingData\": {\n        \"utmSource\": null,\n        \"utmMedium\": null,\n        \"utmCampaign\": null,\n        \"utmipage\": null,\n        \"utmiPart\": null,\n        \"utmiCampaign\": null,\n        \"coupon\": \"summersale30\",\n        \"marketingTags\": []\n    }\n...",
      "language": "json"
    }
  ]
}
[/block]

>ℹ️ For more information about the meaning of each of the fields available in the shopping cart, access the [orderForm](https://developers.vtex.com/vtex-rest-api/reference/orderform-fields) overview.

## Error codes

The following errors may appear as a message in the response body.

### 200 - OK

Despite the code `200` (which indicates the success of the request), if the coupon code (`text`) sent is incorrect or unavailable, the following message will be displayed.

- **Message error example (code couponNotFound)**: `"Cupom free inválido"` (*Coupon name invalid*).
[block:code]
{
  "codes": [
    {
      "code": "...\n\"messages\": [\n        {\n            \"code\": \"couponNotFound\",\n            \"text\": \"Cupom free inválido\",\n            \"status\": \"warning\",\n            \"fields\": {}\n        },\n]\n...",
      "language": "json"
    }
  ]
}
[/block]
### 400 - Bad Request

- **Message error example (code ORD002)**: `"Carrinho inválido"` (*Invalid Cart*). This message indicates that the `orderFormId` used in the request does not exist or is incorrect.
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"fields\": {},\n    \"error\": {\n        \"code\": \"ORD002\",\n        \"message\": \"Carrinho inválido\",\n        \"exception\": null\n    },\n    \"operationId\": \"d6a5b535-68b4-49f7-a783-93762974554b\"\n}",
      "language": "json"
    }
  ]
}
[/block]
### 404 - Not Found

- **Message error example**: `"The requested URL was not found on the server"`. Check that the URL data is correct.
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