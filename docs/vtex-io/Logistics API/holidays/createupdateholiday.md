---
title: "Create/Update Holiday"
slug: "createupdateholiday"
excerpt: "Creates or updates holidays through holiday ID."
hidden: false
createdAt: "2020-01-23T15:28:46.231Z"
updatedAt: "2020-02-17T21:20:02.332Z"
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
      "code": "curl --location --request PUT 'https://{accountName}.{environment}.com.br/api/logistics/pvt/configuration/holidays/holidayId' \\\n--header 'Content-Type: application/json; charset=utf-8' \\\n--header 'Accept: application/json' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--data-raw '{\n  \"name\":\"Natal\",\n  \"startDate\": \"2016-12-25\"\n}'",
      "language": "text",
      "name": "REquest example"
    }
  ]
}
[/block]