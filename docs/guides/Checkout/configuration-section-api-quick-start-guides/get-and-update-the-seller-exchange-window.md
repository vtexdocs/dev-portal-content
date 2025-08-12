---
title: "Get and update the seller exchange window"
slug: "get-and-update-the-seller-exchange-window"
hidden: true
createdAt: "2022-12-12t21:19:51.360z"
updatedAt: "2022-12-12T21:36:31.439Z"
---

A [Marketplace](https://help.vtex.com/en/tutorial/integrating-with-marketplace) is a platform where products from different sellers can be offered to customers in a single place. After the customer makes a purchase and the order is created, there may be scenarios in which the original seller of the product needs to be modified, for example, when they cancel the order due to internal unavailability of product fulfillment.

In such situations, after the customer makes the purchase, VTEX allows the marketplace to have a period of time (window) to change sellers and avoid order cancellation. For more information on the process of changing sellers, please read the guides in the [Help Center](https://help.vtex.com/en/tutorial/change-seller--5TBAwO2kOAMw44uyaaQMQO) and the [Developer Portal](https://developers.vtex.com/vtex-rest-api/docs/change-seller).

> ⚠️ The default window for changing a seller is **2 days**. However, you can set the window for up to **30 days**.

This guide describes how to get a seller change window or update the number of days in a marketplace on your account.

## Getting the current seller change window

To get seller change window in a marketplace, you need to use the [Get window to change seller](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pvt/configuration/window-to-change-seller) endpoint as a **GET** request. In this request, you must send the `accountname` in the URL address, as in the example below:

**Method: GET**

`https://{accountName}.{environment.com.br}/api/checkout/pvt/configuration/window-to-change-seller`

After sending the request, the endpoint will return the response body showing the maximum current period (days after the customer's purchase) allowed to perform the seller change:

```json
"4"
```

## Updating the window to change sellers

To update the seller change window (in days), you need to use a request similar to **Get window to change seller**, but as a **POST** request ([Update window to change seller](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/checkout/pvt/configuration/window-to-change-seller)), as in the example below:

**Method: POST**

`https://{accountName}.{environment.com.br}/api/checkout/pvt/configuration/window-to-change-seller`

See a request body example below (10 days):

```json
{
    "waitingTime": 10
    }
```

After sending the request, the endpoint will return `code 201 (Created)` and an empty response body.

To confirm that the new seller change window has been applied to your account, access the [Get window to change seller](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pvt/configuration/window-to-change-seller) endpoint again as a **GET** request.

## Error codes

The following errors may appear as messages in the response body:

### 401 - Unauthorized

- **Message error example (code ORD062)**: `"Unauthorized"`. The credentials (API key and API token) used in this request are incorrect or not authorized to access this information.

```json
{
    "fields": {},
    "error": {
        "code": "ORD062",
        "message": "Unauthorized",
        "exception": null
    },
    "operationId": "8ec4b686-435f-42ab-8cfd-89306f888c3c"
}
```

### 404 - Not Found

- **Message error example**: `"The requested URL was not found on the server"`. Check if the URL is correct.

```html
<body>
    <h1>404 Not Found</h1>
    <p>The requested URL was not found on this server.</p>
</body>
```
