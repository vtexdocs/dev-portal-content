---
title: "Partial invoices are fully settled by OMS and Payment gateway"
slug: "partial-invoices-are-fully-settled-by-oms-and-payment-gateway"
type: "improved"
createdAt: "2022-06-27T17:00:00.000Z"
hidden: false
excerpt: "We have updated the architecture of how our OMS communicates with VTEX's Payment gateway so that [partial invoices](https://help.vtex.com/en/tracks/pedidos--2xkTisx4SXOWXQel8Jg8sa/q9GPspTb9cHlMeAZfdEUe) also trigger partial settlements in transactions."
---
We have updated the architecture of how our OMS communicates with VTEX's Payment gateway so that [partial invoices](https://help.vtex.com/en/tracks/pedidos--2xkTisx4SXOWXQel8Jg8sa/q9GPspTb9cHlMeAZfdEUe) also trigger partial settlements in transactions.

Previously, a partial invoice triggered a settlement of the order's full, initial value, despite having changes in value due to changes in the order.

Now, the gateway settles the value corresponding to the invoice inserted. Know more about this change in our Announcement.

No additional setting is needed to activate this feature, the OMS is already operating in the new format automatically.

> ℹ️ The partial invoices feature is available to all VTEX stores, but the partial settlement in the gateway is in beta. Besides, for partial invoices to trigger partial settlements in the transaction, it is necessary to use a connector with the [Payment Provider Protocol](https://help.vtex.com/en/tutorial/payment-provider-protocol--RdsT2spdq80MMwwOeEq0m). Legacy connectors do not support the functionality.

- [Register Change on Order](https://developers.vtex.com/vtex-rest-api/reference/registerchange)
- [Invoice notification](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/oms/pvt/orders/-orderId-/invoice)
- [Retrieve Payment transaction](https://developers.vtex.com/vtex-rest-api/reference/getpaymenttransaction)
- [Update order's partial invoice (send tracking number)](https://developers.vtex.com/vtex-rest-api/reference/updatepartialinvoicesendtrackingnumber)

Their descriptions have been updated to guide you through the change.
