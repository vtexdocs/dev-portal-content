---
title: "Ignore profile data from cart"
slug: "ignore-profile-data"
hidden: false
createdAt: "2022-10-26T12:09:54.957Z"
updatedAt: "2022-11-17T12:40:09.545Z"
---
The shopping cart is where the information on the products chosen by the customer while browsing a store is gathered. This data may include item prices, shipping value, payment, and delivery methods, among others.

All VTEX store user profile information is stored in the [Master Data](https://help.vtex.com/en/tutorial/master-data--4otjBnR27u4WUIciQsmkAw). Through this information, it is possible to automatically fill in the customer's data in the cart using the registered email ([SmartCheckout](https://help.vtex.com/en/tutorial/smartcheckout-customer-information-automatic-fill-in--2Nuu3xAFzdhIzJIldAdtan)).

This guide will describe how to disable the automatic inclusion of user profile data through the email registered in a shopping cart.

## Getting and accessing shopping cart information

The first step is to get the `orderFormId` and access the shopping cart information that you want to ignore profile data. For more information, access the [Get cart information by ID](https://developers.vtex.com/vtex-rest-api/docs/get-cart-information-by-id) guide.

When accessing shopping cart information, make sure that the `clientProfileData` has not been sent to the cart, which is indicated in the example below:

```json
...
"clientProfileData": null
...
```

>⚠️ The request [Ignore profile data](https://developers.vtex.com/vtex-rest-api/reference/ignoreprofiledata) will only work if the `clientProfileData` information has not been sent to the cart yet (as shown above). If the cart already has a `clientProfileData` information, the response status will be `403 Forbidden error`, with an `Access Denied` message.

Example of a cart containing customer profile data, and in which the request [Ignore profile data](https://developers.vtex.com/vtex-rest-api/reference/ignoreprofiledata) cannot be applied:

```json
...
"clientProfileData": {
  "email": "clark.kent@examplemail.com",
  "firstName": "Clark",
  "lastName": "Kent",
  "document": "44444444444",
  "documentType": "cpf",
  "phone": "+5511123456789",
  "corporateName": null,
  "tradeName": null,
  "corporateDocument": null,
  "stateInscription": null,
  "corporatePhone": null,
  "isCorporate": false,
  "profileCompleteOnLoading": false,
  "profileErrorOnLoading": false,
  "customerClass": null
},
...
```

## Disabling profile data from the shopping cart

The `orderFormId` information of the shopping cart must be sent through the URL request, as shown by the URL example below:

`https://{accountname}.{environment.com.br}/api/checkout/pub/orderForm/9620cbb7ebc34ca68a86621428816c5a/profile`

Additionally, you need to send the request body containing the parameter `ignoreProfileData` set as `false` or `true` to define whether profile data should be ignored.

See below an example of the request body:
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"ignoreProfileData\": false\n}",
      "language": "json"
    }
  ]
}
[/block]
After sending the request, the endpoint will return the response body with all fields of the object `clientProfileData` shown as `null`.
[block:code]
{
  "codes": [
    {
      "code": "...\n\"clientProfileData\": {\n  \"email\": null,\n  \"firstName\": null,\n  \"lastName\": null,\n  \"document\": null,\n  \"documentType\": null,\n  \"phone\": null,\n  \"corporateName\": null,\n  \"tradeName\": null,\n  \"corporateDocument\": null,\n  \"stateInscription\": null,\n  \"corporatePhone\": null,\n  \"isCorporate\": false,\n  \"profileCompleteOnLoading\": null,\n  \"profileErrorOnLoading\": null,\n  \"customerClass\": null \n},\n...",
      "language": "json"
    }
  ]
}
[/block]
## Error codes

The following errors may appear as a message in the response body.

### 400 - Bad Request

- **Message error example (code ORD002)**: `"Invalid order form"`. The `orderFormId` information is not valid.
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"fields\": {},\n    \"error\": {\n        \"code\": \"ORD002\",\n        \"message\": \"Invalid order form\",\n        \"exception\": null\n    },\n    \"operationId\": \"4ae9e8e4-0fd1-469a-99b1-71705cbe036f\"\n}",
      "language": "json"
    }
  ]
}
[/block]
### 403 - Forbidden

- **Message error example (code CHK003)**: `"Access Denied"`. The request was sent to a cart that already has `clientProfileData` information. Before processing this request, please delete all client information via the [Remove all personal data](https://developers.vtex.com/vtex-rest-api/docs/remove-all-personal-data) endpoint.

```json
{
    "fields": {},
    "error": {
        "code": "CHK003",
        "message": "Access Denied",
        "exception": null
    },
    "operationId": "4ae9e8e4-0fd1-469a-99b1-71705cbe036f"
}
```

### 404 - Not Found

- **Message error example**: `"The requested URL was not found on the server"`. Check that the URL data is correct.

```html
<body>
	<h1>404 Not Found</h1>
	<p>The requested URL was not found on this server.</p>
</body>
```