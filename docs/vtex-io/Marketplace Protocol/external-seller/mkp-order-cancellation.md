---
title: "Marketplace Order Cancellation"
slug: "mkp-order-cancellation"
excerpt: "The seller must be ready to receive order cancellation requests from the marketplace. For that, you will need to implement the Marketplace Order Cancellation endpoint. Whenever this request is received by the seler, the order should be canceled and the fulfillment flow should not proceed.\n\nThe body of the request received by the seller contains only one information: the `marketplaceOrderId`, which identifies the order in the marketplace. The seller should use this ID to trigger the cancellation of the corresponding order.\n\nThe seller should then respond with the same `marketplaceOrderId` and also with the `orderId`, which identifies the order in the seller, the date and time of the notification receipt, and a protocol code that confirms the receipt of the request (which may have the value `null`)."
hidden: false
createdAt: "2020-09-01T13:10:10.118Z"
updatedAt: "2020-09-01T21:12:38.607Z"
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