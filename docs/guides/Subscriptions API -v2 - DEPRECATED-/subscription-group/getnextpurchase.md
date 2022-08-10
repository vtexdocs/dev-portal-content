---
title: "Get Next purchase"
slug: "getnextpurchase"
excerpt: "Lists details of a given subscription group's next purchase, filtering by dateStr."
hidden: false
createdAt: "2019-12-30T04:15:05.393Z"
updatedAt: "2020-03-16T21:20:45.296Z"
---
**DateStr**: Reference date that retrieves all next purchases, starting from the {{dateStr}} inserted. Must be in the format of {{yyyyMMdd}}.
[block:api-header]
{
  "title": "Request body example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "curl --location --request GET 'https://{{accountName}}.{{environment}}.com.br/api/rns/subscriptions-group/nextPurchase/{{dateStr}}' \\\n--header 'Accept: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]