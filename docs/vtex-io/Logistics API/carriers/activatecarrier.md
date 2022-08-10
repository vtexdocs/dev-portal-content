---
title: "Activate Carrier"
slug: "activatecarrier"
excerpt: "Activates a given carrier of your store y carrier ID."
hidden: false
createdAt: "2020-01-23T15:28:46.231Z"
updatedAt: "2020-02-17T13:20:32.061Z"
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
      "code": "curl --location --request POST 'https://{accountName}.{environment}.com.br/api/logistics/pvt/configuration/carriers/carrierId/activation' \\\n--header 'x-vtex-api-appKey: {{X-VTEX-API-AppKey}}' \\\n--header 'x-vtex-api-appToken: {{X-VTEX-API-AppToken}}' \\\n--header 'Content-Type: application/json'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]