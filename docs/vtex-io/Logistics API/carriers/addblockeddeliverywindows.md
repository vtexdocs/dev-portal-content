---
title: "Add Blocked Delivery Windows"
slug: "addblockeddeliverywindows"
excerpt: "Adds blocked delivery windows for your store's carriers."
hidden: false
createdAt: "2020-01-23T15:28:46.231Z"
updatedAt: "2020-02-17T13:20:31.877Z"
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
      "code": "curl --location --request POST 'https://{accountName}.{environment}.com.br/api/logistics/pvt/configuration/carriers/carrierId/adddayofweekblocked' \\\n--header 'Content-Type: application/json; charset=utf-8' \\\n--header 'Accept: application/json' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--data-raw '\"2016-08-09T08:00:00\"'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]