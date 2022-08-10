---
title: "Retrieve Invoice by Id"
slug: "retrieveinvoicebyid"
excerpt: "Returns associated data for the specified Invoice Id, like status  and value, for example."
hidden: false
createdAt: "2019-12-24T00:49:31.616Z"
updatedAt: "2020-07-07T19:09:09.533Z"
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
        <td><code>id</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>status</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>value</code></td>
        <td>decimal</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>accountId</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
    <tr>
        <td><code>creditValue</code></td>
        <td>decimal</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>createdAt</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>resolvedAt</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>updatedAt</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <td><code>originalDueDate</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
    <tr>
        <td><code>dueDate</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>installment</code></td>
        <td>number</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>orderId</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>transactionId</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
<td><code>numberOfInstallments</code></td>
        <td>number</td>
        <td>Yes</td>
        <td></td>
    </tr>
    <tr>
        <td><code>creditAccountId</code></td>
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
      "code": "{\n    \"id\": \"\",\n    \"status\": \"Paid\",\n    \"value\": 101.22,\n    \"accountId\": \"\",\n    \"creditValue\": 0.0,\n    \"createdAt\": \"2019-12-08T16:13:36.0469451Z\",\n    \"resolvedAt\": \"2019-12-17T15:28:25.1776415Z\",\n    \"updatedAt\": \"2019-12-17T15:28:25.240167Z\",\n    \"originalDueDate\": \"2020-01-07T16:13:36.0469451Z\",\n    \"dueDate\": \"2020-01-07T16:13:36.0469451Z\",\n    \"installment\": 1,\n    \"orderId\": \"\",\n    \"transactionId\": \"\",\n    \"numberOfInstallments\": 1,\n    \"creditAccountId\": \"\"\n}",
      "language": "json"
    }
  ]
}
[/block]