---
title: "Get cart information by ID"
slug: "get-cart-information-by-id"
hidden: false
createdAt: "2022-10-07T17:07:32.040Z"
updatedAt: "2022-11-17T12:27:47.716Z"
---

The shopping cart is where the information on the products chosen by the customer while browsing a store is gathered. This data may include item prices, shipping value, payment, and delivery methods, among others.

This guide will describe how to access information for a specific shopping cart by its identification code (`orderFormId`).

## Getting shopping cart ID

The first step is to get the `orderFormId` of the shopping cart you want to check. You can obtain this information in the following ways:

1. Creating a new cart using the [Create a new cart](https://developers.vtex.com/vtex-rest-api/reference/createanewcart) endpoint. The response body of this request will give you the `orderFormId` for an empty cart. See more information at [Create a new cart Guide](https://dash.readme.com/project/vtex-rest-api/v2.1/docs/create-a-new-cart).
2. Accessing the website where a shopping cart is open (the order has not already been concluded), and following these steps:
   a. Go to the **Dev. Tools** screen (press the `F12` key).
   b. Click the **Application** tab, and under **Cookies**, click the name of the site's URL.
   c. In the table, locate the line `checkout.vtex.com` and record the value `_ofid=`. This is the `orderFormId` of the current shopping cart.

![orderFormId Dev Tools](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/get-cart-information-by-id-0.png)

## Accessing shopping cart information

With the `orderFormId` information available, you must use the [Get cart information by ID](https://developers.vtex.com/vtex-rest-api/reference/getcartinformationbyid) endpoint to send the following information through the URL:

- **Path param**: `orderFormId` value.
- **Query param**: `refreshOutdatedData`. You can set up this query as `false` or `true` to define whether some cart information can be updated by the [Update cart items](https://developers.vtex.com/vtex-rest-api/reference/itemsupdate) endpoint.

See an URL example below:

`https://{accountname}.{environment.com.br}/api/checkout/pub/orderForm/ede846222cd44046ba6c638442c3505a?refreshOutdatedData=true`

After sending the request, the endpoint will return the response body containing the shopping cart information, as shown in the example below:
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

> ℹ️ For more information about the meaning of each of the fields available in the shopping cart, access the [orderForm](https://developers.vtex.com/vtex-rest-api/reference/orderform-fields) overview.

## Error code

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
