---
title: "List Dock By Id"
slug: "dockbyid"
excerpt: "Informs a given dock's information, searching by dock ID."
hidden: false
createdAt: "2020-01-23T15:28:46.231Z"
updatedAt: "2020-02-17T13:20:32.589Z"
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
      "code": "curl --location --request GET 'https://{accountName}.{environment}.com.br/api/logistics/pvt/configuration/docks/dockId' \\\n--header 'Content-Type: application/json; charset=utf-8' \\\n--header 'Accept: application/json' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}'",
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
      "code": "{\n  \"id\": \"1a8bce3\",\n  \"name\": \"Centro de Distribuição Principal\",\n  \"priority\": 0,\n  \"dockTimeFake\": \"1.00:00:00\",\n  \"timeFakeOverhead\": \"00:00:00\",\n  \"salesChannels\": [\n    \"1\",\n    \"2\"\n  ],\n  \"salesChannel\": null,\n  \"freightTableIds\": [\n    \"11cc4b6\",\n    \"teste1\",\n    \"186a2a6\",\n    \"1962962\",\n    \"173a63f\"\n  ],\n  \"wmsEndPoint\": \"\",\n  \"pickupStoreInfo\": {\n    \"isPickupStore\": false,\n    \"storeId\": null,\n    \"friendlyName\": null,\n    \"address\": null,\n    \"additionalInfo\": null,\n    \"dockId\": null\n  }\n}",
      "language": "text",
      "name": "200 - OK"
    }
  ]
}
[/block]