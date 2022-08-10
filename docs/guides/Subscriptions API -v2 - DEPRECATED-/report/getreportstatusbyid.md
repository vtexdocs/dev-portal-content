---
title: "Get report status by ID"
slug: "getreportstatusbyid"
excerpt: "Retrieves the Subscription's report status, filtering by its reportId."
hidden: false
createdAt: "2019-12-30T04:15:05.393Z"
updatedAt: "2020-03-02T15:02:19.133Z"
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
      "code": "curl --location --request GET 'https://{{accountName}}.{{environment}}.com.br/api/rns/report/reportStatus/{{reportId}}' \\\n--header 'Accept: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]