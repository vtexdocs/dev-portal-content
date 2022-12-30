---
title: "Account statements"
slug: "accountstatements"
excerpt: "Get the account statements."
hidden: false
createdAt: "2019-12-24T00:49:31.616Z"
updatedAt: "2022-01-05T15:04:13.708Z"
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
        <td><code>statements</code></td>
        <td>array</td>
        <td>Yes</td>
        <td></td>
    </tr>
    <tr>
        <td>&#x21B3;<code>value</code></td>
        <td>decimal</td>
        <td>Yes</td>
        <td></td>
    </tr>
    <tr>
        <td>&#x21B3; <code>date</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
    <tr>
        <td>&#x21B3; <code>origin</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
    <tr>
        <td><code>currentBalance</code></td>
        <td>decimal</td>
        <td>Yes</td>
        <td>Current balance value</td>
    </tr>
    <tr>
        <td><code>intervalBalance</code></td>
        <td>decimal</td>
        <td>Yes</td>
        <td>Balance range that has changed in the listing items</td>
    </tr>
    <tr>
        <td><code>previousBalance</code></td>
        <td>decimal</td>
        <td>Yes</td>
        <td>Balance value before listing items</td>
    </tr>
</table>

## Response body example

[block:code]
{
  "codes": [
    {
      "code": "{\n    \"statements\": [\n        {\n            \"value\": 40.0,\n            \"date\": \"2020-07-07T21:31:23.1126811Z\",\n            \"origin\": \"Credit\"\n        }\n    ],\n    \"currentBalance\": 0.0,\n    \"intervalBalance\": 40.0,\n    \"previousBalance\": 0.0\n}",
      "language": "json"
    }
  ]
}
[/block]
