---
title: "Stop Antifraud Analysis (optional)"
slug: "stopantifraudanalysisoptional"
excerpt: "Stop antifraud analysis."
hidden: false
createdAt: "2020-05-13T21:52:02.370Z"
updatedAt: "2020-06-01T17:35:00.035Z"
---
Implement this API if you want to be notified if the order was canceled either by the store or the buyer before complete the Antifraud analysis.

The parameter in the URL <code>transactions.id</code> is VTEX transaction ID that was passed in the body of send antifraud data api : <code>id</code>



#### REQUEST EXAMPLES AND THEIR RESPONSES
---
[block:code]
{
  "codes": [
    {
      "code": "curl --location --request GET '{{protocol}}://{{accountName}}.{{domain}}/api/pub/antifraud-provider/payment-methods' \\\n--header 'Content-Type: application/json' \\\n--data-raw '{\n  \"reference\": \"v32478982vtx-01\",\n  \"transactionId\": \"D3AA1FC8372E430E8236649DB5EBD08E\",\n  \"paymentId\": \"F5C1A4E20D3B4E07B7E871F5B5BC9F91\",\n  \"paymentMethod\": \"Visa\",\n  \"merchantName\":  \"mystore\",\n  \"card\": {\n    \"number\": \"507860187000012798\",\n    \"holder\": \"John Doe\",\n    \"expiration\": {\n      \"month\": \"06\",\n      \"year\": \"2025\"\n    },\n    \"csc\": \"021\"\n  },\n  \"value\": 32,\n  \"installments\": 3,\n  \"deviceFingerprint\": \"12ade389087fe\",\n  \"miniCart\": {\n    \"buyer\": {\n      \"id\": \"c1245228-1c68-11e6-94ac-0afa86a846a5\",\n      \"firstName\": \"John\",\n      \"lastName\": \"Doe\",\n      \"document\": \"012.345.678-90\",\n      \"documentType\": \"CPF\",\n      \"email\": \"john@doe.com\",\n      \"phone\": \"+55 (21) 98765-4321\"\n    },\n    \"shippingAddress\": {\n      \"country\": \"BRA\",\n      \"street\": \"Rua Praia de Botafogo\",\n      \"number\": \"518\",\n      \"complement\": \"2o. andar\",\n      \"neighborhood\": \"Botafogo\",\n      \"postalCode\": \"22250-040\",\n      \"city\": \"Rio de Janeiro\",\n      \"state\": \"RJ\"\n    },\n    \"billingAddress\": {\n      \"country\": \"BRA\",\n      \"street\": \"Rua Praia de Botafogo\",\n      \"number\": \"518\",\n      \"complement\": \"2o. andar\",\n      \"neighborhood\": \"Botafogo\",\n      \"postalCode\": \"22250-040\",\n      \"city\": \"Rio de Janeiro\",\n      \"state\": \"RJ\"\n    },\n    \"items\": [\n      {\n        \"id\": \"132981\",\n        \"name\": \"Some useful product\",\n        \"price\": 2134.90,\n        \"quantity\": 2,\n        \"discount\": 5.00\n      },\n      {\n        \"id\": \"123242\",\n        \"name\": \"Some useless product\",\n        \"price\": 21.98,\n        \"quantity\": 1,\n        \"discount\": 1.00\n      }\n    ],\n    \"shippingValue\": 11.44,\n    \"taxValue\": 10.01\n  },\n  \"url\": \"https://mystore.ecommerce.com/orders/direct/link/v32478982\",\n  \"callbackUrl\": \"https://requestb.in/19ee59c1\",\n  \"returnUrl\": \"https://mystore.ecommerce.com/orders/direct/link/v32478982\"\n}'",
      "language": "curl",
      "name": "Get Payment Methods Supported"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "[\n  {\n    \"name\": \"CreditCard\"\n  },\n  {\n    \"name\": \"DebitCard\"\n  },\n  {\n    \"name\": \"GiftCard\"\n  },\n  {\n    \"name\": \"BankIssueInvoice\"\n  },\n  {\n    \"name\": \"Voucher\"\n  },\n  {\n    \"name\": \"Promissory\"\n  }\n]",
      "language": "text",
      "name": "200 - OK"
    }
  ]
}
[/block]