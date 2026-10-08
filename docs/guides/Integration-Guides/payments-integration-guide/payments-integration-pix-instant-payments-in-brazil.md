---
title: "Pix: Instant payment in Brazil"
slug: "payments-integration-pix-instant-payments-in-brazil"
excerpt: "Learn how to extend your Payment Provider Protocol implementation so VTEX stores can offer Pix instant payments in Brazil."
hidden: false
createdAt: "2020-10-27T00:35:36.404Z"
updatedAt: "2026-08-04T00:00:00.000Z"
---
[Pix](https://www.bcb.gov.br/estabilidadefinanceira/pix) is the instant payments ecosystem implemented by the Central Bank of Brazil (BCB) to enable online money transfers with lower costs, greater security, and 24/7 availability. Transfers occur directly from the payer’s account to the payee’s account, eliminating intermediaries and reducing transaction costs.

Pix is available to both individuals and legal entities, and both need to have a Pix key registered with a financial institution, such as a bank, fintech, or payment institution, to complete a transaction.

According to the [eligibility criteria](https://www.bcb.gov.br/estabilidadefinanceira/participantespix) set forth by the BCB, certain financial entities will be required to offer this payment method, while others may offer it voluntarily or may not be eligible to participate.

This guide explains how to extend your Payment Provider Protocol implementation so stores can offer Pix as an additional payment method to their customers.

![These are some of the benefits of an instant payments ecosystem highlighted by the BCB](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/payments-integration-pix-instant-payments-in-brazil-0.png)

> ℹ️ For more information about instant payments in Brazil, see the [FAQ](https://www.bcb.gov.br/estabilidadefinanceira/perguntaserespostaspix) provided by the BCB.

> ⚠️ This guide assumes that you are already a [VTEX partner](https://www.vtex.com/en-us/partners/) and that you understand how the [Payment Provider Protocol](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-protocol) works.

## Integration conditions

Before developing the middleware that implements the Payment Provider Protocol, review the following requirements:

- **All endpoints must be served over HTTPS on port 443 with TLS 1.2 support**: Connections over non-secured HTTP won't be accepted under any circumstances.
- **The integrator must create a subdomain or a domain name for the provider endpoints**: IP addresses won't be accepted as names under any circumstances.
- **The middleware must consistently respond within the established response times**: VTEX enforces a maximum response time of 5 seconds for homologation tests and 20 seconds for any other API request.

The Payment Provider Protocol describes nine endpoints, but not all of them apply to Pix. These endpoints are divided into two provider flows:

- [Payment flow](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#get-/manifest): six endpoints, all required for Pix.
- [Configuration flow](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/authorization/token): three optional endpoints, currently not available for Pix.

The following table details the applicability of each endpoint to Pix:

| Provider Flow | Endpoint                       | Applicable to Pix? |
| ------------- | ------------------------------ | ------------------ |
| Payment       | List Payment Provider Manifest | ✅ Yes             |
| Payment       | Create Payment                 | ✅ Yes             |
| Payment       | Cancel Payment                 | ✅ Yes             |
| Payment       | Capture Payment                | ✅ Yes             |
| Payment       | Refund Payment                 | ✅ Yes             |
| Payment       | Inbound Request (BETA)         | ✅ Yes             |
| Payment       | Create Authorization Token     | ⛔ No              |
| Payment       | Provider Authentication        | ⛔ No              |
| Payment       | Get Credentials                | ⛔ No              |

> ⚠️ Pix isn't available for marketplaces that use Checkout Split.

> ⚠️ The following JSON examples are illustrative. Adapt them to your own scenario, including the data required for your integration.

## Integration steps

### Establish the payment methods available

First, your provider must declare which payment methods it handles. To do so, implement the `GET` [List Payment Provider Manifest](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#get-/manifest) endpoint.

The expected response is:

```json
{
    "paymentMethods": [
        {
            "name": "Visa",
            "allowsSplit": "onCapture"
        },
        {
            "name": "Pix",
            "allowsSplit": "disabled"
        },
        {
            "name": "Mastercard",
            "allowsSplit": "onCapture"
        },
        {
            "name": "American Express",
            "allowsSplit": "onCapture"
        },
        {
            "name": "BankInvoice",
            "allowsSplit": "onAuthorize"
        },
        {
            "name": "Privatelabels",
            "allowsSplit": "disabled"
        },
        {
            "name": "Promissories",
            "allowsSplit": "disabled"
        }
    ],
    "customFields": [
        {
            "name": "Merchant's custom field",
            "type": "text"
        },
        {
            "name": "Merchant's custom select field",
            "type": "select",
            "options": [
                {
                    "text": "Field option 1",
                    "value": "1",
                },
                {
                    "text": "Field option 2",
                    "value": "2",
                },
                {
                    "text": "Field option 3",
                    "value": "3",
                }
            ]
        }
    ]
}
```

> ⚠️ Pix doesn't support payment split. For the payment methods that currently support split, see the [List Payment Provider Manifest](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#get-/manifest) endpoint reference.

### Create a Pix payment

To create a Pix payment, implement the `POST` [Create Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments).

> ℹ️ The request includes extensive cart data from Smart Checkout. Validate all payload fields before processing the payment.

See an example of the Create Payment request:

```json
{
    "reference": "32478982",
    "orderId": "v967373115140abc",
    "transactionId": "D3AA1FC8372E430E8236649DB5EBD08E",
    "paymentId": "F5C1A4E20D3B4E07B7E871F5B5BC9F91",
    "paymentMethod": "Pix",
    "paymentMethodCustomCode": null,
    "merchantName": "mystore",
    "value": 4307.23,
    "currency": "BRL",
    "installments": 31,
    "deviceFingerprint": "12ade389087fe",
    "card": {
        "holder": null,
        "number": null,
        "csc": null,
        "expiration": {
            "month": null,
            "year": null
        }
    },
    "miniCart": {
        "shippingValue": 11.44,
        "taxValue": 10.01,
        "buyer": {
            "id": "c1245228-1c68-11e6-94ac-0afa86a846a5",
            "firstName": "John",
            "lastName": "Doe",
            "document": "01234567890",
            "documentType": "CPF",
            "email": "john.doe@example.com",
            "phone": "+5521987654321"
        },
        "shippingAddress": {
            "country": "BRA",
            "street": "Praia de Botafogo St.",
            "number": "300",
            "complement": "3rd Floor",
            "neighborhood": "Botafogo",
            "postalCode": "22250040",
            "city": "Rio de Janeiro",
            "state": "RJ"
        },
        "billingAddress": {
            "country": "BRA",
            "street": "Brigadeiro Faria Lima Avenue",
            "number": "4440",
            "complement": "10th Floor",
            "neighborhood": "Itaim Bibi",
            "postalCode": "04538132",
            "city": "São Paulo",
            "state": "SP"
        },
        "items": [
            {
                "id": "132981",
                "name": "My First Product",
                "price": 2134.90,
                "quantity": 2,
                "discount": 5.00
            },
            {
                "id": "123242",
                "name": "My Second Product",
                "price": 21.98,
                "quantity": 1,
                "discount": 1.00
            }
        ]
    },
    "url": "https://admin.mystore.example.com/orders/v32478982",
    "callbackUrl": "https://api.example.com/some-path/to-notify/status-changes?an=mystore",
    "returnUrl": "https://mystore.example.com/checkout/order/v32478982"
}
```

The expected response is:

```json
{
  "paymentId": "F5C1A4E20D3B4E07B7E871F5B5BC9F91",
  "status": "undefined",
  "tid": "TID1578324421",
  "authorizationId": null,
  "nsu": null,
  "code": "APP123",
  "paymentAppData": {
    "payload": "{\"code\":\"https://bacen.pix/pix/code\",\"qrCodeBase64Image\":\"iVBORw0KGgoAAAANSUhEUgAAAAIAAAACCAYAAABytg0kAAABQGlDQ1BJQ0MgUHJvZmlsZQAAKJFjYGDiSSwoyGFhYGDIzSspCnJ3UoiIjFJgf8LAxSDMwMkgwiCZmFxc4BgQ4ANUwgCjUcG3awyMIPqyLsgspwWXFu+Xeyundb6w0WL33C5M9SiAKyW1OBlI/wHihOSCohIGBsYYIFu5vKQAxG4AskWKgI4CsqeA2OkQ9goQOwnC3gNWExLkDGRfALIFkjMSU4DsB0C2ThKSeDoSG2ovCLAZGZkbhBNwKKmgJLWiBEQ75xdUFmWmZ5QoOAJDJ1XBMy9ZT0fByMDIgIEBFNYQ1Z9vgMOQUYwDIZapzMBgmQEUfIQQSxNmYNiZzsDAU4UQU5/PwMBrxMBw5GJBYlEi3AGM31iK04yNIGzu7QwMrNP+//8M9Ca7JgPD3+v////e/v//32UMDMy3GBgOfAMA4+RdqZ9YRkcAAABWZVhJZk1NACoAAAAIAAGHaQAEAAAAAQAAABoAAAAAAAOShgAHAAAAEgAAAESgAgAEAAAAAQAAAAKgAwAEAAAAAQAAAAIAAAAAQVNDSUkAAABTY3JlZW5zaG900Fpo3gAAAdJpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IlhNUCBDb3JlIDUuNC4wIj4KICAgPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4KICAgICAgPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIKICAgICAgICAgICAgeG1sbnM6ZXhpZj0iaHR0cDovL25zLmFkb2JlLmNvbS9leGlmLzEuMC8iPgogICAgICAgICA8ZXhpZjpQaXhlbFhEaW1lbnNpb24+MjwvZXhpZjpQaXhlbFhEaW1lbnNpb24+CiAgICAgICAgIDxleGlmOlVzZXJDb21tZW50PlNjcmVlbnNob3Q8L2V4aWY6VXNlckNvbW1lbnQ+CiAgICAgICAgIDxleGlmOlBpeGVsWURpbWVuc2lvbj4yPC9leGlmOlBpeGVsWURpbWVuc2lvbj4KICAgICAgPC9yZGY6RGVzY3JpcHRpb24+CiAgIDwvcmRmOlJERj4KPC94OnhtcG1ldGE+Cl89Cn4AAAASSURBVAgdY/wPBAxAwAQiQAAAPfgEAIAu9DkAAAAASUVORK5CYII=\"}"
  },
  "message": "The customer needs to finish the payment flow",
  "delayToAutoSettle": 1209600,
  "delayToAutoSettleAfterAntifraud": 120,
  "delayToCancel": 1800
}
```

> ❗ Set the Pix QR code expiration time between 15 and 60 minutes (900 and 3600 seconds). The provider must also respect the 20-second callback time limit.

For more information, access the [Create Payment endpoint](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments).

### Cancel a payment

To cancel an existing payment, implement the `POST` [Cancel Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/cancellations).

See an example of the Cancel Payment request:

```json
{
    "paymentId": "F5C1A4E20D3B4E07B7E871F5B5BC9F91",
    "requestId": "1234"
}
```

After the provider processes the cancellation, the expected response is:

```json
{
    "paymentId": "F5C1A4E20D3B4E07B7E871F5B5BC9F91",
    "message": "Successfully cancelled",
    "code": null,
    "cancellationId": "1457BD07E6",
    "requestId": "1234"
}
```

For more information, access the [Cancel Payment endpoint](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/cancellations).

### Settle a payment (capture)

After the transaction is successfully completed, the provider can settle the payment.

To settle the payment, VTEX sends the following request to the `POST` [Settle Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/settlements).

See an example of the Settle Payment request:

```json
{
    "paymentId": "5B127F1E0C944EF9ACE264FEC1FC0E91",
    "transactionId": "611966",
    "value": 20.0,
    "requestId": "5678"
}
```

The expected response is:

```json
{
    "paymentId": "5B127F1E0C944EF9ACE264FEC1FC0E91",
    "settleId": "CEE16492C6",
    "value": 20.0,
    "code": null,
    "message": null,
    "requestId": "5678"
}
```

For more information, access the [Settle Payment endpoint](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/settlements).

### Refund a payment

The provider must be ready to receive the following request on the `POST` [Refund Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/refunds) endpoint.

See an example of the Refund Payment request:

```json
{
    "paymentId": "VQKIIBUVOFDBIDLKZPOWSKETDYWCMJSACDVXWFCJVSKXGYVBBVISZRJLLQEKERJEMDYEINOUMFAZZGNEDVBQBABLUKLFBSEEIGLCAQTOGOGURKLFCAHJQTDMBNKYBIST",
    "transactionId": "611966",
    "settleId": "31018A3281",
    "value": 10.0,
    "requestId": "5678"
}
```

The expected response is:

```json
{
    "paymentId": "VQKIIBUVOFDBIDLKZPOWSKETDYWCMJSACDVXWFCJVSKXGYVBBVISZRJLLQEKERJEMDYEINOUMFAZZGNEDVBQBABLUKLFBSEEIGLCAQTOGOGURKLFCAHJQTDMBNKYBIST",
    "refundId": null,
    "value": 0.0,
    "code": "refund-manually",
    "message": "Refund should be done manually",
    "requestId": "5678"
}
```

> ℹ️ This example response indicates that the provider can't process the refund automatically: `refundId` is `null`, `value` is `0.0`, and `code` is `refund-manually`. In this case, the merchant must complete the refund outside the platform. If your provider supports automated Pix refunds, return the refunded `value` and a valid `refundId` instead.

For more information, see the [Refund Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/refunds) endpoint reference.

### Communicate with the gateway

The last endpoint, `POST` [Inbound Request (BETA)](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/inbound-request/-action-), provides a URL that enables a direct connection between the VTEX gateway and the payment provider.

See an example of the Inbound Request (BETA) request:

```json
{
    "requestId": "LA4E20D3B4E07B7E871F5B5BC9F91",
    "transactionId": "D3AA1FC8372E430E8236649DB5EBD08E",
    "paymentId": "F5C1A4E20D3B4E07B7E871F5B5BC9F91",
    "authorizationId": "{{authorizationId}}",
    "tid": "{{tid}}",
    "requestData": {
        "body": "{{originalRequestBody}}"
    }
}
```

As a result, the provider should send the following response:

```json
{
    "requestId": "{{requestId}}",
    "transactionId": "{{transactionId}}",
    "paymentId": "{{paymentId}}",
    "authorizationId": "{{authorizationId}}",
    "tid": "{{tid}}",
    "requestData": {
        "body": "{{originalRequestBody}}"
    }
}
```

> ℹ️ Inbound Request (BETA) is mandatory only for Payment Provider Protocol integrations that use an external Payment App. If you implement Pix with the VTEX Payment App, this endpoint isn't required. For more information, see the [Inbound Request (BETA)](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/inbound-request/-action-).

For more information about Pix, see the [Pix FAQ](https://help.vtex.com/en/docs/tutorials/pix-faq).

After completing all integration steps, complete the [homologation process](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-homologation) so VTEX stores can use your provider as a payment method.
