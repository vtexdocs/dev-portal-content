---
title: "Get feed order status"
slug: "getfeedorderstatus"
hidden: true
createdAt: "2019-12-11T00:42:27.604Z"
updatedAt: "2020-02-20T14:47:52.212Z"
---
<div class="alert alert-danger">
Warning! We have a new version, please if you are starting a project know more about <a href="https://help.vtex.com/en/tutorial/orders-management-feed-v3" target="_blank">Feed v3 in VTEX Help</a>
</div>




## Request has the following properties:

| Attribute    | Type        | Description |
| --------------- |:---------:| --------------------------------------:|
| `accountName` | string | Account Name |
| `maxLot` | integer |  Lot quantity, maximum accept value is 10 |



## Response object has the following properties:

| Attribute    | Type        | Description |
| --------------- |:---------:| --------------------------------------:|
| `eventId` | string | Feed event ID |
| `handle` | string |  Event handle, used in Confirm Item Feed |
| `domain` | integer |  Order Source |
| `state` | integer |  Feed event state |
| `orderId` | string |  Order ID |

The event will be removed if the message "send retry" is equal to, or greater than the maximum retention period.
[block:api-header]
{
  "title": "Request body example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "curl --location --request GET 'https://{{accountName}}.{{environment}}.com.br/api/oms/pvt/feed/orders/status?maxLot={{maxLot}}' \\\n--header 'Accept: application/json' \\\n--header 'Content-Type: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]