---
title: "Update Subscriptions by SubscriptionId"
slug: "updatesubscriptionsbysubscriptionid"
excerpt: "Update, add or alter information of a given Subscription, filtering by `subscriptionId`."
hidden: true
createdAt: "2019-12-30T04:15:05.393Z"
updatedAt: "2022-05-05T16:26:42.516Z"
---
[block:api-header]
{
  "title": "The object has the following properties:"
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Attribute",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "item",
    "1-0": "id",
    "2-0": "name",
    "1-1": "string",
    "2-1": "string",
    "3-0": "productName",
    "3-1": "string",
    "4-0": "imageUrl",
    "4-1": "string",
    "5-0": "nameComplete",
    "5-1": "string",
    "6-0": "quantity",
    "6-1": "integer",
    "7-0": "priceAtSubscriptionDate",
    "7-1": "integer",
    "8-0": "SellingPrice",
    "8-1": "integer",
    "9-0": "endpoint",
    "9-1": "string",
    "10-0": "plan",
    "10-1": "object",
    "0-1": "object",
    "11-0": "frequency",
    "11-1": "object",
    "12-0": "periodicity",
    "12-1": "string",
    "13-0": "interval",
    "13-1": "integer",
    "14-0": "validity",
    "14-1": "object",
    "15-0": "begin",
    "16-0": "end",
    "17-0": "type",
    "17-1": "string",
    "18-0": "purchaseSettings",
    "18-1": "object",
    "19-0": "purchaseDay",
    "19-1": "string",
    "20-0": "paymentMethod",
    "20-1": "object",
    "21-0": "paymentSystem",
    "21-1": "string",
    "22-0": "paymentAccountId",
    "22-1": "string",
    "23-0": "seller",
    "23-1": "string",
    "24-0": "salesChannel",
    "24-1": "string",
    "25-0": "selectedSla",
    "25-1": "string",
    "26-0": "currencyCode",
    "26-1": "string",
    "27-0": "shippingAddress",
    "27-1": "object",
    "28-0": "addressId",
    "28-1": "string",
    "29-0": "number",
    "29-1": "string",
    "30-0": "complement",
    "30-1": "string",
    "31-0": "neighborhood",
    "31-1": "string",
    "32-0": "city",
    "32-1": "string",
    "33-0": "state",
    "33-1": "string",
    "34-0": "country",
    "34-1": "string",
    "35-0": "postalCode",
    "35-1": "string",
    "36-0": "reference",
    "36-1": "string",
    "37-0": "formattedAddress",
    "37-1": "string",
    "38-0": "additionalComponents",
    "38-1": "array",
    "39-0": "longName",
    "39-1": "string",
    "40-0": "shortName",
    "40-1": "string",
    "41-0": "types",
    "41-1": "array",
    "42-0": "geoCoordinate",
    "42-1": "array",
    "43-0": "receiverName",
    "43-1": "string",
    "44-0": "addressType",
    "44-1": "string",
    "45-0": "addressName",
    "45-1": "string",
    "46-0": "status",
    "46-1": "string",
    "47-0": "isSkipped",
    "47-1": "boolean",
    "48-0": "metadata",
    "48-1": "array",
    "49-0": "name",
    "49-1": "string",
    "50-0": "properties",
    "50-1": "object",
    "50-2": "",
    "51-0": "additionalProp1",
    "51-1": "string",
    "52-0": "additionalProp2",
    "52-1": "string",
    "53-0": "additionalProp3",
    "53-1": "string",
    "1-2": "",
    "15-1": "string",
    "16-1": "string"
  },
  "cols": 3,
  "rows": 54
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
      "code": "curl --location --request PATCH 'https://{{accountName}}.{{environment}}.com.br/api/rns/subscriptions/{{subscriptionId}}' \\\n--header 'Content-Type: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--data-raw '{\n  \"item\": {\n    \"sku\": {\n      \"id\": \"string\",\n      \"name\": \"string\",\n      \"productName\": \"string\",\n      \"imageUrl\": \"string\",\n      \"detailUrl\": \"string\",\n      \"nameComplete\": \"string\"\n    },\n    \"quantity\": 0,\n    \"priceAtSubscriptionDate\": 0,\n    \"sellingPrice\": 0,\n    \"endpoint\": \"string\"\n  },\n  \"plan\": {\n    \"frequency\": {\n      \"periodicity\": \"string\",\n      \"interval\": 0\n    },\n    \"validity\": {\n      \"begin\": \"2019-07-04T14:40:30.819Z\",\n      \"end\": \"2019-07-04T14:40:30.819Z\"\n    },\n    \"type\": \"string\"\n  },\n  \"purchaseSettings\": {\n    \"purchaseDay\": \"string\",\n    \"paymentMethod\": {\n      \"paymentSystem\": \"string\",\n      \"paymentAccountId\": \"string\"\n    },\n    \"seller\": \"string\",\n    \"salesChannel\": \"string\",\n    \"selectedSla\": \"string\",\n    \"currencyCode\": \"string\"\n  },\n  \"shippingAddress\": {\n    \"addressId\": \"string\",\n    \"street\": \"string\",\n    \"number\": \"string\",\n    \"complement\": \"string\",\n    \"neighborhood\": \"string\",\n    \"city\": \"string\",\n    \"state\": \"string\",\n    \"country\": \"string\",\n    \"postalCode\": \"string\",\n    \"reference\": \"string\",\n    \"formattedAddress\": \"string\",\n    \"additionalComponents\": [\n      {\n        \"longName\": \"string\",\n        \"shortName\": \"string\",\n        \"types\": [\n          \"string\"\n        ]\n      }\n    ],\n    \"geoCoordinate\": [\n      0\n    ],\n    \"receiverName\": \"string\",\n    \"addressType\": \"string\",\n    \"addressName\": \"string\"\n  },\n  \"status\": \"string\",\n  \"isSkipped\": true,\n  \"metadata\": [\n    {\n      \"name\": \"string\",\n      \"properties\": {\n        \"additionalProp1\": \"string\",\n        \"additionalProp2\": \"string\",\n        \"additionalProp3\": \"string\"\n      }\n    }\n  ]\n}'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]