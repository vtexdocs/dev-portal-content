---
title: "Reindex Subscription"
slug: "reindexrecurrence"
excerpt: "Alters the frequency of a given Subscription (formerly Recurrence) by changing period and interval."
hidden: false
createdAt: "2019-12-30T19:13:49.450Z"
updatedAt: "2020-02-28T14:18:36.206Z"
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
      "code": "curl --location --request PATCH 'https://{{accountName}}.{{environment}}.com.br/api/subscriptions/{{recurrenceId}}/reindex' \\\n--header 'Content-Type: application/json' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--data-raw '[\n    {\n        \"frequency\": {\n            \"periodicity\": \"yearly\",\n            \"interval\": 1\n        }\n    }\n]'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]