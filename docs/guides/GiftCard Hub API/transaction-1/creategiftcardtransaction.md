---
title: "Create GiftCard Transaction"
slug: "creategiftcardtransaction"
excerpt: "Creates a transaction to a giftcard."
hidden: false
createdAt: "2019-12-25T01:06:56.270Z"
updatedAt: "2020-07-16T15:29:02.222Z"
---
## Response body has the following properties: 
<table>
    <tr>
        <th>Name</th>
        <th>Type</th>
        <th> Mandatory </th>
        <th>Description</th>
    </tr>
<tr>
        <td><code>provider</code></td>
        <td>string</td>
       <td></td>
        <td></td>
    </tr>    
<tr>
        <td><code>cardId</code></td>
        <td>string</td>
       <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>id</code></td>
        <td>string</td>
         <td>Yes</td>
        <td>Transaction's ID</td>
    </tr>
 <tr>
        <td><code>_self</code></td>
        <td>object</td>
        <td>Yes</td>
        <td></td>
    </tr>
    <tr>
        <td><code>href</code></td>
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
      "code": "{\n        \"provider\": \"\",\n        \"cardId\": \"6\",\n        \"id\": \"\",\n        \"_self\":{\n            \"href\": \"\"\n        }\n}",
      "language": "json"
    }
  ]
}
[/block]