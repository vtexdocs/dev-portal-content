---
title: "Delete Carrier"
slug: "carrier"
excerpt: "Deletes carrier by carrier ID."
hidden: false
createdAt: "2020-01-23T15:28:46.231Z"
updatedAt: "2020-02-13T20:25:17.075Z"
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
      "code": "curl --location --request DELETE 'https://{accountName}.{environment}.com.br/api/logistics/pvt/configuration/carriers/carrierId' \\\n--header 'Content-Type: application/json; charset=utf-8' \\\n--header 'Accept: application/json' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--data-raw ''",
      "language": "text",
      "name": "Example request"
    }
  ]
}
[/block]