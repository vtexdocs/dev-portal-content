---
title: "Create/Update Pickup Point"
slug: "createupdate"
excerpt: "Creates or updates pickup points in your store by Pickup Point ID."
hidden: false
createdAt: "2020-01-23T15:28:46.231Z"
updatedAt: "2020-02-17T21:20:29.719Z"
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
      "code": "curl --location --request PUT 'https://{accountName}.{environment}.com.br/api/logistics/pvt/configuration/pickuppoints/pickupPointId' \\\n--header 'Content-Type: application/json; charset=utf-8' \\\n--header 'Accept: application/json' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--data-raw '{\n    \"id\": \"1a227d3\",\n    \"name\": \"Loja Copacabana\",\n    \"description\": \"\",\n    \"instructions\": \"Obrigatório apresentar documento de identificação\",\n    \"formatted_address\": \"undefined\",\n    \"address\": {\n        \"postalCode\": \"22070002\",\n        \"country\": {\n            \"acronym\": \"BRA\",\n            \"name\": \"Brazil\"\n        },\n        \"city\": \"Rio de Janeiro\",\n        \"state\": \"RJ\",\n        \"neighborhood\": \"Copacabana\",\n        \"street\": \"Avenida Atlântica\",\n        \"number\": \"\",\n        \"complement\": \"\",\n        \"reference\": null,\n        \"location\": {\n            \"latitude\": -22.974477767944336,\n            \"longitude\": -43.18672561645508\n        }\n    },\n    \"isActive\": true,\n    \"businessHours\": [\n        {\n            \"dayOfWeek\": 1,\n            \"openingTime\": \"08:00:00\",\n            \"closingTime\": \"20:00:00\"\n        },\n        {\n            \"dayOfWeek\": 2,\n            \"openingTime\": \"08:00:00\",\n            \"closingTime\": \"20:00:00\"\n        },\n        {\n            \"dayOfWeek\": 3,\n            \"openingTime\": \"08:00:00\",\n            \"closingTime\": \"20:00:00\"\n        },\n        {\n            \"dayOfWeek\": 4,\n            \"openingTime\": \"08:00:00\",\n            \"closingTime\": \"20:00:00\"\n        },\n        {\n            \"dayOfWeek\": 5,\n            \"openingTime\": \"08:00:00\",\n            \"closingTime\": \"20:00:00\"\n        }\n    ],\n    \"tagsLabel\": [\n        \"zonasul\", \"rio de janeiro\"\n    ]\n}'",
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
      "code": "{\n  \"id\": \"rteste\",\n  \"name\": \"Loja Copacabana\",\n  \"description\": \"\",\n  \"instructions\": \"Obrigatório apresentar documento de identificação\",\n  \"formatted_address\": \"undefined\",\n  \"address\": {\n    \"postalCode\": \"22070002\",\n    \"country\": {\n      \"acronym\": \"BRA\",\n      \"name\": \"Brazil\"\n    },\n    \"city\": \"Rio de Janeiro\",\n    \"state\": \"RJ\",\n    \"neighborhood\": \"Copacabana\",\n    \"street\": \"Avenida Atlântica\",\n    \"number\": \"\",\n    \"complement\": \"\",\n    \"reference\": null,\n    \"location\": {\n      \"latitude\": -22.974477767944336,\n      \"longitude\": -43.18672561645508\n    }\n  },\n  \"isActive\": true,\n  \"businessHours\": [\n    {\n      \"dayOfWeek\": 1,\n      \"openingTime\": \"08:00:00\",\n      \"closingTime\": \"20:00:00\"\n    },\n    {\n      \"dayOfWeek\": 2,\n      \"openingTime\": \"08:00:00\",\n      \"closingTime\": \"20:00:00\"\n    },\n    {\n      \"dayOfWeek\": 3,\n      \"openingTime\": \"08:00:00\",\n      \"closingTime\": \"20:00:00\"\n    },\n    {\n      \"dayOfWeek\": 4,\n      \"openingTime\": \"08:00:00\",\n      \"closingTime\": \"20:00:00\"\n    },\n    {\n      \"dayOfWeek\": 5,\n      \"openingTime\": \"08:00:00\",\n      \"closingTime\": \"20:00:00\"\n    }\n  ],\n  \"tagsLabel\": [\n    \"zonasul\",\n    \"rio de janeiro\"\n  ],\n  \"pickupHolidays\": []\n}",
      "language": "text",
      "name": "200 - OK"
    }
  ]
}
[/block]