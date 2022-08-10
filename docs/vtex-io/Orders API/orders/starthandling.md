---
title: "Start Handling Order"
slug: "starthandling"
excerpt: "Change a Status Order to start-handling by Order ID. For example: in case you need change to {{start-handling}} the order status of order Id {{v5025004rjc-09}}, you will have to replace the variables {{orderId}} for {{v5025004rjc-09}} and status to {{start-handling}}"
hidden: false
createdAt: "2019-12-11T00:42:27.604Z"
updatedAt: "2020-10-27T20:59:31.524Z"
---
[block:api-header]
{
  "title": "Attributes"
}
[/block]
| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `orderId` | string | Order ID |
| `status` | string | Status Order that you want to apply |



## Response codes


204 - [No content](https://httpstatuses.com/204)

429 - [Too many requests](https://httpstatuses.com/429)

403 - [The credentials are not enabled to access the service](https://httpstatuses.com/403)

404 - [Not found](https://httpstatuses.com/404)
[block:api-header]
{
  "title": "Request body example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "curl --location --request POST 'https://{{accountName}}.{{environment}}.com.br/api/oms/pvt/orders/{{orderId}}/start-handling' \\\n--header 'Accept: application/json' \\\n--header 'Content-Type: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]