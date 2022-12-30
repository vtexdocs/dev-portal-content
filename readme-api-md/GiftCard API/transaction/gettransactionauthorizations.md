---
title: "Get Transaction Authorizations"
slug: "gettransactionauthorizations"
excerpt: "Returns the giftcard transaction authorizations."
hidden: false
createdAt: "2019-12-25T01:06:56.455Z"
updatedAt: "2020-07-31T20:07:35.963Z"
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
        <td>Authorization's id</td>
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
      "code": "[\n  {\n        \"oid\": \"b476900cde63460f8e2ebc0965527310\",\n        \"value\": 200.0,\n        \"date\": \"2020-06-29T21:19:46.5466866Z\"\n }\n]",
      "language": "json"
    }
  ]
}
[/block]