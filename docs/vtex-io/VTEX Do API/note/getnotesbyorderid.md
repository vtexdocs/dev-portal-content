---
title: "Get Notes by orderId"
slug: "getnotesbyorderid"
excerpt: "Retrieves notes related to a specific orderId."
hidden: false
createdAt: "2019-12-30T19:34:01.284Z"
updatedAt: "2020-03-02T15:02:24.269Z"
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
      "code": "curl --location --request GET 'https://{{accountName}}.{{environment}}.com.br/api/do/notes?target.id={{orderId}}' \\\n--header 'Accept: application/json' \\\n--header 'Content-Type: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]