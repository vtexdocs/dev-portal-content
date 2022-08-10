---
title: "Cancel Payment"
slug: "cancelpayment"
excerpt: "Cancels a payment that was not yet approved or settled."
hidden: false
createdAt: "2019-12-30T03:21:07.203Z"
updatedAt: "2022-07-07T14:58:51.313Z"
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
        <td><code>paymentId</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>VTEX payment ID from this payment</td>
    </tr>
    <tr>
        <td><code>requestId</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>The unique identifier for this request to ensure its idempotency</td>
    </tr>
     <tr>
        <td><code>authorizationId</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Payment authorization identifier (in case it was authorized previous to the cancellation request)</td>
    </tr>
     <tr>
        <td><code>sandboxMode</code></td>
        <td>string</td>
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
        <td><code>status</code></td>
        <td>string</td>
        <td></td>
        <td><strong>This field is deprecated, please don't send it</strong></td>
    </tr>
      <tr>
        <td><code>message</code></td>
        <td>string</td>
        <td></td>
        <td>Provider's operation/error message to be logged</td>
    </tr>
    <tr>
        <td><code>code</code></td>
        <td>string</td>
        <td></td>
        <td>Provider's operation/error code to be logged (return <code>cancel-manually</code> if you do not support this operation, so we can send a notification to the merchant)</td>
    </tr>
    <tr>
        <td><code>cancellationId</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Provider's cancellation identifier (if the operation has failed you <strong>MUST</strong> return <code>null</code>)</td>
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
      "code": "curl --location --request POST 'https://{{providerBaseUrl}}/payments/{{paymentId}}/cancellations' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'Content-Type: application/json' \\\n--header 'Accept: application/json' \\\n--data-raw '{\n    \"paymentId\": \"B2F246B3CE46469FBDD23039868E95D0\",\n    \"requestId\": \"007B7D9B3BB4440982D8B6BA04126B01\",\n    \"authorizationId\": \"AUT-70D2444272\"\n}'",
      "language": "curl",
      "name": "Success"
    },
    {
      "code": "curl --location --request POST 'https://{{providerApiEndpoint}}/payments/{{paymentId}}/cancellations' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'Content-Type: application/json' \\\n--header 'Accept: application/json' \\\n--data-raw '{\n    \"paymentId\": \"F5C1A4E20D3B4E07B7E871F5B5BC9F91\",\n    \"requestId\": \"D12D9B80972C462980F5067A3A126837\"\n}'",
      "language": "curl",
      "name": "Fail Not Implemented"
    },
    {
      "code": "curl --location --request POST 'https://{providerBaseUrl}/payments/{paymentId}/cancellations' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'Content-Type: application/json' \\\n--header 'Accept: application/json' \\\n--data-raw '{\n    \"paymentId\": \"F5C1A4E20D3B4E07B7E871F5B5BC9F91\",\n    \"requestId\": \"D12D9B80972C462980F5067A3A126837\"\n}'",
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
      "code": "{\n    \"paymentId\": \"B2F246B3CE46469FBDD23039868E95D0\",\n    \"message\": \"Cancellation should be done manually\",\n    \"code\": \"cancel-manually\",\n    \"cancellationId\": null,\n    \"requestId\": \"007B7D9B3BB4440982D8B6BA04126B01\"\n}",
      "language": "curl",
      "name": "200 - Error"
    },
    {
      "code": "{\n    \"paymentId\": \"B2F246B3CE46469FBDD23039868E95D0\",\n    \"message\": null,\n    \"code\": null,\n    \"cancellationId\": \"36153ED9F4FB4F109BE67CD05EE54373\",\n    \"requestId\": \"007B7D9B3BB4440982D8B6BA04126B01\"\n}",
      "language": "curl",
      "name": "200 - OK"
    }
  ]
}
[/block]