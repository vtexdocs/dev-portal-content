---
title: "Update Order Status"
slug: "update-order-status"
excerpt: "API request used to update an order status in VTEX.\n\nThis process is asynchronous and a notification with the order's integration results will be sent to the endpoint specified in the **connectiorEndpoint** field or the **connectiorEndpoint** [App Template](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-app-template), if the connector uses our App template. The field **connectorName** is also optional for connectors that use our App Template and authenticate using the app's auth cookie. \n\nFor a detailed explanation of the steps required to develop a custom connector to become an external marketplace for VTEX sellers, check out our complete [External Marketplace Integration Guide](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-guide)."
hidden: false
createdAt: "2022-04-29T19:11:59.376Z"
updatedAt: "2022-04-29T19:32:22.479Z"
---
## Response body model
[block:code]
{
  "codes": [
    {
      "code": "{\n\t\t\"accountName\": string,\n    \"success\": bool,\n    \"flow\": string,\n    \"operationId\": string,\n    \"marketplaceOrderId\": string,\n\t\t\"code\": string,\n\t\t\"message\": string,\n    \"errors\": \n    [\n        {\n            \"source\": string,\n            \"code\": string,\n            \"description\": string\n        }\n    ],\n    \"fields\": {\n           \"mainOrderId\": string,\n\t\t\t\t\t \"franchiseOrderId\": string\n    }\n}",
      "language": "text",
      "name": "Response body "
    }
  ]
}
[/block]
## Response codes

| Code | Description |
| --- | --- |
| SOI001 | The order was integrated into VTEX successfully |
| SOI002 | The order was approved in VTEX successfully |
| SOI003 | The order was successfully enqueued in our service for processing |
| EOI000 | An unknown error occurred when processing the order, and in this case, the solution would be contacting VTEX for support |
| EOI001 | An unmapped error occurred when processing the order, and more details about the error can be found in the response error list |
| EOI002 | There are no SLAs or items available to fulfill this order. That is: the item(s) can be without stock, inactive in the catalog or not included in connector’s trade policy; the SLA/pickup point chosen in the order is not available or doesn’t have stock for the order’s items; or there aren’t any SLAs available at all to fulfill the order |
| EOI003 | The order total payment value differs from what is expected by the seller, and they do not have Order Authorization rules set up to deal with price divergence |
| EOI004 | This order's cart is invalid. That can mean that either the item(s) in it don’t exist in VTEX catalog or the order's data doesn’t comply with the store configuration (for example, the minimum total value or quantity of items set by the seller was not reached in the order) |
| EOI005 | A validation error occurred while trying to process the order. That is, some field/value sent in the order’s contract is invalid and not filled according to our’s or Checkout/Fulfillment’s documentation |
| EOI006 | An unexpected error occurred in one of VTEX's internal services. Please try to send the request again later, as it’s possible one of our services is going through instabilities |
| EOI007 | The order specified already exists in VTEX and we are not able to create duplicated orders |
| EOI008 | The order cannot be approved because it’s not integrated in VTEX yet |
| EOI009 | This order is out of the valid status to approve, such as canceled, for example |
| EOI010 | The request to our API timed out, meaning we exceeded the response time limit |