---
title: "Set up order integration"
slug: "erp-integration-set-up-order-integration"
hidden: false
createdAt: "2020-03-11T22:25:23.921Z"
updatedAt: "2022-02-03t13:51:54.342Z"
---

In this step, you will send your orders from VTEX to your ERP or WMS.

## Before you begin

After an order is placed in a VTEX store, it follows a predefined [order flow](https://help.vtex.com/tutorial/order-flow-on-the-oms--tutorials_196) in our Order Management System (OMS). Each [status](https://help.vtex.com/tutorial/order-flow-on-the-oms--tutorials_196#understanding-the-status) has a meaning and specified behavior.

There are two ways to track order status changes on VTEX: [Feed or Hook](https://developers.vtex.com/docs/guides/orders-feed). The feed provides an endpoint you can call to check for status changes, while the hook notifies an endpoint provided by the user whenever there is an order update.

The order integration process using the order feed is illustrated in the diagram below.

![Order integration flowchart](https://user-images.githubusercontent.com/77292838/212993154-0cbf395e-1f65-4a87-8ba9-5f80647365f3.png)

See this [boilerplate implementation of an order feed consumer in C#](https://github.com/vtex/FeedConsumerCSharp) to get you started. If you would like a conceptual overview of our Order Management module, see this [beginner article series](https://help.vtex.com/tracks/orders--2xkTisx4SXOWXQel8Jg8sa) in our Help Center. You can learn more about the order feed [here](https://developers.vtex.com/docs/guides/orders-feed).

## Configuring the order feed

Before using the order feed to track status changes, you should configure the filtering rule applied to it using the [Update feed configuration](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/orders/feed/config) endpoint in the Orders API. You can use the [Retrieve feed configuration](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/orders/feed) endpoint to check the current feed configuration at any time.

### Filter

The feed configuration filters the types of order updates that generate events in the queue. This allows you to select the exact types of updates relevant to your integration. The feed can be filtered by changes in status (`”type”: “FromWorkflow”`) or by any changes made to the order's JSON document (`”type”: “FromOrders”`).

When filtering changes in status (`”type”: “FromWorkflow”`) for ERP integrations, `ready-for-handling` is probably the most important to monitor. `start-handling` and `handling` may also be relevant depending on the architecture of your operation. For marketplaces with third-party fulfillment, `cancelation-request` and `waiting-ffmt-authorization` may also be important.

The other filtering type (`”type”: “FromOrders”`) can also be used to filter changes in status or any other change made to an order, which provides a more customizable option. You can, for example, filter orders that have been delivered or had items removed or added to by the store.

Learn more about how to configure filtering options in this [Feed API guide](https://developers.vtex.com/docs/guides/orders-feed).

> The order feed is unique to each `appKey` / `appToken` so that it can be configured and used by different applications without interfering with each other.

>⚠️ The feed configuration does not validate the inserted values. Make sure the elements in the `filter.status` array follow the spelling of the [OMS workflow strings](https://help.vtex.com/en/tutorial/order-flow-and-status--tutorials_196) exactly.

## Getting feed items

To get a batch of events from the order feed, you should use the [Retrieve feed items](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/orders/feed) endpoint in the Orders API. For each event listed, you should determine whether any action is needed by your middleware, depending on the status.

>⚠️ While the order feed is guaranteed to deliver all order status changes, it does not ensure all events are unique. Make sure your middleware is ready to handle duplicate events.

## Committing feed items

To acknowledge an event from the order feed, you should use the [Commit feed items](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/orders/feed) endpoint in the Orders API. This endpoint receives a list of handles corresponding to the events you acknowledge as received. This action removes the event from the feed.

>⚠️ You should commit every status change, even if there is no action taken. Failing to do so will block you from receiving the other events in the feed.

> Committed or not, all events are automatically excluded from the feed after 4 days. To avoid losing data, your middleware should run continuously.

## Getting order details

If an action is required on a specific order due to its current status, you should use the [Get order](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/oms/pvt/orders/-orderId-) endpoint in the Orders API to get all order details (products, payments, delivery, and customer information). The `orderId` can be obtained from the feed event.

In general, an ERP middleware would take action when the status is `ready-for-handling` by retrieving the order details to send to the ERP. However, other actions can be taken in advanced scenarios, such as notifying your logistics operator when an order is `replaced` or `canceled`.

## Start handling order

After the order details have been successfully submitted to the ERP, the final step is to change the order status to `start-handling`. This should only be done once, using the [Start handling](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/oms/pvt/orders/-orderId-/start-handling) endpoint in the Orders API, to start the order processing step.

## Example

Imagine a simple integration scenario in which a store configured a feed to filter only by the `ready-for-handling` status. This is the expected chain of events for a given order:

1. In a periodical [Retrieve feed items](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/orders/feed) request, the implementation receives an update like this:

   ```json
   [
     {
       "eventId": "ED423DDED4C1AE580CADAC1A4D02DA3F",
       "handle":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR ...",
       "domain": "Fulfillment",
       "state": "ready-for-handling",
       "lastState": "window-to-cancel",
       "orderId": "953712004126-01",
       "lastChange": "2019-08-12T20:54:01.134057Z",
       "currentChange": "2019-08-12T20:54:23.7153839Z"
     }
   ]
   ```

2. Since the order is now `ready-for-handling`, the implementation uses the `orderId` from the event to get more information about that order using the [Get order](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/oms/pvt/orders/-orderId-) API call.

3. With that information, it can send relevant data to the ERP, such as which products and quantities should be shipped.

4. Now that the appropriate action has been taken, the implementation may acknowledge to the feed that this specific item was read, passing its `handle` in a [Commit feed items](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/orders/feed) request.

5. Finally, the implementation should update the order status to `start-handling` with the [Start handling](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/oms/pvt/orders/-orderId-/start-handling) endpoint in the Orders API.

>ℹ️ This is a basic example of a typical order feed ERP integration. More complex cases are possible. For example, you can monitor different types of updates and trigger different actions for each.

## Wrapping up

To learn more, check our [ERP integration FAQ](https://developers.vtex.com/docs/guides/faq-erp-integration).

See also the [Feed v3 API guide](https://developers.vtex.com/docs/guides/orders-feed) and check the order [Feed v3 API reference](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/orders/feed/config).

>ℹ️ You can also use a hook to build a reactive order integration, as opposed to a feed, where the integration must actively retrieve events from the queue. To learn more about Hook and which type of integration is best for you, read the [Feed v3 API guide](https://developers.vtex.com/docs/guides/orders-feed).
