---
title: "List Reservation by Warehouse and SKU"
slug: "reservationbywarehouseandsku"
excerpt: "Lists reservations in your store, by searching through warehouse and SKU."
hidden: false
createdAt: "2020-01-23T15:28:46.231Z"
updatedAt: "2020-02-17T21:20:29.525Z"
---
[block:api-header]
{
  "title": "Request body example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "curl --location --request GET 'https://{accountName}.{environment}.com.br/api/logistics/pvt/inventory/reservations/warehouseId/skuId' \\\n--header 'Content-Type: application/json; charset=utf-8' \\\n--header 'Accept: application/json' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]