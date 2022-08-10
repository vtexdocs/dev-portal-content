---
title: "Delete Polygon"
slug: "deletepolygon"
excerpt: "Deletes polygon set up in your store, by polygon name."
hidden: false
createdAt: "2020-01-23T15:28:46.231Z"
updatedAt: "2020-02-17T21:20:30.386Z"
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
      "code": "curl --location --request DELETE 'https://{accountName}.{environment}.com.br/api/logistics/pvt/configuration/geoshape/polygonName' \\\n--header 'Content-Type: application/json; charset=utf-8' \\\n--header 'Accept: application/json' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--data-raw ''",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]