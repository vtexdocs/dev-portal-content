---
title: "Pix: Instant Payments in Brazil"
slug: "payments-integration-pix-instant-payments-in-brazil"
hidden: false
createdAt: "2020-10-27T00:35:36.404Z"
updatedAt: "2022-02-03T15:19:06.694Z"
---
[Pix](https://www.bcb.gov.br/estabilidadefinanceira/pix) is the instant payments ecosystem implementation led by the Central Bank of Brazil (BCB) to enable online money transfers with reduced costs, increased safety and 24/7 availability. Transfers occur directly from the payer’s account to the payee’s account, without the need for intermediaries, resulting in lower transaction costs.

Pix is available to both physical and legal persons, and both need to have an identifier key registered with some financial entity (banks, fintechs or payment institutions) to proceed with the transaction.

According to the [eligibility criteria](https://www.bcb.gov.br/estabilidadefinanceira/participantespix) set forth by the BCB, certain financial entities will be required to offer this payment method, while others may optionally offer it or not be eligible to participate.

In this article, we will explain how to extend your Payment Provider Protocol implementation to allow stores to offer Pix as an additional payment method to their clients.

![These are some of the benefits of an instant payments ecosystem highlighted by the BCB](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/payments-integration-pix-instant-payments-in-brazil-0.png)

> ✔️ If you want to know more about instant payments in Brazil, we have prepared a [blog post](https://vtex.com/pt-br/blog/produto/pix-no-e-commerce/) with all the implications of this new payment method. You can also check out the [FAQ](https://www.bcb.gov.br/estabilidadefinanceira/perguntaserespostaspix) provided by the BCB for more details.

> ⚠️ This tutorial assumes you are already a [VTEX Partner](http://vtex.com/br-pt/partner) and understand how the [Payment Provider Protocol](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-protocol) works.

## Integration conditions

If you are ready to develop the middleware that implements our Payment Provider Protocol, you should be aware of these requirements:

- **All endpoints must be served over HTTPS on port 443 with TLS 1.2 support.** Connections over non-secured HTTP will not be accepted under any circumstances.
- **The integrator must create a subdomain or a domain name for the provider endpoints.** IP addresses will not be accepted as names under any circumstances.
- **The middleware must consistently respond within established response times.** We enforce a maximum response time of 5 seconds for homologation tests, as well as a maximum response time of 20 seconds to any other API request.

While our protocol describes nine endpoints for implementation, not all of them are applicable when integrating Pix instant payments. Regarding the two provider flows:

- [Payment Flow](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#get-/manifest): six endpoints that must be **mandatory** implemented.
- [Configuration Flow endpoints](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/authorization/token): three endpoints whose implementation is **optional and currently not available for Pix**.

The table below gives further detail on the applicability of each endpoint to Pix instant payments.

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

> ℹ️ Pix is **not available** for marketplace clients that use the Checkout Split.

> ⚠️ The following JSONs are just **examples**. Each partner **must adapt** the models to their own realities, with the data needed to realize the integration.

## Integration steps

### Establish the payment methods available

The first information your provider has to inform us is which are the payment methods that it handles. To do so, you can make an API request using the `<span class="api pg-type type-get">`GET [List Payment Provider Manifest](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#get-/manifest) route.

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

> ⚠️ Pix still **does not** handle payment split, but this feature may be released in the future. For more information on payment methods that currently accept split, check the [List Payment Provider Manifest endpoint](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#get-/manifest).

### Create Pix Payment Method

Now you have to create a new payment method. To do this, use the route `<span class="api pg-type type-post">`POST [Create Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments).

> ℹ️ A lot of information is required from the cart data in the Smart Checkout, so be careful and validate all payload information.

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

As a result, we expect the following response:

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

> ❗ The PIX QR Code expiration time must be set ​​between 15 and 60 minutes (900 and 3600 seconds). Also, the partner must respect the callback time (20 seconds).

For more information, access the [Create Payment endpoint](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments).

### Cancel a Payment

To cancel a payment, you must already have created one. To do so, you will make an API request using the route `<span class="api pg-type type-post">`POST [Cancel Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/cancellations).

See an example of the Cancel Payment request:

```json
{
    "paymentId": "F5C1A4E20D3B4E07B7E871F5B5BC9F91",
    "requestId": "1234"
}
```

After the provider realizes the payment cancelation, we expect a response like this:

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

### Settle Payment (capture)

If your transaction was completed successfully, the provider can settle the payment.

Thus, in order to settle the payment, VTEX will send the information below through the `<span class="api pg-type type-post">`POST [Settle Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/settlements).

See an example of the Settle Payment request:

```json
{
    "paymentId": "5B127F1E0C944EF9ACE264FEC1FC0E91",
    "transactionId": "611966",
    "value": 20.0,
    "requestId": "5678"
}
```

The response should be similar to the following response body:

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

### Refund Payment

The provider should be ready to receive the following request through the `<span class="api pg-type type-post">`POST [Refund Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/refunds).

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

For more information, access the [Refund Payment endpoint](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/refunds).

### Communicate with the Gateway

The last endpoint, the `<span class="api pg-type type-post">`POST [Inbound Request (BETA)](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/inbound-request/-action-), implements a URL that facilitates a direct connection between our Gateway service and the Payment Provider.

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

As a result, the client should send the following response:

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

> ℹ️ The Inbound Request (BETA) is mandatory only for integrations via Payment Provider Protocol with an external Payment App. If the Pix payment method was implemented via VTEX Payment App, the Inbound Request is not necessary. For more information, access the [Inbound Request (BETA)](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/inbound-request/-action-).

For more information about the Pix, access its [FAQ](https://help.vtex.com/en/tutorial/pix-faq--3lx7zCU2lQroTEBCYKYbo3).

After completing all integration steps, you should complete our [homologation process](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-homologation) to allow VTEX stores to use your provider as a payment method.
