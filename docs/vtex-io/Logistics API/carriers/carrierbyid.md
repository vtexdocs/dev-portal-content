---
title: "List Carrier By Id"
slug: "carrierbyid"
excerpt: "Lists information about your store's carriers by searching through the Carrier's ID."
hidden: false
createdAt: "2020-01-23T15:28:46.231Z"
updatedAt: "2020-02-13T20:24:00.370Z"
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
      "code": "curl --location --request GET 'https://{accountName}.{environment}.com.br/api/logistics/pvt/configuration/carriers/carrierId' \\\n--header 'Content-Type: application/json; charset=utf-8' \\\n--header 'Accept: application/json' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}'",
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
      "code": "{\n  \"id\": \"11cc4b6\",\n  \"slaType\": \"Normal\",\n  \"name\": \"Correios PAC\",\n  \"scheduledDelivery\": false,\n  \"maxRangeDelivery\": 0,\n  \"dayOfWeekForDelivery\": null,\n  \"dayOfWeekBlockeds\": [],\n  \"freightValue\": [],\n  \"factorCubicWeight\": 0.0167,\n  \"freightTableProcessStatus\": 1,\n  \"freightTableValueError\": null,\n  \"modals\": [],\n  \"onlyItemsWithDefinedModal\": false,\n  \"deliveryOnWeekends\": true,\n  \"carrierSchedule\": [],\n  \"maxDimension\": {\n    \"weight\": 0,\n    \"height\": 110,\n    \"width\": 110,\n    \"length\": 110,\n    \"maxSumDimension\": 200\n  },\n  \"exclusiveToDeliveryPoints\": false,\n  \"minimunCubicWeight\": 10000,\n  \"isPolygon\": false,\n  \"numberOfItemsPerShipment\": null\n}",
      "language": "text",
      "name": "200 - OK"
    }
  ]
}
[/block]