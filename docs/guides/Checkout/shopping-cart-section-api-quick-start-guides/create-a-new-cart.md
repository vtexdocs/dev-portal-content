---
title: "Create a new cart"
slug: "create-a-new-cart"
hidden: false
createdAt: "2022-10-10T19:19:27.723Z"
updatedAt: "2022-11-17T12:27:20.530Z"
---
The shopping cart is where the information on the products chosen by the customer while browsing a store is gathered. This data may include item prices, shipping value, payment, and delivery methods, among others.

This guide will describe how to create a new shopping cart with the API.

## Creating the new shopping cart

To create a new shopping cart, you must use the [Create a new cart](https://developers.vtex.com/vtex-rest-api/reference/createanewcart) endpoint. In this request, it is not required to send any additional information (path params, query, or body).

After making the call, the endpoint will return the response body containing the information about the new shopping cart created, as shown in the example below:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"orderFormId\": \"ede846222cd44046ba6c638442c3505a\",\n    \"salesChannel\": \"1\",\n    \"loggedIn\": false,\n    \"isCheckedIn\": false,\n    \"storeId\": null,\n    \"checkedInPickupPointId\": null,\n    \"allowManualPrice\": false,\n    \"canEditData\": true,\n    \"userProfileId\": null,\n    \"userType\": null,\n    \"ignoreProfileData\": false,\n    \"value\": 0,\n    \"messages\": [],\n    \"items\": [],\n    \"selectableGifts\": [],\n    \"totalizers\": [],\n    \"shippingData\": null,\n    \"clientProfileData\": {\n        \"email\": null,\n        \"firstName\": null,\n        \"lastName\": null,\n        \"document\": null,\n        \"documentType\": null,\n        \"phone\": null,\n        \"corporateName\": null,\n        \"tradeName\": null,\n        \"corporateDocument\": null,\n        \"stateInscription\": null,\n        \"corporatePhone\": null,\n        \"isCorporate\": false,\n        \"profileCompleteOnLoading\": null,\n        \"profileErrorOnLoading\": null,\n        \"customerClass\": null\n    },\n...",
      "language": "json"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "For more information about the meaning of each of the fields available in the shopping cart, access the [orderForm](https://developers.vtex.com/vtex-rest-api/reference/orderform-fields) overview."
}
[/block]

## Accessing shopping cart information

You can access the shopping cart information through the [Get cart information by ID](https://developers.vtex.com/vtex-rest-api/reference/getcartinformationbyid) endpoint. See more information at [Get cart information by ID](https://developers.vtex.com/vtex-rest-api/docs/get-cart-information-by-id) guide.


## Error codes

The following error may appear as a message in the response body.

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