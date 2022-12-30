---
title: "Get GiftCard Transactions"
slug: "getgiftcardtransactions"
excerpt: "Returns all transaction of a giftcard."
hidden: false
createdAt: "2019-12-25T01:06:56.455Z"
updatedAt: "2020-07-31T20:00:34.193Z"
---
## Response body has the following properties

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
        <td></td>
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

## Response body example

[block:code]
{
  "codes": [
    {
      "code": "[\n  {\n    \"id\": \"6\",\n    \"cardId\": \"b476900cde63460f8e2ebc0965527310\",\n    \"provider\": \"\",\n    \"_self\": {\n      \"href\": \"accountname/giftcards/6/transactions/b476900cde63460f8e2ebc0965527310\"\n    }\n  }\n]",
      "language": "json"
    }
  ]
}
[/block]
