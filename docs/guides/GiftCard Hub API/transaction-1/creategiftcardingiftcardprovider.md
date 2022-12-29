---
title: "Create GiftCard in GiftCard Provider"
slug: "creategiftcardingiftcardprovider"
excerpt: "Creates a giftcard in a giftcard provider."
hidden: false
createdAt: "2019-12-25T01:06:56.270Z"
updatedAt: "2020-07-10T17:31:12.671Z"
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
        <td><code>redemptionToken</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>redemptionCode</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>balance</code></td>
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
        <td><code>emissionDate</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>
 <tr>
        <td><code>expiringDate</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>
 <tr>
        <td><code>caption</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>provider</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>discount</code></td>
        <td>boolean</td>
        <td>Yes</td>
        <td></td>
    </tr>
<tr>
        <td><code>transaction</code></td>
        <td>object</td>
        <td>Yes</td>
        <td></td>
    </tr>
<tr>
        <td>&#x21B3;<code>href</code></td>
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
      "code": "{\n        \"id\": \"\",\n        \"redemptionToken\": \"\",\n        \"redemptionCode\": \"\",\n        \"balance\": 0.0,  \n        \"relationName\": \"\",\n        \"emissionDate\": Date, \n        \"expiringDate\": Date, \n        \"caption\": \"\",\n        \"provider\": \"\",\n        \"discount\": false,\n        \"groupName\": \"\",\n        \"transaction\": {\n            \"href\": \"\"\n        }\n}",
      "language": "json"
    }
  ]
}
[/block]