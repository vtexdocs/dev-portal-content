---
title: "Get Subscription List"
slug: "getsubscriptionlist"
excerpt: "Retrieves a list of Subscriptions linked to your store."
hidden: false
createdAt: "2019-12-30T04:15:05.393Z"
updatedAt: "2020-02-28T14:18:38.974Z"
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
      "code": "curl --location --request GET 'https://{{accountName}}.{{environment}}.com.br/api/rns/subscriptions/list' \\\n--header 'Content-Type: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]