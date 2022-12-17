---
title: "Purchase Flows"
slug: "payments-integration-purchase-flows"
hidden: false
createdAt: "2021-03-26T14:45:28.135Z"
updatedAt: "2022-10-07T21:06:12.411Z"
---
A purchase flow (also known as shopping flow) represents the steps or actions a customer takes in order to complete payment for a purchase. In VTEX, the available purchase flows are:

- Transparent
- Redirect
- Payment App

## Transparent

The Transparent purchase flow is used when customers fill in payment information in the standard SmartCheckout template and complete the purchase without leaving the store. This is the most common option if you want to provide a seamless payment experience.

## Redirect

The Redirect purchase flow is used when customers confirm the payment option in the store and are then redirected to a different page to fill in payment information and complete the purchase.

This option is used when the partner needs a specific interaction with the customer that is not provided by the standard SmartCheckout template. 

Some examples include: displaying a QR code for payment, filling in an application form, logging in to an external website.
[block:callout]
{
  "type": "warning",
  "body": "For the connector that will use Redirect, there is no need to pass all the Test Suit tests, only the Redirect one."
}
[/block]

![Payment Redirect](https://files.readme.io/c3f3d8b-Payment_Redirect-editado.png)
The sequence of events in a Redirect payment flow occurs as described in the following steps:

1. The customer clicks on **Finish Payment** in the Checkout.
2. Checkout calls the Gateway with a [Start Transaction request](https://developers.vtex.com/vtex-rest-api/reference/1createanewtransaction).
3. Gateway calls the provider with an [Authorization request](https://developers.vtex.com/vtex-rest-api/reference/4doauthorization) (POST `/payments`).
4. Provider returns in the response body of the Authorization request the status `undefined` and the `paymentURL`.
5. Checkout redirects the customer to the `paymentURL` webpage.
6. On the `paymentURL` webpage, the customer interacts with the provider's interface.
7. Provider captures the input of customer interaction.
8. Provider [responds](https://developers.vtex.com/vtex-rest-api/reference/createpayment#callbacks) to `callbackURL` with final authorization status (`approved` or `denied`).
9. Provider redirects the customer to the `returnURL` webpage.
[block:callout]
{
  "type": "info",
  "body": "The content of the `paymentURL` parameter has to include the complete URL to properly redirect the customer to the desired webpage, including the endpoint path and a code to that specific payment (e.g.:  http://php-connector.herokuapp.com/installments.php?paymentId=7ee64e51-a0d3-4405-874c-d7497ab84572)"
}
[/block]
## Payment App

The Payment App purchase flow is a flexible option used to allow customers to go through a custom payment experience without leaving the store. 

This model applies to a large variety of payment methods thanks to its interaction with the Checkout API. However, Payment Apps must be developed and deployed using [VTEX IO](https://developers.vtex.com/vtex-developer-docs/docs/what-is-vtex-io). For more information, check our [Payment App guide](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-payment-app).

## Operations in the payment flow

The following operations define the patterns of interaction between the Payment Provider and the VTEX Payments Gateway:

  * Authorization
  * Cancellation or Refund
  * Settlement

When a customer completes a purchase, this triggers the creation of a new payment request, starting with the Authorization operation.

### Authorization

As soon as the purchase is complete, the Payments Gateway sends a [POST Create Payment](https://developers.vtex.com/vtex-rest-api/reference/createpayment) request to the provider. 

The payload is quite big, as it contains information such as the items in the cart, billing address, the order ID, payment methods, callbackURL, and others. More information about the endpoints and their payloads will be available in the [Implementing a Payment Provider](ref:payments-integration-implementing-a-payment-provider) section.

After that, the provider should respond to the request. If the payment cannot be processed right the way, the transaction status changes to `undefined`. That does not mean that the payment was canceled or denied, it is just being evaluated.

The system can retry the call asynchronously for seven days until the payment is indeed processed. During this period, VTEX will assume that the payment is “pending".

To break this cycle of asynchronous retries, there are two possible flows depending if the integration uses VTEX IO infrastructure or not:

  * **Without VTEX IO (developed in the partner's infrastructure)**: when the provider gets an updated payment status, it will use a **notification** endpoint from the `callbackURL` parameter to change the payment status in the Gateway to `authorized` or `denied`. Both responses end the authorization flow.
  * **With VTEX IO**: when the provider gets an updated payment status, it will read the `callbackURL` parameter to call a **retry** endpoint. Then, the Gateway makes another Create Payment request to obtain the new status defined by the provider, which will be `authorized` or `denied`. Both responses end the authorization flow.

#### Callback URL

The `callbackUrl` field contains an URL that the payment provider uses to make a callback and inform our gateway of the final payment status: `approved` or `denied`. 

This URL has some query parameters, including the `X-VTEX-signature`. This parameter is mandatory and contains a signature token to identify that the request has been generated from VTEX as a security measure. The signature token has at most 32 characters. You can check an example of callback URL with the signature token below:

```
https://gatewayqa.vtexpayments.com.br/api/pvt/payment-provider/transactions/8FB0F111111122222333344449984ACB/payments/A2A9A25B11111111222222333327883C/callback?accountName=teampaymentsintegrations&X-VTEX-signature=R123456789aBcDeFGHij1234567890tk
```

In the [Transactions page of the Admin](https://help.vtex.com/en/tutorial/how-to-view-the-orders-details--tutorials_452), the signature token appears masked for security reasons, as in this example: `X-VTEX-signature=Rj******tk`.

When making the callback request, we recommend that payment providers use the callback URL exactly as received, which guarantees that all the parameters are included.

#### Mode-off

Mode-off status is a native reliability feature that allows VTEX to track the payment health and stability of their partners, ensuring that the system will not cancel orders due to instabilities.

When VTEX identifies consecutive errors in its payment partners’ integrations — more than five errors over the last five minutes — the mode-off status is activated to handle credit card transactions. 

While the mode-off status is activated, all transactions that allow an asynchronous flow will be retained. During this period, the transaction remains in `authorizing` status.

This process takes an average of two hours and can hold up to two thousand requests. If the provider’s system returns to stability, the mode-off status is deactivated and our system will run processing reattempts for the transactions on standby. 

For more information and frequently asked questions, refer to the [Mode-Off: FAQ](https://help.vtex.com/en/tutorial/mode-off-faq--6hbd7PuvoxuRbPCvTqjxeB) article in our Help Center.
 
### Cancellation or refund

The cancellation flow starts if the order is canceled for any reason. When an order is canceled, it activates the process to cancel the order’s payment as well. 

In this case, there are two scenarios: 

  * The payment was approved and already settled.
  * The payment was not approved.

#### Payment approved and settled 

When a payment is approved and already settled but canceled after that, VTEX makes the call [POST Refund Payment](https://developers.vtex.com/reference/refundpayment) to the payment provider. Also, the Payment Provider Protocol accepts partial refunds when necessary. 

Regardless of the provider's response, VTEX will end the transaction with the status `canceled`.


#### Payment approved but not settled 

When a payment is approved but canceled before being settled, VTEX makes the call [POST Cancel Payment](https://developers.vtex.com/vtex-rest-api/reference/cancelpayment) to the payment provider. 

Regardless of the provider's response, VTEX will end the transaction with the status `canceled`.


#### Payment not approved 

VTEX sends the [POST Cancel Payment](https://developers.vtex.com/reference/cancelpayment) request to the payment provider once there is no need to refund a payment that was not settled.

If the provider does not authorize the payment cancellation and returns a response with an `undefined` status, the flow will run asynchronously for a day. If the provider does not respond after this period, the payment will be canceled.

### Settlement

Once the gateway authorizes the payment, VTEX sends the [POST Settle Payment](https://developers.vtex.com/reference/settlepayment) request to the provider. If the provider does not authorize the settlement right the way, the request will keep running asynchronously for a day. 

During this period, when the provider responds to the call authorizing the settlement, VTEX’s platform changes the transaction status to `finished` and completes the flow.

If after one day of retries the request fails, the payment will be canceled.

## Communication in the payment flow

When using synchronous communication, VTEX will communicate with the payment provider during the purchase flow and this will determine whether the payment was approved or not. 

When using asynchronous communication, VTEX will wait for a longer period of time for approval from the payment provider. This is the case of bank invoice (boleto bancário/Brazil), for example, where the shopper is expected to have a few days to pay for their order through their bank.

Depending on the payment method selected, three endpoints in the payment flow might use synchronous or asynchronous communication:

- [POST Create Payment](https://developers.vtex.com/reference/createpayment)
- [POST Cancel Payment](https://developers.vtex.com/reference/cancelpayment)
- [POST Settle Payment](https://developers.vtex.com/reference/settlepayment)

Since the selection of payment method depends on the customer, **your provider must be prepared to receive multiple repeated requests** in those endpoints.