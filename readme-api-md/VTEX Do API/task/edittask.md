---
title: "Update Task"
slug: "edittask"
excerpt: "Updates a given task's status, for example, filtering by `taskId`."
hidden: false
createdAt: "2019-12-30T19:34:01.284Z"
updatedAt: "2022-01-11T20:54:53.596Z"
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
      "code": "curl --location --request PUT 'https://{{accountName}}.{{environment}}.com.br/api/do/tasks/{{taskId}}' \\\n--header 'Accept: application/json' \\\n--header 'Content-Type: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--data-raw '{\n  \"status\": \"InProgress\"\n}'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]