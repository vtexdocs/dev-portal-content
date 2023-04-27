---
title: "Clearing the orderForm message field from the cart"
slug: "clear-orderform-message-field-from-cart"
hidden: false
createdAt: "2023-01-13t09:00:00.051z"
updatedAt: "2023-01-13T10:00:00.334Z"
---

The orderForm is the main object processed by VTEX Checkout and one of the most important data structures in the architecture of every VTEX store. It stores a lot of contextual information about the order, which is essential for processing order information, such as order items, customer personal information, delivery address, and shipping information.

This guide will describe how to remove all messages from the `messages` field of the orderForm, leaving it empty.

## Removing all messages from the orderForm message field

To remove all messages from the orderForm `messages` field of the shopping cart, you need to use the [Clear orderForm messages](https://developers.vtex.com/vtex-rest-api/reference/clearorderformmessages) endpoint. The `orderFormId` information of the shopping cart must be sent through the URL request, as in the example below:

`https://{accountname}.{environment.com.br}/api/checkout/pub/orderForm/ede846222cd44046ba6c638442c3505a/messages/clear`

Additionally, you need to send the request body containing only two curly brackets, as shown below:

```json
{}
```

After sending the request, the endpoint will return the response body containing the shopping cart information and the `messages` field will empty, as in the example below:

```json

"messages": [],

```

> ℹ️ For more information about the meaning of each field available in the shopping cart, please refer to the [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) overview.

## Error codes

The following errors may appear as messages in the response body:

### 400 - Bad Request

- **Message error example (code 001)**: `"Bad Request"`. This message indicates that information other than `{}` was sent in the request body.

```json
{
    "fields": {},
    "error": {
        "code": "001",
        "message": "Bad request",
        "exception": null
    },
    "operationId": "91b68251-1a60-4716-b846-c7c9c31fa565"
}
```

- **Message error example (code ORD002)**: `"Carrinho inválido"` (*Invalid Cart*). This message indicates that the `orderFormId` used in the request does not exist or is incorrect.

```json
{
    "fields": {},
    "error": {
        "code": "ORD002",
        "message": "Carrinho inválido",
        "exception": null
    },
    "operationId": "5d37a185-bfe6-4686-9d92-aac9482cc63d"
}
```

### 404 - Not Found

- **Message error example**: `"The requested URL was not found on the server"`: check if the URL is correct.

```json
<body>
    <h1>404 Not Found</h1>
    <p>The requested URL was not found on this server.</p>
</body>
```
