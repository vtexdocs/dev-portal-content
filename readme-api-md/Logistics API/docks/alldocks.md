---
title: "List all  docks"
slug: "alldocks"
excerpt: "Informs a list of all docks."
hidden: false
createdAt: "2020-01-23T15:28:46.231Z"
updatedAt: "2021-05-24T15:32:44.949Z"
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
      "code": "curl --location --request GET 'https://{accountName}.{environment}.com.br/api/logistics/pvt/configuration/docks' \\\n--header 'Content-Type: application/json; charset=utf-8' \\\n--header 'Accept: application/json' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}'",
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
      "code": "[\n  {\n    \"id\": \"1a8bce3\",\n    \"name\": \"Centro de Distribuição Principal\",\n    \"priority\": 0,\n    \"dockTimeFake\": \"1.00:00:00\",\n    \"timeFakeOverhead\": \"00:00:00\",\n    \"salesChannels\": [\n      \"1\",\n      \"2\"\n    ],\n    \"salesChannel\": null,\n    \"freightTableIds\": [\n      \"11cc4b6\",\n      \"teste1\",\n      \"186a2a6\",\n      \"1962962\",\n      \"173a63f\"\n    ],\n    \"wmsEndPoint\": \"\",\n    \"pickupStoreInfo\": {\n      \"isPickupStore\": false,\n      \"storeId\": null,\n      \"friendlyName\": null,\n      \"address\": null,\n      \"additionalInfo\": null,\n      \"dockId\": null\n    }\n  },\n  {\n    \"id\": \"1_1_1\",\n    \"name\": \"Doca A\",\n    \"priority\": 1,\n    \"dockTimeFake\": \"00:00:00\",\n    \"timeFakeOverhead\": \"00:00:00\",\n    \"salesChannels\": [\n      \"1\",\n      \"11\",\n      \"4\",\n      \"2\",\n      \"12\",\n      \"13\",\n      \"14\",\n      \"7\",\n      \"16\"\n    ],\n    \"salesChannel\": null,\n    \"freightTableIds\": [\n      \"1962962\",\n      \"teste1\",\n      \"11cc4b6\"\n    ],\n    \"wmsEndPoint\": \"\",\n    \"pickupStoreInfo\": {\n      \"isPickupStore\": false,\n      \"storeId\": null,\n      \"friendlyName\": null,\n      \"address\": null,\n      \"additionalInfo\": null,\n      \"dockId\": null\n    }\n  },\n  {\n    \"id\": \"139270d\",\n    \"name\": \"Doca B\",\n    \"priority\": 0,\n    \"dockTimeFake\": \"1.00:00:00\",\n    \"timeFakeOverhead\": \"1.00:00:00\",\n    \"salesChannels\": [\n      \"1\"\n    ],\n    \"salesChannel\": null,\n    \"freightTableIds\": [],\n    \"wmsEndPoint\": \"\",\n    \"pickupStoreInfo\": {\n      \"isPickupStore\": false,\n      \"storeId\": null,\n      \"friendlyName\": null,\n      \"address\": null,\n      \"additionalInfo\": null,\n      \"dockId\": null\n    }\n  },\n  {\n    \"id\": \"18dd839\",\n    \"name\": \"Doca C\",\n    \"priority\": 0,\n    \"dockTimeFake\": \"00:00:00\",\n    \"timeFakeOverhead\": \"00:00:00\",\n    \"salesChannels\": [\n      \"1\"\n    ],\n    \"salesChannel\": null,\n    \"freightTableIds\": [],\n    \"wmsEndPoint\": \"http://recurrent-env-beta.elasticbeanstalk.com/recorrenciawms\",\n    \"pickupStoreInfo\": {\n      \"isPickupStore\": false,\n      \"storeId\": null,\n      \"friendlyName\": null,\n      \"address\": null,\n      \"additionalInfo\": null,\n      \"dockId\": null\n    }\n  },\n  {\n    \"id\": \"avl\",\n    \"name\": \"Doca InStore\",\n    \"priority\": 0,\n    \"dockTimeFake\": \"1.00:00:00\",\n    \"timeFakeOverhead\": \"1.00:00:00\",\n    \"salesChannels\": [\n      \"18\"\n    ],\n    \"salesChannel\": null,\n    \"freightTableIds\": [],\n    \"wmsEndPoint\": \"\",\n    \"pickupStoreInfo\": {\n      \"isPickupStore\": false,\n      \"storeId\": null,\n      \"friendlyName\": null,\n      \"address\": null,\n      \"additionalInfo\": null,\n      \"dockId\": null\n    }\n  },\n  {\n    \"id\": \"pickup_1\",\n    \"name\": \"Pickup Point 1\",\n    \"priority\": 0,\n    \"dockTimeFake\": \"1.00:00:00\",\n    \"timeFakeOverhead\": \"00:00:00\",\n    \"salesChannels\": [\n      \"1\"\n    ],\n    \"salesChannel\": null,\n    \"freightTableIds\": [],\n    \"wmsEndPoint\": \"\",\n    \"pickupStoreInfo\": {\n      \"isPickupStore\": false,\n      \"storeId\": null,\n      \"friendlyName\": null,\n      \"address\": null,\n      \"additionalInfo\": null,\n      \"dockId\": null\n    }\n  },\n  {\n    \"id\": \"pickup_2\",\n    \"name\": \"Pickup Point 2\",\n    \"priority\": 0,\n    \"dockTimeFake\": \"1.00:00:00\",\n    \"timeFakeOverhead\": \"00:00:00\",\n    \"salesChannels\": [\n      \"1\"\n    ],\n    \"salesChannel\": null,\n    \"freightTableIds\": [],\n    \"wmsEndPoint\": \"\",\n    \"pickupStoreInfo\": {\n      \"isPickupStore\": false,\n      \"storeId\": null,\n      \"friendlyName\": null,\n      \"address\": null,\n      \"additionalInfo\": null,\n      \"dockId\": null\n    }\n  },\n  {\n    \"id\": \"pickup_3\",\n    \"name\": \"Pickup Point 3\",\n    \"priority\": 0,\n    \"dockTimeFake\": \"1.00:00:00\",\n    \"timeFakeOverhead\": \"00:00:00\",\n    \"salesChannels\": [\n      \"1\"\n    ],\n    \"salesChannel\": null,\n    \"freightTableIds\": [],\n    \"wmsEndPoint\": \"\",\n    \"pickupStoreInfo\": {\n      \"isPickupStore\": false,\n      \"storeId\": null,\n      \"friendlyName\": null,\n      \"address\": null,\n      \"additionalInfo\": null,\n      \"dockId\": null\n    }\n  }\n]",
      "language": "text",
      "name": "200 - OK"
    }
  ]
}
[/block]