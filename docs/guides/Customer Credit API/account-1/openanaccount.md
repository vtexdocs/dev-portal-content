---
title: "Open an Account"
slug: "openanaccount"
excerpt: "Open an account."
hidden: false
createdAt: "2019-12-24T00:49:31.616Z"
updatedAt: "2022-05-27T19:21:08.659Z"
---
[block:callout]
{
  "type": "warning",
  "body": "This request should only be used if you do not have an account yet registered. If you already have an account (open or closed) and want to create or modify an account, go to [Open or Change Account](https://developers.vtex.com/vtex-rest-api/reference/openorchangeaccount)."
}
[/block]

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

## Response body example

[block:code]
{
  "codes": [
    {
      "code": "{\n    \"id\": \"\",\n    \"balance\": 0.0,\n    \"document\": \"\",\n    \"status\": \"Open\",\n    \"documentType\": \"CPF\",\n    \"creditLimit\": 500.0,\n    \"updatedAt\": \"2020-07-07T20:25:19.0836013Z\",\n    \"createdAt\": \"2020-07-07T20:25:19.0366858Z\",\n    \"description\": \"\",\n    \"availableCredit\": 500.0,\n    \"preAuthorizedCredit\": 0.0,\n    \"email\": \"\",\n    \"tolerance\": 1.0,\n    \"availableBalance\": 500.0\n}",
      "language": "json"
    }
  ]
}
[/block]
