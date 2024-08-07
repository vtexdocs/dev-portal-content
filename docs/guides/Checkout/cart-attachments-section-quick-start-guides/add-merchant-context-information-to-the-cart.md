---
title: "Adding merchant context information to the cart"
slug: "add-merchant-context-information-to-the-cart"
hidden: true
createdAt: "2022-11-28T16:53:57.489Z"
updatedAt: "2022-11-28T18:28:26.690Z"
---

The shopping cart gathers information on the products the customer chooses while browsing a store, such as prices, shipping costs, payment methods, delivery methods, etc. This data may include item prices, shipping value, payment, and delivery methods, among others.

This guide will describe how to add relevant information related to a specific order to a shopping cart via API.

## Getting shopping cart information

The first step is to get the `orderFormId` of the shopping cart to which you want to add the merchant context information. For more information, read the [Getting cart information by ID](https://developers.vtex.com/vtex-rest-api/docs/get-cart-information-by-id) guide.

## Adding merchant context information to the shopping cart

To add merchant context information to the shopping cart, you need to use the [Add merchant context data](https://developers.vtex.com/vtex-rest-api/reference/addmerchantcontextdata) endpoint. In this request, you must send the `orderFormId` through the URL address, as in the example below:

`https://{accountName}.{environment.com.br}/api/checkout/pub/orderForm/ede846222cd44046ba6c638442c3505a/attachments/merchantContextData`

Additionally, you need to send the request with the merchant context information within the `salesAssociateData` object. See a request body example containing the vendor (seller) identification code: [block:code]
{ "codes": [
    { "code": "{\n     \"salesAssociateData\": {\n          \"salesAssociateId\": \"seller123\"\n     }\n}", "language": "json" } ] } [/block] After sending the request, the endpoint will return the response body containing the merchant context data in the shopping cart, as in the example below: [block:code]
{ "codes": [
    { "code": "...\n\"merchantContextData\": {\n        \"salesAssociateData\": {\n            \"salesAssociateId\": \"seller123\"\n        }\n    }\n...", "language": "json" } ] } [/block]

> ℹ️️ For more information about the meaning of each field available in the shopping cart, see the [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) overview.

## Error codes

The following errors may appear as a message in the response body.

### 400 - Bad Request

- **Message error example (code ORD002)**: `"Invalid order form"`. The `orderFormId` information is not valid. [block:code]
{ "codes": [
  { "code": "{\n    \"fields\": {},\n    \"error\": {\n        \"code\": \"ORD002\",\n        \"message\": \"Invalid order form\",\n        \"exception\": null\n    },\n    \"operationId\": \"5d9f54e6-7db4-46d6-bca9-deeb278b8b98\"\n}", "language": "json" } ] } [/block]

### 404 - Not Found

- `Message error example: "The requested URL was not found on the server"`: Check if the URL is correct. [block:code]
{
"codes": [
  {
    "code": "<body>\n\t<h1>404 Not Found</h1>\n\t<p>The requested URL was not found on this server.</p>\n</body>",
    "language": "json"
  }
] } [/block]