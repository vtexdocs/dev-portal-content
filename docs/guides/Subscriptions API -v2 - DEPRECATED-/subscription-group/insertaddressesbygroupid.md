---
title: "Insert Addresses by groupId"
slug: "insertaddressesbygroupid"
excerpt: "Insert address information of a given Subscription group, filtering by groupId."
hidden: true
createdAt: "2019-12-30T04:15:05.393Z"
updatedAt: "2020-03-02T15:02:17.869Z"
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
      "code": "curl --location --request POST 'https://{{accountName}}.{{environment}}.com.br/api/rns/subscriptions-group/{{groupId}}/addresses' \\\n--header 'Content-Type: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--data-raw '{\n  \"addressId\": \"string\",\n  \"street\": \"string\",\n  \"number\": \"string\",\n  \"complement\": \"string\",\n  \"neighborhood\": \"string\",\n  \"city\": \"string\",\n  \"state\": \"string\",\n  \"country\": \"string\",\n  \"postalCode\": \"string\",\n  \"reference\": \"string\",\n  \"formattedAddress\": \"string\",\n  \"additionalComponents\": [\n    {\n      \"longName\": \"string\",\n      \"shortName\": \"string\",\n      \"types\": [\n        \"string\"\n      ]\n    }\n  ],\n  \"geoCoordinate\": [\n    0\n  ],\n  \"receiverName\": \"string\",\n  \"addressType\": \"string\",\n  \"addressName\": \"string\"\n}'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]