---
title: "Remove blocked delivery windows"
slug: "removeblockeddeliverywindows"
excerpt: "Removes the blocked delivery windows set to your store's shipping policies.\n\r\n\r> Note that, while most of our API endpoints return time fields in UTC, this endpoint returns time adjusted to the configured time zone of the account."
hidden: false
createdAt: "2020-01-23T15:28:46.231Z"
updatedAt: "2021-10-05T17:33:12.688Z"
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
      "code": "curl --location --request POST 'https://{accountName}.{environment}.com.br/api/logistics/pvt/configuration/carriers/carrierId/removedayofweekblocked' \\\n--header 'Content-Type: application/json; charset=utf-8' \\\n--header 'Accept: application/json' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--data-raw '\"2016-08-09T08:00:00\"'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]