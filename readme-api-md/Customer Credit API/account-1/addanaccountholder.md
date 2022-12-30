---
title: "Add an account Holder"
slug: "addanaccountholder"
hidden: false
createdAt: "2019-12-24T00:49:31.616Z"
updatedAt: "2020-07-08T21:04:14.589Z"
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
        <td><code>level</code></td>
        <td>number</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>claims</code></td>
        <td>object</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td>&#x21B3;<code>email</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>id</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>
 <tr>
        <td><code>createdAt</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
</table>

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"level\": 2,\n    \"claims\": {\n        \"email\": \"\"\n    },\n    \"id\": \"\",\n    \"createdAt\": \"2020-07-08T20:53:09.1309171Z\"\n}",
      "language": "text"
    }
  ]
}
[/block]