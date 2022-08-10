---
title: "Retrieve Blocked Delivery Windows"
slug: "retrieveblockeddeliverywindows"
excerpt: "Lists all blocked delivery windows of your store's carriers, searching by carrier ID."
hidden: false
createdAt: "2020-01-23T15:28:46.231Z"
updatedAt: "2021-03-10T20:18:20.119Z"
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
      "code": "curl --location --request GET 'https://{accountName}.{environment}.com.br/api/logistics/pvt/configuration/carriers/carrierId/getdayofweekblocked' \\\n--header 'Content-Type: application/json; charset=utf-8' \\\n--header 'Accept: application/json' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]