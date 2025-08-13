---
title: "Feed v3"
slug: "orders-feed"
hidden: false
createdAt: "2021-03-29T19:21:28.241z"
updatedAt: "2025-05-20T14:42:22.990Z"
---

The [order feed](https://developers.vtex.com/docs/guides/orders-overview#feed-v3) is a list of order updates. This means that whenever an order is updated, the event is included as a new entry in the feed. Updates can include status changes, items added or removed by the store, order delivered, and others.

In this sense, the feed is not a list of orders, but rather a list of events. For example, if the status of an order is changed to `Approve payment` and then to `Authorize shipping`, the feed will receive two events: one for each update, both related to the same order. You can configure the feed to filter the updates that will actually generate feed events, instead of having all updates in all orders generating events in the feed queue.

This guide explains how Feed and Hook work and how to configure them to build order integrations. Also, in the latter part of the article, we explain the differences between each and when to choose one over the other based on the specific needs of your operation.

>ℹ️ Feed and Hook are independent configurations to build order integrations.

## Best practices for integrations

When designing an orders integration, consider the practices below to increase performance and avoid throttling errors:

- Optimize your code to get only the required data.
- Use caching for often-used data.
- Consider including code that catches errors. By ignoring these errors and persisting in making requests, your app will not be able to recover gracefully.
- After getting a 429 status code error, you should stop making additional API requests and wait before retrying. We recommend a 1-minute backoff time.
- Configure your integration to communicate asynchronously with VTEX APIs in order to keep requests in a queue and do other processing tasks while waiting for the next queued job to run.

>⚠️ If your integration is getting 429 status code errors, we recommend you to regulate the rate of your requests for smoother distribution. When the account exceeds the request limit, VTEX Admin might also become unavailable.

## Order integration: Feed vs. List orders

Some stores use the List orders API request to check order status changes. However, this method only returns orders that have already been indexed, which may lead to some problems:

- If a problem in the system prevents indexing, you will not be able to consume the order list, and order updates may not be visible.

- Because the `list` method depends on indexing, it's slower and performs less than the feed.

On the other hand, the feed has been specifically developed to track order updates. It runs before indexing and doesn't depend on it, making it the most reliable and fastest method to track order updates.

>⚠️ If you have an integration based on the List orders API request, you should migrate it to the feed. However, keep in mind that this means changing the integration flow. Read the [order integration guide](https://developers.vtex.com/docs/guides/erp-integration-set-up-order-integration) to learn how to implement this change.

## Access

Configuring and using Feed v3 and Hook is only allowed when authorization is granted in the Order Management module.

The feed's application key must have a [role](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc#) with one of the appropriate resources: `Feed v3 and Hook Admin` or `Feed v3 and Hook view only`, depending on the intended use.

>⚠️ Each [appKey](https://help.vtex.com/en/tutorial/application-keys--2iffYzlvvz4BDMr6WGUtet) can configure or access only one feed. This means that different users sharing an appKey access the same feed. In this case, if a user [commits](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/orders/feed) an item to the queue, the item is removed from the feed and won't be available to any users sharing the same appKey. Therefore, we recommend configuring one feed per appKey per user, ensuring that each user has access to their own feed.

## Configuration

The feed is set up through a POST request to the [Create or update Feed configuration](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/orders/feed/config) endpoint.

The body of this request has two objects, the `filter` and the `queue`.

### `filter`

When you configure the filter, you define which order updates should be displayed in the feed. Two types of filters can be used in the feed: `FromWorkflow` and `FromOrders`. You can see an example and description of each filter below.

#### `FromWorkflow`

When you use the `FromWorkflow` configuration, you can only filter order updates by status. You can pass an array of statuses in the field `status`, and whenever an order status is changed to one of those statuses, an update will appear in the feed.

You can see the list of possible order statuses in the article [Order flow in orders management](https://help.vtex.com/en/tutorial/fluxo-de-pedido/#understanding-the-status).

```json
"filter": {
    "type": "FromWorkflow",
    "status": [
        “order-completed”,
        "ready-for-handling",
        “start-handling”,
        “handling”,
        “waiting-ffmt-authorization”,
        “cancel”
        ]
    }
```

>ℹ️ The `FromWorkflow` filter may be limited for some of the integration needs of your store. If you want more filter options, consider using the `FromOrders` filter.

#### `FromOrders`

`FromOrders` allows you to filter updates in your feed by any property in the order JSON document, not only status changes. This is done with a JSONata expression passed in the `expression` field.

```json
"filter": {
    "type": "FromOrders",
    "expression": "status = \"payment-pending\"",
    "disableSingleFire": false
    }
```

>⚠️ The two filter types are mutually exclusive. If you pass `FromWorkflow` in the `type` field, you should not include the `expression` field nor `disableSingleFire` in the body. The reverse is also true. If you pass `FromOrders` `type`, you should not include the `status` field. If you combine them, you will get a `409 conflict` status response.

>ℹ️ If the `filter` is not configured, the `FromWorkflow` type is used, and all status changes will appear in the feed.

##### `expression`

This field receives a string with a JSONata query expression that defines what conditions must be met for an order to be included in the feed.

JSONata is a query and transformation language for JSON data. You can learn more about it in the [JSONata documentation](https://docs.jsonata.org/overview.html).

This filter offers many possibilities that can't be achieved with the `FromWorkflow` configuration. For example, you can filter orders that have been delivered or had items added or removed by the store. You can also combine two or more selection criteria. See the examples below:

- Delivered orders

```JSONata
finished = true
```

- Orders with added items

```JSONata
$count(changesAttachment.changesData.itemsAdded) > 0
```

- Orders with removed items

```JSONata
$count(changesAttachment.changesData.itemsRemoved) > 0
```

You can also filter multiple properties at the same time. For example, the following is an expression that filters orders that contain at least one refrigerator that costs at least $1000.00:

```JSONata
$count(items[name ~> /.*refrigerator.*/i and price>=1000]) > 0
```

Here are some additional expression examples:

- Order in specific status and trade policy (sales channel)

```JSONata
(status = "ready-for-handling" and salesChannel="2")
```

- Orders from a seller that don't have a specific [trade policy](https://help.vtex.com/en/tutorial/como-funciona-uma-politica-comercial--6Xef8PZiFm40kg2STrMkMV) (sales channel)

```JSONata
(salesChannel.Id != "3" and sellers.id ="sellerId")
```

- Order with refund/item return

```JSONata
$count(packageAttachment.packages.restitutions.Refund.value) > 0
```

- Order invoiced with a specific shipping policy

```JSONata
status = "invoiced" and (packageAttachment.packages[$[$contains($string(courier), "Carrier Name")]])
```

>❗ Keep in mind that the `expression` field receives only strings and all JSONata expressions have to be escaped. For example, the expression `status = “canceled”` has to be passed as `”status = \\”canceled\\””` to be read correctly by the API.

The following is an example of a complete `filter` object with a more complex and escaped JSONata expression.

```json
"filter": {
    "type": "FromOrders",
    "expression": "(status = \"handling\" and salesChannel = \"2\"  and $count(packageAttachment.packages.restitutions.Refund.value) > 0)",
    “disableSingleFire”: false
},
```

##### Expression tests

You should validate the events of the configured expression before implementing the filter in your integration. There are three useful tests:

- [The API endpoint for JSONata Testing](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/orders/expressions/jsonata).
- [JSONata Exerciser](https://try.jsonata.org/) which tests the expression against a real JSON file. To run this test, copy the order to JSONata Exerciser and simulate different expressions and requests. Use an order extracted from the [Get order](https://developers.vtex.com/docs/api-reference/orders-api-pii-version#get-/api/orders/pvt/document/-orderId-) endpoint from the [Orders API - PII data architecture](https://developers.vtex.com/docs/api-reference/orders-api-pii-version#overview).

  >⚠️ Be aware that the [Get order](https://developers.vtex.com/docs/api-reference/orders-api-pii-version#get-/api/orders/pvt/document/-orderId-) endpoint from **Orders API - PII data architecture** differs from the [Get order](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/oms/pvt/orders/-orderId-) endpoint from **Orders API**.

- Configure a test feed or hook with a test [appKey](https://developers.vtex.com/docs/guides/getting-started-authentication) and check whether the events behave as expected.

##### `disableSingleFire`

This field limits how often a specific order shows in the feed after it meets the filter conditions. If this field is `false`, orders will appear in the feed only once.

>❗ The `FromOrders` filter receives order updates whenever any change is made to the order JSON document, provided the order meets the criteria set in the `expression` field. Because of this, if the `disableSingleFire` field is set to `true`, orders may appear more than once in a feed — even hundreds of times in some cases. To prevent that from happening, keep `disableSingleFire` set to `false`.

### `queue`

The properties of this object define the behavior of feed items once they are included in the feed or are retrieved. This is an example of the `queue` object:

```json
"queue": {
    "visibilityTimeoutInSeconds": 240,
    "messageRetentionPeriodInSeconds": 345600
    }
```

- `visibilityTimeoutInSeconds` - This is the maximum time after retrieving an item from the feed when it can be [committed](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/orders/feed). When a user retrieves the events from the feed queue using the [Retrieve Feed items](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/orders/feed) API request, the returned items are omitted from the feed for the time set in this field. Then, the user may take any necessary actions and [commit](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/orders/feed) the items to the feed. If events are not committed, they are returned to the feed after this time expires.

- `MessageRetentionPeriodInSeconds` - Items will be excluded from the feed — even if they aren't [committed](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/orders/feed) — when they stay in the feed longer than the retention period defined in this field.

>⚠️ The minimum value for the `messageRetentionPeriodInSeconds` field is `345600` and the maximum is `1209600`.

### Other fields

There are also a couple of other fields that give us some information about the state of the field:

- `quantity`: Current number of messages in the feed, including messages that may not be visible due to time out after retrieval.
- `approximateAgeOfOldestMessageInSeconds`: Approximate age of the oldest message in the feed (in seconds).

### Examples

Here are two complete example bodies for the [Feed configuration response](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/orders/feed/config), using each `filter` type:

```json
{
    "filter": {
        "type": "FromWorkflow",
        "status": [
            “order-completed”,
            "ready-for-handling",
            “start-handling”,
            “handling”,
            “waiting-ffmt-authorization”,
            “cancel”
        ]
    },
    "queue": {
        "visibilityTimeoutInSeconds": 240,
        "messageRetentionPeriodInSeconds": 345600
    },
    "quantity": 1261,
    "aproximateAgeOfOldestMessageInSeconds": 1113.349305555555
}
```

```json
{
    "filter": {
        "type": "FromOrders",
        "expression": "status = \"payment-pending\"",
        "disableSingleFire": false
    },
    "queue": {
        "visibilityTimeoutInSeconds": 240,
        "messageRetentionPeriodInSeconds": 345600
    },
    "quantity": 1261,
    "aproximateAgeOfOldestMessageInSeconds": 1113.349305555555
}
```

>ℹ️ When a new feed is configured, its queue contains any orders that are changed right after the setup is complete. If the feed is reconfigured, events from the former queue will remain in the feed until they are [committed](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/orders/feed) or the retention period expires.

>❗ If the feed doesn't receive any new events in its queue during the time set in `messageRetentionPeriodInSeconds`, your configuration will be removed, and you will have to reconfigure it with the [Feed configuration API call](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/orders/feed/config) to continue using the feed. Therefore, it's important to be mindful of the filter configuration you are using. You can check it any time using the [Get feed configuration](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/orders/feed/config) endpoint.

## Feed readout

Every system that depends on order updates should consume the feed to be able to take the necessary actions based on that information. The most common behavior is a store system or an integration reading every event in the feed and, based on its status, making a decision for each one.
>⚠️ When filtering statuses, be aware that all possible order statuses must be dealt with during integration to avoid errors. Particular attention should be paid to `Status Null`, which may be unidentified and end up being mapped as another status, which can potentially lead to errors.

### Example

The order feed can be useful in many ways. For instance, say you want to develop an integration between your ERP and VTEX. This integration could have the following behavior:

1. It retrieves ten events from the feed.
2. For each one of the ten events, it evaluates the status the order was changed to.
3. If the order changed to the status `Ready for handling`, the integration gets the complete order data, records it in the ERP, and updates the status on VTEX to `Handling shipping` (which indicates the start of handling).
4. Then, it commits the events to the Feed (removing them from the queue).
5. After reading and removing these ten events from the list, the integration moves to the following ten events in the feed and repeats the process.

![feedFlow-min](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/orders-feed-0.png)

Check the [back-office order integration guide](https://developers.vtex.com/docs/guides/erp-integration-set-up-order-integration) to learn more about how you can integrate the VTEX order feed with an ERP.

## Hook

Hook is a counterpart to Feed. It allows integrations to consume order update data differently. Instead of receiving events to form a queue that can be retrieved, a hook automatically sends the items to a URL provided by the user in the hook configuration.

>⚠️ Since Hook is a counterpart, [access](#access) follows the same principles described for Feed above. This means each appKey can configure or access only one hook. Different users that sharing the same appKey access the same hook. We recommend configuring one hook per appKey per user, ensuring that each user has access to their own hook.

### Hook configuration

Similar to a feed, a hook can be configured through a POST call to the [Create or update hook configuration](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/orders/hook/config) endpoint of the Orders API. Here are a couple of body examples for the request, each using a different filter type:

`FromWorkflow`

```json
{
    "filter": {
        "type": "FromWorkflow",
        "status": [
            "payment-pending"
        ]
    },
    "hook": {
        "url": "https://endpoint.example/path",
            "headers": {
                "key": "value"
            }
    }
}
```

`FromOrders`

```json
{
    "filter": {
        "type": "FromOrders",
        "expression": "status = \"payment-pending\"",
        "disableSingleFire": true
    },
    "hook": {
        "url": "https://endpoint.example/path",
            "headers": {
                "key": "value"
            }
    }
}
```

As you can see, the `filter` object is configured the same way as the `filter` in the feed configuration described above. The other object in the body is the `hook` object, which contains information about how the data should be sent to the integration:

- `url` is the endpoint path that should receive the order update information.

- `headers` contains the credentials that should be used to access the given endpoint.

- `key` is the endpoint key that should be used to access the given endpoint.

When the hook is configured, VTEX sends a ping to the endpoint given in the configuration request body to ensure it is up and running. It is a `POST` request similar to this:

```json
{
    "hookConfig": "ping"
}
```

>⚠️ The given endpoint should return status 200 for the above-mentioned request. Otherwise, the Hook API will return status `400 Bad Request`, and you won't be able to save the configuration.

>⚠️ We recommend configuring the hook in the main account. This ensures more visibility to commit all events correctly and that the configured endpoint is more frequently notified, preventing the hook from being excluded due to inactivity.

### Hook notifications

If configured, the Hook notifies the integration endpoint whenever an order update is made and meets the conditions specified in the `filter`.

If a new event is not correctly notified to the endpoint, the interval for future retries is recalculated based on an internal geometric progression algorithm.

>❗ If the hook has no notifications for three days, your configuration will be removed, and you will have to reconfigure it with the [Hook configuration API](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/orders/hook/config) call to continue using it. Therefore, it's important to be mindful of your filter configuration. You can check it any time using the [Get hook configuration](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/orders/hook/config) endpoint.

>⚠️ When notified, the configured endpoint must always respond with HTTP status 200 within 5000 ms.
Below is an example of a hook notification request body made to the integration endpoint.

```json
{
   "Domain": "Marketplace",
   "OrderId": "v40484048naf-01",
   "State": "payment-approved",
   "LastChange": "2019-07-29T23:17:30.0617185Z",
   "Origin": {
       "Account": "accountABC",
       "Key": "vtexappkey-keyEDF"
   }
}
```

>⚠️ When using a hook, it's important to be aware that it's a reactive feature. This means your middleware or ERP system must be ready to deal with whatever volume of data the hook sends. Large peaks in sales – due to Black Friday, for example – tend to increase hook notifications. If the implementation is not prepared for this peak, it may cause problems in the integration, compromising the store’s ability to handle orders and receive further notifications. Learn more about how to deal with this issue in the next section. Getting order updates from a feed requires the integration to make periodical API calls, returning whatever number of available updates each time, with no guarantee of ordination due to the infrastructure and technology used. A hook, on the other hand, notifies the integration whenever a new update is available. This means a feed is active, whereas a hook is reactive.

Because of this, a hook can be more efficient and provide a lower response time for each order update. But as a reactive feature, the integration must have scalability to handle great variations in data volume, such as can be caused by a Black Friday sales peak, for example.

Some ERPs, for instance, do not have this scaling capacity. If you integrate a hook with an ERP, a possible workaround is to build middleware that is able to handle large variations in the data volume received from the hook and have the integration send the data to the ERP at a lower speed based on the capacity of the ERP.

Another option is using a hook as the primary source of data for the integration and a feed as a backup source that may be used when the hook integration has trouble scaling.

We recommend a hook for larger and more complex operations, which tend to have greater middleware scalability capacity and can benefit more from the feature’s efficiency.

On the other hand, a feed requires active [retrieving](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/orders/feed) and [committing](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/orders/feed) items to the queue. This means the integration has control over how many order updates it receives, and it knows how much data it needs to be able to handle at any given time. For this reason, it is less likely for the integration to crash or miss updates from the queue.

To learn more, read the [order integration with ERP](https://developers.vtex.com/docs/guides/erp-integration-set-up-order-integration) guide and the API reference for [Feed v3](https://developers.vtex.com/vtex-rest-api/reference/feed-v3) and [Hook](https://developers.vtex.com/docs/guides/orders-overview#creating-an-order-integration).
