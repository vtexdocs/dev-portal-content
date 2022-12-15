---
title: "Cancel Subscriptions by SubscriptionId"
slug: "cancelsubscriptionsbysubscriptionid"
excerpt: "Cancels all Subscriptions of a subscription group. This operation does not have a rollback. Once cancelled, it cannot be re-activated"
hidden: true
createdAt: "2019-12-30T04:15:05.393Z"
updatedAt: "2020-03-02T15:02:16.643Z"
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
      "code": "curl --location --request PATCH 'https://{{accountName}}.{{environment}}.com.br/api/rns/subscriptions/{{subscriptionId}}/cancel' \\\n--header 'Content-Type: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]