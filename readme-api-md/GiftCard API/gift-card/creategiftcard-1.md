---
title: "Create GiftCard"
slug: "creategiftcard-1"
excerpt: "Creates a GiftCard for a specific user"
hidden: false
createdAt: "2019-12-25T01:06:56.455Z"
updatedAt: "2022-11-01T14:16:19.655Z"
---

## Warning

- The field `userProfileId` should be filled with a value that identifies the client. It is the ID itself.
- The field `expiringDate` should be filled in ISO 8601 format `YYYY-MM-DDThh:mm:ss.fff`

> ℹ️️ The `redemptionCode` field for a Gift Card is auto-generated on creation and cannot be set to an arbitrary value.

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
        <td></td>
        <td>Field to be filled in when it is not necessary to use a loyalty program for the Gift Card. Observation: A
            new <code>relationName</code>value is required for each new Gift Card to be created.</td>
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
        <td></td>
        <td>Field to be filled in if a loyalty program must be created for the Gift Card.</td>
    </tr>
    <tr>
        <td><code>transaction</code></td>
        <td>object</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>&#x21B3; <code>href</code></td>
        <td>string</td>
        <td></td>
        <td>Resource URL</td>
    </tr>
</table>

## Response body example

[block:code]
{
  "codes": [
    {
      "code": "{\n        \"id\": \"teste@teste.com.br_7\",\n        \"redemptionToken\": \"YIRV-NGSR-ECBY-DBBF\",\n        \"redemptionCode\": \"YIRV-NGSR-ECBY-DBBF\",\n        \"balance\": 122.1000, \n        \"relationName\": \"\",\n        \"emissionDate\": \"2020-07-30T15:04:42.6432065Z\", \n        \"expiringDate\": \"2020-09-01T13:15:30Z\", \n        \"caption\": \"VTEX Fidelidade\",\n        \"provider\": \"\",\n        \"groupName\": \"\", \n        \"transaction\": {\n                \"href\": \"/accountname/giftcards/teste@teste.com.br_7/transactions\"\n        }\n}",
      "language": "json"
    }
  ]
}
[/block]
