---
title: "Update Order Status"
slug: "external-marketplace-update-order-status"
hidden: false
createdAt: "2022-06-09T21:07:59.637Z"
updatedAt: "2022-06-09T21:42:27.190Z"
---
[block:callout]
{
  "type": "warning",
  "body": "If you used our previous method for integrating orders, you can still find their documentation in [Order Logs](https://developers.vtex.com/vtex-rest-api/docs/deprecated-order-logs) and [How to collect orders from sales channels](https://developers.vtex.com/vtex-rest-api/docs/deprecated-how-to-collect-orders-from-sales-channels). The previous method, however, will not be maintained. If you are integrating orders for the first time, we recommend you use the instructions in this article.",
  "title": "New method for integrating orders"
}
[/block]
The order flow describes the status, possibilities, and actions throughout the life cycle of an order. With the flow, retailers can also track the mapped order status on the platform. Learn more in [Order flow and status](https://help.vtex.com/en/tutorial/order-flow-and-status--tutorials_196#order-status-details).

It’s important to note that when sending a request to update the order status, if the order is not currently in the correct status at VTEX to advance to the requested one, an error will be returned. That means that the connector has to manage when a status should be updated or not. For example:

- If the order is in the `waiting-for-manual-authorization` status at VTEX, that means the order has a price divergence, and we need to wait for the seller to either reject this order (cancel) or authorize it. Sending an order approval while the order is in this status will fail (with a code `EOI011`) since the seller hasn’t authorized the integration of the order yet.
- In this case, it’s recommended for the connector to try to approve the order at a later time, after receiving the error from Channel Order API, and keep trying until the seller takes action and the status change.
- Another option is to use [Order hooks and feeds](https://developers.vtex.com/vtex-rest-api/docs/orders-feed) from our OMS VTEX module. That way the connector can know when the order status was updated and the approval can be sent.

## API Reference: Update order status

Use the request example below to update the status of an order. The description and requirement of each of the fields present in the request body are found in our [Update Order Status](ref:update-order-status) API Reference.


### Request body

```
{
    "marketplaceOrderId": string,
    "connectorName": string,
    "connectorEndpoint": string,
		"marketplaceOrderStatus": string
}
```

### Order Notification Results
    - **Error**
        - EOI000 - Unknown error
        - EOI001 - Unmapped error
        - EOI008 - Cannot approve an order that is not integrated yet
        - EOI009 - Order out of valid status to approve
    - **Success**
        - SOI002 - Order approved

### Response

```
{
    "marketplaceOrderId": "123456789",
    "accountName": null,
    "code": "SOI003",
    "flow": "ApproveOrder",
    "success": true,
    "operationId": null,
    "errors": null,
    "fields": null,
    "message": "Order successfully enqueued"
}
```

### Notification

```
{
  "marketplaceOrderId": "123456789",
  "accountName": "connections",
  "code": "SOI002",
  "flow": "ApproveOrder",
  "success": true,
  "operationId": "ca254d31-c547-4693-9532-72e060264a88",
  "errors": null,
  "fields": {
    "mainOrderId": "MKP-123456789",
    "franchiseOrderId": null
  },
  "message": "Order approved successfully"
}
```