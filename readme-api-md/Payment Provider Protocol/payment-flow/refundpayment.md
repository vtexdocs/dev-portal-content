---
title: "Refund Payment"
slug: "refundpayment"
excerpt: "Refunds a payment that was previously settled. You can expect partial refunds."
hidden: false
createdAt: "2019-12-30T03:21:07.203Z"
updatedAt: "2022-04-04T14:22:57.854Z"
---
<br>

## Request body
---

<table>
    <tr>
        <th>Name</th>
        <th>Type</th>
        <th>Mandatory</th>
        <th>Description</th>
    </tr>
      <tr>
        <td><code>requestId</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Provider's settlement identifier</td>
    </tr>
      <tr>
        <td><code>settleId</code></td>
        <td>number</td>
        <td>Yes</td>
        <td>The authorization identifier for this payment</td>
    </tr>
    <tr>
        <td><code>paymentId</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>VTEX payment ID from this payment</td>
    </tr>
      <tr>
        <td><code>tid</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Provider's unique identifier for the transaction</td>
    </tr>
    <tr>
        <td><code>value</code></td>
        <td>number</td>
        <td>Yes</td>
        <td>The amount to be settled/captured</td>
    </tr>
      <tr>
        <td><code>transactionId</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>VTEX identifier for this transaction</td>
    </tr>
      <tr>
        <td><code>recipients</code></td>
        <td>array</td>
        <td></td>
        <td>Array containing the information for the recipients of this payment in case the Payment Provider is configured to allow the split of payments</td>
    </tr>
     <tr>
        <td>&#x21B3;<code>id</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Recipient identifier</td>
    </tr>
    <tr>
        <td>&#x21B3;<code>name</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Recipient name</td>
    </tr>
     <tr>
        <td>&#x21B3;<code>documentType</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Recipient document type</td>
    </tr>
       <tr>
        <td>&#x21B3;<code>document</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Recipient document number</td>
    </tr>
    <tr>
        <td>&#x21B3;<code>role</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Indicates if the recipient is the seller or the marketplace</td>
    </tr>
     <tr>
        <td>&#x21B3;<code>chargeProcessingFee</code></td>
        <td>boolean</td>
        <td></td>
        <td>Indicates whether or not this recipient is charged for processing fees</td>
    </tr>
     <tr>
        <td>&#x21B3;<code>chargebackLiable</code></td>
        <td>boolean</td>
        <td></td>
        <td>Indicates whether or not this recipient is liable to chargebacks</td>
    </tr>
     <tr>
        <td>&#x21B3;<code>amount</code></td>
        <td>number</td>
        <td>Yes</td>
        <td>Amount due to this recipient</td>
    </tr>
     <tr>
        <td><code>sandboxMode</code></td>
        <td>boolean</td>
        <td></td>
        <td>Indicates whether or not this request is being sent from a sandbox environment</td>
    </tr>
</table>

<br>

## Response body
---

<table>
    <tr>
        <th>Name</th>
        <th>Type</th>
        <th>Mandatory</th>
        <th>Description</th>
    </tr>
    <tr>
        <td><code>paymentId</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>The same <code>paymentId</code> sent in the request</td>
    </tr>
    <tr>
        <td><code>refundId</code></td>
        <td>string</td>
        <td></td>
        <td>Provider's refund identifier (if the operation has failed you <strong>MUST</strong> return <code>null</code>)</td>
    </tr>
    <tr>
        <td><code>value</code></td>
        <td>decimal</td>
        <td>Yes</td>
        <td>The amount that was refunded (if the operation has failed you <strong>MUST</strong> return <code>0</code>)</td>
    </tr>
    <tr>
        <td><code>code</code></td>
        <td>string</td>
        <td></td>
        <td>Provider's operation/error code to be logged (return <code>refund-manually</code> if you do not support this operation, so we can send a notification to the merchant)</td>
    </tr>
    <tr>
        <td><code>message</code></td>
        <td>string</td>
        <td></td>
        <td>Provider's operation/error message to be logged</td>
    </tr>
    <tr>
        <td><code>requestId</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>The same <code>requestId</code> sent in the request</td>
    </tr>
</table>

## Request examples and their responses
[block:code]
{
  "codes": [
    {
      "code": "curl --location --request POST 'https://{{providerApiEndpoint}}/payments/{{paymentId}}/refunds' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'Content-Type: application/json' \\\n--header 'Accept: application/json' \\\n--data-raw '{\n    \"paymentId\": \"F5C1A4E20D3B4E07B7E871F5B5BC9F91\",\n    \"transactionId\": \"D3AA1FC8372E430E8236649DB5EBD08E\",\n    \"settleId\": \"Q5C1A4E20D3B4E07B7E871F5B5BC9F91\",\n    \"value\": 57.0,\n    \"requestId\": \"LA4E20D3B4E07B7E871F5B5BC9F91\"\n}'",
      "language": "curl",
      "name": "Success"
    },
    {
      "code": "curl --location --request POST 'https://{{providerApiEndpoint}}/payments/{{paymentId}}/refunds' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'Content-Type: application/json' \\\n--header 'Accept: application/json' \\\n--data-raw '{\n    \"paymentId\": \"F5C1A4E20D3B4E07B7E871F5B5BC9F91\",\n    \"transactionId\": \"D3AA1FC8372E430E8236649DB5EBD08E\",\n    \"settleId\": \"Q5C1A4E20D3B4E07B7E871F5B5BC9F91\",\n    \"value\": 57.0,\n    \"requestId\": \"LA4E20D3B4E07B7E871F5B5BC9F91\"\n}'",
      "language": "curl",
      "name": "Fail Not Implemented"
    },
    {
      "code": "curl --location --request POST 'https://{{providerApiEndpoint}}/payments/{{paymentId}}/refunds' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'Content-Type: application/json' \\\n--header 'Accept: application/json' \\\n--data-raw '{\n    \"paymentId\": \"F5C1A4E20D3B4E07B7E871F5B5BC9F91\",\n    \"transactionId\": \"D3AA1FC8372E430E8236649DB5EBD08E\",\n    \"settleId\": \"Q5C1A4E20D3B4E07B7E871F5B5BC9F91\",\n    \"value\": 57.0,\n    \"requestId\": \"LA4E20D3B4E07B7E871F5B5BC9F91\"\n}'",
      "language": "curl",
      "name": "Fail Generic Error"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"paymentId\": \"F5C1A4E20D3B4E07B7E871F5B5BC9F91\",\n  \"refundId\": \"2EA354989E7E4BBC9F9D7B66674C2574\"\n  \"value\": 57,\n  \"code\": null,\n  \"message\": \"Sucessfully refunded\",\n  \"requestId\": \"LA4E20D3B4E07B7E871F5B5BC9F91\"\n}",
      "language": "curl",
      "name": "200 - OK"
    },
    {
      "code": "{\n  \"paymentId\": \"F5C1A4E20D3B4E07B7E871F5B5BC9F91\",\n  \"refundId\": null,\n  \"value\": 0,\n  \"code\": \"ERR123\",\n  \"message\": \"Refund has failed due to an internal error\",\n  \"requestId\": \"LA4E20D3B4E07B7E871F5B5BC9F91\"\n}",
      "language": "curl",
      "name": "500 - Internal Server Error"
    },
    {
      "code": "{\n  \"paymentId\": \"F5C1A4E20D3B4E07B7E871F5B5BC9F91\",\n  \"refundId\": null,\n  \"value\": 0,\n  \"code\": \"refund-manually\",\n  \"message\": \"This payment needs to be manually refunded\",\n  \"requestId\": \"LA4E20D3B4E07B7E871F5B5BC9F91\"\n}",
      "language": "curl",
      "name": "501 - Not Implemented"
    }
  ]
}
[/block]