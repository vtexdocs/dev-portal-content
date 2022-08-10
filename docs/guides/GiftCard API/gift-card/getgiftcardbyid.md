---
title: "Get GiftCard by ID"
slug: "getgiftcardbyid"
excerpt: "Returns associated data for a specified giftcardId."
hidden: false
createdAt: "2019-12-25T01:06:56.455Z"
updatedAt: "2021-09-27T15:19:41.296Z"
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
        <td>Gift card <code>id</code></td>
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
        <td>Gift card current balance. For Gift Cards newly created, the balance will be 0.0</td>
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
        <td><code>transaction</code></td>
        <td>object</td>
        <td>Yes</td>
        <td></td>
    </tr>
<tr>
        <td>&#x21B3; <code>href</code></td>
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
      "code": "{\n        \"id\": \"7\",\n        \"redemptionToken\": \"YIRV-NGSR-ECBY-DBBF\",\n        \"redemptionCode\": \"YIRV-NGSR-ECBY-DBBF\",\n        \"balance\": 122.1000,\n        \"relationName\": \"\",\n        \"emissionDate\": \"2020-07-30T15:04:42.643\",\n        \"expiringDate\": \"2020-09-01T13:15:30\",\n        \"caption\": \"\",\n        \"provider\": \"\",\n        \"transaction\": {\n                \"href\": \"/accountname/giftcards/7/transactions\"\n        }\n}",
      "language": "json"
    }
  ]
}
[/block]