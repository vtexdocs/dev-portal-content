---
title: "Feed v3"
slug: "orders-feed"
hidden: false
createdAt: "2021-03-29T19:21:28.241Z"
updatedAt: "2022-11-29T22:43:22.990Z"
---
The [Orders Feed](https://developers.vtex.com/vtex-rest-api/reference/feed-v3) is basically a list of order updates, meaning that whenever there is an update in an order, it will be included as a new item in the Feed. These updates can be status changes, addition or removal of items by the store, or the order being delivered, for example.

The Feed is therefore not a list of orders but rather a list of events. For example, if an order’s status gets changed to `Approve Payment` and then to `Authorize Shipping`, two events will be received by the Feed: one for each of these updates, both referring to the same order. You can configure the Feed to filter what events will actually generate feed items or not, instead of every update that happens in every single order generating items in the feed queue.

Here you will learn how the Feed and Hook work and how to configure them to build order integrations. Also, towards the end of the article we discuss the particularities of each and why should you choose one over the other given the specific needs of your operation.

## Order integration: Feed vs. List orders

Some stores use the List orders API request to check order status changes. However, this method only returns orders that have already been indexed, and this may lead to some problems:

- If any issue in the system prevents indexation, you will not be able to consume the order list, and order updates may go unseen.

- Because it depends on indexation, the `list` method is slower and has a weaker performance than the Feed.

On the other hand, the Feed has been developed specifically to track order updates. It happens before indexation and does not depend on it, making it the most reliable and fastest method to track order updates.
[block:callout]
{
  "type": "warning",
  "body": "If you already use an integration based on the List orders API request, you should migrate to using the feed. But keep in mind that this means changing the integration flow. See this [order integration guide](https://developers.vtex.com/vtex-rest-api/docs/erp-integration-set-up-order-integration) to learn how to implement this change.",
  "title": "Migrate your integration"
}
[/block]

## Access

Feed v3 and hook configuration and use are only permitted by granting authorization in the Orders Management module.

The Feed application key must have a [role](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc#) with one of the appropriate resources: `Feed v3 and Hook Admin` or `Feed v3 and Hook view only`, depending on the intended use.
[block:callout]
{
  "type": "warning",
  "body": "Each appKey can configure or access only one Feed. This means that different users that share one appKey access the same Feed. For example, if one user commits an item in the queue, that item is removed from the Feed and will be available for neither of those users sharing that same appKey. Therefore we recommend the configuration of one Feed per appKey per user, ensuring each user has access to an exclusive Feed."
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "Before getting data from the Orders Feed queue, you need to configure it. Otherwise, the API will return a `404 not found`. Only after configuration do order updates start appearing on the Feed queue. Below you can learn more about Feed configuration."
}
[/block]

## Configuration

Feed configuration is done through a POST request to the [Create or update Feed configuration](https://developers.vtex.com/vtex-rest-api/reference/feed-v3#feedconfiguration) endpoint.

The body for this request is composed of two objects, the `filter` and the `queue`.

### `filter`

By configuring the filter, you define which order updates should appear in the Feed. There are two types of filters that can be used in the Feed: `FromWorkflow` and `FromOrders`. Below you can see an example of each and more details.

#### `FromWorkflow`

When you use the `FromWorkflow` type configuration, you can only filter order updates by status. You can pass an array of statuses in the field `status`, and whenever an order status is changed to one of those statuses, it appears in the Feed.

The list of possible order statuses can be seen in the article [Order flow in orders management](https://help.vtex.com/en/tutorial/fluxo-de-pedido/#understanding-the-status).

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

[block:callout]
{
  "type": "info",
  "body": "The `FromWorkflow` filtering type may be limited depending on your store’s integration necessities. If you want more filtering options, consider using the filter `FromOrders`."
}
[/block]

#### `FromOrders`

The `FromOrders` type configuration allows you to filter updates in your Feed by any property in the order JSON document, not only changes in status. This is done with a JSONata expression passed in the `expression` field.

```json
"filter": {
    "type": "FromOrders",
    "expression": "status = \"payment-pending\"",
    "disableSingleFire": false
    }
```

[block:callout]
{
  "type": "warning",
  "body": "The two filter configuration types are mutually exclusive. If you pass `FromWorkflow` in the `type` field, you should not include the `expression` field nor the `disableSingleFire` in your body. The reverse is also true. If you pass `type` as `FromOrders`, you should not include the `status` field. Failing to observe this will result in a status `409 conflict` response."
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "If the `filter` is not configured, the `FromWorkflow` type is used, and all status changes will appear on the Feed."
}
[/block]

##### `expression`

This field receives a string with a JSONata query expression that defines what conditions must be met for an order to be included in the Feed.

JSONata is a query and transformation language for JSON data, and you can learn more about it in the [JSONata documentation](https://docs.jsonata.org/overview.html).

This type of filtering provides lots of possibilities that can not be achieved with the `FromWorkflow` type configuration. You can, for example, filter orders that have been delivered or that have had items removed or added to by the store. You can also combine two or more selection criteria. See the examples below:

- Delivered orders

```
isAllDelivered = true
```

- Orders with items added

```
$count(changesAttachment.changesData.itemsAdded) > 0
```

- Orders with items removed

```
$count(changesAttachment.changesData.itemsRemoved) > 0
```

You can also filter multiple properties at once. For example, this is an expression that filters orders that contain at least one refrigerator that costs at least $1000,00:

```
$count(items[name ~> /.*refrigerator.*/i and price>=1000]) > 0
```

See more expression examples:

- Order in specific status and sales channel

```
(status = "ready-for-handling" and salesChannel="2")
```

- Orders from a seller that do not have a specific [trade policy](https://help.vtex.com/pt/tutorial/como-funciona-uma-politica-comercial--6Xef8PZiFm40kg2STrMkMV) (sales channel)

```
(salesChannel.Id != "3" and sellers.id ="sellerId")
```

- Order with restitution/item return

```
$count(packageAttachment.packages.restitutions.Refund.value) > 0
```

- Order invoiced with a specific shipping policy

```
status = "invoiced" and (packageAttachment.packages[$[$contains($string(courier), "Carrier Name")]])
```

>❗ Keep in mind that the `expressions` field receives only strings, and all JSONata expressions have to be escaped. For example, the expression `status = “canceled”` has to be passed as `”status = \\”canceled\\””` to be read correctly by the API.

See an example of a complete `filter` object with a more complex and escaped JSONata expression.

```json
"filter": {
    "type": "FromOrders",
    "expression": "(status = \"handling\" and salesChannel = \"2\"  and $count(packageAttachment.packages.restitutions.Refund.value) > 0)",
    “disableSingleFire”: false
},
```

##### Expression tests

You should validate the events of the configured expression before implementing the filter in your integration. There are three useful tests:

- [The API endpoint for JSONata Testing](https://developers.vtex.com/vtex-rest-api/reference/testjsonataexpression);
- [JSONata Exerciser](https://try.jsonata.org/) which tests the expression against a real JSON file. To perform this test copy the order to JSONata Exerciser and simulate different expressions and requests. Use an order extracted from the [Get Order API endpoint](https://developers.vtex.com/vtex-rest-api/reference/getorder).
- Configure a test feed or hook with a test [appkey](https://developers.vtex.com/docs/guides/getting-started-authentication) and validate that the events meet what was expected.

##### `disableSingleFire`

This field sets a limit to how many times a specific order shows on the Feed after it first meets filtering conditions. If this field is `false`, orders will appear in the Feed only once.
>❗ The `FromOrders` type filter receives order updates whenever any change is made to the order JSON document, providing the order meets the criteria set in the `expression` field. Because of this, if the `disableSingleFire` field is set to `true`, orders may appear more than once on a Feed - even up to hundreds of times in some cases. To prevent that from happening, keep `disableSingleFire` set to `false`.

### `queue`

This object’s properties dictate the behavior of Feed items once they are included in the Feed or are retrieved. This is an example of the `queue`object:

```json
"queue": {
    "visibilityTimeoutInSeconds": 240,
    "messageRetentionPeriodInSeconds": 345600
    }
```

- `visibilityTimeoutInSeconds` - This is the maximum time after retrieving an item from the feed when it can be committed. When a user retrieves the events from the Feed queue using the [Retrieve Feed items](https://developers.vtex.com/vtex-rest-api/reference/feed-v3#getfeedorderstatus1) API request, the returned items are omitted from the Feed by a period of time set in this field. Then the user may take any actions needed and commit those items to the Feed. If not committed, events are returned to the Feed after this period of time expires.

- `MessageRetentionPeriodInSeconds` - Items will be excluded from the Feed - even if not committed - when they stay on the Feed longer than the retention period defined in this field.

### Other fields

There are also a couple of other fields which give us some information on the state of the field:

- `quantity`: current number of messages in the feed, including messages that may not be visible due to time out after retrieval.
- `approximateAgeOfOldestMessageInSeconds`: approximate age of the oldest message in the feed, measured in seconds.

### Examples

Here are two complete example bodies for the [Feed configuration response](https://developers.vtex.com/vtex-rest-api/reference/getfeedconfiguration), using each of the `filter` types:

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

[block:callout]
{
  "type": "info",
  "body": "When a new Feed is configured, its queue is made up of whichever orders are changed starting from the moment of the configuration. If the Feed is reconfigured, events corresponding to the former queue will remain on the Feed until they are committed or until the retention period expires."
}
[/block]

>❗ Should the Feed not receive any new events in its queue for the time set in `messageRetentionPeriodInSeconds`, your configuration will be removed, and you will have to reconfigure it, using the [Feed configuration API call](https://developers.vtex.com/vtex-rest-api/reference/feed-v3#feedconfiguration) in order to continue to use the Feed. So it is important to be mindful of the filter configuration you are using. You can check it at any time using the [Get feed configuration](https://developers.vtex.com/vtex-rest-api/reference/feed-v3#getfeedconfiguration) endpoint.

## Feed readout

Every system that depends on order updates should consume the Feed to be able to take the necessary actions based on that information. The most common behavior is, therefore, that of a store system or an integration reading every event in the Feed and, based on the status, making a decision for each one.
[block:callout]
{
  "type": "warning",
  "body": "When filtering statuses, be aware that all possible order statuses must be dealt with during integration to avoid errors. Special attention should be given to `Status Null`, which may be unidentified and end up being mapped as another status, potentially leading to errors."
}
[/block]

### Example

The Orders Feed can be useful in lots of different ways. For instance, say you want to develop an integration between your ERP and VTEX. This integration could have the following behavior:

1. It retrieves ten events from the Feed.
2. For each one of these ten events, it evaluates to which status the order was changed.
3. If the change was to the `Ready for Handling` status, the integration gets the complete order data, records it in the ERP, updates the status in VTEX to `Preparing Delivery` (informing the start of the handling).
4. Then, it commits the events to the Feed (removing them from the queue).
5. After reading and removing these ten events from the list, the integration moves to the next ten events in the Feed and repeats the whole process.

![feedFlow-min](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/orders-feed-0.png)

Access this [backoffice order integration guide](https://developers.vtex.com/docs/guides/erp-integration-set-up-order-integration) to learn more about how you can integrate VTEX’s order Feed with an ERP.

## Hook

The Hook is a complement to the Feed, which allows integrations to consume order updates data in a different way. Instead of receiving events to form a queue that can be retrieved, the Hook sends the items automatically to an URL provided by the user in the Hook configuration.
[block:callout]
{
  "type": "warning",
  "body": "Since the Hook is a complement, [access](https://developers.vtex.com/vtex-rest-api/docs/feed-v3-1#access) follows the same principles described above for the Feed. This means each appKey can configure or access only one Hook. Different users that share one appKey access the same Hook. Therefore we recommend the configuration of one Hook per appKey per user, ensuring each user has access to an exclusive Hook."
}
[/block]

### Configuration

Similarly to the Feed, the Hook can be configured through a POST call to the [Create or update hook configuration](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/orders/hook/config) endpoint of the Orders API. Here are a couple of example bodies for that request, each with a different type of filter:

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

As you can see, the `filter` object is configured in the same way as the `filter` in the Feed configuration described above. The other object in that body is the `hook` object, which contains information on how the information should be sent to the integration:

- `url` is the path of the endpoint that should receive the information of the order updates.

- `headers` contains the credentials that should be used to access the given endpoint.

- `key` is the endpoint key that should be used to access the given endpoint.

When the hook is configured, VTEX sends a ping to the endpoint given in the configuration request’s body to ensure that it is up and running. It is a `POST` request similar to this:

```json
{
    “hookConfig”: “ping”
}
```

[block:callout]
{
  "type": "warning",
  "body": "The given endpoint should return a status 200 for the above-mentioned request. Otherwise, the Hook API will return a status `400 Bad Request`, and saving the configuration won't be possible."
}
[/block]

[block:callout]
{
  "type": "warning",
  "body": "We recommend configuring the Hook on the main account. This ensures more visibility to commit all events correctly and that the configured endpoint is more frequently notified, and that there is greater, preventing Hook exclusion by inactivity."
}
[/block]

### Hook notifications

If configured, the Hook notifies the integration endpoint whenever an order update happens that meets the conditions specified in the `filter`.

If a new event is not correctly notified to the endpoint, the interval for future retries is recalculated based on an internal geometric progression algorithm.
>❗ If the hook has no notifications for three days, your configuration will be removed, and you will have to reconfigure it, using the [Hook configuration API call](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/orders/hook/config) in order to continue to use it. So it is important to be mindful of the filter configuration you are using. You can check it at any time using the [Get hook configuration](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/orders/hook/config) endpoint.

[block:callout]
{
  "type": "warning",
  "body": "When notified, the configured endpoint must always respond with HTTP status 200 within 5000 ms."
}
[/block]
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

[block:callout]
{
  "type": "warning",
  "body": "When using the Hook, it is important to be aware that it is a reactive feature. This means your middleware or ERP system must be ready to deal with whatever volume of data is sent by the Hook. Large peaks in sales - due to Black Friday, for example - tend to generate increase in Hook notifications. If the implementation is not prepared for this peak, it may cause the integration to malfunction, compromising the store’s ability to handle orders and receive further notifications. Learn more about how to deal with this issue in the next session."
}
[/block]

## Feed or Hook, which should you use?

Both the Feed and the Hook allow you to get order updates automatically in order to integrate with other systems and improve your store’s processes. However, they are different and it is important to understand which one best suits your needs.

Getting order updates from the Feed requires the integration to make periodical API calls, each time returning whatever number of updates is available. The Hook on the other hand, notifies the integration whenever there is a new update available. This means the Feed is active, whereas the Hook is reactive.

Because of this, the Hook can be more efficient and provide a lower response time for each order update. But as it is a reactive feature, the integration must have scalability so it can handle great variations in data volume, such as can be caused by a Black Friday sales peak, for example.

Some ERP, for instance, do not have this scaling capacity. So if you integrate the Hook with an ERP, a possible workaround is to build middleware able to handle large variations in the volume of data received from the Hook, but to have the integration send data along to the ERP at a lower speed according to the ERP’s capability.

Another possibility is to use the Hook as the primary source of data for the integration and the Feed as a backup source that may be called upon in case the Hook integration has trouble scaling.

Therefore we recommend the Hook for larger and more complex operations, which tend to have greater middleware scalability capacity and benefit more from the feature’s efficiency.

On the other hand, the Feed requires active retriving and commiting items in the queue. This means the integration has control over how many order updates it receives, knowing how much data it needs to be able to handle at any given time. Because of this it is less likely that the integration crashes or misses updates on the queue.

To learn more, see this guide on [order integration with ERP](https://developers.vtex.com/docs/guides/erp-integration-set-up-order-integration) and the API reference for the [Feed v3](https://developers.vtex.com/vtex-rest-api/reference/feed-v3) and the [Hook](https://developers.vtex.com/docs/guides/orders-overview#creating-an-order-integration).
