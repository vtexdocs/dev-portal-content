---
title: "Update partial Subscription"
slug: "updatepartialrecurrence"
excerpt: "Updates partial information of a given subscription (formerly Recurrence)."
hidden: false
createdAt: "2019-12-30T19:13:49.450Z"
updatedAt: "2020-02-28T14:18:35.790Z"
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
      "code": "curl --location --request PATCH 'https://{{accountName}}.{{environment}}.com.br/api/subscriptions/{{recurrenceId}}' \\\n--header 'Content-Type: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--data-raw '{\n    \"deliveryDay\": 18,\n    \"deliveryWeekday\": \"Monday\",\n    \"status\": \"inactive\"\n}'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]