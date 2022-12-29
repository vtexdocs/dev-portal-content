---
title: "Cancel GiftCard Transaction"
slug: "cancelgiftcardtransaction"
excerpt: "Creates a cancellation in the transaction. Cancel a item reservation or create a refund."
hidden: false
createdAt: "2019-12-25T01:06:56.455Z"
updatedAt: "2020-07-31T20:12:43.996Z"
---
## Response body has the following properties: 
<table>
    <tr>
        <th>Name</th>
        <th>Type</th>
        <th>Mandatory</th>
        <th>Description</th>
    </tr>
    <tr>
        <td><code>oid</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Cancellation's id</td>
    </tr>
 <tr>
        <td><code>value</code></td>
        <td>decimal</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>date</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
</table>

<br></br>

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n        \"oid\": \"b6a120d512534564813fd76a491ff5e7\",\n        \"value\": 13.0,\n        \"date\": \"2020-07-01T20:10:35.3516996Z\"\n}",
      "language": "json"
    }
  ]
}
[/block]