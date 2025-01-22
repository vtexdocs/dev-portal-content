---
title: "Using Master Data v2 triggers to interact with orders"
slug: "using-master-data-v2-triggers-to-interact-with-orders"
hidden: false
createdAt: "2022-05-03T13:57:44.519Z"
updatedAt: "2022-05-03T14:07:07.237Z"
---
This documentation assumes that you use Master Data V2 and are familiar with JSON Schemas.

All Master Data V2 interactions occur through API.  We strongly recommend you use Postman and familiarize with our API [documentation](https://developers.vtex.com/docs/api-reference/master-data-api-v2#overview).

>❗ The Master Data v2 orders entity has been deprecated for all VTEX accounts created after January 2023 and previously existing accounts that did not use it. We do not recommend this feature for creating orders integrations, due to the inconsistencies that may occur. The [orders Feed and Hook](https://developers.vtex.com/vtex-rest-api/docs/orders-feed) is the preferred way to integrate orders. If your store already uses this data entity, migrate your integration to the [orders Feed and Hook](https://developers.vtex.com/vtex-rest-api/docs/orders-feed) as soon as possible.

A trigger is nothing more than configuring a predetermined condition and taking an action (HTTP request or sending an email).

You can use dynamic expressions usind dot notation  in place of variables.
So fetching the order's email address would look something like this:
{!order.clientProfiledata.email}

In this example we will be setting up a trigger that will be activated when the order status changes to invoiced.  You'll be POSTing a JSON Schema with all the necessary information.

Please consult the OMS API documentation to see the list of supported statuses.  Ex: order-completed.

```json
..."v-trigger": [
               {
                   "name": "TestTrigger",
                   "condition": "status=devolucao-completed",
                   "active": true,
                   "action": {...

```

In case of more complicated conditions, or statuses that are not directly supported by the OMS API you can use dot notation to consult a nested value.

You can create conditions based on any value of any field, including nested fields up to the second level.

```json
..."v-trigger": [
               {
                   "name": "TestTrigger",
                   "condition": "Body.ChildOne.ChildTwo=Foo",
                   "active": true,
                   "action": {...





```