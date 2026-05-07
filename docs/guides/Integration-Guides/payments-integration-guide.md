---
title: "Payments"
slug: "payments-integration-guide"
hidden: false
createdAt: "2020-10-27T00:24:27.500Z"
updatedAt: "2026-04-17T00:00:00.000Z"
---
Communication between systems and services of stores, partners and platform is carried out through integration protocols. At VTEX, we use the Payment Provider Protocol (PPP), a protocol created to assist companies that carry out financial transaction operations.

Before continuing, make sure you are familiar with some terms that are frequently used in articles in this :

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

> ℹ️ To integrate a payment solution in VTEX, you must join our [Partner Program](https://vtex.com/us-en/partners) to get access to your own VTEX account. If you are already a client or partner, you can [open a support ticket](https://help.vtex.com/en/tutorial/opening-tickets-to-vtex-support--16yOEqpO32UQYygSmMSSAM) if you have any questions.

> ℹ️ If you are looking for endpoint-level technical details, such as request and response schemas and protocol operations, refer to the Payments content in the [API Reference](https://developers.vtex.com/docs/api-reference).

## Payments documentation structure

### Payment Methods and Purchase Flows

| Article                                                                                      | Description                                                                                                                                          |
| -------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Payment Methods](https://developers.vtex.com/docs/guides/payments-integration-payment-methods) | Overview of payment method families accepted by VTEX: credit and debit cards, digital wallets, bank transfers, Pix, boleto, and alternative methods. |
| [Purchase Flows](https://developers.vtex.com/docs/guides/payments-integration-purchase-flows)   | The three payment flow models available on VTEX: Transparent, Redirect, and Payment App.                                                             |

### Anti-fraud

| Article                                                                                                                                                                                | Description                                                                                       |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| [Anti-fraud Provider Protocol](https://developers.vtex.com/docs/guides/how-the-integration-protocol-between-vtex-and-antifraud-companies-works)                                           | Overview of the anti-fraud integration protocol, including endpoints, testing, and certification. |
| [Implementing a pre-analysis anti-fraud flow for debit card transactions](https://developers.vtex.com/docs/guides/implementing-a-pre-analysis-antifraud-flow-for-debit-card-transactions) | How to configure pre-authorization risk analysis for debit card transactions.                     |
| [Cardholder document configuration](https://developers.vtex.com/docs/guides/cardholder-document-configuration)                                                                            | How to configure the cardholder document field for anti-fraud provider integration.               |

### Customer Credit

| Article                                                                                                       | Description                                                |
| ------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| [Managing a Customer Credit account](https://developers.vtex.com/docs/guides/managing-a-customer-credit-account) | How to create and manage customer credit accounts via API. |
| [Managing a Customer Credit invoice](https://developers.vtex.com/docs/guides/managing-a-customer-credit-invoice) | How to create and manage credit invoices via API.          |

### Gift Cards

| Article                                                                                                               | Description                                                                         |
| --------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| [Gift Card system architecture](https://developers.vtex.com/docs/guides/gift-card-integration-guide-system-architecture) | Overview of the Gift Card Hub, Provider Protocol, and native provider architecture. |
| [Managing VTEX gift cards](https://developers.vtex.com/docs/guides/managing-vtex-gift-cards)                             | How to create, update, and manage native VTEX gift cards via API.                   |

### Operations & Configuration

| Article                                                                                                                           | Description                                                                        |
| --------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| [Custom Auto Capture Feature](https://developers.vtex.com/docs/guides/custom-auto-capture-feature)                                   | How to define a custom delay interval for automatic payment capture (settlement).  |
| [Setting up the type of interest rate](https://developers.vtex.com/docs/guides/setting-up-the-type-of-interest-rate)                 | How to configure interest rate types for installment payments via the Gateway API. |
| [Metadata information in payment transactions](https://developers.vtex.com/docs/guides/metadata-information-in-payment-transactions) | How to send and retrieve custom metadata in payment transactions.                  |

### Payment App & Checkout UI

| Article                                                                                                                                                                         | Description                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| [Payment App](https://developers.vtex.com/docs/guides/payments-integration-payment-app)                                                                                            | How to implement a Payment App for custom payment UX during checkout.     |
| [Layout Development Guide for payment methods in Smart Checkout VTEX](https://developers.vtex.com/docs/guides/layout-development-guide-for-payment-methods-in-smart-checkout-vtex) | How to develop a custom layout for your payment method in Smart Checkout. |

### Payment Methods & Wallets

| Article                                                                                                                                                                                | Description                                                                                   |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| [Pix: Instant Payments in Brazil](https://developers.vtex.com/docs/guides/payments-integration-pix-instant-payments-in-brazil)                                                            | How to implement Pix as a payment method for Brazilian stores.                                |
| [PSE Payment Method](https://developers.vtex.com/docs/guides/pse-payment-method)                                                                                                          | How to implement the PSE bank transfer method for Colombian stores.                           |
| [Google Pay: processing information for payment providers and anti-fraud](https://developers.vtex.com/docs/guides/google-pay-processing-information-for-payment-providers-and-anti-fraud) | How Google Pay transactions are identified and processed by providers and anti-fraud systems. |
| [Setting up Merchant ID in Apple Pay](https://developers.vtex.com/docs/guides/setting-up-merchant-id-in-apple-pay)                                                                        | How to configure your Apple Developer Merchant ID for Apple Pay integration.                  |

### Payment Provider Protocol

| Article                                                                                                                       | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| [Payment Provider Protocol](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-protocol)              | Core concepts and overview of the PPP.                                                                      |
| [Integrating a new payment provider on VTEX](https://developers.vtex.com/docs/guides/integrating-a-new-payment-provider-on-vtex) | End-to-end step-by-step guide for integrating a new payment provider.                                       |
| [Implementing a Payment Provider](https://developers.vtex.com/docs/guides/payments-integration-implementing-a-payment-provider)  | How to develop your middleware to communicate with the PPP endpoints.                                       |
| [Payment Provider Framework](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-framework)            | Alternative method for developing payment connectors using VTEX IO.                                         |
| [PPP Versioning](https://developers.vtex.com/docs/guides/ppp-versioning)                                                         | How connector versioning works and how to upgrade to a new PPP version.                                     |
| [PPP for Point of Sale (POS) - VTEX Sales App](https://developers.vtex.com/docs/guides/payments-integration-ppp-applied-to-pos)  | How to apply the PPP for payments on physical points of sale with VTEX Sales App.                           |
| [Split Payouts on Payment Provider Protocol](https://developers.vtex.com/docs/guides/split-payouts-on-payment-provider-protocol) | How marketplace payment splits work within the PPP, including commission, seller payouts, and refund flows. |

### Security

| Article                                                                                              | Description                                                                                  |
| ---------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| [PCI - DSS Compliance](https://developers.vtex.com/docs/guides/payments-integration-pci-dss-compliance) | PCI DSS certification requirements and when they apply to your integration.                  |
| [Secure Proxy](https://developers.vtex.com/docs/guides/payments-integration-secure-proxy)               | VTEX's solution for securely transferring sensitive card data without PCI DSS certification. |

### Testing & Homologation

| Article                                                                                                                  | Description                                                                |
| ------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------- |
| [Payment Provider Homologation](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-homologation) | How to run the test suite and request approval for your payment connector. |

### Tokenization & Card Vault

| Article                                                                                                       | Description                                              |
| ------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| [Implementing payments tokenization](https://developers.vtex.com/docs/guides/implementing-payments-tokenization) | How to implement tokenization in your payment connector. |
| [Managing tokenized cards](https://developers.vtex.com/docs/guides/managing-tokenized-cards)                     | How to query, import, and manage tokenized card data.    |
