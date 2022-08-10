---
title: "Register change on order"
slug: "registerchange"
excerpt: "This request allows [changing an order](https://help.vtex.com/en/tutorial/alteracao-de-itens-de-um-pedido-finalizado--tutorials_190) by:\n\r- Adding items\n\r- Removing items\n\r- Applying discount to the total value of the order\n\r- Incrementing the total value of the order. \n\nIn those scenarios of order changes, it is possible to insert a [Partial invoice](https://help.vtex.com/en/tracks/pedidos--2xkTisx4SXOWXQel8Jg8sa/q9GPspTb9cHlMeAZfdEUe). The total value of the order will be updated after the insertion of the invoice, even when there's a partial invoice scenario. The updated value is settled by VTEX's Payment Gateway. The reimbursement for the shopper is automatic. \n\r\n\rThis action can only be done for orders in these status:\n\r- `handling`\n\r- `waiting-for-fulfillment`. \n\r\n\r> The `Change order` resource is needed to use this API request. This is included in `OMS - Full access` and `IntegrationProfile - Fulfillment Oms`, among other default roles available in the Admin. Learn more about the [License manager roles and resources](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc#)."
hidden: false
createdAt: "2019-12-11T00:42:27.604Z"
updatedAt: "2022-06-27T20:21:47.766Z"
---
[block:callout]
{
  "type": "warning",
  "title": "Prices and discounts expressed in cents",
  "body": "Take note that `discountValue`, `incrementValue` and `price` should be expressed in cents. As such, $100 would be written as `10000` in the request body."
}
[/block]

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