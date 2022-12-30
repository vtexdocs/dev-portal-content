---
title: "Marketplace order cancellation"
slug: "marketplace-order-cancellation"
excerpt: "This request may be sent from VTEX to the external seller in case of order cancelation. For that, the seller will need to implement the Marketplace order cancellation endpoint. Whenever this request is received by the seler, the order should be canceled and the fulfillment flow should not proceed. \n\nFor the seller to: \n\n- **Evaluate a cancellation request:** it is possible to send an empty body as a response to the cancellation request, meaning that the seller is evaluating whether to proceed with the cancellation or not. \n\n- **Confirm the cancellation request:** it is possible to confirm the order cancellation by the marketplace by responding to the call with a body including only one information: the `marketplaceOrderId`, which identifies the order in the marketplace. The seller should use this ID to trigger the cancellation of the corresponding order. The seller should then respond with the same `marketplaceOrderId` and also with the `orderId`, which identifies the order in the seller, the date and time of the notification receipt, and a protocol code that confirms the receipt of the request (which may have the value `null`). \n\n- **Refuse a cancellation request:** it is possible to to [send the Invoice](https://developers.vtex.com/vtex-rest-api/reference/external-seller#send-invoice), meaning that the cancellation has been denied, and the flow continues to the [Order Invoicing](https://developers.vtex.com/vtex-rest-api/docs/external-seller-integration-connector#order-invoicing) step, and the ones that follow it. \n\nThis call should be made twice: once for the *Evaluate cancellation request* scenario, and a second time to *Confirm cancellation* or *Refuse cancellation*."
hidden: false
createdAt: "2020-09-01T13:10:10.118Z"
updatedAt: "2022-01-26T21:01:04.669Z"
---
## Request body example
[block:code]
{
  "codes": [
    {
      "code": "{\n   \"marketplaceOrderId\": \"959311095\"\n}",
      "language": "json"
    }
  ]
}
[/block]
## Response body fields

<table>
    <tr>
        <th>Name</th>
        <th>Type</th>
        <th>Mandatory</th>
        <th>Description</th>
    </tr>
    <tr>
        <td><code>date</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Date and time of the notification receipt.</td>
    </tr>
    <tr>
        <td><code>marketplaceOrderId</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>ID that identifies the order in the marketplace.</td>
    </tr>
    <tr>
        <td><code>orderId</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>ID that identifies the order in the seller.</td>
    </tr>
    <tr>
        <td><code>receipt</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Protocol code that confirms the receipt of the request. The value of this field may be null.</td>
    </tr>
</table>

## Response body example
[block:code]
{
  "codes": [
    {
      "code": "{\n   \"date\": \"2014-10-06 18:52:00\",\n   \"marketplaceOrderId\": \"959311095\",\n   \"orderId\": \"123543123\",\n   \"receipt\": \"e39d05f9-0c54-4469-a626-8bb5cff169f8\"\n}",
      "language": "json"
    }
  ]
}
[/block]