---
title: "Retrieve Subscription report by schedule"
slug: "requestreportbyschedule"
excerpt: "Retrieves a report regarding the Subscriptions scheduled to execute at the date interval requested"
hidden: true
createdAt: "2019-12-30T04:15:05.393Z"
updatedAt: "2020-03-02T15:02:18.852Z"
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
      "code": "curl --location --request GET 'https://{{accountName}}.{{environment}}.com.br/api/rns/report/subscriptionsScheduled?requesterEmail=user@vtex.com.br&beginDate=20190101&endDate=20190701' \\\n--header 'Accept: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]