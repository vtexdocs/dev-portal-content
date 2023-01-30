---
title: "Get invoiced orders placed in inStore"
slug: "get-invoiced-orders-placed-in-instore"
hidden: false
createdAt: "2022-06-06T14:00:14.522Z"
updatedAt: "2022-08-16T20:27:25.550Z"
---

To get the invoiced orders that were made through inStore, it is necessary that the team of developers responsible for your store create an [integration using the Order Feed](https://developers.vtex.com/docs/guides/erp-integration-set-up-order-integration). To do this, follow the settings below:


1. Configure the feed notifications with the order filter with the following information:
* The `"status"` field with the value `"invoiced"`.
* The `"customData.cart-type"` field with a value of `"INSTORE"`.
2. Once the feed is set up, you can check the notifications of the orders placed by inStore. In the notification, there will be the `"OrderId"` field that must be used in the [Get order](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/oms/pvt/orders/-orderId-) endpoint.
3. Use the [Get order](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/oms/pvt/orders/-orderId-) endpoint to query the order information. The order must contain the following data:
* The `salesChannel` field with the ID of the business policy used by the sales channel.
* The field `"isCheckedIn"` with the value `true` for orders placed in the physical store.

From this information, a billing middleware for the physical store integrated with inStore is required to perform this query. You must contract a middleware from VTEX by contacting [our Support](https://support.vtex.com/hc/en-us).

> ℹ️️ To check the order once, you can also use the [List orders](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/oms/pvt/orders) endpoint, but we do not recommend the use for integrations.
