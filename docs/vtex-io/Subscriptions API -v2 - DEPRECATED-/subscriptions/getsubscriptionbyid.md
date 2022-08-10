---
title: "Retrieve subscription by Id"
slug: "getsubscriptionbyid"
excerpt: "Lists Subscription's details, searching by subscriptionId."
hidden: false
createdAt: "2019-12-30T04:15:05.393Z"
updatedAt: "2020-02-28T14:18:38.654Z"
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