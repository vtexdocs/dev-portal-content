---
title: "Get Subscriptions"
slug: "getrecurrencebyemail"
excerpt: "Retrieves a given Subscription (formerly recurrence). There are three options of filtering your Subscruptions v1. It's possible to get a list of all Subscriptions v1, by not adding any query params to your request, and simply executing a call to the url. It is also possible to list the Subscriptions by email, filtering by the email query param. And finnally, it is possible to list recurrences with failures on the last execution cycle, filtering by the cycleStatus query param."
hidden: false
createdAt: "2019-12-30T19:13:49.450Z"
updatedAt: "2020-02-28T21:10:12.577Z"
---
[block:api-header]
{
  "title": "Request body example - all Subscriptions v1"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "curl --location --request GET 'https://{{accountName}}.{{environment}}.com.br/api/subscriptions' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}'",
      "language": "text",
      "name": "Request example - all subscriptions"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Request body example - by email"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "curl --location --request GET 'https://{{accountName}}.{{environment}}.com.br/api/subscriptions?q={{email}}' \\\n--header 'Accept: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--data-raw ''",
      "language": "text",
      "name": "Request example - email"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Request body example - failure on last execution cycle"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "curl --location --request GET 'https://{{accountName}}.{{environment}}.com.br/api/subscriptions?cycleStatus=FAILURE' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}'",
      "language": "text",
      "name": "Request example - failure on last execution cycle"
    }
  ]
}
[/block]