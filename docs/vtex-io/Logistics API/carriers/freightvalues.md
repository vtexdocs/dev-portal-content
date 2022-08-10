---
title: "List Freight Values"
slug: "freightvalues"
excerpt: "Lists freight values apoointed to your store's carriers, searching by carrier ID and cep."
hidden: false
createdAt: "2020-01-23T15:28:46.231Z"
updatedAt: "2020-02-13T20:28:42.758Z"
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
      "code": "curl --location --request GET 'https://{accountName}.{environment}.com.br/api/logistics/pvt/configuration/freights/carrierId/cep/values' \\\n--header 'Content-Type: application/json; charset=utf-8' \\\n--header 'Accept: application/json' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Response body example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "[\n  {\n    \"zipCodeStart\": \"0\",\n    \"zipCodeEnd\": \"99999999\",\n    \"weightStart\": 1,\n    \"weightEnd\": 1000,\n    \"absoluteMoneyCost\": 1,\n    \"pricePercent\": 0,\n    \"pricePercentByWeight\": 0,\n    \"maxVolume\": 1000000000,\n    \"timeCost\": \"2.00:00:00\",\n    \"country\": \"BRA\",\n    \"operationType\": 0,\n    \"restrictedFreights\": [],\n    \"polygon\": \"\",\n    \"minimumValueInsurance\": 0\n  },\n  {\n    \"zipCodeStart\": \"0\",\n    \"zipCodeEnd\": \"99999999\",\n    \"weightStart\": 1001.001,\n    \"weightEnd\": 10000,\n    \"absoluteMoneyCost\": 15,\n    \"pricePercent\": 0,\n    \"pricePercentByWeight\": 0,\n    \"maxVolume\": 1000000000,\n    \"timeCost\": \"2.00:00:00\",\n    \"country\": \"BRA\",\n    \"operationType\": 0,\n    \"restrictedFreights\": [],\n    \"polygon\": \"\",\n    \"minimumValueInsurance\": 0\n  },\n  {\n    \"zipCodeStart\": \"0\",\n    \"zipCodeEnd\": \"99999999\",\n    \"weightStart\": 10001.001,\n    \"weightEnd\": 100000,\n    \"absoluteMoneyCost\": 20,\n    \"pricePercent\": 0,\n    \"pricePercentByWeight\": 0,\n    \"maxVolume\": 1000000000,\n    \"timeCost\": \"2.00:00:00\",\n    \"country\": \"BRA\",\n    \"operationType\": 0,\n    \"restrictedFreights\": [],\n    \"polygon\": \"\",\n    \"minimumValueInsurance\": 0\n  }\n]",
      "language": "text",
      "name": "200 - OK"
    }
  ]
}
[/block]