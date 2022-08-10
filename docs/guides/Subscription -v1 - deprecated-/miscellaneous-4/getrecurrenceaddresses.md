---
title: "Get Subscription addresses"
slug: "getrecurrenceaddresses"
excerpt: "Retrieves the addresses attached to a given subscription (formerly recurrence) by recurrenceId."
hidden: false
createdAt: "2019-12-30T19:13:49.450Z"
updatedAt: "2020-02-28T14:18:36.295Z"
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
      "code": "curl --location --request GET 'https://{{accountName}}.{{environment}}.com.br/api/subscriptions/{{recurrenceId}}/addresses' \\\n--header 'Accept: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--data-raw ''",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]