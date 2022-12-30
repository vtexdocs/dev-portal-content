---
title: "Export order report with status 'Completed'"
slug: "statuscompleted"
excerpt: "Retrieves a list of all order reports that are 'completed', by 'accountName'."
hidden: true
createdAt: "2019-12-11T00:42:27.604Z"
updatedAt: "2021-10-15T17:41:53.490Z"
---
[block:callout]
{
  "type": "warning",
  "title": "Unpublished page",
  "body": "As indicated in this slack thread, this API can not be used by clients, so the API reference was unpublished and, now, the mentions to it removed from the help articles.\n\nhttps://vtex.slack.com/archives/C0165UTUA2E/p1631212209018400"
}
[/block]
Learn more about [Order export and reports in VTEX Help.](https://help.vtex.com/en/tutorial/exporting-orders-with-oms)


Attention: the scope of the export log is per user.


| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `accountName` | string | Store Account Name |


## Response object has the following properties:


| Attribute    | Type        | Description |
| --------------- |:---------:| --------------------------------------:|
| `cancelled` | boolean|  If the export request was cancelled |
| `completedDate` | string | Order Export process completed date |
| `dateOfRequest` | string | Order Export request date  |
| `email` | string | Order Export requester email |
| `filter` | string | Order Export request filter |
| `hostUri` | string | Host URL |
| `id` | string | Order Export request Id |
| `instanceId` | string |  Instace Id |
| `lasUpdateTime` | string | Order export process update time |
| `linkToDownload` | string | Link to Order Export Download |
| `publishId` | string | Order Export publish Id |
| `query` | string | Order Export request filter query |
| `rowNumber` | integer |  Order export total rows |
| `rowsProcessed` | integer | Order export total processed rows |
| `startDate` | string | Order Export process start date |
| `utcTime` | string | UTC time |


[block:api-header]
{
  "title": "Request body example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "curl --location --request GET 'https://accountname.vtexcommercestable.com.br/api/oms/pvt/admin/reports/completed' \\\n--header 'Content-Type: application/json' \\\n--header 'x-vtex-api-appKey: {{X-VTEX-API-AppKey}}' \\\n--header 'x-vtex-api-appToken: {{X-VTEX-API-AppToken}}'",
      "language": "text",
      "name": "Example request"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Response body example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "[\n  {\n    \"id\": \"a83d6d30-a52a-4706-9fc9-e2e7c1841acb\",\n    \"cancelled\": false,\n    \"query\": \"{\\\"Queries\\\":[{\\\"Quoted\\\":true,\\\"FieldName\\\":\\\"InstanceId\\\",\\\"FieldValue\\\":\\\"263FD533551E445CACEEC991385EF610\\\"},{\\\"Quoted\\\":true,\\\"FieldName\\\":\\\"OrderIsComplete\\\",\\\"FieldValue\\\":\\\"True\\\"}],\\\"Oper\\\":\\\"AND\\\"}\",\n    \"filter\": \"generateCsv=true&orderBy=creationDate%2cdesc&page=1&utc=-0300\",\n    \"email\": \"renan.servare@vtex.com.br\",\n    \"hostUri\": \"http://accountname.vtexcommercestable.com.br/\",\n    \"utcTime\": \"-0300\",\n    \"dateOfRequest\": \"2017-05-10T18:31:28.3984674+00:00\",\n    \"startDate\": \"2017-05-10T18:31:27.4043359+00:00\",\n    \"lasUpdateTime\": \"2017-05-10T18:31:35.5250685+00:00\",\n    \"instanceId\": \"i-0b359c34e40c3f281\",\n    \"publishId\": \"263fd533551e445caceec991385ef610\",\n    \"linkToDownload\": \"http://accountname.vtexcommercestable.com.br/api/oms/pub/636300378883984674/report?AWSAccessKeyId=ASIAJM7A43QHIYFHFSMQ&Expires=1494527496&x-amz-security-token=FQoDYXdzEHsaDBnJIX7Yxf7j6gEuTCK3A3AS4wJiFF97%2FpIGtq4rpqA2F7CqU0g%2BIhPPdD%2FaqnF9TKxX1%2BSj4JloO%2F54XdgL3VZyb%2B76Z0FrOZAYnGZvuE%2FMB4KUz1d4NKFOh0sFt%2FxzYFrBOLvMO%2F%2FW3LMG%2FuyiHecP9pYceVysntj41jJeRcLG%2BRBN4Z69TQBQrUp%2FOS%2FOaJFssVvF6olk5WjK9gYxBDpUUiOQvyAIdhmRKiMfhfOSdT%2FgrPG06YGJE18lm4kIThxH3aqE1k2pl3gVd250QRFzGrFRCPgylnlm5C9xEFf2Mr794Dc2I2ki5GCR8Vhxwgi3rlCvI4G8R1PIXcwG7YfFyzb%2BgKUYCsAcvUschtbpWm5ahXZsJG2FioeFIzHbd3xQ5I2yjV9lrKyUiQHjxsyX7Z0dd7YkKkclmOR85wrhgxHLLpOrM021lYNbm1K9a%2FfPjIOxhMt3a1dgkwNaIJmgxnY3n%2FDgNSJsDpYEpckx9tNqbcuCEJYLC54fmbOH%2B3Nip%2Fks3X%2FBmvzo2iB79Y5cucIEkl9wFeKr9kqw5t5u4ciFf%2F4opHnT85eHZm3POEYsD9XxcIHUrlYyLbMawaFwBgklp6oo7LDNyAU%3D&Signature=%2BFGUxl8zViIqttg5f5y%2F9tbAQhw%3D\",\n    \"completedDate\": \"2017-05-10T18:31:35.5530698+00:00\",\n    \"rowsProcessed\": 8,\n    \"rowNumber\": 8\n  }\n]",
      "language": "text",
      "name": "200 - OK"
    }
  ]
}
[/block]