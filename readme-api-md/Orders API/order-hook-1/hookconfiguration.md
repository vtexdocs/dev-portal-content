---
title: "Create or update hook configuration"
slug: "hookconfiguration"
excerpt: "Configures filtering rules applied to orders hook. Learn more with the [orders hook guide](https://developers.vtex.com/vtex-rest-api/docs/orders-feed#hook).\n\r\n\rThere are two types of filtering that can be used: \n\r\n\r - `FromWorkflow`: filters orders by status.\n\r\n\r - `FromOrders`: uses JSONata expressions to filter orders according to any property in the orders JSON document.\n\r\n\r This enables stores to filter delivered orders and orders in which products have been added or removed, for example.\n\r\n\rTo learn more, access the [JSONata documentation](https://docs.jsonata.org/overview.html) and test filtering JSONata expressions with our [expressions API](https://developers.vtex.com/vtex-rest-api/reference/feed-v3#testjsonataexpression)."
hidden: false
createdAt: "2019-12-11T00:42:27.604Z"
updatedAt: "2022-09-06T20:48:28.109Z"
---
[block:callout]
{
  "type": "info",
  "body": "Learn more with the [Feed v3 guide.](https://developers.vtex.com/vtex-rest-api/docs/feed-v3-1)"
}
[/block]
| Status avaible to filter    |
| --------------------------- |
|order-created|
|on-order-completed|
|payment-pending| 
|waiting-for-order-authorization|
|approve-payment|
|payment-approved|
|request-cancel|
|waiting-for-seller-decision|
|authorize-fulfillment|
|order-create-error|
|order-creation-error|
|window-to-cancel|
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

[block:callout]
{
  "type": "info",
  "body": "Learn more about [Order Status in VTEX Help.](https://help.vtex.com/en/faq/from-to-for-order-status)"
}
[/block]





## Response codes


200 - Success

400 - Bad Request  - "Unable to check address" / "Only https scheme is accepted"

403 - The credentials are not enabled to access the service

404 - Value not found 

429 - Too many requests

The status event will be removed, if it can't deliver a message more than 100 times, 4 days progressively.



[block:api-header]
{
  "title": "Request body examples"
}
[/block]
`FromWorkflow`
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"filter\": {\n        \"type\": \"FromWorkflow\",\n        \"status\": [\"order-completed\", \"handling\", \"ready-for-handling\", \"waiting-ffmt-authorization\", \"cancel\"]\n    },\n    \"hook\": {\n        \"url\": \"https://endpoint.example/path\",\n        \"headers\": {\n            \"key\": \"value\"\n        }\n    }\n}",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]
`FromOrders`
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"filter\": {\n        \"type\": \"FromOrders\",\n        \"expression\": \"status = \\\"payment-pending\\\"\",\n        \"disableSingleFire\": false\n    },\n    \"hook\": {\n        \"url\": \"https://endpoint.example/path\",\n        \"headers\": {\n            \"key\": \"value\"\n        }\n    }\n}",
      "language": "text"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Response body example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"Domain\": \"Fulfillment\",\n  \"OrderId\": \"v52277740atmc-01\",\n  \"State\": \"ready-for-handling\",\n  \"LastState\": \"window-to-cancel\",\n  \"LastChange\": \"2019-08-14T17:11:39.2550122Z\",\n  \"CurrentChange\": \"2019-08-14T17:12:48.0965893Z\",\n  \"Origin\": {\n    \"Account\": \"automacaoqa\",\n    \"Key\": \"vtexappkey-appvtex\"\n  }\n}",
      "language": "text",
      "name": "200 - OK"
    }
  ]
}
[/block]