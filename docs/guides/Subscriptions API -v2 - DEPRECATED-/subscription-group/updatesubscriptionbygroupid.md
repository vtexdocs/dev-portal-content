---
title: "Update Subscription by groupId"
slug: "updatesubscriptionbygroupid"
excerpt: "Updates a Subscription by `groupId`."
hidden: false
createdAt: "2019-12-30T04:15:05.393Z"
updatedAt: "2022-05-05T16:26:42.663Z"
---
If you need to update information within a given Subscription group, you don't need to insert the whole JSON body in your request. Just add an array of the parameter with the desired information you want to alter. 

Example: if you want to change the quantity of an SKU within a subscription group, (adding, or removing items), just use the following body in your request. 
[block:code]
{
  "codes": [
    {
      "code": "curl --location --request PATCH 'http://api.vtexinternal.com/api/rns/subscriptions-group/734D48BE8D6350A2810A520B3AC6919B?an=recorrenciaqa' \\\n--header 'Content-Type: application/json' \\\n--header 'Content-Type: text/plain' \\\n--data-raw '{\n    \"item\": [\n        {\n            \"sku\": {\n                \"id\": \"22\"\n            },\n            \"quantity\": 2\n        }\n    ]\n}'",
      "language": "text",
      "name": "Example request - Change SKU quantity"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Request body example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "curl --location --request PATCH 'https://{{accountName}}.{{environment}}.com.br/api/rns/subscriptions-group/{{groupId}}' \\\n--header 'Content-Type: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--data-raw '{\n  \"item\": [\n    {\n      \"sku\": {\n        \"id\": \"string\",\n        \"name\": \"string\",\n        \"productName\": \"string\",\n        \"imageUrl\": \"string\",\n        \"detailUrl\": \"string\",\n        \"nameComplete\": \"string\"\n      },\n      \"quantity\": 0,\n      \"endpoint\": \"string\",\n      \"priceAtSubscriptionDate\": 0,\n      \"sellingPrice\": 0,\n      \"SubscriptionId\": \"string\",\n      \"cycleCount\": 0,\n      \"status\": \"ACTIVE\",\n      \"createdAt\": \"2019-06-20T18:27:41.230Z\",\n      \"lastUpdate\": \"2019-06-20T18:27:41.230Z\",\n      \"originalOrderId\": \"string\",\n      \"originalItemIndex\": 0,\n      \"metadata\": [\n        {\n          \"name\": \"string\",\n          \"properties\": {\n            \"additionalProp1\": \"string\",\n            \"additionalProp2\": \"string\",\n            \"additionalProp3\": \"string\"\n          }\n        }\n      ],\n      \"isSkipped\": true\n    }\n  ],\n  \"plan\": {\n    \"frequency\": {\n      \"periodicity\": \"string\",\n      \"interval\": 0\n    },\n    \"validity\": {\n      \"begin\": \"2019-06-20T18:27:41.230Z\",\n      \"end\": \"2019-06-20T18:27:41.230Z\"\n    },\n    \"type\": \"string\"\n  },\n  \"purchaseSettings\": {\n    \"purchaseDay\": \"string\",\n    \"paymentMethod\": {\n      \"paymentSystem\": \"string\",\n      \"paymentAccountId\": \"string\"\n    },\n    \"seller\": \"string\",\n    \"salesChannel\": \"string\",\n    \"selectedSla\": \"string\",\n    \"currencyCode\": \"string\"\n  },\n  \"shippingAddress\": {\n    \"addressId\": \"string\",\n    \"street\": \"string\",\n    \"number\": \"string\",\n    \"complement\": \"string\",\n    \"neighborhood\": \"string\",\n    \"city\": \"string\",\n    \"state\": \"string\",\n    \"country\": \"string\",\n    \"postalCode\": \"string\",\n    \"reference\": \"string\",\n    \"formattedAddress\": \"string\",\n    \"additionalComponents\": [\n      {\n        \"longName\": \"string\",\n        \"shortName\": \"string\",\n        \"types\": [\n          \"string\"\n        ]\n      }\n    ],\n    \"geoCoordinate\": [\n      0\n    ],\n    \"receiverName\": \"string\",\n    \"addressType\": \"string\",\n    \"addressName\": \"string\"\n  },\n  \"status\": \"string\",\n  \"isSkipped\": true,\n  \"metadata\": [\n    {\n      \"name\": \"string\",\n      \"properties\": {\n        \"additionalProp1\": \"string\",\n        \"additionalProp2\": \"string\",\n        \"additionalProp3\": \"string\"\n      }\n    }\n  ]\n}'",
      "language": "text",
      "name": "Request example - full example"
    }
  ]
}
[/block]