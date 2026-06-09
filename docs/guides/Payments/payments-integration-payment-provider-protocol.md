---
title: "Payment Provider Protocol"
slug: "payments-integration-payment-provider-protocol"
hidden: false
createdAt: "2020-10-27T17:56:02.690Z"
updatedAt: "2026-05-13T00:00:00.000Z"
excerpt: "The integration standard that defines how payment providers connect to the VTEX Gateway."
---

The Payment Provider Protocol (PPP) is the integration standard that defines how payment providers connect to the VTEX Gateway. Through the PPP, providers can authorize, settle, refund, and cancel transactions on the VTEX platform.

There are two ways to build a payment connector:

- **External middleware:** Develop your own backend service that implements the PPP endpoints.
- **VTEX IO (Payment Provider Framework):** Use a VTEX IO boilerplate that provides the endpoint structure out of the box.

> ℹ️ Before starting, you need a [partnership agreement for financial services](https://www.vtex.com/en-us/partners) and access to a VTEX environment. Providers processing credit, debit, or co-branded cards must also meet [PCI DSS compliance](https://developers.vtex.com/docs/guides/payments-integration-pci-dss-compliance) requirements or use [Secure Proxy](https://developers.vtex.com/docs/guides/payments-integration-secure-proxy).

## In this section

| Article                                                                                                                          | Description                                                                         |
| -------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| [Integrating a new payment provider on VTEX](https://developers.vtex.com/docs/guides/integrating-a-new-payment-provider-on-vtex) | End-to-end overview of the steps to integrate a payment provider.   |
| [Implementing a Payment Provider](https://developers.vtex.com/docs/guides/payments-integration-implementing-a-payment-provider)  | How to develop the middleware that implements the PPP endpoints.    |
| [Payment Provider Framework](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-framework)            | How to build a connector on VTEX IO using the PPP boilerplate.      |
| [PPP Versioning](https://developers.vtex.com/docs/guides/ppp-versioning)                                                         | Protocol version history and migration notes.                       |
| [PPP applied to POS](https://developers.vtex.com/docs/guides/payments-integration-ppp-applied-to-pos)                            | How to use the PPP for physical store payments with VTEX Sales App. |
| [Split Payouts on Payment Provider Protocol](https://developers.vtex.com/docs/guides/split-payouts-on-payment-provider-protocol) | How to configure split payouts for marketplace transactions.        |

Learn more about the protocol flow in the [Help Center tutorial](https://help.vtex.com/docs/tutorials/payment-provider-protocol) and the [Payment Provider Protocol API](https://developers.vtex.com/docs/api-reference/payment-provider-protocol).
