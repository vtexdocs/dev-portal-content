---
title: "Payment Provider Protocol for Point of Sale (POS) - VTEX Sales App"
slug: "payments-integration-ppp-applied-to-pos"
hidden: false
createdAt: "2022-09-28T22:39:13.979Z"
updatedAt: "2022-09-29T17:49:33.957Z"
---
VTEX has multiple solutions to deliver a [Unified Commerce](https://help.vtex.com/en/tracks/unified-commerce-strategies--3WGDRRhc3vf1MJb9zGncnv) experience to shoppers, being able to handle orders from both the ecommerce and physical stores. To deal with the physical store experience, VTEX offers the [VTEX Sales App](https://help.vtex.com/en/tracks/instore-getting-started-and-setting-up--zav76TFEZlAjnyBVL5tRc), where sellers can serve customers and complete the entire sales process. When finishing a purchase, the customer will have the option to make the payment with a physical card in a payment terminal, also known as a Point of Sale (POS).

For payment partners to integrate their solutions for payments using a POS, there are a series of requirements that must be taken into account. You can check a summary of the requirements in the list below:

- Develop a payment connector using the [Payment Provider Protocol (PPP)](https://help.vtex.com/en/tutorial/payment-provider-protocol--RdsT2spdq80MMwwOeEq0m). There are some details required in the connector to deal with payments on a POS, such as:
  - Include the supported payment methods (credit or debit card) in the [Manifest](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#get-/manifest).
  - Use [callbacks](https://help.vtex.com/tutorial/payment-provider-protocol--RdsT2spdq80MMwwOeEq0m#payment-authorization) for asynchronous payments.
  - Work with [Payment Apps](https://developers.vtex.com/docs/guides/payments-integration-payment-app) to identify the POS and wait for its response.
  - The endpoint must return to any call in less than 20 seconds.
- For testing, have a VTEX store configured with the supported payment methods. This should be provided by VTEX.
- If needed for testing, have a device with the [VTEX Sales App installed](https://help.vtex.com/en/tracks/instore-using-the-app--4BYzQIwyOHvnmnCYQgLzdr/2rPSJ8519UCCZo5uEBkqxh).
- Developers might want to create their Payment App to identify the POS. This app will also have to be installed in the store.

> ⚠️ To develop a new payment connector, it is mandatory to follow the **prerequisites determined by VTEX**. You can learn about them in the [Implementation prerequisites section of our Payment Provider Protocol article](https://help.vtex.com/en/tutorial/payment-provider-protocol--RdsT2spdq80MMwwOeEq0m#implementation-prerequisites).

## Payment connector pre-requisites

There are some steps needed for the connector to be able to process payments in the physical world, which are described below:

1. Route [GET List Payment Provider Manifest](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#get-/manifest) (`/manifest`). The response body of the endpoint must contain the payment methods `Venda Direta Credito` and `Venda Direta Debito`. In case a split of receivables is offered, this must be informed in the `allowsSplit` field for each payment method. Example of response body properly configured:

```json
{
  paymentMethods:
  [
    {
      name: "American Express",
      allowsSplit: "onCapture"
    },
    {
      name: "Diners",
      allowsSplit: "onCapture"
    },
    {
      name: "Elo",
      allowsSplit: "onCapture"
    },
    {
      name: "Hipercard",
      allowsSplit: "onCapture"
    },
    {
      name: "Mastercard",
      allowsSplit: "onCapture"
    },
    {
      name: "Visa",
      allowsSplit: "onCapture"
    },
    {
      name: "Boleto Bancário",
      allowsSplit: "onAuthorize"
    },
    {
      name: "Visa Electron",
      allowsSplit: "disabled"
    },
    {
      name: "Maestro",
      allowsSplit: "disabled"
    },
    {
      name: "Pix",
      allowsSplit: "onAuthorize"
    },
+    {
+      name: "Venda Direta Debito",
+      allowsSplit: "onCapture"
+    },
+    {
+      name: "Venda Direta Credito",
+      allowsSplit: "onCapture"
+    }
  ]
}
```

2. Route [POST Create Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments) (`/payments`). This route must be idempotent, which means that the provider must be able to correctly handle if the route is called many times with the same `paymentId`. The provider should not recreate the payment for multiple calls but has to return the most updated status instead.

## Scenery and flow

Here we describe the payment flow in the context of a physical store using a POS. The following sequence diagram represents all the steps in this flow, where the green bars are the steps that the payment provider is responsible for:
![Fluxo PPP com POS atualizado](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/payments-integration-ppp-applied-to-pos-0.png)

1. The flow starts with a buyer finishing a purchase in a VTEX physical store created on [VTEX Sales App](https://help.vtex.com/en/tracks/instore-getting-started-and-setting-up--zav76TFEZlAjnyBVL5tRc).
2. The VTEX Sales App makes an [Authorization](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/pvt/transactions/-transactionId-/authorization-request) request to the VTEX Payment Gateway.
3. Our Gateway makes a [Create Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments) request to the connector defined in the store settings for the specific payment method used in the purchase (i.e.: `Venda Direta Credito`).
4. The Gateway receives the Create Payment response from the connector with the `undefined` status and the `appname` field of the `paymentAppData` parameter filled with the name of an app (i.e.: `vtex.challenge-terminal-connector-app`). It means that the payment is not concluded and it needs to do a challenge by opening a [Payment App](https://developers.vtex.com/docs/guides/payments-integration-payment-app#understanding-the-payment-app-flow), which will be responsible to identify the POS.
5. The VTEX Sales App receives the response from the Gateway and opens the app to start the challenge.
6. The seller interacts with the app to identify the POS to be used in the payment process. Then the app sends the serial number of the POS to the connector and closes.
7. The connector requests to update the order in the payment processor with the serial number of the POS.
8. After the app closes, a callback is triggered in the VTEX Sales App to the Gateway, initiating the sequence of requests to make the payment in the POS.
   1. The Gateway makes a Create Payment request to the connector with the same payment ID used in step 3. This means that the Gateway is waiting for an update on the payment status.
   2. The connector calls the payment processor to start the payment in the POS.
   3. The payment processor calls the POS to make the payment with the card. Then, the payment processor returns to the connector telling that the payment in the POS has started.
   4. Since it takes some time for the payment to be concluded in the POS, the connector returns to the Gateway once more with an `undefined` status and information to open another Payment App called `vtex.challenge-wait-for-confirmation`.
   5. The Gateway returns to the VTEX Sales App telling it to open the [Wait for confirmation app](#wait-for-confirmation).
9. The VTEX Sales App opens the [Wait for confirmation app](#wait-for-confirmation), so the user visually understands that the VTEX Sales App is waiting for the POS to finish the payment.
   1. The [Wait for confirmation app](#wait-for-confirmation) asks the Gateway for the updated payment status.
   2. The Gateway uses the Create Payment request to the connector for the updated payment status.
   3. While the POS does not finish the payment and responds, the Payment Connector keeps responding that the payment status is `undefined`.
   4. The Gateway responds to the [Wait for confirmation app](#wait-for-confirmation) app with the `undefined` status.
   5. The [Wait for confirmation app](#wait-for-confirmation) enters in a loop, repeating from step 9.1., calling the Gateway again for the updated status until the POS finishes the payment and the status change or there is a timeout. The time for the timeout is defined in the `secondsWaiting` parameter from the payload. If there is a timeout, the payment is canceled and the buyer has to finish the order again. More information can be found in the [Wait for confirmation app](#wait-for-confirmation) subsection in this article.
10. After step 8.3., many of the steps occurred in the background. But from that point, the buyer is allowed to insert the card and interact with the POS to perform the payment.
11. The POS responds to the payment processor from the request in step 8.3.
12. The payment processor processes the transaction and uses a webhook to call the connector.
13. The payment provider makes a mandatory [callback](https://help.vtex.com/en/tutorial/payment-provider-protocol--RdsT2spdq80MMwwOeEq0m#payment-authorization) request to the Gateway (without which it is not possible to approve or deny the POS transaction), sending the following information to VTEX:
    - Payload containing card information (`cardBrand`, `firstDigits` and `lastDigits` fields)
    - Payment status (`approved` or `denied`)
14. The [Wait for confirmation app](#wait-for-confirmation) requests the Gateway once more for the updated payment status.
15. The [Wait for confirmation app](#wait-for-confirmation) receives the updated payment status.
16. The [Wait for confirmation app](#wait-for-confirmation) responds to the VTEX Sales App that it can proceed, so the app is closed.
17. From a callback, the VTEX Sales App calls the Gateway to know the status of the payment.
18. The Gateway responds to the VTEX Sales App with the last status. If the payment status is `denied` or `canceled`, the VTEX Sales App shows an error and the buyer can try to finish the purchase again from the checkout. Else, the purchase is concluded and the order is placed in the system.

### Details on the Create Payment route

The request body of the [Create Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments) endpoint has many parameters. Some of them require more attention in the context of physical stores and are detailed below:

- `card`: VTEX’s Gateway does not receive card data for payments in physical stores. Therefore, this object is sent with all its fields as `null`.

```json
"card": {
        "holder": null,
        "number": null,
        "csc": null,
        "expiration": {
            "month": null,
            "year": null
        },
        "document": null,
        "token": null
    }
```

- `paymentMethod`: for payments in physical stores, instead of using values like `"Visa"` and `"Mastercard"`, this field will be filled with the values `"Venda Direta Debito"` or `"Venda Direta Credito"`. If the connector works both for ecommerce and physical payments, it can decide which of them is being used by checking this field.
- `callbackUrl`: this field is needed since physical payments follow an asynchronous flow. The Gateway uses this field to tell the provider which URL has to be used to notify VTEX about updates in the payment status. First, the payment is created with an `undefined` status. Then, when the status changes to `approved` or `denied`, the provider has to send a request to the URL from the `callbackUrl` field with the updated status. You can find more details about this flow in the [Additional interactions and paymentAppData](#additional-interactions-and-paymentappdata) section and the [Payment App](https://developers.vtex.com/docs/guides/payments-integration-payment-app#understanding-the-payment-app-flow) article.

### Asynchronous flow and delayToCancel

When VTEX Payment Gateway calls the Create Payment endpoint, the connector starts an asynchronous authorization process, which returns immediately with an `undefined` status. This flow is similar to other asynchronous payment methods like Pix and Boleto (common methods used in Brazil). After the Gateway receives the initial status as `undefined`, at some point the payment will be concluded and the status will be updated to `approved` or `denied`.

It is important to note that the payment cannot stay `undefined` forever. There is a limit of time that VTEX’s Gateway waits for the conclusion of the payment. If this time limit is exceeded, the Gateway automatically calls the [Cancel Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/cancellations) endpoint of the connector. This time limit is defined by the connector and informed by the `delayToCancel` field in the response body of the Create Payment route, expressed in seconds.

### Additional interactions and paymentAppData

At VTEX, payments in physical stores follow an asynchronous flow that requires additional interactions with the user, also called challenges, until it is approved. To offer this kind of interaction, the connector has to tell our Gateway from the `paymentAppData` field in the response of the Create Payment endpoint. This field contains the name of the VTEX IO app (`appName`) that will be presented on the VTEX Sales App and the data needed for the app to work (`payload`).

We have some apps that are ready to use for additional interaction with payments on a POS.

> ℹ️ Besides the provided apps, partners can also develop apps for their specific needs. You can check more details in the [Payment App](https://developers.vtex.com/docs/guides/payments-integration-payment-app) article.

#### Terminal connector App

This app uses the device camera to read the barcode of the POS that will be used for the purchase. After reading the barcode, the information is sent automatically to the URL defined by the `submitUrl` parameter. The payload sent by the app to the URL uses the following format: `{"serialNumber": "12345"}`.

Fields used in this app:

- `appName`:
  - `vtex.terminal-connector-app`
- `payload`:
  - `submitUrl` (string): URL where the `serialNumber` is sent to.

Payload example:

```json
"paymentAppData": {
    "appName": "vtex.terminal-connector-app",
    "payload":
        "{
            \"submitUrl\": \"https://coolacquirer.com/instore_config/1231231\"
        }"
}
```

![Print of the Terminal connector App using the camera to scan the bar code of the POS](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/payments-integration-ppp-applied-to-pos-2.png)

#### Wait for confirmation

This app is returned by the connector after the payment has started on the POS, so that the VTEX Sales App polls for the payment status. The waiting time for a status change in the payment is defined by the `secondsWaiting` parameter, which comes from the connector in the payload.

Fields used in this app:

- `appName`:
  - `vtex.challenge-wait-for-confirmation`
- `payload`:
  - `secondsWaiting` (int): defines how many seconds the app will keep open waiting for a payment status update.

Payload example:

```json
"paymentAppData": {
    "appName": "vtex.challenge-wait-for-confirmation",
    "payload": "{ \"secondsWaiting\": 600 }"
}
```

### Interaction with the POS

After the user interacts with the app that identifies the POS, the payment processor is responsible for the communication with the POS to read the physical card of the buyer. When communicating with the POS, the payment process is done without VTEX’s intervention. The payment processor is also responsible to deal with retries caused by password errors, insufficient credit, and other reasons.

When the payment processor receives an answer that the payment is either approved or denied, it has to tell VTEX Payment Gateway the response with the payment status. This is done through the callback flow using the URL in the `callbackUrl` field from the Create Payment request. You can find more details about this flow in the [Payment Authorization section of the Payment Provider Protocol](https://help.vtex.com/tutorial/payment-provider-protocol--RdsT2spdq80MMwwOeEq0m#payment-authorization) article.

The callback flow starts with the payment connector calling the URL in the `callbackUrl` field to the Gateway. The callback request can be one of two types: retry or notification. If it is a retry, the `/retry` route will be used and the Gateway will make another Create Payment request to receive the updated status. If it is a notification, the connector calls the `/notification` endpoint to tell the Gateway about the updated status. For physical payments, the payload of the callback request must have three additional fields about the card used in the payment, which are used for conciliations and merchant’s financial reports:

- `cardBrand`: Brand of the card.
- `firstDigits`: First six digits of the card number.
- `lastDigits`: Last four digits of the card number.

## Testing your connector

Before a VTEX store can provide payments in the physical world, some setup steps are needed in the payments Gateway. VTEX provides a store to the payment provider for testing during the development process, which will be already configured and ready to use. Nevertheless, you can follow the steps below to configure a store whenever needed:

1. Install the connector you developed in the store. If you are creating a PPF connector using VTEX IO, check the steps in the [Payment Provider Framework](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-framework#placing-an-order-with-your-new-connector) article to properly install this type of connector. If you need help with the installation, you can [open a ticket to VTEX support team](https://help.vtex.com/en/tutorial/opening-tickets-to-vtex-support--16yOEqpO32UQYygSmMSSAM?locale=en).
2. Configure a Gateway affiliation with the installed connector. You can find more details in the [Registering gateway affiliations](https://help.vtex.com/en/tutorial/registering-gateway-affiliations--tutorials_444) article.
3. Configure a payment condition that works with a POS. For credit cards is **Venda Direta Crédito**, and for debit cards is **Venda Direta Débito**. Remember to choose the configured affiliation. You can find more details in the [Configuring payment conditions](https://help.vtex.com/en/tutorial/how-to-configure-payment-conditions--tutorials_455) article.
4. Make the payment method available on the VTEX Sales App by following the steps in the [Define payment methods displayed on VTEX Sales App](https://developers.vtex.com/docs/guides/define-payment-methods-displayed-on-vtex-sales-app) article. The ID of the payment conditions used in the `filter` array is `44` for debit and `45` for credit and it can also be checked on the **Payment Conditions** page of the Admin.
5. Make a purchase on VTEX Sales App with the payment condition you configured with your connector.

## Making your connector available to everyone

When you decide the connector is ready to be available for every VTEX store, you can start the homologation process. You will have to test the endpoints of your connector with the [Payment Provider Test Suite](https://apps.vtex.com/vtex-payment-provider-test-suite/p) app and, if all the tests pass, you will have to [open a ticket to VTEX support team](https://help.vtex.com/en/tutorial/opening-tickets-to-vtex-support--16yOEqpO32UQYygSmMSSAM?locale=en) to publish your connector. You can find more details about the homologation process in the [Payment Provider Protocol](https://help.vtex.com/en/tutorial/payment-provider-protocol--RdsT2spdq80MMwwOeEq0m#3-payment-provider-homologation) and the [Payment Provider Homologation](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-homologation) articles.
