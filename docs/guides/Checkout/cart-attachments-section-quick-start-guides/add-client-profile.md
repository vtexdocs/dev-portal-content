---
title: "Adding customer profile information to the cart"
slug: "add-customer-profile-information-to-the-cart"
hidden: true
createdAt: "2022-11-14T18:48:53.756Z"
updatedAt: "2022-11-28T16:43:13.348Z"
---

The shopping cart gathers information on the products the customer chooses while browsing a store, such as prices, shipping costs, payment methods, delivery methods, etc. This data may include item prices, shipping value, payment, and delivery methods, among others.

This guide will describe how to add customer profile information to the shopping cart via API.

## Getting shopping cart information

The first step is to get the `orderFormId` of the shopping cart to which you want to add the customer preferences information. For more information, read the [Getting cart information by ID](https://developers.vtex.com/docs/guides/get-cart-information-by-id) guide.

## Adding customer profile information to the shopping cart

To add customer profile information to the shopping cart, use the [Add client profile](https://developers.vtex.com/vtex-rest-api/reference/addclientprofile) endpoint. In this request, you must send the `orderFormId` through the URL address, as shown in the example below:

`https://{accountName}.{environment.com.br}/api/checkout/pub/orderForm/ede846222cd44046ba6c638442c3505a/attachments/clientProfileData`

Additionally, you need to send the request body containing the following customer information:

- **Required**:
      - `email`: Customer email address.
      - `firstName`: Customer first name.
      - `lastName`: Customer last name.
      - `documentType`: Type of document provided by the customer (e.g., CPF in Brazil, SSN in the U.S.).
      - `document`: Document number provided by the customer.

- **Recommended (optional)**:
      - `phone`: Customer phone number.

- **If the client is a legal entity**:
      - `corporateName`: Company name.
      - `tradeName`: Trade name.
      - `corporateDocument`: Corporate document.
      - `stateInscription`: State document number.
      - `corporatePhone`: Business phone number.
      - `isCorporate`: `True`.

After sending the request, the endpoint will return the response body containing the client information in the shopping cart, as in the example below:

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

> ℹ️️ For more information on each field available in the shopping cart, see the [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) overview.

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

- **Message error example (code ORD007)**: `"The email field in the customer profile attachment is invalid"`: This message indicates that the `email` used in the request does not exist or is incorrect.

```json
{
    "fields": {},
    "error": {
        "code": "ORD007",
        "message": "The email field in the customer profile attachment is invalid",
        "exception": null
    },
    "operationId": "37fcbaf6-9245-46b2-8735-f5fb304d1ac2"
}
```

### 404 - Not Found

- **Message error example**: `"The requested URL was not found on the server"`: Check if the URL is correct.

```html
<body>
    <h1>404 Not Found</h1>
    <p>The requested URL was not found on this server.</p>
</body>
```