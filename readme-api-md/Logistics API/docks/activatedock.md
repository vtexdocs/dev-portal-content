---
title: "Activate dock"
slug: "activatedock"
excerpt: "Activates dock through dock ID."
hidden: false
createdAt: "2020-01-23T15:28:46.231Z"
updatedAt: "2021-05-24T15:32:45.036Z"
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
      "code": "curl --location --request POST 'https://{accountName}.{environment}.com.br/api/logistics/pvt/configuration/docks/dockId/activation' \\\n--header 'x-vtex-api-appKey: {{X-VTEX-API-AppKey}}' \\\n--header 'x-vtex-api-appToken: {{X-VTEX-API-AppToken}}' \\\n--header 'Content-Type: application/json'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]