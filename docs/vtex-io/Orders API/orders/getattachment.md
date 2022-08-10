---
title: "List Order Attachment"
slug: "getattachment"
excerpt: "Retrieve an order attachment, by its name and order ID. For example, in case you need to get an attachment from order ID {{v5025004rjc-09}}, you should replace the variables {{orderId}} for {{v5025004rjc-09}} and {{attachmentName}} for the correspondent name of the attachment you're searching for."
hidden: false
createdAt: "2019-12-11T00:42:27.604Z"
updatedAt: "2020-02-17T21:20:21.221Z"
---
> Learn more about [Order Flow in VTEX Help](https://help.vtex.com/en/tutorial/order-flow-on-the-oms)


| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `orderId` | string | Order Id |
| `attachmentName` | string | Order Attachment Name |





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
      "code": "curl --location --request GET 'https://{{accountName}}.{{environment}}.com.br/api/oms/pvt/orders/{{orderId}}/message-attachment?attachmentName=teste' \\\n--header 'Accept: application/json' \\\n--header 'Content-Type: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]