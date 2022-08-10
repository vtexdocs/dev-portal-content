---
title: "Capture Payment"
slug: "capturepayment"
excerpt: "Captures (settle) a payment that was previously approved."
hidden: false
createdAt: "2019-12-30T03:21:07.203Z"
updatedAt: "2020-11-05T13:33:01.050Z"
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
        <td><code>transactionId</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>VTEX transaction ID related to this payment</td>
    </tr>
      <tr>
        <td><code>requestId</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>The unique identifier for this request to ensure its idempotency</td>
    </tr>
    <tr>
        <td><code>paymentId</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>VTEX payment ID from this payment</td>
    </tr>
    <tr>
        <td><code>value</code></td>
        <td>number</td>
        <td>Yes</td>
        <td>The amount to be settled/captured</td>
    </tr>
      <tr>
        <td><code>authorizationId</code></td>
        <td>number</td>
        <td>Yes</td>
        <td>The authorization identifier for this payment</td>
    </tr>
      <tr>
        <td><code>tid</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Provider's unique identifier for the transaction</td>
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
        <td><code>settleId</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Provider's settlement identifier (if the operation has failed you <strong>MUST</strong> return <code>null</code>)</td>
    </tr>
    <tr>
        <td><code>value</code></td>
        <td>decimal</td>
        <td>Yes</td>
        <td>The amount that was settled/captured (if the operation has failed you <strong>MUST</strong> return <code>0</code>)</td>
    </tr>
    <tr>
        <td><code>code</code></td>
        <td>string</td>
        <td></td>
        <td>Provider's operation/error code to be logged</td>
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
      "code": "curl --location --request POST 'https://{{providerApiEndpoint}}/payments/{{paymentId}}/refunds' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'Content-Type: application/json' \\\n--header 'Accept: application/json' \\\n--data-raw '{\n    \"requestId\": \"2020-06-22T21:50:11-250\",\n    \"settleId\": \"67CD012142\",\n    \"paymentId\": \"2DEF94F658644860ACA807E121E18C98\",\n    \"tid\": \"TID-2803DE74DA\",\n    \"value\": 2.50,\n    \"transactionId\": \"12B0AB6E8843411FB69E34EFCCA12A91\",\n    \"recipients\": [\n        {\n            \"id\": \"mymarketplace\",\n            \"name\": \"My Marketplace QA\",\n            \"documentType\": \"CNPJ\",\n            \"document\": \"99999999999999\",\n            \"role\": \"marketplace\",\n            \"amount\": 1.70\n        },\n        {\n            \"id\": \"mystore\",\n            \"name\": \"My Store QA\",\n            \"documentType\": \"CNPJ\",\n            \"document\": \"99999999999990\",\n            \"role\": \"seller\",\n            \"amount\": 0.8\n        }\n    ]\n}'",
      "language": "curl",
      "name": "Success"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n    \"paymentId\": \"2DEF94F658644860ACA807E121E18C98\",\n    \"refundId\": \"C4D23547BDB9427B971D01CD969ECBA3\",\n    \"value\": 2.50,\n    \"code\": null,\n    \"message\": null,\n    \"requestId\": \"2020-06-22T21:50:11-250\"\n}",
      "language": "curl",
      "name": "200 - OK"
    },
    {
      "code": "{\n    \"paymentId\": \"2DEF94F658644860ACA807E121E18C98\",\n    \"refundId\": null,\n    \"value\": 0.0,\n    \"code\": \"refund-manually\",\n    \"message\": \"Refund should be done manually\",\n    \"requestId\": \"2020-06-22T21:50:11-250\"\n}",
      "language": "curl",
      "name": "200 - Error"
    }
  ]
}
[/block]