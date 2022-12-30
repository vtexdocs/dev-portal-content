---
title: "Add Subscription item by groupId"
slug: "additemsubscription-groupid"
excerpt: "Adds an SKU to a given Subscription, filtering by groupId."
hidden: true
createdAt: "2019-12-30T04:15:05.393Z"
updatedAt: "2020-03-02T15:02:17.668Z"
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
      "code": "curl --location --request POST 'https://{{accountName}}.{{environment}}.com.br/api/rns/subscriptions-group/{{groupId}}/additem' \\\n--header 'Content-Type: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--data-raw '{\n  \"sku\": {\n    \"id\": \"string\",\n    \"name\": \"string\",\n    \"productName\": \"string\",\n    \"imageUrl\": \"string\",\n    \"detailUrl\": \"string\",\n    \"nameComplete\": \"string\"\n  },\n  \"quantity\": 0,\n  \"priceAtSubscriptionDate\": 0,\n  \"sellingPrice\": 0,\n  \"endpoint\": \"string\"\n}'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]