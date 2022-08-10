---
title: "Change credit limit of an Account"
slug: "changecreditlimitofanaccount"
excerpt: "Increase the credit limit of an account."
hidden: false
createdAt: "2019-12-24T00:49:31.616Z"
updatedAt: "2020-07-08T20:40:51.560Z"
---
## Warning
---
The value will be summed with the current account credit limit.

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
        <td><code>balance</code></td>
        <td>decimal</td>
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
        <td><code>creditLimit</code></td>
        <td>decimal</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>updatedAt</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>createdAt</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <td><code>description</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
    <tr>
        <td><code>availableCredit</code></td>
        <td>decimal</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>preAuthorizedCredit</code></td>
        <td>decimal</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>tolerance</code></td>
        <td>decimal</td>
        <td>Yes</td>
        <td></td>
    </tr>
<td><code>availableTolerance</code></td>
        <td>decimal</td>
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
      "code": "{\n    \"id\": \"\",\n    \"balance\": 0.0,\n    \"status\": \"Open\",\n    \"creditLimit\": 5000.0,\n    \"updatedAt\": \"2020-07-07T21:31:23.5189979Z\",\n    \"createdAt\": \"2020-06-30T18:49:35.424369Z\",\n    \"description\": \"\",\n    \"availableCredit\": 5000.0,\n    \"preAuthorizedCredit\": 0.0,\n    \"tolerance\": 0.0,\n    \"availableBalance\": 5000.0\n}",
      "language": "json"
    }
  ]
}
[/block]