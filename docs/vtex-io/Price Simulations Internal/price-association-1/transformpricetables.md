---
title: "Transform pricetables"
slug: "transformpricetables"
hidden: true
createdAt: "2021-02-02T13:50:02.025Z"
updatedAt: "2021-02-02T21:15:02.526Z"
---
## Request Headers 
---
<table>
  <tr>
        <td><b>Header</b></td>
        <td><b>Value</b></td>
    </tr>
    <tr>
        <td><code>Content-Type</code></td>
        <td><b>application/json</b></td>
    </tr>
  <tr>
        <td><code>Accept</code></td>
        <td><b>application/json</b></td>
    </tr>
</table>

<br>

## Request Body
---
<table>
    <tr>
        <th>Name</th>
        <th>Type</th>
        <th>Mandatory</th>
        <th>Description</th>
    </tr>
    <tr>
        <td><code>public</code></td>
        <td>object</td>
        <td>Yes</td>
        <td>Object to register session criteria</td>
    </tr>
    <tr>
        <td>&#x21B3;<code>customSessionKeys</code></td>
        <td>object</td>
        <td>Yes</td>
        <td>Criteria of the Custom Price you want to be retrieved</td>
    </tr>
     <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3;<code>value</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Order Configuration criteria</td>
    </tr>
    <tr>
        <td><code>profile</code></td>
        <td>object</td>
        <td>Yes</td>
        <td>Object to register session criteria</td>
    </tr>
    <tr>
        <td>&#x21B3;<code>email</code></td>
        <td>object</td>
        <td>Yes</td>
        <td>User's email</td>
    </tr>
     <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3;<code>value</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Order Configuration criteria</td>
    </tr>
</table>
<br>

## Response Body 
---

<table>
    <tr>
        <th>Name</th>
        <th>Type</th>
        <th>Mandatory</th>
        <th>Description</th>
    </tr>
    <tr>
        <td><code>profile</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
    <tr>
        <td>&#x21B3;<code>priceTables</code></td>
        <td>object</td>
        <td>Yes</td>
        <td></td>
    </tr>
         <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3;<code>value</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Order Configuration criteria</td>
    </tr>
</table>
<br>

## Request examples and their responses 
---
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"profile\": {\n        \"priceTables\": {\n            \"value\": \"\"\n        }\n    }\n}",
      "language": "curl",
      "name": "200 - OK"
    }
  ]
}
[/block]