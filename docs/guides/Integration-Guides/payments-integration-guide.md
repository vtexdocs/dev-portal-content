---
title: "Payments"
slug: "payments-integration-guide"
hidden: false
createdAt: "2020-10-27T00:24:27.500Z"
updatedAt: "2022-06-23T17:26:11.955Z"
---
Communication between systems and services of stores, partners and platform is carried out through integration protocols. At VTEX, we use the Payment Provider Protocol (PPP), a protocol created to assist companies that carry out financial transaction operations.

Before continuing, make sure you are familiar with some terms that are frequently used in articles in this guide:

* **Acquirer:** a company that specializes in payment processing. For more information, access [What is an acquirer?](https://help.vtex.com/en/tutorial/what-is-an-acquirer--7N1oRTG8dGmOiIugC0cs4E).
* **Merchant or Client:** an individual or business that holds its ecommerce or physical stores operations in the VTEX platform.
* **Customer:** an individual or business that purchases a product or service from a VTEX client.
* **Provider:** agent that will process the merchant's payments. It can be a payment system, payment provider, or a gateway.
* **Partner:**  agent responsible to carry out the integration between the provider and the VTEX platform.
* **VTEX Payment Gateway:** VTEX system responsible for processing payments. The gateway communicates with the provider through the Payment Provider Protocol (PPP).
* **Payment Service Provider (PSP):**  financial entity that is authorized to process financial transactions between merchants, acquiring banks, and card networks. It is a fast and cost-effective way to accept payments without needing to open a company in another country or having to create a merchant account.
* **Payload:** set of data sent in JSON format through a request body of an endpoint.
* **Connector:** provider affiliation that acts as a bridge between the provider and the VTEX checkout.
* **Oauth:** authorization protocol made for Application Programming Interfaces (APIs). It allows the provider system to access the customer data to process a payment transaction.

The articles listed below present the characteristics and mode of operation of our payment architecture, providing implementation information to allow you to integrate your payment service into VTEX or use the payment solutions already available.

## Structure of this guide

| Article                                                                                                                                                                                | Description                                                                                                                       |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| [Integrating a new payment provider on VTEX](https://developers.vtex.com/docs/guides/integrating-a-new-payment-provider-on-vtex)                                                          | A step-by-step guide to integrating your payment provider into VTEX.                                                              |
| [Payment Provider Protocol](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-protocol)                                                                       | Overview of our integration protocol, the Payment Provider Protocol (PPP).                                                        |
| [Payment Provider Protocol for Point of Sale (POS) - VTEX Sales App](https://developers.vtex.com/docs/guides/payments-integration-ppp-applied-to-pos)                                                  | PPP information for use in physical stores.                                                                                       |
| [Implementing a Payment Provider](https://developers.vtex.com/docs/guides/payments-integration-implementing-a-payment-provider)                                                           | How to develop your middleware to communicate with the PPP.                                                                       |
| [Payment Provider Framework](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-framework)                                                                     | Overview of our alternative method of developing payment connectors through VTEX IO.                                              |
| [Purchase Flows](https://developers.vtex.com/docs/guides/payments-integration-purchase-flows)                                                                                             | Information on the types of payment flows available on VTEX.                                                                      |
| [Payment App](https://developers.vtex.com/docs/guides/payments-integration-payment-app)                                                                                                   | Overview of the Payment App and how to implement it in your store.                                                                |
| [Payment Methods](https://developers.vtex.com/docs/guides/payments-integration-payment-methods)                                                                                           | Overview of payment methods accepted by VTEX.                                                                                     |
| [Payment Provider Homologation](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-homologation)                                                               | How to carry out the tests to request the approval of your payment connector.                                                     |
| [Anti-fraud Provider Protocol](https://developers.vtex.com/docs/guides/how-the-integration-protocol-between-vtex-and-antifraud-companies-works)                                           | Overview of our anti-fraud integration protocol, the Anti-fraud Provider Protocol.                                                |
| [PCI - DSS Compliance](https://developers.vtex.com/docs/guides/payments-integration-pci-dss-compliance)                                                                                   | Information about the PCI-DSS certification and when it is required.                                                              |
| [Secure Proxy](https://developers.vtex.com/docs/guides/payments-integration-secure-proxy)                                                                                                 | Information about the VTEX solution for transferring sensitive data in an environment without the use of PCI - Dss certification. |
| [Split Payouts on Payment Provider Protocol](https://developers.vtex.com/docs/guides/split-payouts-on-payment-provider-protocol)                                                          | Overview of our Split Payouts process on the PPP.                                                                                 |
| [Layout Development Guide for payment methods in Smart Checkout VTEX](https://developers.vtex.com/docs/guides/layout-development-guide-for-payment-methods-in-smart-checkout-vtex)        | How to develop a custom layout for your payment method.                                                                           |
| [Custom Auto Capture Feature](https://developers.vtex.com/docs/guides/custom-auto-capture-feature)                                                                                        | Information from the VTEX solution created to define a custom delay interval for automatically capturing payments.                |
| [Pix: Instant Payments in Brazil](https://developers.vtex.com/docs/guides/payments-integration-pix-instant-payments-in-brazil)                                                            | How to implement the PIX payment method in your store.                                                                            |
| [PSE Payment Method](https://developers.vtex.com/docs/guides/pse-payment-method)                                                                                                          | How to implement the PSE payment method in your store.                                                                            |
| [Installing Affirm Payment App](https://developers.vtex.com/docs/guides/installing-affirm-payment-app-1)                                                                                  | How to implement the Affirm Payment App payment method in your store.                                                             |
| [Google Pay: processing information for payment providers and anti-fraud](https://developers.vtex.com/docs/guides/google-pay-processing-information-for-payment-providers-and-anti-fraud) | How the Google Pay payment method is identified in transactions.                                                                  |

> ✔️ To integrate a payment solution in VTEX you must fill out the registration form to join our [Partner Program](https://vtex.com/us-en/partners) to get access to your own VTEX account. If you are already a client or partner, you can [open a support ticket](https://help.vtex.com/en/tutorial/opening-tickets-to-vtex-support--16yOEqpO32UQYygSmMSSAM) if you have any questions.
