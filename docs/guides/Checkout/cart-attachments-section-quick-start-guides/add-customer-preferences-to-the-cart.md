---
title: "Adding customer preferences to the cart"
slug: "add-customer-preferences-to-the-cart"
hidden: true
createdAt: "2022-11-23T17:14:33.259Z"
updatedAt: "2022-11-28t18:28:09.484z"
---

The shopping cart gathers information on the products the customer chooses while browsing a store, such as prices, shipping costs, payment methods, delivery methods, etc. This data may include item prices, shipping value, payment, and delivery methods, among others.

This guide will describe how to add customer preferences information (website locale and newsletter options) to the shopping cart via API.

## Getting shopping cart information

The first step is to get the `orderFormId` of the shopping cart to which you want to add the customer preferences information. For more information, read the [Getting cart information by ID](https://developers.vtex.com/docs/guides/get-cart-information-by-id) guide.

## Adding customer preferences to the shopping cart

To add customer preferences information to the shopping cart, use the [Add client preferences](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/attachments/clientPreferencesData) endpoint. In this request, you must send the `orderFormId` through the URL address, as shown in the example below:

`https://{accountName}.{environment.com.br}/api/checkout/pub/orderForm/ede846222cd44046ba6c638442c3505a/attachments/clientPreferencesData`

Additionally, you need to send the request body containing the following customer preferences information:

- `locale`: Defines the website language chosen by the customer (e.g. PT, EN, ES).
- `optinNewsLetter`: Indicates if the customer subscribed to the store newsletter.

See a request body example below: [block:code]
{ "codes": [
    { "code": "{\n     \"locale\": \"EN\",\n     \"optinNewsLetter\": true\n}", "language": "json" } ] } [/block] After sending the request, the endpoint will return the response body containing the client preferences information in the shopping cart, as in the example below: [block:code]
{ "codes": [
    { "code": "...\n\"clientPreferencesData\": {\n        \"locale\": \"EN\",\n        \"optinNewsLetter\": true\n    }\n...", "language": "json" } ] } [/block]

> ℹ️️ For more information on each field available in the shopping cart, see the [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) overview.

## Error code

The following errors may appear as a message in the response body.

### 400 - Bad Request

- **Message error example (code ORD002)**: `"Invalid order form"`. The `orderFormId` information is not valid. [block:code]
{ "codes": [
  { "code": "{\n    \"fields\": {},\n    \"error\": {\n        \"code\": \"ORD002\",\n        \"message\": \"Invalid order form\",\n        \"exception\": null\n    },\n    \"operationId\": \"5d9f54e6-7db4-46d6-bca9-deeb278b8b98\"\n}", "language": "json" } ] } [/block]

### 404 - Not Found

- **Message error example**: `"The requested URL was not found on the server"`: Check if the URL is correct. [block:code]
{
"codes": [
  {
    "code": "<body>\n\t<h1>404 Not Found</h1>\n\t<p>The requested URL was not found on this server.</p>\n</body>",
    "language": "json"
  }
] } [/block]