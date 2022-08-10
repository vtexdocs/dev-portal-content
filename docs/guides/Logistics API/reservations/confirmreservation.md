---
title: "Confirm reservation"
slug: "confirmreservation"
excerpt: "Confirms reservation by reservation ID."
hidden: false
createdAt: "2020-01-23T15:28:46.231Z"
updatedAt: "2021-05-24T15:32:45.605Z"
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
      "code": "curl --location --request POST 'https://{accountName}.{environment}.com.br/api/logistics/pvt/inventory/reservations/reservationId/confirm' \\\n--header 'Content-Type: application/json; charset=utf-8' \\\n--header 'Accept: application/json' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--data-raw ''",
      "language": "text"
    }
  ]
}
[/block]