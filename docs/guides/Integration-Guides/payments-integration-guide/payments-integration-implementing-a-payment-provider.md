---
title: "Implementing a Payment Provider"
slug: "payments-integration-implementing-a-payment-provider"
excerpt: "Learn how to build payment provider middleware that implements the Payment Provider Protocol endpoints for VTEX integrations."
hidden: false
createdAt: "2021-03-26T17:05:15.623Z"
updatedAt: "2026-05-12T00:00:00.000Z"
---
This guide describes how to develop the middleware that interprets the calls between VTEX and your payment provider.

The Payment Provider Protocol consists of nine endpoints, divided into two sections: **Payment Flow** and **Configuration Flow**. The middleware must handle the requests and responses for all these endpoints.

> ⚠️ Before you begin, review the [Implementation prerequisites](https://help.vtex.com/en/tutorial/payment-provider-protocol--RdsT2spdq80MMwwOeEq0m#implementation-prerequisites) in the Payment Provider Protocol article.

## Developing the middleware

### Requirements

The middleware can be developed in any programming language. The following requirements apply:

* The endpoint must be served over HTTPS on port 443 with TLS 1.2 support. Endpoints served over HTTP are not accepted.
* The API must be publicly accessible. Restricted APIs are not accepted during the homologation process.
* The endpoint must use a subdomain or domain name. IP addresses are not accepted.
* The endpoint must respond in less than 5 seconds during homologation tests and less than 20 seconds for any other call.

## Payment Flow

The following endpoints implement the operations for authorization, cancellation, refund, and settlement.

### 1. GET Manifest

This endpoint returns the provider's manifest, which contains metadata settings such as payment methods, split configuration, and custom fields.

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
        "name": "MasterCard",
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
    ]
   }
```

> ⚠️ If you support any type of [custom payment](https://help.vtex.com/docs/tutorials/how-to-configure-a-custom-payment), use only the supported method type (`Cobranded`, `Privatelabels`, or `Promissories`) in the `"name"` field. Do not include the specific name of the custom payment (for example, "Colombian Bank Promissory").

For more information, see the [GET List Payment Provider Manifest](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#get-/manifest) endpoint documentation.

### 2. POST Create Payment

When a customer completes a purchase at checkout, the provider must create a payment associated with the order. Therefore, the provider must be ready to receive the request body containing the full cart information:

```json
{
    "reference": "32478982",
    "orderId": "1047232106697",
    "sellerId": "xpto",
    "transactionId": "611966",
    "paymentId": "5B127F1E0C944EF9ACE264FEC1FC0E91",
    "paymentMethod": "cash",
    "paymentMethodCustomCode": "{{paymentMethodCustomCode}}",
    "merchantName": "mystore",
    "value": "29,90",
    "currency": "BRL",
    "installments": "0",
    "deviceFingerprint": "12ade389087fe",
    "card": {
        "holder": "{{cardHolder}}",
        "number": "{{cardNumber}}",
        "csc": "{{cardSecurityCode}}",
        "expiration": {
            "month": "{{cardExpirationMonth}}",
            "year": "{{cardExpirationYear}}"
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
            "phone": "+12125357200"
        },
        "shippingAddress": {
            "country": "USA",
            "street": "12 E 49th St",
            "number": "10017",
            "complement": "Tower 49 Gallery",
            "neighborhood": "Central Midtown",
            "postalCode": "10017",
            "city": "New York",
            "state": "NY"
        },
        "billingAddress": {
            "country": "USA",
            "street": "12 E 49th St",
            "number": "10017",
            "complement": "Tower 49 Gallery",
            "neighborhood": "Central Midtown",
            "postalCode": "10017",
            "city": "New York",
            "state": "NY"
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
    "callbackUrl": "{{callbackUrl}}",
    "returnUrl": "{{returnUrl}}"
}
```

The `callbackUrl` is used for retry operations in the payment flow. If the provider uses redirect as a payment flow, the `returnUrl` must also be included so VTEX can redirect the shopper back to checkout after payment.

> ⚠️ Both `callbackURL` and `returnURL` are generated by VTEX and included in the request payload sent to the provider.

The provider must return the following response:

```json

{
    "paymentId": "5B127F1E0C944EF9ACE264FEC1FC0E91",
    "status": "undefined",
    "authorizationId": "AUT-E4B9C36034-ASYNC",
    "paymentUrl": "https://example.vtexpayments.com.br/api/pub/fake-payment-provider/payment-redirect/611966/payments/5B127F1E0C944EF9ACE264FEC1FC0E91",
    "nsu": "NSU-171BE62CB7-ASYNC",
    "tid": "TID-20E659E8E5-ASYNC",
    "acquirer": "TestPay",
    "code": "2000-ASYNC",
    "message": null,
    "delayToAutoSettle": 21600,
    "delayToAutoSettleAfterAntifraud": 1800,
    "delayToCancel": 21600
}
```

The `delayToAutoSettle` and `delayToAutoSettleAfterAntifraud` parameters define how long the system waits before starting the settlement flow. The `delayToCancel` parameter works similarly, but triggers the cancellation flow after the timeout.

> ⚠️ All three delay values are defined by the provider and must be specified in seconds.

The `code` and `message` parameters are optional fields where the provider can include additional information about the transaction. Both values persist through subsequent calls.

For a complete field reference, see the [POST Create Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments) endpoint documentation.

### 3. POST Cancel Payment

To cancel a payment created previously, the provider must accept a request containing two fields: `paymentId` (the identifier of the payment to cancel) and `requestId` (the identifier that ensures idempotency).

Idempotency means the same cancellation request can be sent multiple times without changing the result. As described in the [Operations](https://developers.vtex.com/docs/guides/payments-integration-purchase-flows#operations-in-the-payment-flow) section, the cancellation flow can be retried for up to one day until the provider responds.

```json
{
    "paymentId": "F5C1A4E20D3B4E07B7E871F5B5BC9F91",
    "requestId": "1234"
}
```

After completing the cancellation, the provider must return a response like this:

```json
{
    "paymentId": "F5C1A4E20D3B4E07B7E871F5B5BC9F91",
    "message": "Successfully canceled",
    "code": null,
    "cancellationId": "1457BD07E6",
    "requestId": "1234"
}
```

For more details, see the [Cancel Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/cancellations) endpoint documentation.

### 4. POST Capture Payment

After a transaction is authorized successfully, the provider can capture the payment. VTEX supports partial settles.

A payment can be settled in two scenarios:

* When the store invoices the order.
* After the period defined in `delayToAutoSettle` or  `delayToAutoSettleAfterAntifraud` times out.

The `value` field is required for the settlement operation.

VTEX sends the following request to settle a payment:

```json
{
    "paymentId": "5B127F1E0C944EF9ACE264FEC1FC0E91",
    "transactionId": "611966",
    "value": 20.0,
    "requestId": "5678"
}
```

The response `value` can match the full amount from the request or a smaller amount for a settlement capture:

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

For more details, see the [Capture Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/settlements) endpoint documentation.

### 5. POST Refund Payment

VTEX supports partial refunds. For example, if a cart contains two items and the store needs to return only one, the refund can cover just that item's value instead of the full order amount.

The provider must accept the following request:

```json
{
    "paymentId": "F5C1A4E20D3B4E07B7E871F5B5BC9F91",
    "transactionId": "611966",
    "settleId": "31018A3281",
    "value": 10.0,
    "requestId": "5678"
}
```

Expected response:

```json
{
    "paymentId": "F5C1A4E20D3B4E07B7E871F5B5BC9F91",
    "refundId": null,
    "value": 0.0,
    "code": "refund-manually",
    "message": "Refund should be done manually",
    "requestId": "5678"
}
```

The provider can return a `value` smaller than the requested amount to perform a partial refund.

For more details, see the [Refund Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/refunds) endpoint documentation.

### 6. POST Inbound Request (BETA)

The Inbound Request endpoint (BETA) enables a direct connection between the VTEX Gateway and the payment provider through an URL. It handles communication with the provider's backend through the gateway, sending the transaction context securely.

Request example:

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

Expected response:

```json
{
  "requestId": "LA4E20D3B4E07B7E871F5B5BC9F91",
  "paymentId": "F5C1A4E20D3B4E07B7E871F5B5BC9F91",
  "responseData": {
    "statusCode": 200,
    "contentType": "application/json",
    "content": "{\"myAttribute\":\"anyValue\"}"
  }
}
```

For more details, see the [Inbound Request (BETA)](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/inbound-request/-action-) endpoint documentation.

## Configuration Flow

On VTEX, merchants enable connectors through the VTEX Admin. The setup process is similar for all partners. For instructions, see the [Register payment and anti-fraud providers](https://help.vtex.com/docs/tutorials/registering-gateway-affiliations) article on the Help Center.

The Configuration Flow implements an authentication mechanism that allows the provider to recognize and authorize the merchant's request. The endpoints below generate three credentials — `appKey`, `appToken`, and `applicationId` — that are stored by VTEX, allowing the merchant to enable the connector without manually copying credentials.

> ℹ️ This flow is optional and does not affect the integration with VTEX. If you do not plan to implement it, skip to the [Homologation](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-homologation) section.

### 1. POST Create Authorization Token

The request body for this endpoint is:

```json
{
    "applicationId": "vtex",
    "returnUrl": "https://admin.mystore.example.com/provider-return?authorizationCode="
}
```

> ⚠️ he `applicationId` value is always `"vtex"`.

The provider must return an identification token that VTEX uses to redirect the merchant to the provider's application:

```json
{
    "applicationId": "vtex",
    "token": "auth_token_39766d98535d43a491d03b8c3bea060f"
}
```

For more details, see the [Create Authorization Token](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/authorization/token) endpoint documentation.

### 2. GET Provider Authentication

This endpoint allows the merchant to review the provider's terms and conditions.

Using the token from the previous response, VTEX redirects the merchant to the provider's login page. The response must include an `authorizationCode` associated with the `returnUrl` from the first step of the Configuration Flow.

```json
{
    "authorizationCode": "auth_code_5b7be276c8e04e95bb1e"
}
```

> ⚠️ By returning the `authorizationCode`, the provider grants access to the "vtex" application.

For more details, see the [Provider Authentication](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#get-/authorization/redirect) endpoint documentation.

### 3. GET Credentials

This endpoint returns the three credential values.

Expected response:

```json
{
    "applicationId": "vtex",
    "appKey": "test_key_AE06E97A8C5B45DFA2DC665D6BE91E",
    "appToken": "test_token_90FB36380D114B37BC0557AEEE40ED"
}
```

The credentials are stored by VTEX and activated when the merchant enables the connector.

For more details, see the [Get Credentials](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#get-/authorization/credentials) endpoint documentation.
