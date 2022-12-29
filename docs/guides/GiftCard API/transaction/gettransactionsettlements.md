---
title: "Get Transaction Settlements"
slug: "gettransactionsettlements"
excerpt: "Returns the giftcard transaction settlements."
hidden: false
createdAt: "2019-12-25T01:06:56.455Z"
updatedAt: "2020-08-19T22:00:51.768Z"
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
        <td>Settlement's id</td>
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
      "code": "[\n  {\n        \"oid\": \"\",\n        \"value\": 0,\n        \"date\": \"2020-07-01T20:10:35.3516996Z\"\n}\n]",
      "language": "json"
    }
  ]
}
[/block]