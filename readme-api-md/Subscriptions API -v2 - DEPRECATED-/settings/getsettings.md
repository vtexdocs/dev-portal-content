---
title: "Get Subscriptions Settings"
slug: "getsettings"
excerpt: "Lists the current Subscriptions settings in your store."
hidden: true
createdAt: "2019-12-30T04:15:05.393Z"
updatedAt: "2022-05-05T16:26:43.394Z"
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
      "code": "curl --location --request GET 'https://{{accountName}}.{{environment}}.com.br/api/rns/settings' \\\n--header 'Accept: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]