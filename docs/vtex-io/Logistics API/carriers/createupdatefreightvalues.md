---
title: "Create/Update Freight Values"
slug: "createupdatefreightvalues"
excerpt: "Creates or updates the freight values of your store's carriers."
hidden: false
createdAt: "2020-01-23T15:28:46.231Z"
updatedAt: "2020-02-13T20:28:09.672Z"
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
      "code": "curl --location --request POST 'https://{accountName}.{environment}.com.br/api/logistics/pvt/configuration/freights/carrierId/values/update' \\\n--header 'Content-Type: application/json; charset=utf-8' \\\n--header 'Accept: application/json' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--data-raw '[\n  {\n    \"absoluteMoneyCost\": \"1.00\",\n    \"country\": \"BRA\",\n    \"maxVolume\": 1000000000,\n    \"operationType\": 1,\n    \"pricePercent\": 0,\n    \"pricePercentByWeight\": 0,\n    \"timeCost\": \"2.00:00:00\",\n    \"weightEnd\": 1000,\n    \"weightStart\": 1,\n    \"zipCodeEnd\": \"99999999\",\n    \"zipCodeStart\": \"0\",\n    \"polygon\": \"\"\n  }\n]'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]