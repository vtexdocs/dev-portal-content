---
title: "Get GiftCard using JSON"
slug: "getgiftcardusingjson"
excerpt: "Returns the giftcards based on the cart data."
hidden: false
createdAt: "2019-12-25T01:06:56.455Z"
updatedAt: "2020-07-13T15:02:48.473Z"
---
## WARNING
---
Giftcards with balance 0.0 must be not returned if user is not authenticated.
<br>

## Response body has the following properties:
<table>
    <tr>
        <th>Name</th>
        <th>Type</th>
        <th>Mandatory</th>
        <th>Description</th>
    </tr>
    <tr>
        <td><code>id</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Gift card <code>id</code></td>
    </tr>
 <tr>
        <td><code>provider</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>balance</code></td>
        <td>string</td>
        <td></td>
        <td>Gift card current balance. For Gift Cards newly created, the balance will be 0.0</td>
    </tr>
 <tr>
        <td><code>totalBalance</code></td>
        <td>decimal</td>
        <td></td>
        <td></td>
    </tr>
 <tr>
        <td><code>relationName</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>caption</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>groupName</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
 <tr>
        <td><code>transaction</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
<tr>
        <td>&#x21B3;<code>href</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Resource URL</td>
    </tr>
</table>

<br>

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "[   \n    {\n        \"id\": \"\"\n        \"provider\": \"\",\n        \"balance\": 0, \n        \"totalBalance\": 0, \n        \"relationName\": \"\",\n        \"caption\": \"\",\n        \"groupName\": \"\",\n        \"transaction\": {\n            \"href\": \"\"\n        }\n    }\n]",
      "language": "json"
    }
  ]
}
[/block]