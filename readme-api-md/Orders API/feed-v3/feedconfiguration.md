---
title: "Create or update feed configuration"
slug: "feedconfiguration"
excerpt: "The Orders Feed v3 is the best way to create order integrations. Below you can find details on the configuration API specification, and to know more see our [Feed v3 guide](https://developers.vtex.com/vtex-rest-api/docs/orders-feed) and our [order integration guide](https://developers.vtex.com/vtex-rest-api/docs/erp-integration-set-up-order-integration)\n\r\n\rThere are two types of filtering that can be used. The `FromWorkflow` type filters orders by status, whereas the `FromOrders` type uses JSONata expressions to filter orders according to any property in the orders JSON document. This enables stores to filter delivered orders and orders in which products have been added or removed, for example. To learn more, access the [JSONata documentation](https://docs.jsonata.org/overview.html) and test filtering JSONata expressions with our [Test JSONata expression](https://developers.vtex.com/vtex-developer-docs/reference/test-jsonata-expression) endpoint."
hidden: false
createdAt: "2019-12-11T00:42:27.604Z"
updatedAt: "2022-05-03T14:14:34.959Z"
---
Learn more about all [Order Status and flow](https://help.vtex.com/en/tutorial/fluxo-e-status-de-pedidos--tutorials_196) in VTEX OMS.

| Status available to filter    |
| --------------------------- |
|order-created|
|on-order-completed|
|on-order-completed-ffm|
|payment-pending| 
|waiting-for-order-authorization|
|approve-payment|
|payment-approved|
|request-cancel|
|waiting-for-seller-decision|
|waiting-ffmt-authorization|	
|waiting-for-authorization|
|waiting-for-manual-authorization|	
|authorize-fulfillment|
|order-create-error|
|order-creation-error|
|window-to-cancel|
|window-to-change-seller|
|waiting-for-mkt-authorization|
|waiting-seller-handling|
|ready-for-handling|
|start-handling|
|handling|
|invoice-after-cancellation-deny|
|order-accepted|
|invoice|
|invoiced|
|replaced|
|cancellation-requested|
|cancel|
|canceled|


## Response codes

200 - Success

403 - The credentials are not enabled to access the service

404 - Value not found

429 - Too many requests

The event will be removed if the message "send retry" is equal to, or greater than the maximum retention period.

## Request body example
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"filter\": {\n        \"type\": \"FromWorkflow\",\n        \"status\": [\n            “order-completed”,\n            \"ready-for-handling\",\n            “start-handling”,\n            “handling”,\n            “waiting-ffmt-authorization”,\n            “cancel”\n        ]\n    },\n    \"queue\": {\n        \"visibilityTimeoutInSeconds\": 240,\n        \"messageRetentionPeriodInSeconds\": 345600\n    },\n    \"quantity\": 1261,\n    \"aproximateAgeOfOldestMessageInSeconds\": 1113.349305555555\n}",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]