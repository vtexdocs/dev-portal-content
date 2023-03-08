---
title: "How to update a canceled order’s status in VTEX"
slug: "external-marketplace-integration-canceled-orders"
hidden: false
createdAt: "2021-09-02T20:58:44.715Z"
updatedAt: "2022-02-03T20:09:10.012Z"
---

An order can be canceled by the marketplace, or by the VTEX Admin The diagram below describes the notification flow, for cancelling the order and updating the status in VTEX:
![MarketplaceConnections - cancelling order](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/external-marketplace-integration-canceled-orders-0.jpg)

## Cancelling the Order and Updating the status

Follow the steps below, once receiving the notification:



1. Connector receives **Cancel Order notification** from the marketplace.  
We suggest that connectors store notifications in a queue by store for processing.
2. Connectors record the **order integration status**, to validate if the order has been integrated to VTEX, avoiding reprocessing of orders.
3. **For orders that have been integrated in VTEX:**
    a.  Connectors should verify the order status in VTEX through the [Get Order API](https://developers.vtex.com/docs/api-reference/orders-api/#get-/api/oms/pvt/orders/-orderId-). 
Orders with the `invoiced` status cannot be canceled in VTEX right away. Connectors must first issue a return invoice, through the [Order Invoice Notification API](https://developers.vtex.com/docs/api-reference/orders-api/#post-/api/oms/pvt/orders/-orderId-/invoice), use the `“type”=”input”` parameter in the call, to issue a return invoice.
    b. For orders with statuses other than `invoiced`, call the [Cancel Order API](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/oms/pvt/orders/-orderId-/cancel). 
  c. VTEX OMS will receive the request and cancel the order. 
  d.VTEX notifies the connector through the endpoint `/pvt/orders/{orderId}/cancel`. 
  e. Connectors receive the notification and respond with 200 and the payload described below.
  f. Once receiving the response, VTEX updates the order status to `canceled`.  

4. **For orders that have not been integrated in VTEX:**
    a. Inform the user that the order is already canceled in VTEX.

[block:code]
{
  "codes": [
    {
      "code": "{\n    \"orderId\": string, //ID do pedido na VTEX\n    \"receipt\": string, //GUID gerado pelo integrador \n    \"date\": string //Data em que a notificação foi recebido\n}",
      "language": "text",
      "name": "Connector's response example for the cancel order notification"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "warning",
  "body": "Note that if the order status in VTEX is `invoiced`, a return invoice must be sent through the Order Invoice Notification API, before following the Cancel Order flow described below. Use the `\"type\"=\"input\"` parameter in the call, to issue a return invoice.",
  "title": "Order status: invoiced"
}
[/block]

## API Reference

Use the endpoints described below to perform this step. It is important to note that when consuming this API, the connector must have a valid VTEX App Key and App Token.

![MarketplaceConnections Docs - English - Fluxo de chamada das APIs-1](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/external-marketplace-integration-canceled-orders-1.jpg)

>ℹ️ All parameters in the endpoints below must be declared in the request. In case one of the parameters does not have a value, you must still send it as `null`.

### Cancel Order

Check out our [Cancel Order](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/oms/pvt/orders/-orderId-/cancel) API Reference to know more details about this call.


### Order Invoice Notification

Use the request example below to generate an order invoice. Check out our [Order Invoice Notification](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/oms/pvt/orders/-orderId-/invoice) ​API Reference to know more details.

[block:code]
{
  "codes": [
    {
      "code": "{\n   \"type\": \"Output\",\n   \"invoiceNumber\": \"NFe-00001\",\n   \"courier\": \"\",\n   \"trackingNumber\": \"\",\n   \"trackingUrl\": \"\",\n   \"items\": [\n      {\n         \"id\": \"345117\",\n         \"quantity\": 1,\n         \"price\": 9003\n      }\n   ],\n   \"issuanceDate\": \"2019-11-21T00:00:00\",\n   \"invoiceValue\": 9508\n}",
      "language": "text",
      "name": "Order Invoice Notification - Request Example"
    }
  ]
}
[/block]

## Scenario 1: customer cancels order in marketplace

This scenario occurs when the marketplace’s customer cancels an order in the marketplace, and the connector sends the cancellation request to VTEX. 

When to perform: after receiving the cancellation notification from the marketplace

Connectors should:

1. Validate if order has been integrated in VTEX.
2. Validate if order status allows cancellation (all but `invoiced`).
3. If steps 1 and 2 are attended, call the Cancel Order API.
4. Store VTEX's response to the call.
5. Receive cancelling confirmation from VTEX and respond with `200` status, along with the response received in step 4.
6. Log status for cancellation action.

## Scenario 2: orders canceled in VTEX

This scenario occurs when VTEX cancels an order, and connectors should update the marketplace.

1. VTEX OMS sends Order Cancel notification.
2. Connector stores VTEX's response to the call.
3. Receive cancelling confirmation from VTEX and respond with `200` status, along with the response received in step 2.
4. Log status for cancellation action.

## Scenario 3: orders integrated in VTEX with the “canceled” status 

This scenario occurs when connectors list marketplace orders, and orders that had already been integrated in VTEX have been canceled in the marketplace

Connectors should:

1. Validate if order has been integrated in VTEX.
2. Validate if order status allows cancellation (all but `invoiced`).
3. If steps 1 and 2 are attended, call the Cancel Order API.
4. Log status for cancellation action.
