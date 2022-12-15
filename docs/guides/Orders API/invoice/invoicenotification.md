---
title: "Order invoice notification"
slug: "invoicenotification"
excerpt: "Entering the [invoice in the order](https://help.vtex.com/en/tracks/orders--2xkTisx4SXOWXQel8Jg8sa/2WgQrlHTyVo4hLjhUs1LMT) is a required step for its [status](https://help.vtex.com/en/tutorial/order-flow-and-status--tutorials_196#order-status-details) to change to Invoiced - a sign that the order has been successfully completed. Remember that once an order is read as invoiced by the system, this status cannot be changed. \n\nThe total value of the order will be updated after the insertion of the invoice, even when there's a [Partial invoice](https://help.vtex.com/en/tracks/orders--2xkTisx4SXOWXQel8Jg8sa/q9GPspTb9cHlMeAZfdEUe) scenario. The updated value is settled by VTEX's Payment Gateway. The reimbursement for the shopper is automatic. \n\nWe strongly recommend that you always send the object of the invoiced items. With this practice, rounding errors will be avoided. \n\nWhen returning items, an input invoice must be sent through this call. For that, the `type` field should be filled in with `input`. \n\nIt is not allowed to use the same `invoiceNumber` in more than one request to the Order Invoice Notification endpoint.\n\nFor marketplace integrations: once the order is invoiced, the seller should use this request to send the invoice information to the marketplace. Be aware that this endpoint is also used by the seller to send the order tracking information. This, however, should be done in a separate moment, once the seller has the tracking information.  \n\r\n\r> The `Notify invoice` resource is needed to use this API request. This is included in `OMS - Full access` and `IntegrationProfile - Fulfillment Oms`, among other default roles available in the Admin. Learn more about the [License manager roles and resources](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc#).\n\r\n\r> 📘 Onboarding guide \r\n>\r\n> Check the new [Orders onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/orders-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Orders and is organized by focusing on the developer's journey."
hidden: false
createdAt: "2019-12-11T00:42:27.604Z"
updatedAt: "2022-11-04T14:49:17.107Z"
---
## Request body example
[block:code]
{
  "codes": [
    {
      "code": "{\n   \"type\": \"Output\",\n   \"invoiceNumber\": \"NFe-00001\",\n   \"courier\": \"\",\n   \"trackingNumber\": \"\",\n   \"trackingUrl\": \"\",\n   \"items\": [\n      {\n         \"id\": \"345117\",\n         \"quantity\": 1,\n         \"description\": \"335\",\n         \"price\": 9003\n      }\n   ],\n   \"issuanceDate\": \"2013-11-21T00:00:00\",\n   \"invoiceValue\": 9508\n}",
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