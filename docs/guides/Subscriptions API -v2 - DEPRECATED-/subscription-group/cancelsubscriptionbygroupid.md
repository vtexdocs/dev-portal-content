---
title: "Cancel Subscription by groupId"
slug: "cancelsubscriptionbygroupid"
excerpt: "Cancels Subscription by `groupId`"
hidden: false
createdAt: "2019-12-30T04:15:05.393Z"
updatedAt: "2022-05-05T16:26:42.750Z"
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
      "code": "curl --location --request PATCH 'https://{{accountName}}.{{environment}}.com.br/api/rns/subscriptions-group/{{groupId}}/cancel' \\\n--header 'Content-Type: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]