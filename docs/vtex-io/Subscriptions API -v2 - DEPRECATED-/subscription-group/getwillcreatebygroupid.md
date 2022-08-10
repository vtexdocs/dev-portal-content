---
title: "List 'Will create' by groupId"
slug: "getwillcreatebygroupid"
excerpt: "Retrieves Subscription groups listed as 'will create', filtering by groupId."
hidden: false
createdAt: "2019-12-30T04:15:05.393Z"
updatedAt: "2020-03-02T15:02:18.327Z"
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
      "code": "curl --location --request GET 'https://{{accountName}}.{{environment}}.com.br/api/rns/subscriptions-group/{{groupId}}/will-create' \\\n--header 'Accept: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]