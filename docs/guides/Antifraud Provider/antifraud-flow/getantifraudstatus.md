---
title: "Get Antifraud Status"
slug: "getantifraudstatus"
excerpt: "GET antifraud Status. Implement this API because VTEX will call it to get the status of the antifraud analysis."
hidden: false
createdAt: "2020-05-13T21:52:02.370Z"
updatedAt: "2020-05-18T23:03:49.227Z"
---
GET antifraud Status. Implement this API because VTEX will call it to get the status of the antifraud analysis. This call is performed every two hours up to 5 days. After 5 days in undefined status the order will expire and will be cancelled.

The parameter in the URL `transactions.id` is VTEX transaction ID that was passed in the body  of send antifraud data api : `id`

#### RESPONSE BODY
---

<table>
    <tr>
        <td><code>id</code></td>
        <td><strong>string</strong></td>
        <td>VTEX transaction ID. The ID of this transaction must be in the response.</td>
    </tr>
        <tr>
        <td><code>tid</code></td>
        <td><strong>string</strong></td>
     <td>Provider transaction ID. The ID of this transaction must be in the response. The antifraud provider MUST generates an unique transaction Id.</td>
    </tr>
    <tr>
        <td><code>status</code></td>
        <td><strong>string</strong></td>
        <td>Transaction status from provider. Must be one of the values: <i>approved</i>, <i>denied</i> or <i>undefined</i></td>
    </tr>
    <tr>
        <td><code>score</code></td>
        <td><strong>decimal</strong></td>
        <td>The value of the score risk in percentage. 100.00 as max value means total fraud</td>
    </tr>
    <tr>
        <td><code>AnalysisType</code></td>
        <td><strong>string</strong></td>
        <td>Analysis type. Valid values are <strong>authomatic</strong> or <strong>manual</strong></td>
    </tr>
    <tr>
        <td><code>responses</code>&nbsp;(optional)</td>
        <td><strong>dictionary or string</strong></td>
        <td>Key Value dictionary to add custom responses from  analysis</td>
    </tr>
    <tr>
        <td><code>tid</code></td>
        <td><strong>string</strong></td>
        <td>Transaction ID in the provider. This is the transaction identifier that the provider assigns</td>
    </tr>
    <tr>
        <td><code>code</code>&nbsp;(optional)</td>
        <td><strong>string</strong></td>
        <td>Error code returned from provider. <strong>Will be logged in transaction interactions log</strong></td>
    </tr>
    <tr>
        <td><code>message</code>&nbsp;(optional)</td>
        <td><strong>string</strong></td>
        <td>Error message returned from provider. <strong>Will be logged in transaction interactions log</strong></td>
    </tr>
</table>



#### REQUEST EXAMPLES AND THEIR RESPONSES
---
[block:code]
{
  "codes": [
    {
      "code": "curl --location --request GET '{{protocol}}://{{accountName}}.{{domain}}/api/pub/antifraud-provider/transactions/{{transactionId}}' \\\n--header 'Content-Type: application/json' \\\n--header 'X-PROVIDER-API-AppKey: ProviderAppKey' \\\n--header 'X-PROVIDER-API-AppToken: ProviderAppToken' \\\n--data-raw '{\n  \"reference\": \"v32478982vtx-01\",\n  \"transactionId\": \"D3AA1FC8372E430E8236649DB5EBD08E\",\n  \"paymentId\": \"F5C1A4E20D3B4E07B7E871F5B5BC9F91\",\n  \"paymentMethod\": \"Visa\",\n  \"merchantName\":  \"mystore\",\n  \"card\": {\n    \"number\": \"507860187000012798\",\n    \"holder\": \"John Doe\",\n    \"expiration\": {\n      \"month\": \"06\",\n      \"year\": \"2025\"\n    },\n    \"csc\": \"021\"\n  },\n  \"value\": 32,\n  \"installments\": 3,\n  \"deviceFingerprint\": \"12ade389087fe\",\n  \"miniCart\": {\n    \"buyer\": {\n      \"id\": \"c1245228-1c68-11e6-94ac-0afa86a846a5\",\n      \"firstName\": \"John\",\n      \"lastName\": \"Doe\",\n      \"document\": \"012.345.678-90\",\n      \"documentType\": \"CPF\",\n      \"email\": \"john@doe.com\",\n      \"phone\": \"+55 (21) 98765-4321\"\n    },\n    \"shippingAddress\": {\n      \"country\": \"BRA\",\n      \"street\": \"Rua Praia de Botafogo\",\n      \"number\": \"518\",\n      \"complement\": \"2o. andar\",\n      \"neighborhood\": \"Botafogo\",\n      \"postalCode\": \"22250-040\",\n      \"city\": \"Rio de Janeiro\",\n      \"state\": \"RJ\"\n    },\n    \"billingAddress\": {\n      \"country\": \"BRA\",\n      \"street\": \"Rua Praia de Botafogo\",\n      \"number\": \"518\",\n      \"complement\": \"2o. andar\",\n      \"neighborhood\": \"Botafogo\",\n      \"postalCode\": \"22250-040\",\n      \"city\": \"Rio de Janeiro\",\n      \"state\": \"RJ\"\n    },\n    \"items\": [\n      {\n        \"id\": \"132981\",\n        \"name\": \"Some useful product\",\n        \"price\": 2134.90,\n        \"quantity\": 2,\n        \"discount\": 5.00\n      },\n      {\n        \"id\": \"123242\",\n        \"name\": \"Some useless product\",\n        \"price\": 21.98,\n        \"quantity\": 1,\n        \"discount\": 1.00\n      }\n    ],\n    \"shippingValue\": 11.44,\n    \"taxValue\": 10.01\n  },\n  \"url\": \"https://mystore.ecommerce.com/orders/direct/link/v32478982\",\n  \"callbackUrl\": \"https://requestb.in/19ee59c1\",\n  \"returnUrl\": \"https://mystore.ecommerce.com/orders/direct/link/v32478982\"\n}'",
      "language": "curl",
      "name": "Get Antifraud Status"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"id\": \"BF900B7CB15147F98D91208989100A05\",\n  \"tid\": \"3146f46162f042f483cd3979ba4e8317\",\n  \"status\": \"approved\",\n  \"fraudRiskPercentage\": 5.01,\n  \"analysisType\": \"authomatic\",\n  \"responses\": {\n    \"foo\": \"anyFoo\",\n    \"custom\": \"customAnyValue\"\n  }\n}",
      "language": "curl",
      "name": "200 - OK"
    }
  ]
}
[/block]