---
title: "Payments"
slug: "payments-overview"
excerpt: "Understand how VTEX Payments connects merchants to providers and supports payment provider, anti-fraud, and gift card integrations."
hidden: false
createdAt: "2022-04-28T21:34:56.911Z"
updatedAt: "2026-05-12T00:00:00.000Z"
---
> ℹ️ **Help us improve our documentation!** Tell us about your experience with this article by completing [this form](https://forms.gle/fQoELRA1yfKDqmAb8).

VTEX connects merchants to payment providers through a gateway-based architecture. The [VTEX Payment Gateway](https://help.vtex.com/tutorial/what-is-a-payment-gateway--2KH9Wdi7F6swOU4amECSOk) communicates with external providers via connectors built on standardized protocols, supporting credit and debit cards, digital wallets, [Pix](https://help.vtex.com/pt/docs/tutorials/pix-faq), [boleto](https://help.vtex.com/docs/tutorials/registered-ticket-flow), gift cards, customer credit, and other payment methods.

For the complete payments documentation — including implementation guides, payment methods, tokenization, testing, security, and configuration — see the [Payments category](https://developers.vtex.com/docs/guides/payments-integration-guide).

## How VTEX Payments works

When a customer places an order, the checkout sends the payment request to the VTEX Payment Gateway. The gateway routes the request to the appropriate connector, which communicates with the external provider to authorize, settle, or refund the transaction.

The key components are:

- **Payment Gateway:** VTEX system that processes all payment transactions and routes them to the correct provider.
- **Connector:** Provider affiliation that bridges the gateway and the external provider. Connectors are built using integration protocols.
- **Provider:** External service (PSP, acquirer, anti-fraud, or gift card provider) that processes the transaction.

There are three [purchase flows](https://developers.vtex.com/docs/guides/payments-integration-purchase-flows) available: **Transparent** (the shopper stays on the VTEX checkout), **Redirect** (the shopper is sent to the provider's page), and **Payment App** (custom payment UX built with VTEX IO).

## Integration paths

VTEX supports three types of payment-related integrations. Each uses a dedicated protocol that defines the endpoints your connector must implement.

### Payment provider

Payment providers build connectors using the [Payment Provider Protocol (PPP)](https://help.vtex.com/docs/tutorials/payment-provider-protocol). The protocol defines how the provider communicates with the VTEX Gateway for authorization, settlement, refund, and cancellation operations. Providers can build their connector either as an external middleware or using the [Payment Provider Framework](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-framework) on VTEX IO.

After development, connectors must pass a [homologation process](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-homologation) and meet [PCI DSS compliance](https://developers.vtex.com/docs/guides/payments-integration-pci-dss-compliance) requirements (when applicable), or use the [Secure Proxy](https://developers.vtex.com/docs/guides/payments-integration-secure-proxy) as an alternative before going live.

See the following resources to implement and publish your connector:

- [Implementing a Payment Provider](https://developers.vtex.com/docs/guides/payments-integration-implementing-a-payment-provider)
- [Integrating a new payment provider on VTEX](https://developers.vtex.com/docs/guides/integrating-a-new-payment-provider-on-vtex)
- [Payment Provider Protocol API](https://developers.vtex.com/docs/api-reference/payment-provider-protocol)

### Anti-fraud provider

Anti-fraud providers integrate risk analysis into the payment flow through the [Anti-fraud Provider Protocol](https://developers.vtex.com/docs/guides/how-the-integration-protocol-between-vtex-and-antifraud-companies-works). This protocol defines endpoints for sending transaction data, receiving risk assessments, and updating analysis status.

To get started with your anti-fraud integration:

- [Pre-analysis anti-fraud flow for debit card transactions](https://developers.vtex.com/docs/guides/implementing-a-pre-analysis-antifraud-flow-for-debit-card-transactions)
- [Anti-fraud Provider Protocol API](https://developers.vtex.com/docs/api-reference/antifraud-provider-protocol)

### Gift card provider

On VTEX, gift cards are a payment method processed at Checkout. External providers can integrate their gift card services using the Giftcard Provider Protocol and connect with the [Giftcard Hub](https://developers.vtex.com/docs/api-reference/giftcard-hub-api), which aggregates multiple providers. VTEX also provides a [native gift card system](https://developers.vtex.com/docs/api-reference/giftcard-api).

Related articles:

- [Gift Card integration guide](https://developers.vtex.com/docs/guides/gift-card-integration-guide)
- [Managing VTEX gift cards](https://developers.vtex.com/docs/guides/managing-vtex-gift-cards)
- [Giftcard Provider Protocol API](https://developers.vtex.com/docs/api-reference/giftcard-provider-protocol)

## Key APIs

Use these APIs to manage payment transactions, connectors, and related services:

| API | Description |
| --- | --- |
| [Payment Provider Protocol API](https://developers.vtex.com/docs/api-reference/payment-provider-protocol) | Endpoints for payment connectors (authorization, settlement, refund, cancellation). |
| [Anti-fraud Provider Protocol API](https://developers.vtex.com/docs/api-reference/antifraud-provider-protocol) | Endpoints for anti-fraud provider integration. |
| [Payments Gateway API](https://developers.vtex.com/docs/api-reference/payments-gateway-api) | Endpoints for managing transactions, payment rules, and gateway affiliations. |
| [GiftCard API](https://developers.vtex.com/docs/api-reference/giftcard-api) | Endpoints for managing native VTEX gift cards. |
| [GiftCard Hub API](https://developers.vtex.com/docs/api-reference/giftcard-hub-api) | Endpoints for aggregating multiple gift card providers. |
| [Giftcard Provider Protocol API](https://developers.vtex.com/docs/api-reference/giftcard-provider-protocol) | Endpoints for external gift card provider integration. |
| [Customer Credit API](https://developers.vtex.com/docs/api-reference/customer-credit-api) | Endpoints for managing customer credit accounts and invoices. |
| [Card Token Vault API](https://developers.vtex.com/docs/api-reference/card-token-vault-api) | Endpoints for card tokenization and vault operations. |

## Next steps

- [Payments category](https://developers.vtex.com/docs/guides/payments-integration-guide) — complete documentation covering implementation, payment methods, tokenization, testing, security, and operations.
