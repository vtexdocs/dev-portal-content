---
title: "Implementing a Payment Provider"
slug: "payments-integration-implementing-a-payment-provider"
hidden: false
createdAt: "2021-03-26T17:05:15.623Z"
updatedAt: "2022-02-03T14:28:50.706Z"
---
The following sections show how to develop the middleware that will interpret the calls made between VTEX and the provider.

It also shows that the payment provider protocol consists of nine endpoints, divided into two sessions: **Payment flow** and **Configuration flow**. The middleware must be able to receive the information supplied by all these calls properly.

> ⚠️ To develop a new payment connector, it is mandatory to follow the **prerequisites determined by VTEX**. You can learn about them in the [Implementation prerequisites section of our Payment Provider Protocol article](https://help.vtex.com/en/tutorial/payment-provider-protocol--RdsT2spdq80MMwwOeEq0m#implementation-prerequisites).

## Developing the middleware

### Requirements

The middleware can be developed using any programming language, there are no restrictions. However, we established four requirements for this stage:

* The endpoint must be served over HTTPS on port 443 with TLS 1.2 support. **That format is required,** in no case endpoints served over HTTP will be accepted in the implementation process.
* The partner’s API must be public. In the homologation process, we will **not **accept any kind of restricted APIs.
* The partner must create a subdomain or a domain name to the endpoint. IP addresses will not be accepted as names under any circumstances.
* We want our processes to run quickly, so it is important that the endpoint responds in less than 5 seconds to the homologation tests. Also, the endpoint must respond in less than 20 seconds to any call.

With the requirements aligned, we can proceed to the Payment Flow.

## Payment Flow

The following endpoints are used to implement the operations that happen in the authorization, cancellation or refund, and settlement flows.

**1. GET Manifest**

Through this endpoint, the provider's manifest is displayed, consisting of a variety of metadata settings such as payment methods, split configuration, and custom fields.

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

> ⚠️ If you support any type of [custom payment](https://help.vtex.com/en/tutorial/how-to-configure-a-custom-payment--tutorials_451), please indicate only the method supported type (Cobranded, Privatelabels or Promissories) in the `"name"` field. It is not necessary to describe the specific name of the supported custom payment (e.g., Colombian Bank Promissory).

For more information about this step, you can check the [GET List Payment Provider Manifest](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#get-/manifest) endpoint documentation.

**2. POST Create Payment**

When a customer makes a purchase at the checkout, the provider must create a payment related to the order. Therefore, the provider must be ready to receive the request body that will contain all the cart information:

```json
{
    "reference": "32478982",
    "orderId": "1047232106697",
    "selerId": "xpto",
    "transactionId": "611966",
    "paymentId": "5B127F1E0C944EF9ACE264FEC1FC0E91",
    "paymentMethod": "cash",
    "paymentMethodCustomCode": "{{paymentMethodCustomCode}}",
    "merchantName": "lojaexemplo",
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

The `callbackURL` is an URL used to make retries in the operation flow. In addition, if the partner adopts redirect as a payment flow, you should also include the `returnURL` in the request payload. Thus, VTEX will be able to realize the redirect flow, if necessary.

> ⚠️ Both `callbackURL` and `returnURL` are developed by the provider.

On the other hand, we need that your provider returns this call with the following response:

```json

{
    "paymentId": "5B127F1E0C944EF9ACE264FEC1FC0E91",
    "status": "undefined",
    "authorizationId": "AUT-E4B9C36034-ASYNC",
    "paymentUrl": "https://exemplo2.vtexpayments.com.br/api/pub/fake-payment-provider/payment-redirect/611966/payments/5B127F1E0C944EF9ACE264FEC1FC0E91",
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

The parameters `delayToAutoSettle` and `delayToAutoSettleAfterAntifraud` define the total of time that the system will wait to start the capture flow. A similar process happens for the parameter  `delayToCancel`, but after the timeout, the system will proceed to the cancellation flow.

> ⚠️ All of these three periods of time are established by the provider and should be counted in seconds.

Also, the parameters `code` and `message` are fields to which the provider can send us any information about the process. Both are optional and will appear in the next calls.

All the fields are described in the [POST Create Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments) documentation.

**3. POST Cancel Payment**

To cancel a payment, you must already have created one. Your provider must be ready to receive only two information: the `paymentId`, the identifier of the payment that will be canceled, and the `requestId`, the identifier that ensures its idempotency.

For “idempotency”, we mean an action ability to be done several times. As we explained in the [Operations](https://developers.vtex.com/docs/guides/payments-integration-purchase-flows#operations-in-the-payment-flow) section, the cancellation flow can be retried during a whole day until the provider responds to the call.

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

Refer to the [complete documentation](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/cancellations) for more details.

**4. POST Capture Payment**

If your transaction was completed successfully, the provider can capture the payment. In fact, it is really important for you to know that VTEX supports partial captures.

This happens because the payment can be captured in two different moments:

* When the store invoices the order.
* After the period defined in the fields `delayToAutoSettle` and  `delayToAutoSettleAfterAntifraud` is timeout.

In this context, the field `value` is mandatory and crucial for the operation to be realized properly.

VTEX will send the information below to capture a payment:

```json
{
    "paymentId": "5B127F1E0C944EF9ACE264FEC1FC0E91",
    "transactionId": "611966",
    "value": 20.0,
    "requestId": "5678"
}
```

The response will be similar to the request body. But the parameter `value` can be fulfilled with the full amount that was sent in the request or with a smaller one. It all depends on how much the provider wants to capture.

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

Refer to the [Capture Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/settlements) endpoint documentation for more details.

**5. POST Refund Payment**

VTEX also supports partial refunds, it is a similar logic for the capture.

For example, consider a purchasing cart with two items. One scenario that can happen is that the store needs to return just one of the purchased items. In this case, we can refund just the value of that one single item instead of refunding the full value that includes both items and shipping.

In any case, the provider should be ready to receive the following request:

```json
{
    "paymentId": "VQKIIBUVOFDBIDLKZPOWSKETDYWCMJSACDVXWFCJVSKXGYVBBVISZRJLLQEKERJEMDYEINOUMFAZZGNEDVBQBABLUKLFBSEEIGLCAQTOGOGURKLFCAHJQTDMBNKYBIST",
    "transactionId": "611966",
    "settleId": "31018A3281",
    "value": 10.0,
    "requestId": "5678"
}
```

The response expected is:

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

Remember that, if needed, the provider can return the call with the field `value` fulfilled with an amount smaller than the value informed in the request to realize a partial refund.

Refer to the [Post Refund Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/refunds) endpoint for more details.

**6. POST Inbound Request (BETA)**

The Inbound Request (BETA) implements an URL that facilitates a direct connection between our Gateway service and the Payment Provider.

It is responsible for the communication with the provider's back-end through our gateway, relying on the security of sending the context of the transaction by VTEX.

An example of the request is:

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

An expected response would be:

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

Refer to the [Post Inbound Request (BETA)](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/inbound-request/-action-) endpoint for more details.

## Configuration Flow

In VTEX, the merchant has to enable one or more connectors through the Admin. The setup is basically the same for all the partners and you can check the [tutorial](https://help.vtex.com/en/tutorial/afiliacoes-de-gateway--tutorials_444) on our Help Center.

However, this operation follows an authentication flow that allows the provider to recognize and authorize the merchant’s solicitation. The following endpoints generate three credentials -  `appKey`, `appToken` and `applicationId` - that are saved by the VTEX system, which allows the merchant to enable the connector without copying and pasting any credentials.

[block:callout]
{
  "type": "info",
  "body": "This flow is optional and does not impact your connection with VTEX. If you do not intend to implement it, skip to the [Homologation](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-homologation) section."
}
[/block]

**1. POST Create Authorization Token**

For the first step, the request body will be:

```json
{
    "applicationId": "vtex",
    "returnUrl": "https://admin.mystore.example.com/provider-return?authorizationCode="
}
```

> ⚠️ The `applicationId` will always be \"vtex\".

Then, the provider should return an identification token so we can redirect the merchant to the provider application.

```json
{
    "applicationId": "vtex",
    "token": "auth_token_39766d98535d43a491d03b8c3bea060f"
}
```

Refer to the [Create Authorization Token](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/authorization/token) endpoint documentation to check all the details.

**2. GET Provider Authentication**

This call enables the merchant to analyse the provider’s terms and conditions to use its service.

With the token supplied in the previous response body, VTEX can redirect the merchant to the provider login page.

In the response body, we expect an `authorizationCode` related to the `returnUrl` sent to you in the first step of the configuration flow.

```json
{
    "authorizationCode": "auth_code_5b7be276c8e04e95bb1e",
    Grant access to "vtex" application
}
```

Refer to the [Get Provider Authentication](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#get-/authorization/redirect) endpoint for more details.

**3. GET Credentials**

Finally, the provider must send us the values of the three credentials.

We expect a response similar to this one:

```json
{
    "applicationId": "vtex",
    "appKey": "test_key_AE06E97A8C5B45DFA2DC665D6BE91E",
    "appToken": "test_token_90FB36380D114B37BC0557AEEE40ED"
}
```

With that, the credentials will be saved in our system and activated at the moment the merchant decides to enable the conector.

Refer to the [Get Credentials](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#get-/authorization/credentials) endpoint to check all the details.
