---
title: "Retrieve store configuration"
slug: "retrievestoreconfiguration"
excerpt: "Get store configuration data."
hidden: false
createdAt: "2019-12-24T00:49:31.616Z"
updatedAt: "2020-07-09T20:45:15.386Z"
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
        <td><code>dailyInterestRate</code></td>
        <td>decimal</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>invoicePostponementLimit</code></td>
        <td>number</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>taxRate</code></td>
        <td>decimal</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>maxPostponementDays</code></td>
        <td>number</td>
        <td></td>
        <td></td>
    </tr>
 <tr>
        <td><code>defaultCreditValue</code></td>
        <td>decimal</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>automaticCheckingAccountCreationEnabled</code></td>
        <td>boolean</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>toleranceEnabled</code></td>
        <td>boolean</td>
        <td></td>
        <td></td>
    </tr>
 <tr>
        <td><code>myCreditsEnabled</code></td>
        <td>boolean</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>maxPreAuthorizationGrowthRate</code></td>
        <td>decimal</td>
        <td>Yes</td>
        <td></td>
    </tr>
 <tr>
        <td><code>notificationsSettings</code></td>
        <td>object</td>
        <td></td>
        <td></td>
    </tr>
<tr>
        <td>&#x21B3; <code>daysPrior</code></td>
        <td>array</td>
        <td></td>
        <td></td>
    </tr>
 <td>&#x21B3<code>daysAfter</code></td>
        <td>array</td>
        <td></td>
        <td></td>
    </tr>
 <tr>
        <td><code>days</code></td>
        <td>number</td>
        <td></td>
        <td></td>
    </tr>
 <tr>
        <td><code>timeOfDay</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>
</table>

<br>

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"dailyInterestRate\": 0.5,\n    \"invoicePostponementLimit\": 1,\n    \"taxRate\": 0.4,\n    \"maxPostponementDays\": 3,\n    \"defaultCreditValue\": 100.0,\n    \"postponementEnabled\": false,\n    \"automaticCheckingAccountCreationEnabled\": false,\n    \"toleranceEnabled\": false,\n    \"myCreditsEnabled\": false,\n    \"maxPreAuthorizationGrowthRate\": 0.2,\n    \"notificationsSettings\": {\n        \"daysPrior\": [],\n        \"daysAfter\": [\n            {\n                \"days\": 1,\n                \"timeOfDay\": \"16:00:00\"\n            },\n            {\n                \"days\": 0,\n                \"timeOfDay\": \"12:00:00\"\n            }\n        ]\n    }\n}",
      "language": "json"
    }
  ]
}
[/block]