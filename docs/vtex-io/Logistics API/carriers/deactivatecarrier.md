---
title: "Deactivate Carrier"
slug: "deactivatecarrier"
excerpt: "Deactivates a given carrier by carrier ID."
hidden: false
createdAt: "2020-01-23T15:28:46.231Z"
updatedAt: "2020-02-17T13:20:32.161Z"
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
      "code": "curl --location --request POST 'https://{accountName}.{environment}.com.br/api/logistics/pvt/configuration/carriers/carrierId/deactivation' \\\n--header 'x-vtex-api-appKey: {{X-VTEX-API-AppKey}}' \\\n--header 'x-vtex-api-appToken: {{X-VTEX-API-AppToken}}' \\\n--header 'Content-Type: application/json'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]