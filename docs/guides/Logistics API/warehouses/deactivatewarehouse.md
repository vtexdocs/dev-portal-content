---
title: "Deactivate warehouse"
slug: "deactivatewarehouse"
excerpt: "Deactivates a given warehouse by warehouse ID."
hidden: false
createdAt: "2020-01-23T15:28:46.231Z"
updatedAt: "2021-05-24T15:32:45.206Z"
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
      "code": "curl --location --request POST 'https://{accountName}.{environment}.com.br/api/logistics/pvt/configuration/warehouses/warehouseId/deactivation' \\\n--header 'x-vtex-api-appKey: {{X-VTEX-API-AppKey}}' \\\n--header 'x-vtex-api-appToken: {{X-VTEX-API-AppToken}}' \\\n--header 'Content-Type: application/json'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]