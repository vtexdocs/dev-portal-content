---
title: "Set up order processing"
slug: "erp-integration-set-up-order-processing"
hidden: false
createdAt: "2020-03-11T21:04:40.735Z"
updatedAt: "2022-04-12T15:06:12.084Z"
---

In this step, you will send order updates from your ERP or WMS to VTEX.

## Before you begin

When an order is processed in an external fulfillment platform such as an ERP or WMS, it's not enough to set up order integration. VTEX should also receive order updates when applicable.

During handling an order can be [changed](https://help.vtex.com/tutorial/change-making-changes-to-an-order--3d1XLIgPQcwaKGyMiWaYog?locale=en), [cancelled](https://help.vtex.com/tracks/orders--2xkTisx4SXOWXQel8Jg8sa/4ts2ItvjYo8wm5gg76miS3) or [invoiced](https://help.vtex.com/tracks/orders--2xkTisx4SXOWXQel8Jg8sa/2WgQrlHTyVo4hLjhUs1LMT). These events should be notified as illustrated in the diagram below.

![Order processing flowchart](https://user-images.githubusercontent.com/77292838/212996730-82bcc38a-58b3-4f03-b91f-f17e1f2e107c.png)

If your freight carrier is integrated with VTEX, all you need to do is inform its identifier and tracking number when invoicing the order and order tracking information will be set up. Otherwise you should add the order tracking updates you want customers to see separately, as seen in the diagram below.

![Order tracking flowchart](https://user-images.githubusercontent.com/77292838/212996800-e7bb2549-175a-4598-b3b3-56c406ae1f21.png)

## Change order

Changing items is a feature that allows your store to modify the items or prices of an order. With this feature, the store can handle eventual changes in orders motivated by customer mistakes, product unavailability, and the inclusion of discounts, among other things. Learn more about how it works and its restrictions in the article [Changing items from a completed order](https://help.vtex.com/en/tutorial/changing-items-from-a-complete-order--tutorials_190#).

Check this [Change order guide](https://developers.vtex.com/docs/guides/change-order) to learn how you can implement this feature to your integration.

## Change seller

If your store is a marketplace, your integration must also be prepared to change which seller is assigned to fulfill a given order. Learn more about the circumstances and limitations of this type of process in the article [How to use the Change Seller feature](https://help.vtex.com/en/tutorial/how-to-use-the-change-seller-feature--5TBAwO2kOAMw44uyaaQMQO#).

To learn how to implement this in your integration, check the [Change seller integration guide](https://developers.vtex.com/docs/guides/change-seller).

## Cancel order

The [Cancel order](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/oms/pvt/orders/-orderId-/cancel) endpoint in the Orders API allows you to cancel an order. Optionally, you can add more information by creating a note in the order timeline using the [Create note](https://developers.vtex.com/docs/api-reference/vtex-do-api#post-/notes) endpoint in the VTEX DO API.

The order cancellation can be confirmed through the orders feed.

>⚠️ Keep in mind that the OMS [order flow](https://help.vtex.com/tutorial/order-flow-on-the-oms--tutorials_196) does not allow an order to be cancelled after it has been invoiced and that order cancellations cannot be reversed.

## Invoice order

The [Order Invoice Notification](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/oms/pvt/orders/-orderId-/invoice) endpoint in the Orders API allows you to notify VTEX that you are ready to ship the order and add invoice information to the order.

>⚠️ Note that invoice information includes tracking number and URL. However this is not required to send the invoice to VTEX. It may be added later.

## Order tracking

Order tracking information is directly related to an order's invoice. An order's tracking number and URL may be sent to VTEX when [first invoicing an order](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/oms/pvt/orders/-orderId-/invoice), or later, with the [Update order's partial invoice API request](https://developers.vtex.com/docs/api-reference/orders-api#patch-/api/oms/pvt/orders/-orderId-/invoice/-invoiceNumber-).

### Tracking messages

Once an order was invoiced and has their tracking number and URL, if the designated carrier is integrated with VTEX, VTEX can log tracking messages and send them to your customers. If your freight carrier is not integrated with VTEX, you should add the tracking messages using the [Update order tracking status](https://developers.vtex.com/docs/api-reference/orders-api#put-/api/oms/pvt/orders/-orderId-/invoice/-invoiceNumber-/tracking) endpoint of the Orders API.

## Wrapping up

If you have done things correctly, you should have set up order processing. This includes sending notifications to VTEX when orders are changed, cancelled or invoiced, as well as when tracking updates are available from non-integrated freight carriers.
