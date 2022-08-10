---
title: "Update Order's partial invoice (Send Tracking Number)"
slug: "updatepartialinvoicesendtrackingnumber"
excerpt: "Update invoice of a given order, with its tracking number."
hidden: false
createdAt: "2019-12-11T00:42:27.604Z"
updatedAt: "2020-10-21T22:18:25.259Z"
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