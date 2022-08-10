---
title: "Set up order integration"
slug: "erp-integration-set-up-order-integration"
hidden: false
createdAt: "2020-03-11T22:25:23.921Z"
updatedAt: "2022-02-03T13:51:54.342Z"
---
In this step, you will send your orders from VTEX to your ERP or WMS.

## Before you start

After an order is placed in a VTEX store, it follows a predefined [order flow](https://help.vtex.com/tutorial/order-flow-on-the-oms--tutorials_196) in our Order Management System (OMS). Each [status](https://help.vtex.com/tutorial/order-flow-on-the-oms--tutorials_196#understanding-the-status) has a meaning and specified behavior.

There are two ways to track order status changes in VTEX: the orders [Feed and the Hook](https://developers.vtex.com/vtex-rest-api/docs/feed-v3-1). While the feed provides an endpoint you can call to check for status changes, the hook notifies an endpoint provided by the user whenever there is an order update.

The order integration process using the orders feed is illustrated in the diagram below.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/7df0e42-image4.png",
        "image4.png",
        319,
        602,
        "#dd2574"
      ],
      "sizing": "original",
      "caption": "Order integration flowchart"
    }
  ]
}
[/block]
See this [boilerplate implementation of an orders feed consumer in C#](https://github.com/vtex/FeedConsumerCSharp) to get you started. If you would like a conceptual overview of our Orders Management module, check out this [beginner track](https://help.vtex.com/tracks/orders--2xkTisx4SXOWXQel8Jg8sa) in our Help Center. More details on the orders feed can be found [here](https://developers.vtex.com/vtex-rest-api/docs/feed-v3-1).


## Configure orders feed

Before using the orders feed to track status changes, you should configure the filtering rule applied to it using the [Update feed configuration](https://developers.vtex.com/vtex-rest-api/reference/feedconfiguration) endpoint in the Orders API. You can use the [Retrieve feed configuration](https://developers.vtex.com/vtex-rest-api/reference/getfeedorderstatus1) endpoint to check the current feed configuration at any time.


### Filter

The Feed configuration filters what types of order updates actually generate events in the queue. This allows you to select the exact types of updates that are relevant for your integration. The Feed can be filtered by changes in status (`”type”: “FromWorkflow”`) or by any changes made to the order JSON document (`”type”: “FromOrders”`).

When filtering changes in status (`”type”: “FromWorkflow”`) for ERP integrations, `ready-for-handling` is probably the most important to monitor. `start-handling` and `handling` may also be relevant depending on your operation’s architecture. For marketplaces with external fulfillment, `cancelation-request` and `waiting-ffmt-authorization` may also be pertinent.

The other filtering type (`”type”: “FromOrders”`) can also be used to filter changes in status or any other change made to an order, which provides a much more customizable option. You can, for example, filter orders that have been delivered or that have had items removed or added to by the store. 

Learn more about how to configure filtering options in this [Feed API guide](https://developers.vtex.com/vtex-rest-api/docs/feed-v3-1).
[block:callout]
{
  "type": "info",
  "body": "The orders feed is unique to each `appKey` / `appToken` so that it can be configured and used by different applications with no interference between them."
}
[/block]

[block:callout]
{
  "type": "warning",
  "body": "The feed configuration does not perform any validation on the values inserted. Make sure the elements in the `filter.status` array follow the spelling of the [OMS workflow strings](https://help.vtex.com/tutorial/from-to-for-order-status--frequentlyAskedQuestions_773) exactly."
}
[/block]
## Get feed items

To get a batch of events from the orders feed, you should use the [Retrieve feed items](https://developers.vtex.com/vtex-developer-docs/reference/feed-v3) endpoint in the Orders API. For each event listed, you should determine whether any action is needed by your middleware depending on the status.
[block:callout]
{
  "type": "warning",
  "body": "While the orders feed is guaranteed to deliver all order status changes, it does not guarantee all events are unique. Make sure your middleware is ready to treat duplicate events."
}
[/block]
## Commit feed items

To acknowledge an event from the orders feed, you should use the [Commit feed items](https://developers.vtex.com/vtex-developer-docs/reference/feed-v3) endpoint in the Orders API. This endpoint receives a list of handles corresponding to the events that you acknowledge having received. This action removes the event from the feed.
[block:callout]
{
  "type": "warning",
  "body": "You should commit every status change, even if there is no action to take upon it. Failing to do so will block you from receiving the other events in the feed."
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "Committed or not, all events are automattically excluded from the feed after a period of 4 days. To avoid losing data, your middleware should run continuously."
}
[/block]
## Get order details

If there is any action to be done on a specific order due to their current status, you should use the [Get order](https://developers.vtex.com/vtex-rest-api/reference/getorder) endpoint in the Orders API to get all order details (products, payments, delivery and customer data). The `orderId` can be obtained from the feed event.

In general, an ERP middleware would take action when the status is `ready-for-handling` by retrieving the order details to send to the ERP. But other actions can be taken in advanced scenarios, such as notifying your logistics operator when an order is `replaced` or `cancelled`.


## Start handling order

After order details have been successfully submitted to the ERP, the final step is to change the order status to `start-handling`. This should only be done once, using the [Start handling](https://developers.vtex.com/vtex-rest-api/reference/starthandling) endpoint in the Orders API, to start the order processing stage.


## Example

Let’s imagine a simple integration scenario, in which a store configured a feed to filter only by the status `ready-for-handling`. This is the expected chain of events to happen for a given order:

1. In a periodical [Retrieve feed items](https://developers.vtex.com/vtex-developer-docs/reference/feed-v3) request, the implementation receives an update like this:
    ```json
    [
      {
        "eventId": "ED423DDED4C1AE580CADAC1A4D02DA3F",
        “handle":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR ...",
        "domain": "Fulfillment",
        "state": "ready-for-handling",
        "lastState": "window-to-cancel",
        "orderId": "953712004126-01",
        "lastChange": "2019-08-12T20:54:01.134057Z",
        "currentChange": "2019-08-12T20:54:23.7153839Z"
      }
    ]
    ```

2. Since the order is now `ready-for-handling`, the implementation uses the `orderId` from the event to get more information on that order, using the [Get order](https://developers.vtex.com/vtex-rest-api/reference/getorder) API call.

3. With that information, it can now send pertinent data to the ERP, for example, which products and what quantities should be shipped.

4. Now that the appropriate action has been taken, the implementation may acknowledge to the feed that this specific item was read, passing its `handle` on a [Commit feed items](https://developers.vtex.com/vtex-developer-docs/reference/feed-v3) request.

5. Finally, the implementation should update the order’s status to `start-handling` with the [Start handling](https://developers.vtex.com/vtex-rest-api/reference/starthandling) endpoint in the Orders API.
[block:callout]
{
  "type": "info",
  "body": "This is a basic example of a typical Orders Feed ERP integration. There are many possibilities of more complex use. You can, for example, monitor different types of updates and trigger different actions for each."
}
[/block]
## Wrapping up

To learn more, access our [ERP integration FAQ](https://developers.vtex.com/vtex-developer-docs/docs/faq-erp-integration).

See also the [Feed v3 API guide](https://developers.vtex.com/vtex-rest-api/docs/feed-v3-1) and check the order [Feed v3 API reference](https://developers.vtex.com/vtex-developer-docs/reference/feed-v3).
[block:callout]
{
  "type": "info",
  "body": "You can also use a hook in order to build a reactive order integration, as oposed to the feed, with which the integration must actively retrieve events from the queue. To learn more about the Hook and find out which type is best for you, access the [Feed v3 API guide](https://developers.vtex.com/vtex-developer-docs/docs/feed-v3-1)."
}
[/block]