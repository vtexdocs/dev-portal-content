---
title: "List tasks"
slug: "listtasksbyassignee"
excerpt: "There are four options of filtering your list of tasks. It is possible to filter them by: assignees, filtering by their emails and status; targets, filtering by the `targetId` and `status`; paged tasks, filtering by `page`, `perPage` and `status`; and context, filtering by `context`, `page`, `perPage`, and `status`."
hidden: false
createdAt: "2019-12-30T19:34:01.284Z"
updatedAt: "2022-01-11T20:54:53.566Z"
---
[block:api-header]
{
  "title": "Request body example - by Assignee"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "curl --location --request GET 'https://{{accountName}}.{{environment}}.com.br/api/do/tasks?assignee.email={{person@email.com}}&status={{open}}' \\\n--header 'Accept: application/json' \\\n--header 'Content-Type: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}'",
      "language": "text",
      "name": "Request example by Assignee"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Request body example - by Target"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "curl --location --request GET 'https://{{accountName}}.{{environment}}.com.br/api/do/tasks?target.id={{name}}&status={{open}}' \\\n--header 'Accept: application/json' \\\n--header 'Content-Type: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}'",
      "language": "text",
      "name": "Request example by Target"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Request body example - by Paged Tasks"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "curl --location --request GET 'https://{{accountName}}.{{environment}}.com.br/api/do/tasks?page={{1}}&perPage={{10}}&status=;{{-Closed}}' \\\n--header 'Accept: application/json' \\\n--header 'Content-Type: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}'",
      "language": "text",
      "name": "Request example Paged tasks"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Request body example - by Context"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "curl --location --request GET 'https://{{accountName}}.{{environment}}.com.br/api/do/tasks?context={{context}}&page={{1}}&perPage={{10}}&status={{-Closed}}' \\\n--header 'Accept: application/json' \\\n--header 'Content-Type: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}'",
      "language": "text",
      "name": "Request example by Context"
    }
  ]
}
[/block]