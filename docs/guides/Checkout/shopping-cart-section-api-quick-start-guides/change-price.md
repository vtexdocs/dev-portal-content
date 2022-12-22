---
title: "Change the price of an SKU in a cart"
slug: "change-price"
hidden: false
createdAt: "2022-10-26T19:19:16.231Z"
updatedAt: "2022-11-17T12:38:07.532Z"
---
The shopping cart is where the information on the products chosen by the customer while browsing a store is gathered. This data may include item prices, shipping value, payment, and delivery methods, among others.

This guide will describe how to change the price of an SKU (item) in a cart by the API.
>ℹ️ Before starting to manually change prices on an item, make sure the [Manual Price](https://developers.vtex.com/vtex-rest-api/docs/enable-the-manual-price) feature is already enabled in your store.

## Getting and accessing shopping cart information

The first step is to get the `orderFormId` and access the shopping cart information that you want to change the item price. For more information, access the [Get cart information by ID](https://developers.vtex.com/vtex-rest-api/docs/get-cart-information-by-id) guide.

Below is an example of pricing details for items contained in a shopping cart:
[block:code]
{
  "codes": [
    {
      "code": "\"items\": [\n        {\n            ...\n            \"price\": 1200000,\n            \"listPrice\": 1200000,\n            \"manualPrice\": null,\n            \"manualPriceAppliedBy\": null,\n            ...\n }\n...\n]",
      "language": "json"
    }
  ]
}
[/block]

>ℹ️ For more information about the meaning of each of the fields available in the shopping cart, access the [orderForm](https://developers.vtex.com/vtex-rest-api/reference/orderform-fields) overview.

## Changing the price of a shopping cart item

With the `orderFormId` information available, you must use the [Change price](https://developers.vtex.com/vtex-rest-api/reference/pricechange) endpoint to send the path parameters information through the URL:

- **orderFormId**: value.
- **itemIndex**: a string indicating the index of the item in the cart. Each cart item is identified by an index, starting with `0`.

See an URL example below:

`https://{accountname}.{environment.com.br}/api/checkout/pub/orderForm/36a1646105f243e1a9012c915631344b/items/0/price`

Additionally, you need to send the request body containing the new price to be applied to the item:
[block:code]
{
  "codes": [
    {
      "code": "{\"price\":850000}",
      "language": "json"
    }
  ]
}
[/block]
After sending the request, the endpoint will return the response body with the new item price indicated by the `manualPrice` property. The identification of the user responsible for the price change is available in the `manualPriceAppliedBy` property.
[block:code]
{
  "codes": [
    {
      "code": "\"items\": [\n        {\n            ...\n            \"price\": 1200000,\n            \"listPrice\": 1200000,\n            \"manualPrice\": 850000,\n            \"manualPriceAppliedBy\": “99e09db4-fc3b-4c8e-a15b-5194516”,\n            ...\n }\n...\n]",
      "language": "json"
    }
  ]
}
[/block]
## Error codes

The following errors may appear as a message in the response body.

### 400 - Bad Request

- **Message error example (code CHK0041)**: `"Índice de item inválido"` (*invalid item index*). This message indicates that the `itemIndex` used in the request does not exist or is incorrect.
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"fields\": {},\n    \"error\": {\n        \"code\": \"CHK0041\",\n        \"message\": \"Índice de item inválido\",\n        \"exception\": null\n    },\n    \"operationId\": \"8b1c2f39-641a-4ec1-ba91-b8a9d5b1cd19\"\n}",
      "language": "json"
    }
  ]
}
[/block]
### 403 - Forbidden

- **Message error example (code CHK003)**: `"Access Denied"`. The feature **Manual Price** is not activated on your store. See how to enable it on [Enable the Manual Price](https://developers.vtex.com/vtex-rest-api/docs/enable-the-manual-price).
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"fields\": {},\n    \"error\": {\n        \"code\": \"CHK003\",\n        \"message\": \"Access Denied\",\n        \"exception\": null\n    },\n    \"operationId\": \"4ae9e8e4-0fd1-469a-99b1-71705cbe036f\"\n}",
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