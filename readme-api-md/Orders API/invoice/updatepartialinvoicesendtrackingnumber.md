---
title: "Update order's partial invoice (send tracking number)"
slug: "updatepartialinvoicesendtrackingnumber"
excerpt: "Update a given order, adding its tracking number to its [Partial invoice](https://help.vtex.com/en/tracks/pedidos--2xkTisx4SXOWXQel8Jg8sa/q9GPspTb9cHlMeAZfdEUe).\n\r\n\rAfter using this call to add a tracking number to an order, you can use the [Update order tracking status](https://developers.vtex.com/vtex-rest-api/reference/tracking#updatetrackingstatus) API request to add tracking events.\n\r\n\r> The `Notify invoice` resource is needed to use this API request. This is included in `OMS - Full access` and `IntegrationProfile - Fulfillment Oms`, among other default roles available in the Admin. Learn more about the [License manager roles and resources](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc)."
hidden: false
createdAt: "2019-12-11T00:42:27.604Z"
updatedAt: "2022-06-27T20:21:48.186Z"
---
> Learn more about [Order Invoice Notifications in VTEX Help.](https://help.vtex.com/pt/tutorial/entering-tax-receipts-in-the-order--tutorials_193)


## Request object has the following properties:

| Attribute    | Type        | Description |
| --------------- |:---------:| --------------------------------------:|
| `orderId` | string | Order Id |
| `invoiceNumber` | string | Invoice Number |
| `trackingNumber` | string | Package Tracking Number |
| `trackingUrl` | string | Package Tracking URL |
| `courier` | string | Selected Courier |
| `dispatchedDate` | string | Date when package was dispatched, nullable variable. Datetime format |

## Response object has the following properties:


| Attribute    | Type        | Description |
| --------------- |:---------:| --------------------------------------:|
| `date` | string | Invoice Date |
| `orderId` | string | Order Id |
| `receipt` | string | Invoice receipt confirmation ID |


[block:api-header]
{
  "title": "Request body example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "curl --location --request PATCH 'https://{{accountName}}.{{environment}}.com.br/api/oms/pvt/orders/v5195004lux-01/invoice/7999972' \\\n--header 'Accept: application/json' \\\n--header 'Content-Type: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--data-raw '{\n\t\"trackingNumber\":\"9997LUX\",\n\t\"trackingUrl\":\"http://www.trackingu.rl\",\n\t\"courier\":\"Todos os CEPS\"\n  \"dispatchedDate\":null\n}'",
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
      "code": "{\n  \"date\": \"2019-02-08T13:16:13.4617653+00:00\",\n  \"orderId\": \"00-v5195004lux-01\",\n  \"receipt\": \"527b1ae251264ef1b7a9b597cd8f16b9\"\n}",
      "language": "text",
      "name": "200 - OK"
    }
  ]
}
[/block]