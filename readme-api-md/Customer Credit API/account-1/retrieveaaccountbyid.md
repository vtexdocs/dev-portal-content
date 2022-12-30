---
title: "Retrieve an Account by Id"
slug: "retrieveaaccountbyid"
excerpt: "Retrieve an account by id."
hidden: false
createdAt: "2019-12-24T00:49:31.616Z"
updatedAt: "2020-07-07T20:40:11.759Z"
---
#### Response body has the following properties

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
        <td><code>document</code></td>
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
        <td><code>documentType</code></td>
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
    <tr>
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
        <td><code>email</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
    <tr>
        <td><code>tolerance</code></td>
        <td>decimal</td>
        <td>Yes</td>
        <td></td>
    </tr>
    <tr>
        <td><code>availableTolerance</code></td>
        <td>decimal</td>
        <td>Yes</td>
        <td></td>
    </tr>
</table>

#### Response body example

[block:code]
{
  "codes": [
    {
      "code": "{\n    \"id\": \"\",\n    \"balance\": 0.0,\n    \"document\": \"\",\n    \"status\": \"Open\",\n    \"documentType\": \"CPF\",\n    \"creditLimit\": 500.0,\n    \"updatedAt\": \"2020-03-26T17:38:42.6147902Z\",\n    \"createdAt\": \"2019-12-03T00:19:03.4984796Z\",\n    \"description\": \"\",\n    \"availableCredit\": 500.0,\n    \"preAuthorizedCredit\": 0.0,\n    \"email\": \"\",\n    \"tolerance\": 0.0,\n    \"availableBalance\": 500.0\n}",
      "language": "json"
    }
  ]
}
[/block]
