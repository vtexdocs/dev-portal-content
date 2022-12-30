---
title: "Payment Provider Protocol applied to payments with POS"
slug: "payments-integration-ppp-with-pos"
hidden: true
createdAt: "2022-09-28T22:39:15.077Z"
updatedAt: "2022-09-28T22:39:15.077Z"
---
VTEX has multiple solutions to deliver a [Unified Commerce](https://help.vtex.com/en/tracks/unified-commerce-strategies--3WGDRRhc3vf1MJb9zGncnv) experience to shoppers, being able to handle orders from both the ecommerce and physical stores. To deal with the physical store experience, VTEX offers the [inStore app](https://help.vtex.com/en/tracks/instore-getting-started-and-setting-up--zav76TFEZlAjnyBVL5tRc), where sellers can serve customers and complete the entire sales process. When finishing a purchase, the customer will have the option to make the payment with a physical card in a payment terminal, also known as a Point of Sale (POS).

For payment partners to integrate their solutions for payments using a POS, there are a series of requirements that must be taken into account. You can check a summary of the requirements in the list below:

- Develop a payment connector using the [Payment Provider Protocol (PPP)](https://help.vtex.com/en/tutorial/payment-provider-protocol--RdsT2spdq80MMwwOeEq0m). There are some details required in the connector to deal with payments on a POS, such as:
  - Include the supported payment methods (credit or debit card) in the [Manifest](https://developers.vtex.com/vtex-rest-api/reference/manifest-1).
  - Use [callbacks](https://help.vtex.com/tutorial/payment-provider-protocol--RdsT2spdq80MMwwOeEq0m#payment-authorization) for asynchronous payments.
  - Work with [Payment Apps](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-payment-app) to identify the POS and wait for its response.
- For testing, have a VTEX store configured with the supported payment methods. This should be provided by VTEX.
- If needed for testing, have a device with the [inStore app installed](https://help.vtex.com/en/tracks/instore-using-the-app--4BYzQIwyOHvnmnCYQgLzdr/2rPSJ8519UCCZo5uEBkqxh).
- Developers might want to create their Payment App to identify the POS. This app will also have to be installed in the store.

## Payment connector pre-requisites

There are some steps needed for the connector to be able to process payments in the physical world, which are described below:

1. Route [GET List Payment Provider Manifest](https://developers.vtex.com/vtex-rest-api/reference/manifest-1) (`/manifest`). The response body of the endpoint must contain the payment methods `Venda Direta Credito` and `Venda Direta Debito`. In case a split of receivables is offered, this must be informed in the `allowsSplit` field for each payment method. Example of response body properly configured:

```diff
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