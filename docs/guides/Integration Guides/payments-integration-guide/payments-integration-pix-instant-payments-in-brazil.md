---
title: "Pix: Instant Payments in Brazil"
slug: "payments-integration-pix-instant-payments-in-brazil"
hidden: false
createdAt: "2020-10-27T00:35:36.404Z"
updatedAt: "2022-02-03T15:19:06.694Z"
---
[Pix](https://www.bcb.gov.br/estabilidadefinanceira/pix) is the instant payments ecosystem implementation led by the Central Bank of Brazil (BCB) to enable online money transfers with reduced costs, increased safety and 24/7 availability. Transfers occur directly from the payer’s account to the payee’s account, without the need for intermediaries, resulting in lower transaction costs.

Pix will be available for persons and businesses. Both need to have an identifier key registered in some financial entity - banks, fintechs or payment institutions - to proceed with the transaction. According to the [eligibility criteria](https://www.bcb.gov.br/estabilidadefinanceira/participantespix) set forth by the BCB, certain entities will be required to offer this payment method, while others may optionally offer it or not be eligible to participate.

In this step, we’ll explain how to extend your Payment Provider Protocol implementation to allow stores to offer Pix as an additional payment method to their clients.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/bf3c11b-post_BCexplica_pagamentos_instantaneos_ingles_Features.png",
        "post_BCexplica_pagamentos_instantaneos_ingles_Features.png",
        1436,
        938,
        "#eaecea"
      ],
      "caption": "These are some of the benefits of an instant payments ecosystem [highlighted by the BCB](https://www.bcb.gov.br/en/financialstability/instantpayments)"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "success",
  "body": "If you want to know more instant payments in Brazil, we have prepared a [blog post](https://vtex.com/pt-br/blog/produto/pix-no-e-commerce/) with all the implications of this new payment method. You can also check out the [FAQ](https://www.bcb.gov.br/estabilidadefinanceira/perguntaserespostaspix) provided by the BCB for more details.",
  "title": "Pix in e-commerce: everything you need to know"
}
[/block]

[block:callout]
{
  "type": "warning",
  "body": "This tutorial assumes you are already a [VTEX Partner](http://vtex.com/br-pt/partner) and understand how the [Payment Provider Protocol](doc:payment-provider-protocol) works.",
  "title": "Are you ready for a Payment Provider implementation?"
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "On November 3th, the BCB will realize some transactions strictly for tests. \nOn November 16th, Pix will be available for operations working fully.",
  "title": "Expected launch: November 2020"
}
[/block]

## Integration conditions

If you are ready to develop the middleware that implements our Payment Provider Protocol, you should be aware of these requirements:

- **All endpoints must be served over HTTPS on port 443 with TLS 1.2 support.** Connections over non-secured HTTP will not be accepted under any circumstances.

- **The integrator must create a subdomain or a domain name for the provider endpoints.** IP addresses will not be accepted as names under any circumstances.

- **The middleware must consistently respond within established response times.** We enforce a maximum response time of 5 seconds for homologation tests, as well as a maximum response time of 20 seconds to any other API request.

While our protocol describes ten endpoints for implementation, not all of them are applicable when integrating Pix instant payments. Regarding the two provider flows:

- [Payment Flow](https://developers.vtex.com/vtex-rest-api/reference/payment-flow): its implementation is **mandatory**.

- [Configuration Flow](https://developers.vtex.com/vtex-rest-api/reference/configuration-flow): its implementation is **optional and currently not available for Pix**.

The table below gives further detail on the applicability of each endpoint to Pix instant payments. More details on the integration steps are given in the rest of this tutorial.
[block:parameters]
{
  "data": {
    "h-1": "Endpoint",
    "0-1": "List Payment Methods",
    "h-0": "Provider Flow",
    "h-2": "Applicable to Pix?",
    "0-0": "Payment",
    "1-0": "Payment",
    "0-2": ":warning: Obsolete",
    "1-1": "List Payment Provider Manifest",
    "1-2": ":white-check-mark: Yes",
    "2-0": "Payment",
    "2-1": "Create Payment",
    "2-2": ":white-check-mark: Yes",
    "3-0": "Payment",
    "3-1": "Cancel Payment",
    "4-1": "Capture Payment",
    "5-1": "Refund Payment",
    "4-0": "Payment",
    "5-0": "Payment",
    "6-0": "Payment",
    "6-1": "Inbound Request (BETA)",
    "7-1": "Create Authorization Token",
    "8-1": "Provider Authentication",
    "9-1": "Get Credentials",
    "7-0": "Configuration",
    "8-0": "Configuration",
    "9-0": "Configuration",
    "7-2": ":x: No",
    "8-2": ":x: No",
    "9-2": ":x: No",
    "3-2": ":white-check-mark: Yes",
    "4-2": ":white-check-mark: Yes",
    "5-2": ":white-check-mark: Yes",
    "6-2": ":white-check-mark: Yes"
  },
  "cols": 3,
  "rows": 10
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "Pix is <strong>not available</strong> for marketplace clients that use the Checkout Split.",
  "title": "Marketplace restrictions"
}
[/block]

[block:callout]
{
  "type": "danger",
  "body": "We strongly advise against using the <span class=\"api\"><span class=\"pg-type type-get\">GET</span>[List Payment Methods] (<https://developers.vtex.com/vtex-developer-docs/reference/paymentmethods>) to proceed with the implementation. This route is obsolete and it will be deprecated in soon - early 2021",
  "title": "GET List Payment Methods route"
}
[/block]

[block:callout]
{
  "type": "warning",
  "body": "The following JSONs are just <strong>examples</strong>. Each partner <strong>must adapt</strong> the models to their own realities, with the data needed to realize the integration.",
  "title": "Request and response examples"
}
[/block]

## Integration steps

### Establish the payment methods available

The first information your provider has to inform us is which are the payment methods that it handles. To do so, you can make an API call using the <span class="api pg-type type-get">GET</span>[List Payment Provider Manifest](https://developers.vtex.com/vtex-developer-docs/reference/manifest-1) route.

The expected response is:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"paymentMethods\": [\n        {\n            \"name\": \"Visa\",\n            \"allowsSplit\": \"onCapture\"\n        },\n        { \n            \"name\": \"Pix\",\n            \"allowsSplit\": \"disabled\"\n        },\n        {\n            \"name\": \"Mastercard\",\n            \"allowsSplit\": \"onCapture\"\n        },\n        {\n            \"name\": \"American Express\",\n            \"allowsSplit\": \"onCapture\"\n        },\n        {\n            \"name\": \"BankInvoice\",\n            \"allowsSplit\": \"onAuthorize\"\n        },\n        {\n            \"name\": \"Privatelabels\",\n            \"allowsSplit\": \"disabled\"\n        },\n        {\n            \"name\": \"Promissories\",\n            \"allowsSplit\": \"disabled\"\n        }\n    ],\n    \"customFields\": [\n        {\n            \"name\": \"Merchant's custom field\",\n            \"type\": \"text\"\n        },\n        {\n            \"name\": \"Merchant's custom select field\",\n            \"type\": \"select\",\n            \"options\": [\n                {\n                    \"text\": \"Field option 1\",\n                    \"value\": \"1\",\n                },\n                {\n                    \"text\": \"Field option 2\",\n                    \"value\": \"2\",\n                },\n                {\n                    \"text\": \"Field option 3\",\n                    \"value\": \"3\",\n                }\n            ]\n        }\n    ]\n}",
      "language": "curl",
      "name": "200 OK"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "warning",
  "title": "Payment split for Pix",
  "body": "Pix does <strong>not</strong> handle payment split yet, this functionality will be released soon."
}
[/block]
For more details, check the [complete documentation] (<https://developers.vtex.com/vtex-developer-docs/reference/manifest-1>).

### Create Pix Payment Method

Now you have to create a new payment method and there’s only one route as an option: <span class="api pg-type type-post">POST</span>[Create Payment] (<https://developers.vtex.com/vtex-developer-docs/reference/createpayment>).

There’s a lot of information needed stem from the cart data in the Smart Checkout, so be careful and validate all the payload’s information.

The request goes like this:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"reference\": \"32478982\",\n    \"orderId\": \"v967373115140abc\",\n    \"transactionId\": \"D3AA1FC8372E430E8236649DB5EBD08E\",\n    \"paymentId\": \"F5C1A4E20D3B4E07B7E871F5B5BC9F91\",\n    \"paymentMethod\": \"Pix\",\n    \"paymentMethodCustomCode\": null,\n    \"merchantName\": \"mystore\",\n    \"value\": 4307.23,\n    \"currency\": \"BRL\",\n    \"installments\": 31,\n    \"deviceFingerprint\": \"12ade389087fe\",\n    \"card\": {\n        \"holder\": null,\n        \"number\": null,\n        \"csc\": null,\n        \"expiration\": {\n            \"month\": null,\n            \"year\": null\n        }\n    },\n    \"miniCart\": {\n        \"shippingValue\": 11.44,\n        \"taxValue\": 10.01,\n        \"buyer\": {\n            \"id\": \"c1245228-1c68-11e6-94ac-0afa86a846a5\",\n            \"firstName\": \"John\",\n            \"lastName\": \"Doe\",\n            \"document\": \"01234567890\",\n            \"documentType\": \"CPF\",\n            \"email\": \"john.doe@example.com\",\n            \"phone\": \"+5521987654321\"\n        },\n        \"shippingAddress\": {\n            \"country\": \"BRA\",\n            \"street\": \"Praia de Botafogo St.\",\n            \"number\": \"300\",\n            \"complement\": \"3rd Floor\",\n            \"neighborhood\": \"Botafogo\",\n            \"postalCode\": \"22250040\",\n            \"city\": \"Rio de Janeiro\",\n            \"state\": \"RJ\"\n        },\n        \"billingAddress\": {\n            \"country\": \"BRA\",\n            \"street\": \"Brigadeiro Faria Lima Avenue\",\n            \"number\": \"4440\",\n            \"complement\": \"10th Floor\",\n            \"neighborhood\": \"Itaim Bibi\",\n            \"postalCode\": \"04538132\",\n            \"city\": \"São Paulo\",\n            \"state\": \"SP\"\n        },\n        \"items\": [\n            {\n                \"id\": \"132981\",\n                \"name\": \"My First Product\",\n                \"price\": 2134.90,\n                \"quantity\": 2,\n                \"discount\": 5.00\n            },\n            {\n                \"id\": \"123242\",\n                \"name\": \"My Second Product\",\n                \"price\": 21.98,\n                \"quantity\": 1,\n                \"discount\": 1.00\n            }\n        ]\n    },\n    \"url\": \"https://admin.mystore.example.com/orders/v32478982\",\n    \"callbackUrl\": \"https://api.example.com/some-path/to-notify/status-changes?an=mystore\",\n    \"returnUrl\": \"https://mystore.example.com/checkout/order/v32478982\"\n}'",
      "language": "curl",
      "name": "Pix Success Approved"
    }
  ]
}
[/block]
As a result, we expect the following response:
[block:callout]
{
  "type": "danger",
  "body": "Have in mind that, by default, the QRCode <strong>must</strong> have five minutes (300 seconds) expiration time. Also, the partner <strong>must</strong> respect the callback time (20 seconds).",
  "title": "Establish an organized flow"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"paymentId\": \"F5C1A4E20D3B4E07B7E871F5B5BC9F91\",\n  \"status\": \"undefined\",\n  \"tid\": \"TID1578324421\",\n  \"authorizationId\": null,\n  \"nsu\": null,\n  \"code\": \"APP123\",\n  \"paymentAppData\": {\n    \"payload\": \"{\\\"code\\\":\\\"https://bacen.pix/pix/code\\\",\\\"qrCodeBase64Image\\\":\\\"iVBORw0KGgoAAAANSUhEUgAAAAIAAAACCAYAAABytg0kAAABQGlDQ1BJQ0MgUHJvZmlsZQAAKJFjYGDiSSwoyGFhYGDIzSspCnJ3UoiIjFJgf8LAxSDMwMkgwiCZmFxc4BgQ4ANUwgCjUcG3awyMIPqyLsgspwWXFu+Xeyundb6w0WL33C5M9SiAKyW1OBlI/wHihOSCohIGBsYYIFu5vKQAxG4AskWKgI4CsqeA2OkQ9goQOwnC3gNWExLkDGRfALIFkjMSU4DsB0C2ThKSeDoSG2ovCLAZGZkbhBNwKKmgJLWiBEQ75xdUFmWmZ5QoOAJDJ1XBMy9ZT0fByMDIgIEBFNYQ1Z9vgMOQUYwDIZapzMBgmQEUfIQQSxNmYNiZzsDAU4UQU5/PwMBrxMBw5GJBYlEi3AGM31iK04yNIGzu7QwMrNP+//8M9Ca7JgPD3+v////e/v//32UMDMy3GBgOfAMA4+RdqZ9YRkcAAABWZVhJZk1NACoAAAAIAAGHaQAEAAAAAQAAABoAAAAAAAOShgAHAAAAEgAAAESgAgAEAAAAAQAAAAKgAwAEAAAAAQAAAAIAAAAAQVNDSUkAAABTY3JlZW5zaG900Fpo3gAAAdJpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IlhNUCBDb3JlIDUuNC4wIj4KICAgPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4KICAgICAgPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIKICAgICAgICAgICAgeG1sbnM6ZXhpZj0iaHR0cDovL25zLmFkb2JlLmNvbS9leGlmLzEuMC8iPgogICAgICAgICA8ZXhpZjpQaXhlbFhEaW1lbnNpb24+MjwvZXhpZjpQaXhlbFhEaW1lbnNpb24+CiAgICAgICAgIDxleGlmOlVzZXJDb21tZW50PlNjcmVlbnNob3Q8L2V4aWY6VXNlckNvbW1lbnQ+CiAgICAgICAgIDxleGlmOlBpeGVsWURpbWVuc2lvbj4yPC9leGlmOlBpeGVsWURpbWVuc2lvbj4KICAgICAgPC9yZGY6RGVzY3JpcHRpb24+CiAgIDwvcmRmOlJERj4KPC94OnhtcG1ldGE+Cl89Cn4AAAASSURBVAgdY/wPBAxAwAQiQAAAPfgEAIAu9DkAAAAASUVORK5CYII=\\\"}\"\n  },\n  \"message\": \"The customer needs to finish the payment flow\",\n  \"delayToAutoSettle\": 1209600,\n  \"delayToAutoSettleAfterAntifraud\": 120,\n  \"delayToCancel\": 300\n}",
      "language": "curl",
      "name": "200 OK"
    }
  ]
}
[/block]
The complete documentation is [here] (<https://developers.vtex.com/vtex-developer-docs/reference/createpayment>).

### Cancel a Payment

To cancel a payment, you must already have created one. To do so, you’ll make an API call using the route <span class="api pg-type type-post">POST</span>[Cancel Payment] (<https://developers.vtex.com/vtex-developer-docs/reference/cancelpayment>):
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"paymentId\": \"F5C1A4E20D3B4E07B7E871F5B5BC9F91\",\n    \"requestId\": \"1234\"\n}",
      "language": "curl",
      "name": "Success"
    }
  ]
}
[/block]
After the provider realizes the payment cancelation, we expect is a response like this:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"paymentId\": \"F5C1A4E20D3B4E07B7E871F5B5BC9F91\",\n    \"message\": \"Successfully cancelled\",\n    \"code\": null,\n    \"cancellationId\": \"1457BD07E6\",\n    \"requestId\": \"1234\"\n}",
      "language": "curl",
      "name": "200 OK"
    }
  ]
}
[/block]
See the [complete documentation] (<https://developers.vtex.com/vtex-developer-docs/reference/cancelpayment>) for more details.

### Capture Payment

If your transaction was completed successfully, the provider can capture the payment.  

So, to capture payment, VTEX will send the information below through the <span class="api pg-type type-post">POST</span>[Capture Payment route] (<https://developers.vtex.com/vtex-developer-docs/reference/capturepayment>):
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"paymentId\": \"5B127F1E0C944EF9ACE264FEC1FC0E91\",\n    \"transactionId\": \"611966\",\n    \"value\": 20.0,\n    \"requestId\": \"5678\"\n}",
      "language": "curl",
      "name": "Success"
    }
  ]
}
[/block]
The response should be similar to the following response body:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"paymentId\": \"5B127F1E0C944EF9ACE264FEC1FC0E91\",\n    \"settleId\": \"CEE16492C6\",\n    \"value\": 20.0,\n    \"code\": null,\n    \"message\": null,\n    \"requestId\": \"5678\"\n}",
      "language": "curl",
      "name": "200 OK"
    }
  ]
}
[/block]
You can check more details in the [endpoint’s documentation] (<https://developers.vtex.com/vtex-developer-docs/reference/capturepayment>).

### Refund Payment

The provider should be ready to receive the following request through the <span class="api pg-type type-post">POST</span>[Refund Payment route](https://developers.vtex.com/vtex-developer-docs/reference/refundpayment):
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"paymentId\": \"VQKIIBUVOFDBIDLKZPOWSKETDYWCMJSACDVXWFCJVSKXGYVBBVISZRJLLQEKERJEMDYEINOUMFAZZGNEDVBQBABLUKLFBSEEIGLCAQTOGOGURKLFCAHJQTDMBNKYBIST\",\n    \"transactionId\": \"611966\",\n    \"settleId\": \"31018A3281\",\n    \"value\": 10.0,\n    \"requestId\": \"5678\"\n}",
      "language": "curl",
      "name": "Success"
    }
  ]
}
[/block]
The expected response is:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"paymentId\": \"VQKIIBUVOFDBIDLKZPOWSKETDYWCMJSACDVXWFCJVSKXGYVBBVISZRJLLQEKERJEMDYEINOUMFAZZGNEDVBQBABLUKLFBSEEIGLCAQTOGOGURKLFCAHJQTDMBNKYBIST\",\n    \"refundId\": null,\n    \"value\": 0.0,\n    \"code\": \"refund-manually\",\n    \"message\": \"Refund should be done manually\",\n    \"requestId\": \"5678\"\n}",
      "language": "curl",
      "name": "200 OK"
    }
  ]
}
[/block]
Go to the [route’s documentation] (<https://developers.vtex.com/vtex-developer-docs/reference/refundpayment>) to check all the details.

### Communicate with the Gateway

The last route - <span class="api pg-type type-post">POST</span>[Inbound Request (BETA)] (<https://developers.vtex.com/vtex-developer-docs/reference/inboundrequestbeta>) -  implements an URL that facilitates a direct connection between our Gateway service and the Payment Provider.

The request will be:
[block:code]
{
  "codes": [
    {
      "code": "'{\n    \"requestId\": \"LA4E20D3B4E07B7E871F5B5BC9F91\",\n    \"transactionId\": \"D3AA1FC8372E430E8236649DB5EBD08E\",\n    \"paymentId\": \"F5C1A4E20D3B4E07B7E871F5B5BC9F91\",\n    \"authorizationId\": \"{{authorizationId}}\",\n    \"tid\": \"{{tid}}\",\n    \"requestData\": {\n        \"body\": \"{{originalRequestBody}}\"\n    }\n}'",
      "language": "curl",
      "name": "Success"
    }
  ]
}
[/block]
As a result, the client should send the following response:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"requestId\": \"{{requestId}}\",\n    \"transactionId\": \"{{transactionId}}\",\n    \"paymentId\": \"{{paymentId}}\",\n    \"authorizationId\": \"{{authorizationId}}\",\n    \"tid\": \"{{tid}}\",\n    \"requestData\": {\n        \"body\": \"{{originalRequestBody}}\"\n    }\n}",
      "language": "curl",
      "name": "200 OK"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "The Inbound Request (BETA) is mandatory only for integrations via Payment Provider Protocol with an external Payment App. If the Pix payment method was implemented via VTEX Payment App, the Inbound Request is not necessary.",
  "title": "Not required for Payment App"
}
[/block]
Check the complete endpoint documentation [here] (<https://developers.vtex.com/vtex-developer-docs/reference/inboundrequestbeta>).

For more information and frequently asked questions, refer to [Pix - FAQ](https://help.vtex.com/pt/tutorial/pix-faq--3lx7zCU2lQroTEBCYKYbo3).

## Wrapping up

If you have completed all integration steps, you should have a working implementation of our Payment Provider Protocol with Pix instant payments. The last step before VTEX stores can use your provider is to complete our homologation process.
