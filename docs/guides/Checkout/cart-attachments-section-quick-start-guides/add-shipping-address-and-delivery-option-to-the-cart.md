---
title: "Add shipping address and delivery options to the cart"
slug: "add-shipping-address-and-delivery-option-to-the-cart"
hidden: true
createdAt: "2022-11-21T13:53:48.224Z"
updatedAt: "2022-11-28T16:48:23.435Z"
---
The shopping cart is where the information on the products chosen by the customer while browsing a store is gathered. This data may include item prices, shipping value, payment, and delivery methods, among others.

This guide will describe how to add shipping address and delivery options information in the shopping cart by the API.

## Getting shopping cart information

The first step is to get the `orderFormId` of the shopping cart that you want to add the shipping address and delivery option information to. For more information, access the [Get cart information by ID](https://developers.vtex.com/vtex-rest-api/docs/get-cart-information-by-id) guide.

## Adding a shipping address to the shopping cart

To add a shipping address to the shopping cart, you need to use the [Add shipping address and select delivery option](https://developers.vtex.com/vtex-rest-api/reference/addshippingaddress) endpoint. In this request, you must send the `orderFormId` through the URL address, as shown in the example below:

`https://{accountName}.{environment.com.br}/api/checkout/pub/orderForm/ede846222cd44046ba6c638442c3505a/attachments/shippingData`

Additionally, you need to send the request body with the `selectedAddresses` array containing the following information:

- `addressType`: type of address (e.g. "residential", "pickup").
- `receiverName`: name of the person responsible for receiving the order at the address.
- `postalCode`: postal code information.
- `city`: shipping address city.
- `state`: shipping address state.
- `country`: shipping address country, indicated by the three-letter ISO code (e.g. "BRA", "USA").
- `street`: shipping address street.
- `number`: shipping address number.
- `neighborhood`: shipping address neighborhood.
- `complement`: shipping address complement (if necessary).
- `reference`: complement that might help locate the shipping address more precisely in case of delivery.
- `geoCoordinates`: longitude and latitude information of the shipping address.

After sending the request, the endpoint will return the response body containing the shipping address information in the shopping cart, as shown in the example below:
[block:code]
{
  "codes": [
    {
      "code": "...\n\"shippingData\": {\n        \"address\": {\n            \"addressType\": \"residential\",\n            \"receiverName\": \"receiver-name\",\n            \"addressId\": \"c1333270f408494c88858ddc8b3de07e\",\n            \"isDisposable\": true,\n            \"postalCode\": \"12345-000\",\n            \"city\": \"Rio de Janeiro\",\n            \"state\": \"RJ\",\n            \"country\": \"BRA\",\n            \"street\": \"Praia de Botafogo\",\n            \"number\": \"300\",\n            \"neighborhood\": \"Botafogo\",\n            \"complement\": \"3rd floor\",\n            \"reference\": \"Grey building\",\n            \"geoCoordinates\": [\n                -47.924747467041016,\n                -15.832582473754883\n            ]\n        },\n...",
      "language": "json"
    }
  ]
}
[/block]

> ℹ️️ For more information about the meaning of each of the fields available in the shopping cart, access the [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) overview.

## Adding a delivery option to the shopping cart

To add a delivery option to the shopping cart, you must have already added a shipping address (according to the [previous section](#adding-a-shipping-address-to-the-shopping-cart)), and use the same [Add shipping address and select delivery option](https://developers.vtex.com/vtex-rest-api/reference/addshippingaddress) endpoint. However, you need to send the request body with the `logisticsInfo` array containing the following information:

- `itemIndex`: item's position in the array or cart.
- `selectedDeliveryChannel`: delivery channel selected by the customer (e.g. "delivery", "pickup-in-point").
- `selectedSla`: selected SLA (e.g. "normal", "express").

After sending the request, the endpoint will return the response body containing the delivery option information in the shopping cart, as shown in the example below:
[block:code]
{
  "codes": [
    {
      "code": "...\n\"logisticsInfo\": [\n            {\n                \"itemIndex\": 0,\n                \"selectedSla\": \"normal\",\n                \"selectedDeliveryChannel\": \"delivery\",\n                \"addressId\": \"954ee939c1274633bfb7a5af4d6c642d\",\n                \"slas\": [],\n                \"shipsTo\": [\n                    \"BRA\"\n                ],\n                \"itemId\": \"5\",\n                \"deliveryChannels\": [\n                    {\n                        \"id\": \"delivery\"\n                    }\n                ]\n            },\n...",
      "language": "json"
    }
  ]
}
[/block]
## Error codes

The following errors may appear as a message in the response body.

### 400 - Bad Request

- **Message error example (code ORD001)**: `"The CEP (XXXX) field in the shipping attachment is invalid"`: this message indicates that the `postalCode` used in the request does not exist or is incorrect.
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"fields\": {},\n    \"error\": {\n        \"code\": \"ORD001\",\n        \"message\": \"The CEP (12340) field in the shipping attachment is invalid\",\n        \"exception\": null\n    },\n    \"operationId\": \"37fcbaf6-9245-46b2-8735-f5fb304d1ac2\"\n}",
      "language": "json"
    }
  ]
}
[/block]
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
- **Message error example (code ORD015)**: `"Unable to communicate with seller VTEX- Test International"`: this message indicates that the `geoCoordinates` used in the request do not exist or are incorrect.
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"fields\": {},\n    \"error\": {\n        \"code\": \"ORD015\",\n        \"message\": \"Unable to communicate with seller VTEX- Test International\",\n        \"exception\": null\n    },\n    \"operationId\": \"37fcbaf6-9245-46b2-8735-f5fb304d1ac2\"\n}",
      "language": "json"
    }
  ]
}
[/block]
- **Message error example (code ORD026)**: `"A communication error with Postal Code Service has occurred"`: this message indicates that the `country` information used in the request is not in three-letter ISO code format or does not exist.
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"fields\": {},\n    \"error\": {\n        \"code\": \"ORD026\",\n        \"message\": \"A communication error with Postal Code Service has occurred\",\n        \"exception\": null\n    },\n    \"operationId\": \"37fcbaf6-9245-46b2-8735-f5fb304d1ac2\"\n}",
      "language": "json"
    }
  ]
}
[/block]
- **Message error example (code CHK0041)**: `"Invalid item index"`: this message indicates that the `itemIndex` used in the request does not exist or is incorrect.
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"fields\": {},\n    \"error\": {\n        \"code\": \"CHK0041\",\n        \"message\": \"Invalid item index\",\n        \"exception\": null\n    },\n    \"operationId\": \"5d9f54e6-7db4-46d6-bca9-deeb278b8b98\"\n}",
      "language": "json"
    }
  ]
}
[/block]
### 404 - Not Found

- **Message error example**: `"The requested URL was not found on the server"`: check that the URL data is correct.
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