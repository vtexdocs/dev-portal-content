---
title: "Retry subscription by groupId"
slug: "retrysubscriptionbygroupid"
excerpt: "Permits the retry of a Subscription group, via API, filtering by groupId and instanceId."
hidden: true
createdAt: "2019-12-30T04:15:05.393Z"
updatedAt: "2020-03-02T15:02:18.144Z"
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
      "code": "curl --location --request POST 'https://{{accountName}}.{{environment}}.com.br/api/rns/subscriptions-group/{{groupid}}/instances/{{instanceId}}/retry' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]