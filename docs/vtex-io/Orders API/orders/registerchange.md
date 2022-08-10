---
title: "Register Change on Order"
slug: "registerchange"
excerpt: "Register an order change of product or amount. Order status that allows Order Change: {{handling}}, {{waiting-for-fulfillment}}, and {{ready-for-invoicing}}."
hidden: false
createdAt: "2019-12-11T00:42:27.604Z"
updatedAt: "2021-06-07T13:03:29.062Z"
---
> Learn  more about [Changing completed orders in our article](https://help.vtex.com/en/tutorial/changing-completed-orders--tutorials_190)



| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `orderId` | string | Order ID |
| `reason` | string | Order Change Reason |
| `discountValue` | integer | Order Change Discount Value (in cents) |
| `incrementValue` | integer | Order Change Increment Value (in cents) |
| `itemsRemoved` | object | Object of items removed details |
| `itemsAdded` | object | Object of items added details |
| `id` | string | Changed Item ID |
| `price` | integer | Changed Item Price (in cents) |
| `quantity` | integer | Changed Item Quantity |
[block:callout]
{
  "type": "warning",
  "title": "Prices and discounts expressed in cents",
  "body": "Take note that `discountValue`, `incrementValue` and `price` should be expressed in cents. As such, $100 would be written as `10000` in the request body."
}
[/block]
## Response object has the following properties:


| Attribute    | Type        | Description |
| --------------- |:---------:| --------------------------------------:|
| `date` | string |  Order Change Date |
| `orderId` | string | Order ID |
| `receipt` | string |  Order Change Receipt ID |

[block:api-header]
{
  "title": "Request body example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "curl --location --request POST 'https://{{accountName}}.{{environment}}.com.br/api/oms/pvt/orders/{{orderId}}/changes' \\\n--header 'Accept: application/json' \\\n--header 'Content-Type: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--data-raw '{\n  \"itemsAdded\": [\n    {\n      \"id\": \"1234568064\",\n      \"quantity\": 1,\n      \"price\": 0\n    },\n    {\n      \"id\": \"1234568356\",\n      \"quantity\": 1,\n      \"price\": 90\n    }\n  ],\n  \"itemsRemoved\": [\n    {\n      \"id\": \"267\",\n      \"quantity\": 1,\n      \"price\": 8990\n    }\n  ],\n  \"reason\": \"Unavailable Product\",\n  \"discountValue\": 8900,\n  \"incrementValue\": 0\n}'",
      "language": "text",
      "name": "Request example"
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
      "code": "{\n  \"date\": \"2019-02-08T13:54:33.6868469+00:00\",\n  \"orderId\": \"v502538llux-01\",\n  \"receipt\": \"535d4581-a2a2-4fd2-a206-1c61eae91b1e\"\n}",
      "language": "text",
      "name": "200 - OK"
    }
  ]
}
[/block]