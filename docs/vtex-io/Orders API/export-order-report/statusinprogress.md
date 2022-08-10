---
title: "Export Order Report with Status 'In Progress'"
slug: "statusinprogress"
excerpt: "Retrieves a list of all order reports that are 'in progress', by 'accountName'."
hidden: false
createdAt: "2019-12-11T00:42:27.604Z"
updatedAt: "2020-02-28T14:18:17.177Z"
---
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
      "code": "curl --location --request GET 'https://accountname.vtexcommercestable.com.br/api/oms/pvt/admin/reports/inprogress' \\\n--header 'Content-Type: application/json' \\\n--header 'x-vtex-api-appKey: {{X-VTEX-API-AppKey}}' \\\n--header 'x-vtex-api-appToken: {{X-VTEX-API-AppToken}}'",
      "language": "text",
      "name": "Request example"
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
      "code": "[\n  {\n    \"id\": \"b7bdafba-2456-4aba-9bc0-1d598df685bd\",\n    \"cancelled\": false,\n    \"query\": \"{\\\"Queries\\\":[{\\\"Quoted\\\":true,\\\"FieldName\\\":\\\"InstanceId\\\",\\\"FieldValue\\\":\\\"263FD533551E445CACEEC991385EF610\\\"},{\\\"Quoted\\\":true,\\\"FieldName\\\":\\\"OrderIsComplete\\\",\\\"FieldValue\\\":\\\"True\\\"}],\\\"Oper\\\":\\\"AND\\\"}\",\n    \"filter\": \"generateCsv=true&orderBy=creationDate%2cdesc&page=1&utc=-0300\",\n    \"email\": \"renan.servare@vtex.com.br\",\n    \"hostUri\": \"http://accountname.vtexcommercestable.com.br/\",\n    \"utcTime\": \"-0300\",\n    \"dateOfRequest\": \"2017-05-10T16:21:31.7452567+00:00\",\n    \"startDate\": \"2017-05-10T16:21:30.7714518+00:00\",\n    \"lasUpdateTime\": \"2017-05-10T16:21:30.7714518+00:00\",\n    \"instanceId\": \"i-0a3b7a89f1fe13ba9\",\n    \"publishId\": \"263fd533551e445caceec991385ef610\",\n    \"linkToDownload\": null,\n    \"completedDate\": null,\n    \"rowsProcessed\": 0,\n    \"rowNumber\": null\n  }\n]",
      "language": "text",
      "name": "200 - OK"
    }
  ]
}
[/block]