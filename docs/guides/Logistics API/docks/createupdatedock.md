---
title: "Create/update dock"
slug: "createupdatedock"
excerpt: "Creates or updates docks to be used in your logistic operation."
hidden: false
createdAt: "2020-01-23T15:28:46.231Z"
updatedAt: "2022-06-28T20:03:23.251Z"
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
      "code": "curl --location --request POST 'https://{accountName}.{environment}.com.br/api/logistics/pvt/configuration/docks' \\\n--header 'Content-Type: application/json; charset=utf-8' \\\n--header 'Accept: application/json' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--data-raw '{\n    \"id\": \"catete\",\n    \"name\": \"Loja Catete\",\n    \"priority\": 0,\n    \"dockTimeFake\": \"00:00:00\",\n    \"timeFakeOverhead\": \"00:00:00\",\n    \"salesChannels\": [\n      \"1\"\n    ],\n    \"salesChannel\": null,\n    \"freightTableIds\": [],\n    \"wmsEndPoint\": \"\",\n    \"address\": {\n        \"postalCode\": \"22220070\",\n        \"country\": {\n          \"acronym\": \"BRA\",\n          \"name\": \"Brazil\"\n        },\n        \"city\": \"Rio de Janeiro\",\n        \"state\": \"RJ\",\n        \"neighborhood\": \"Catete\",\n        \"street\": \"Artur Bernardes Street\",\n        \"number\": \"100\",\n        \"complement\": \"\",\n        \"coordinates\": [[-43.18228090000002, -22.9460398 ]]\n      }\n  }'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]