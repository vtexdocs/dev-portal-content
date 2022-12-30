---
title: "Send payment notification"
slug: "sendpaymentnotificationpiicompliant"
excerpt: "Send a payment notification of a given order, by order ID and payment ID.\n\r\n\r> The `Notify payment` resource is needed to use this API request. This is included in `OMS - Full access` and `IntegrationProfile - Fulfillment Oms`, among other default roles available in the Admin. Learn more about the [License manager roles and resources](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc#)."
hidden: true
createdAt: "2022-04-26T15:47:38.592Z"
updatedAt: "2022-04-26T19:59:29.461Z"
---
> Learn more about [Transaction Details in VTEX Help](https://help.vtex.com/en/tutorial/how-to-view-the-orders-details)


## Request object has the following properties:

| Attribute    | Type        | Description |
| --------------- |:---------:| --------------------------------------:|
| `orderId` | string | Order Id |
| `paymentId` | string | Payment ID |


## Response codes


200 - Success

400 - Bad request

403 - The credentials are not enabled to access the service

404 - Value not found 

429 - Too many requests


## Request body example

```json
curl --location --request POST 'https://{{accountName}}.{{environment}}.com.br/api/oms/pvt/orders/{{orderId}}/payments/{{paymentId}}/payment-notification' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \
--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}'
```