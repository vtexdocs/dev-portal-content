---
title: "Retrieve subscription by ID"
slug: "getsubscriptionbyid"
excerpt: "Lists Subscription's details, searching by `subscriptionId`."
hidden: false
createdAt: "2019-12-30T04:15:05.393Z"
updatedAt: "2022-05-05T16:26:42.495Z"
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
      "code": "curl --location --request GET 'https://{{accountName}}.{{environment}}.com.br/api/rns/subscriptions/{{subscriptionId}}' \\\n--header 'Accept: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]