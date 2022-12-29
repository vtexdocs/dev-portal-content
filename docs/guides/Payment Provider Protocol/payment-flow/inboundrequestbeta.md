---
title: "Inbound Request (BETA)"
slug: "inboundrequestbeta"
excerpt: "Forwards a request back to your endpoint using the inboundRequestsUrl provided in the POST /payments payload."
hidden: false
createdAt: "2019-12-30T03:21:07.203Z"
updatedAt: "2020-09-29T21:25:30.646Z"
---
The `:action` part of the path will be the same you have used to call the `inboundRequestsUrl`.

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
        <td><code>paymentId</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>VTEX payment ID from this payment</td>
    </tr>
    <tr>
        <td><code>authorizationId</code></td>
        <td>string</td>
        <td></td>
        <td>Provider's unique identifier for the authorization</td>
    </tr>
    <tr>
        <td><code>tid</code></td>
        <td>string</td>
        <td></td>
        <td>Provider's unique identifier for the transaction</td>
    </tr>
    <tr>
        <td><code>requestData</code></td>
        <td>object</td>
        <td>Yes</td>
        <td></td>
    </tr>
    <tr>
        <td>&#x21B3; <code>body</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>The original request body (when sending a JSON, it's gonna be a serialized version of it)</td>
    </tr>
    <tr>
        <td><code>requestId</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>The unique identifier for this request to ensure its idempotency</td>
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
        <td><code>responseData</code></td>
        <td>object</td>
        <td>Yes</td>
        <td></td>
    </tr>
    <tr>
        <td>&#x21B3; <code>statusCode</code></td>
        <td>int</td>
        <td>Yes</td>
        <td>Your desired status code</td>
    </tr>
    <tr>
        <td>&#x21B3; <code>contentType</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Your desired content-type</td>
    </tr>
    <tr>
        <td>&#x21B3; <code>content</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Your desired content body</td>
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
      "code": "curl --location --request POST 'https://{{providerApiEndpoint}}/payments/{{paymentId}}/refunds' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'Content-Type: application/json' \\\n--header 'Accept: application/json' \\\n--data-raw '{\n    \"requestId\": \"LA4E20D3B4E07B7E871F5B5BC9F91\",\n    \"transactionId\": \"D3AA1FC8372E430E8236649DB5EBD08E\",\n    \"paymentId\": \"F5C1A4E20D3B4E07B7E871F5B5BC9F91\",\n    \"authorizationId\": \"{{authorizationId}}\",\n    \"tid\": \"{{tid}}\",\n    \"requestData\": {\n        \"body\": \"{{originalRequestBody}}\"\n    }\n}'",
      "language": "curl",
      "name": "Success "
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"requestId\": \"LA4E20D3B4E07B7E871F5B5BC9F91\",\n  \"paymentId\": \"F5C1A4E20D3B4E07B7E871F5B5BC9F91\",\n  \"responseData\": {\n    \"statusCode\": 200,\n    \"contentType\": \"application/json\",\n    \"content\": \"{\\\"myAttribute\\\":\\\"anyValue\\\"}\"\n  }\n}",
      "language": "curl",
      "name": "200 - OK"
    }
  ]
}
[/block]