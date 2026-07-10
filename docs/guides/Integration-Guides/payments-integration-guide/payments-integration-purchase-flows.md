---
title: "Purchase Flows"
slug: "payments-integration-purchase-flows"
hidden: false
createdAt: "2021-03-26T14:45:28.135Z"
updatedAt: "2026-07-06T00:00:00.000Z"
excerpt: "Understand the Transparent, Redirect, and Payment App purchase flows in VTEX and how the Gateway authorizes, cancels, refunds, and settles payments with providers."
---

A purchase flow (also known as shopping flow) represents the steps a customer takes to complete payment for a purchase. In VTEX, the available purchase flows are:

- [Transparent](#transparent)
- [Redirect](#redirect)
- [Payment App](#payment-app)

## Transparent

The Transparent purchase flow is used when customers fill in payment information in the standard SmartCheckout template and complete the purchase without leaving the store. This is the most common option to provide a seamless payment experience.

The sequence of events in a Transparent payment flow occurs as follows:

1. The customer fills in the payment information in the SmartCheckout template and clicks **Finish Payment**.
2. Checkout sends a [Start Transaction request](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/pvt/transactions) to the Gateway.
3. The Gateway sends an [Authorization request](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments) (POST `/payments`) to the provider, including the payment data.
4. The provider processes the payment and returns the authorization status in the response body: `approved` or `denied`. For asynchronous methods, the provider returns `undefined` and later notifies the final status through the `callbackUrl`.
5. The Gateway relays the status to Checkout, which displays the Order Placed screen when the payment is `approved` or an error when it is `denied`.

## Redirect

The Redirect purchase flow is used when customers confirm the payment option in the store and are then redirected to a different page to fill in payment information and complete the purchase.

This option is used when the partner needs a specific interaction with the customer that is not provided by the standard SmartCheckout template.

Some examples include: displaying a QR code for payment, filling in an application form, logging in to an external website.

> ⚠️ For the connector that uses Redirect, there is no need to pass all the Test Suite tests, only the Redirect one.

![Payment Redirect](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/payments-integration-purchase-flows-0.png)

The sequence of events in a Redirect payment flow occurs as described in the following steps:

1. The customer clicks **Finish Payment** in the Checkout.
2. Checkout calls the Gateway with a [Start Transaction request](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/pvt/transactions).
3. Gateway calls the provider with an [Authorization request](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments) (POST `/payments`).
4. Provider returns in the response body of the Authorization request the status `undefined` and the `paymentURL`.
5. Checkout redirects the customer to the `paymentURL` webpage.
6. On the `paymentURL` webpage, the customer interacts with the provider's interface.
7. Provider captures the input of customer interaction.
8. Provider [responds](https://help.vtex.com/en/tutorial/payment-provider-protocol--RdsT2spdq80MMwwOeEq0m#payment-authorization) to `callbackUrl` with the final authorization status (`approved` or `denied`).
9. Provider redirects the customer to the `returnURL` webpage.

> ℹ️ The content of the `paymentURL` parameter must include the complete URL to redirect the customer to the intended webpage, including the endpoint path and a code for that specific payment. For example: `https://php-connector.herokuapp.com/installments.php?paymentId=7ee64e51-a0d3-4405-874c-d7497ab84572`.

## Payment App

The Payment App purchase flow is a flexible option that lets customers go through a custom payment experience without leaving the store. It supports a wide variety of payment methods through its interaction with the Checkout API. Unlike the Transparent and Redirect flows, Payment Apps must be developed and deployed using [VTEX IO](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-io).

The sequence of events in a Payment App flow occurs as follows:

1. The customer selects a payment method associated with a Payment App and confirms the purchase.
2. Checkout starts the transaction and sends the payment to the Gateway.
3. The Gateway sends an [Authorization request](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments) (POST `/payments`) to the provider. The provider returns the status `undefined` and the `paymentAppData` field, which identifies the Payment App and its payload.
4. Checkout instantiates the Payment App and renders the custom payment experience, such as a QR code or a 3D Secure 2 authentication challenge.
5. The customer completes the interaction, and the Payment App notifies Checkout to validate the transaction.
6. Checkout retrieves the final status from the Gateway and displays the Order Placed screen when the payment is `approved` or an error when it is `denied`.

For a detailed explanation of this flow, see the [Payment App](https://developers.vtex.com/docs/guides/payments-integration-payment-app#understanding-the-payment-app-flow) guide.

## Operations in the payment flow

The following operations define the patterns of interaction between the Payment Provider and the VTEX Payments Gateway:

- [Authorization](#authorization)
- [Cancellation or Refund](#cancellation-or-refund)
- [Settlement](#settlement)

When a customer completes a purchase, this triggers the creation of a new payment request, starting with the Authorization operation.

### Authorization

As soon as the purchase is complete, the Payments Gateway sends a [POST Create Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments) request to the provider.

The payload is large and contains information such as the cart items, billing address, order ID, payment methods, and `callbackUrl`. For more information about the endpoints and their payloads, see the [Implementing a Payment Provider](https://developers.vtex.com/docs/guides/payments-integration-implementing-a-payment-provider) article.

The provider then responds to the request. If the payment cannot be processed right away, the transaction status changes to `undefined`. This does not mean the payment was canceled or denied; it is still being evaluated.

The system retries the call asynchronously for up to seven days until the payment is processed. During this period, VTEX considers the payment "pending".

There are two ways to break this cycle of asynchronous retries, depending on whether the integration uses VTEX IO infrastructure:

- **Without VTEX IO (developed in the partner's infrastructure):** When the provider gets an updated payment status, it calls a **notification** endpoint from the `callbackUrl` parameter to change the payment status in the Gateway to `authorized` or `denied`. Both responses end the authorization flow.
- **With VTEX IO:** When the provider gets an updated payment status, it reads the `callbackUrl` parameter to call a **retry** endpoint. The Gateway then makes another Create Payment request to obtain the new status (`authorized` or `denied`) defined by the provider. Both responses end the authorization flow.

#### Callback URL

The `callbackUrl` field contains a URL that the payment provider uses to make a callback and inform the Gateway of the final payment status: `approved` or `denied`.

This URL has query parameters, including the mandatory `X-VTEX-signature`. As a security measure, this parameter contains a signature token of at most 32 characters that identifies the request as generated by VTEX. The following example shows a callback URL with the signature token:

```
https://gatewayqa.vtexpayments.com.br/api/pvt/payment-provider/transactions/8FB0F111111122222333344449984ACB/payments/A2A9A25B11111111222222333327883C/callback?accountName=teampaymentsintegrations&X-VTEX-signature=R123456789aBcDeFGHij1234567890tk
```

In the [Transactions page of the Admin](https://help.vtex.com/en/tutorial/how-to-view-the-orders-details--tutorials_452), the signature token appears masked for security reasons, as in this example: `X-VTEX-signature=Rj******tk`.

When making the callback request, use the callback URL exactly as received to guarantee that all parameters are included.

#### Contingency Mode

Contingency Mode status is a native reliability feature that allows VTEX to track the payment health and stability of its partners, ensuring the system does not cancel orders due to instabilities.

When VTEX identifies consecutive errors in its payment partners’ integrations — more than five errors over the last five minutes — the Contingency Mode status is activated to handle credit card transactions.

While the Contingency Mode status is activated, all transactions that allow an asynchronous flow are retained. During this period, the transaction remains in `authorizing` status.

This process takes an average of two hours and can hold up to two thousand requests. When the provider’s system returns to stability, the Contingency Mode status is deactivated, and the system reattempts processing for the transactions on standby.

For more information and frequently asked questions, see the [Contingency Mode](https://help.vtex.com/docs/tutorials/mode-off-faq) article in the VTEX Help Center.

### Cancellation or refund

The cancellation flow starts when the order is canceled for any reason. Canceling an order also starts the process to cancel its payment.

In this case, there are two scenarios:

- The payment was approved and already settled.
- The payment was not approved.

#### Payment approved and settled

When a payment is approved and already settled but canceled after that, VTEX makes the call [POST Refund Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/refunds) to the payment provider. Also, the Payment Provider Protocol accepts partial refunds when necessary.

Regardless of the provider's response, VTEX ends the transaction with the status `canceled`.

#### Payment approved but not settled

When a payment is approved but canceled before being settled, VTEX makes the call [POST Cancel Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/cancellations) to the payment provider.

Regardless of the provider's response, VTEX ends the transaction with the status `canceled`.

#### Payment not approved

VTEX sends the [POST Cancel Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/cancellations) request to the payment provider once there is no need to refund a payment that was not settled.

If the provider does not authorize the payment cancellation and returns an `undefined` status, the flow runs asynchronously for a day. If the provider does not respond within this period, the payment is canceled.

### Settlement

Once the Gateway authorizes the payment, VTEX sends the [POST Settle Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/settlements) request to the provider. If the provider does not authorize the settlement right away, the request keeps running asynchronously for a day.

During this period, when the provider responds authorizing the settlement, the VTEX platform changes the transaction status to `finished` and completes the flow.

If the request fails after one day of retries, the payment is canceled.

## Communication in the payment flow

With synchronous communication, VTEX communicates with the payment provider during the purchase flow to determine whether the payment is approved.

With asynchronous communication, VTEX waits longer for the provider’s approval. This applies to methods like bank invoice (boleto bancário in Brazil), where the shopper has a few days to pay through their bank.

Depending on the payment method selected, three endpoints in the payment flow might use synchronous or asynchronous communication:

- [POST Create Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments)
- [POST Cancel Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/cancellations)
- [POST Settle Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/settlements)

Since the selection of payment method depends on the customer, **your provider must be prepared to receive multiple repeated requests** in those endpoints.
