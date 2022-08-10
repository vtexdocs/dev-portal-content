---
title: "Retrieve blocked delivery windows"
slug: "retrieveblockeddeliverywindows"
excerpt: "Lists all blocked delivery windows of your store's shipping policies, searching by carrier ID.\n\r\n\r> Note that, while most of our API endpoints return time fields in UTC, this endpoint returns **Scheduled Delivery** related time fields adjusted to the configured time zone of the account."
hidden: false
createdAt: "2020-01-23T15:28:46.231Z"
updatedAt: "2021-10-05T17:33:12.605Z"
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
      "code": "curl --location --request GET 'https://{accountName}.{environment}.com.br/api/logistics/pvt/configuration/carriers/carrierId/getdayofweekblocked' \\\n--header 'Content-Type: application/json; charset=utf-8' \\\n--header 'Accept: application/json' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]