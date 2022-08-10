---
title: "Create GiftCard Settlement Transaction"
slug: "creategiftcardsettlementtransaction"
excerpt: "Creates a settlement transaction to a giftcard."
hidden: false
createdAt: "2019-12-25T01:06:56.270Z"
updatedAt: "2020-07-22T15:09:34.492Z"
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
        <td>Settlement's ID</td>
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

##Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n        \"oid\": \"\",\n        \"value\": 300.0,\n        \"date\": \"2020-05-19T21:19:46.5466866Z\"\n}",
      "language": "json"
    }
  ]
}
[/block]