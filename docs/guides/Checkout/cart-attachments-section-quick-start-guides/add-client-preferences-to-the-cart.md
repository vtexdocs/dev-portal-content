---
title: "Add client preferences to the cart"
slug: "add-client-preferences-to-the-cart"
hidden: true
createdAt: "2022-11-23T17:14:33.259Z"
updatedAt: "2022-11-28T18:28:09.484Z"
---
The shopping cart is where the information on the products chosen by the customer while browsing a store is gathered. This data may include item prices, shipping value, payment, and delivery methods, among others.

This guide will describe how to add client preferences information (website languages and newsletter options) to the shopping cart by the API.

## Getting shopping cart information

The first step is to get the `orderFormId` of the shopping cart that you want to add client preferences information to. For more information, access the [Get cart information by ID](https://developers.vtex.com/vtex-rest-api/docs/get-cart-information-by-id) guide.

## Adding client preferences to the shopping cart

To add client preferences information to the shopping cart, you need to use the [Add client preferences](https://developers.vtex.com/vtex-rest-api/reference/addclientpreferences) endpoint. In this request, you must send the `orderFormId` through the URL address, as shown in the example below:

`https://{accountName}.{environment.com.br}/api/checkout/pub/orderForm/ede846222cd44046ba6c638442c3505a/attachments/clientPreferencesData`

Additionally, you need to send the request body containing the following client preferences information:

- `locale`: determines website language chosen by the shopper (e.g. PT, EN, ES).
- `optinNewsLetter`: indicates whether the shopper opted in to receive the store's newsletter.

See a request body example below:
[block:code]
{
  "codes": [
    {
      "code": "{\n     \"locale\": \"EN\",\n     \"optinNewsLetter\": true\n}",
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
      "code": "...\n\"clientPreferencesData\": {\n        \"locale\": \"EN\",\n        \"optinNewsLetter\": true\n    }\n...",
      "language": "json"
    }
  ]
}
[/block]

>ℹ️ For more information about the meaning of each of the fields available in the shopping cart, access the [orderForm](https://developers.vtex.com/vtex-rest-api/reference/orderform-fields) overview.

## Error codes

The following errors may appear as a message in the response body.

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