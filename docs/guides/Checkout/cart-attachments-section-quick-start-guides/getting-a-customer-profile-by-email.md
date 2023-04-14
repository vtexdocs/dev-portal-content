---
title: "Getting a customer profile by email"
slug: "getting-a-customer-profile-by-email"
hidden: true
createdAt: "2022-11-14T14:46:37.123Z"
updatedAt: "2022-11-28T16:44:35.966Z"
---

The shopping cart gathers information on the products the customer chooses while browsing a store, such as prices, shipping costs, payment methods, delivery methods, etc. This data may include item prices, shipping value, payment, and delivery methods, among others.

The information added to the customer profile can be used in the shopping cart to reduce the time the customer spends at Checkout and improve their shopping experience. For more information, read [Purchasing with SmartCheckout](https://help.vtex.com/en/tutorial/smartcheckout-customer-information-automatic-fill-in--2Nuu3xAFzdhIzJIldAdtan#purchasing-with-smartcheckout).

This guide will describe how to get client profile information using the email address registered in your store.

## Getting customer profile information

To access the customer profile information, you must use the [Get client profile by email](https://developers.vtex.com/vtex-rest-api/reference/getclientprofilebyemail) endpoint. In this request, you must send the customer's email through the URL address, as in the example below:

`https://{accountname}.{environment.com.br}/api/checkout/pub/profiles?email=test1@test2.com`

After sending the request, the endpoint will return the response body containing the client profile information, as in the example below:

[block:code]
{ "codes": [
    { "code": "...\n{\n  \"userProfileId\": \"fb542e51-5488-4c34-8d17-ed8fcf597a94\",\n  \"profileProvider\": \"VTEX\",\n  \"availableAccounts\": [],\n  \"availableAddresses\": [\n    {\n      \"addressType\": \"residential\",\n      \"receiverName\": \"Clark Kent\",\n      \"addressId\": \"666c2e830bd9474ab6f6cc53fb6dd2d2\",\n      \"isDisposable\": false,\n      \"postalCode\": \"12345-000\",\n      \"city\": \"Metropolis\",\n      \"state\": \"NY\",\n      \"country\": \"USA\",\n      \"street\": \"My street\",\n      \"number\": \"123\",\n      \"neighborhood\": \"My neighborhood\",\n      \"complement\": null,\n      \"reference\": null,\n      \"geoCoordinates\": [\n        -47.924747467041016,\n        -15.832582473754883\n      ]\n    }\n  ],\n  \"userProfile\": {\n    \"email\": \"clark.kent@example.com\",\n    \"firstName\": \"Clark\",\n    \"lastName\": \"Kent\",\n    \"document\": \"12345678900\",\n    \"documentType\": \"cpf\",\n    \"phone\": \"+556199999999\",\n    \"corporateName\": null,\n    \"tradeName\": null,\n    \"corporateDocument\": null,\n    \"stateInscription\": null,\n    \"corporatePhone\": null,\n    \"isCorporate\": false,\n    \"profileCompleteOnLoading\": null,\n    \"profileErrorOnLoading\": null,\n    \"customerClass\": null\n  },\n  \"isComplete\": true\n}\n...", "language": "json" } ] } [/block]

>ℹ️️ Fields not completed in the customer profile will be displayed as `null`.

## Error codes

The following errors may appear as a message in the response body.

### 200 - OK

Despite the `200` code, which indicates the success of the request, if the email used is not registered in your store or the customer profile is invalid or incomplete, the response body will not contain any customer profile information. In these conditions, the [SmartCheckout](https://help.vtex.com/en/tutorial/smartcheckout-customer-information-automatic-fill-in--2Nuu3xAFzdhIzJIldAdtan) feature cannot be used in the shopping cart.

[block:code]
{ "codes": [
    { "code": "{\n    \"userProfileId\": null,\n    \"profileProvider\": null,\n    \"availableAccounts\": [],\n    \"availableAddresses\": [],\n    \"userProfile\": null,\n    \"isComplete\": false\n}", "language": "json" } ] } [/block]

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