---
title: "Order Invoice Notification"
slug: "invoicenotification"
excerpt: "Once the order is invoiced, the seller should use this request to send the invoice information to the marketplace.\n\nWe strongly recommend that you always send the object of the invoiced items. With this practice, rounding errors will be avoided.\n\nIt is not allowed to use the same `invoiceNumber` in more than one request to the Order Invoice Notification endpoint.\n\nBe aware that this endpoint is also used by the seller to send the order tracking information. This, however, should be done in a separate moment, once the seller has the tracking information."
hidden: false
createdAt: "2019-12-11T00:42:27.604Z"
updatedAt: "2020-09-01T12:31:32.394Z"
---
## Request body example
[block:code]
{
  "codes": [
    {
      "code": "{\n   \"type\": \"Output\",\n   \"invoiceNumber\": \"NFe-00001\",\n   \"courier\": \"\",\n   \"trackingNumber\": \"\",\n   \"trackingUrl\": \"\",\n   \"items\": [\n      {\n         \"id\": \"345117\",\n         \"quantity\": 1,\n         \"price\": 9003\n      }\n   ],\n   \"issuanceDate\": \"2013-11-21T00:00:00\",\n   \"invoiceValue\": 9508\n}",
      "language": "json"
    }
  ]
}
[/block]
## Response body fields

| Field    | Type        | Description |
| --------------- |:---------:| --------------------------------------:|
| `date` | string | Invoice Date |
| `orderId` | string | Order Id |
| `receipt` | string | Invoice receipt confirmation ID |

## Response body example
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"date\": \"2019-02-08T13:16:13.4617653+00:00\",\n  \"orderId\": \"00-v5195004lux-01\",\n  \"receipt\": \"527b1ae251264ef1b7a9b597cd8f16b9\"\n}",
      "language": "json",
      "name": "200 - OK"
    }
  ]
}
[/block]