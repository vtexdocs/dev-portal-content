---
title: "List Pickup Point By ID"
slug: "getbyid"
excerpt: "Lists your store's pickup points while searching by ID."
hidden: false
createdAt: "2020-01-23T15:28:46.231Z"
updatedAt: "2020-02-17T21:20:29.817Z"
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
      "code": "curl --location --request GET 'https://{accountName}.{environment}.com.br/api/logistics/pvt/configuration/pickuppoints/pickupPointId' \\\n--header 'Content-Type: application/json; charset=utf-8' \\\n--header 'Accept: application/json' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}'",
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
      "code": "{\n  \"id\": \"12345\",\n  \"name\": \"Loja Barra da Tijuca\",\n  \"description\": \"Loja Barra da Tijuca\",\n  \"instructions\": \"Loja Barra da Tijuca\",\n  \"formatted_address\": \"undefined\",\n  \"address\": {\n    \"postalCode\": \"22220070\",\n    \"country\": {\n      \"acronym\": \"BRA\",\n      \"name\": \"Brazil\"\n    },\n    \"city\": \"Rio de Janeiro\",\n    \"state\": \"RJ\",\n    \"neighborhood\": \"Catete\",\n    \"street\": \"Rua Artur Bernardes\",\n    \"number\": \"\",\n    \"complement\": \"\",\n    \"location\": {\n      \"latitude\": -22.92860984802246,\n      \"longitude\": -22.92860984802246\n    }\n  },\n  \"isActive\": true,\n  \"warehouseId\": null,\n  \"businessHours\": [\n    {\n      \"dayOfWeek\": 0,\n      \"openingTime\": \"11:00:00\",\n      \"closingTime\": \"21:00:00\"\n    }\n  ]\n}",
      "language": "text",
      "name": "200 - OK"
    }
  ]
}
[/block]