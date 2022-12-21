---
title: "Payment integrations can now be developed for payments on a POS"
slug: "payment-integrations-can-now-be-developed-for-payments-on-a-pos"
type: "added"
createdAt: "2022-09-29T17:48:50.582Z"
hidden: false
---

![Payments](https://img.shields.io/badge/-Payments-blueviolet)

VTEX has solutions for selling at ecommerce and physical stores, providing a [Unified Commerce](https://help.vtex.com/en/tracks/unified-commerce-strategies--3WGDRRhc3vf1MJb9zGncnv) experience to shoppers. This includes the context of payments, where shoppers can pay for the purchase on a payment terminal, also known as a Point of Sale (POS).

We have just updated our documentation to enable payment partners to develop their integrations for payments on a POS, with purchases made through the [inStore](https://help.vtex.com/en/tracks/instore-getting-started-and-setting-up--zav76TFEZlAjnyBVL5tRc). This solution is a specific application of our [Payment Provider Protocol (PPP)](https://help.vtex.com/en/tutorial/payment-provider-protocol--RdsT2spdq80MMwwOeEq0m) to accept physical credit and debit cards as payment methods. There are some requirements for this solution to work, including:

- Develop a payment connector with some details taken into account, such as:
  - Include the supported payment methods (credit or debit card) in the [Manifest](https://developers.vtex.com/vtex-rest-api/reference/manifest-1).
  - Use [callbacks](https://help.vtex.com/tutorial/payment-provider-protocol--RdsT2spdq80MMwwOeEq0m#payment-authorization) for asynchronous payments.
  - Work with [Payment Apps](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-payment-app) to identify the POS and wait for its response.
- For testing, have a VTEX store configured with the supported payment methods. This should be provided by VTEX.
- If needed for testing, have a device with the [inStore app installed](https://help.vtex.com/en/tracks/instore-using-the-app--4BYzQIwyOHvnmnCYQgLzdr/2rPSJ8519UCCZo5uEBkqxh).
- Developers might want to create their Payment App to identify the POS. This app will also have to be installed in the store.

You can check all the details to implement this solution on our [Payment Provider Protocol applied to payments with POS](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-ppp-applied-to-pos) article.
