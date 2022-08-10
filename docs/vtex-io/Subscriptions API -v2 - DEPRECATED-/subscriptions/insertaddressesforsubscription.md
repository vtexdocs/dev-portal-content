---
title: "Insert Addresses for Subscription"
slug: "insertaddressesforsubscription"
excerpt: "Inserts address's information to complement the Subscription details."
hidden: false
createdAt: "2019-12-30T04:15:05.393Z"
updatedAt: "2020-02-28T14:18:39.194Z"
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
      "code": "curl --location --request POST 'https://{{accountName}}.{{environment}}.com.br/api/rns/subscriptions/{{subscriptionId}}/addresses' \\\n--header 'Content-Type: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--data-raw '[\n    {\n        \"addressId\": \"1234567890\",\n        \"street\": \"Avenida do Estado\",\n        \"number\": \"1\",\n        \"complement\": null,\n        \"neighborhood\": \"Barra da Tijuca\",\n        \"city\": \"Rio de Janeiro\",\n        \"state\": \"RJ\",\n        \"country\": \"BRA\",\n        \"postalCode\": \"22204-004\",\n        \"reference\": null,\n        \"formattedAddress\": null,\n        \"additionalComponents\": null,\n        \"geoCoordinate\": null,\n        \"receiverName\": \"Fulano\",\n        \"addressType\": \"residential\",\n        \"addressName\": \"xt5353818181nhshs\"\n    }\n]'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]