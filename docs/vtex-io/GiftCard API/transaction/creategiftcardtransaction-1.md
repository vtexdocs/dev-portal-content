---
title: "Create GiftCard Transaction"
slug: "creategiftcardtransaction-1"
excerpt: "Register a new giftcard transaction and authorize the item reservation."
hidden: false
createdAt: "2019-12-25T01:06:56.455Z"
updatedAt: "2020-07-27T14:42:25.687Z"
---
## WARNING
---
The Gift Card System collection was deprecated. 

From now on, the user can edit the Gift Card's credit using the fields `operation` and `value`.
To increase the balance, the user can fill the field `operation` with `credit` in the body's request. To decrease the balance, fill the field `operation` with `debit` also in the body's request. 

In both cases, the user can fill the field `value` to set the amount of credit you want to add or subtract from the balance.

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
        <td> Transaction Id</td>
    </tr>
 <tr>
        <td><code>cardId</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Gift card <code>id</code></td>
    </tr>
<tr>
        <td><code>provider</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></code></td>
    </tr>
 <tr>
        <td><code>_self</code></td>
        <td>object</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td>&#x21B3; <code>href</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Resource Url</td>
    </tr>
</table>

<br>

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"id\": \"7\",\n  \"cardId\": \"155f9212323d47d5b72ba31e9a031dd9\",\n  \"provider\": \"\",\n  \"_self\": {\n    \"href\": \"cosmetics2/giftcards/7/transactions/155f9212323d47d5b72ba31e9a031dd9\"\n  }\n}",
      "language": "json"
    }
  ]
}
[/block]