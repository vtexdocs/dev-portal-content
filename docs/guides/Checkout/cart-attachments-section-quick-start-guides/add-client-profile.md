---
title: "Add client profile to the cart"
slug: "add-client-profile"
hidden: true
createdAt: "2022-11-14T18:48:53.756Z"
updatedAt: "2022-11-28T16:43:13.348Z"
---
The shopping cart is where the information on the products chosen by the customer while browsing a store is gathered. This data may include item prices, shipping value, payment, and delivery methods, among others.

This guide will describe how to add a client profile information to the shopping cart by the API.

## Getting shopping cart information

The first step is to get the `orderFormId` of the shopping cart you want to add the client profile information to. For more information, access the [Get cart information by ID](https://developers.vtex.com/vtex-rest-api/docs/get-cart-information-by-id) guide.

## Adding a client profile to the shopping cart

To add a client profile information to the shopping cart, you must use the [Add client profile](https://developers.vtex.com/vtex-rest-api/reference/addclientprofile) endpoint. In this request, you must send the `orderFormId` through the URL address, as shown in the example below:

`https://{accountName}.{environment.com.br}/api/checkout/pub/orderForm/ede846222cd44046ba6c638442c3505a/attachments/clientProfileData`

Additionally, you must send the request body containing the following client information:

- **Mandatory**:
      - `email`: customer's email address.
      - `firstName`: customer's first name.
      - `lastName`: customer's last name.
      - `documentType`: type of document informed by the customer (e.g. CPF in Brazil, SSN in the US).
      - `document`: document number informed by the customer.

- **Recommended (optional)**:
      - `phone`: customer’s phone number.

- **If the client is a legal entity**:
      - `corporateName`: company name.
      - `tradeName`: trade name.
      - `corporateDocument`: corporate document.
      - `stateInscription`: state inscription.
      - `corporatePhone`: corporate phone number.
      - `isCorporate`: `true`.

After sending the request, the endpoint will return the response body containing the client information in the shopping cart, as shown in the example below:

```json
...
"clientProfileData": {
        "email": "customer@examplemail.com",
        "firstName": "first-name",
        "lastName": "last-name",
        "document": "123456789",
        "documentType": "cpf",
        "phone": "+55110988887777",
        "corporateName": "company-name",
        "tradeName": "trade-name",
        "corporateDocument": "12345678000100",
        "stateInscription": "12345678",
        "corporatePhone": "+551100988887777",
        "isCorporate": false,
        "profileCompleteOnLoading": false,
        "profileErrorOnLoading": false,
        "customerClass": null
    }
...
```

> ℹ️️ For more information about the meaning of each of the fields available in the shopping cart, access the [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) overview.

## Error codes

The following errors may appear as a message in the response body.

### 400 - Bad Request

- **Message error example (code ORD002)**: `"Invalid order form"`. The `orderFormId` information is not valid.

```json
{
    "fields": {},
    "error": {
        "code": "ORD002",
        "message": "Invalid order form",
        "exception": null
    },
    "operationId": "5d9f54e6-7db4-46d6-bca9-deeb278b8b98"
}
```

- **Message error example (code ORD007)**: `"The email field in the client profile attachment is invalid"`: this message indicates that the `email` used in the request does not exist or is incorrect.

```json
{
    "fields": {},
    "error": {
        "code": "ORD007",
        "message": "The email field in the client profile attachment is invalid",
        "exception": null
    },
    "operationId": "37fcbaf6-9245-46b2-8735-f5fb304d1ac2"
}
```

### 404 - Not Found

- **Message error example**: `"The requested URL was not found on the server"`: check that the URL data is correct.

```html
<body>
	<h1>404 Not Found</h1>
	<p>The requested URL was not found on this server.</p>
</body>
```