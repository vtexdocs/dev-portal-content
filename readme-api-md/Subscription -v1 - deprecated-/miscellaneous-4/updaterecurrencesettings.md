---
title: "Update Subscription settings"
slug: "updaterecurrencesettings"
excerpt: "Updates the Subscriptions' (formerly Recurrence) settings of your store by salesChannel and defaultSLA."
hidden: false
createdAt: "2019-12-30T19:13:49.450Z"
updatedAt: "2020-02-28T14:18:36.569Z"
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
      "code": "curl --location --request PUT 'https://{{accountName}}.{{environment}}.com.br/api/subscriptions/settings' \\\n--header 'Content-Type: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--data-raw '{\n    \"salesChannel\": \"1\",\n    \"defaultSLA\": \"Normal\"\n}'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]