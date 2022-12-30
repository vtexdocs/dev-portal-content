---
title: "Get Transaction Cancellations"
slug: "gettransactioncancellations"
excerpt: "Returns the giftcard transaction cancellations."
hidden: false
createdAt: "2019-12-25T01:06:56.455Z"
updatedAt: "2020-07-31T20:10:56.639Z"
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

<br>

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "[{\n        \"oid\": \"b6a120d512534564813fd76a491ff5e7\",\n        \"value\": 13.00,\n        \"date\": \"2020-07-01T20:10:35.3516996Z\"\n}]",
      "language": "json"
    }
  ]
}
[/block]