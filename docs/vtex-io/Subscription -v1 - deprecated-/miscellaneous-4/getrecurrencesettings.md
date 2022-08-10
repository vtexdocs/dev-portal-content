---
title: "Get Subscription settings"
slug: "getrecurrencesettings"
excerpt: "Retrieves your store's Subscriptions' (formerly recurrence) settings."
hidden: false
createdAt: "2019-12-30T19:13:49.450Z"
updatedAt: "2020-02-28T14:18:36.474Z"
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
      "code": "curl --location --request GET 'https://{{accountName}}.{{environment}}.com.br/api/subscriptions/settings' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]