---
title: "Payment methods"
slug: "payments-integration-payment-methods"
hidden: false
createdAt: "2020-11-12T18:46:20.596Z"
updatedAt: "2026-08-11T00:00:00.000Z"
excerpt: "Learn about the payment method families supported by VTEX and the identifiers used to declare them in the Payment Provider Protocol."
---

Payment methods are the different ways a customer can pay for a product or a service. VTEX supports the following types of payment methods:

- Credit cards
- Debit cards
- Digital wallets
- Cash
- Custom payments
  - Notes payable
  - Private label
  - Co-branded
- Regional payments
  - Instant payments (Pix/Brazil)
  - Bank invoice (boleto bancário/Brazil)
  - PSE (Colombia)

## Checking which payment methods are available

The list above covers the payment method families supported by the platform. It is not an exhaustive list of what a specific store can offer. Availability depends on the store's country, the payment providers connected to the account, and the account configuration.

To find out which payment methods an account can offer:

- Check the [list of payment providers by country](https://help.vtex.com/en/docs/tutorials/list-of-payment-providers-by-country) to see which providers operate in a specific market and which methods they support.
- Review the payment providers configured in the Payments module of the VTEX Admin. For more information, see [Register payment and anti-fraud providers](https://help.vtex.com/en/docs/tutorials/registering-gateway-affiliations).

Payment methods also vary from country to country. Before integrating with VTEX, check whether the methods your system processes are compatible with the platform.

## Declaring payment methods in your integration

A payment provider declares the payment methods it supports through the `paymentMethods` array returned by the [List Payment Provider Manifest](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#get-/manifest) endpoint. Each entry contains a `name`, which identifies the payment method, and an `allowsSplit` value, which declares whether that provider supports payment split for the method.

Use the following identifiers in the `name` field:

| Payment method | `name` value |
| --- | --- |
| Visa | `Visa` |
| Mastercard | `Mastercard` |
| American Express | `American Express` |
| Pix | `Pix` |
| Bank invoice (boleto bancário) | `BankInvoice` |
| Co-branded | `Cobranded` |
| Private label | `Privatelabels` |
| Notes payable (Promissory) | `Promissories` |

> ⚠️ For custom payments, use only the supported method types (`Cobranded`, `Privatelabels`, or `Promissories`) in the `name` field. Do not use the commercial name of the custom payment, such as "Colombian Bank Promissory".

Cash is not declared through the Payment Provider Protocol. It is configured directly in the VTEX Sales App.

For the full request and response schemas, see the [Payment Provider Protocol](https://developers.vtex.com/docs/api-reference/payment-provider-protocol) API reference. To learn how each method behaves during authorization, settlement, and cancellation, see [Purchase Flows](https://developers.vtex.com/docs/guides/payments-integration-purchase-flows).

## Credit cards

Financial institutions can offer a credit limit to their account holders. Customers use that credit through a credit card to make a purchase and pay for it later.

Credit cards operate through card networks, which manage credit card operations. Mastercard, Visa, American Express, and Diners are examples of card networks. For more information, see [Credit card payment flow](https://help.vtex.com/en/docs/tracks/credit-card-payment-flow).

Credit cards can also support payment in installments, depending on the payment condition configured in the store. In the Payment Provider Protocol, the number of installments is sent in the `installments` field of the Create Payment request.

## Debit cards

A debit card is offered by a financial institution to its account holders. Purchases are paid right away, with the amount deducted directly from the customer's bank account.

Like credit cards, debit cards also operate through card networks.

For configuration examples, see [Setting up Visa Debit](https://help.vtex.com/en/docs/tutorials/how-to-set-up-visa-debit) and [Setting up debit direct sale](https://help.vtex.com/en/docs/tracks/setting-up-debit-direct-sale) in the VTEX Sales App.

## Cash

Cash payments can be enabled in the VTEX Sales App. After you configure and enable this payment method, cash payments can be received at a brick-and-mortar store or on delivery. For more information, see [Configuring cash payments through VTEX Sales App](https://help.vtex.com/en/docs/tracks/configuring-cash-payments-through-vtex-sales-app).

## Digital wallets

A digital wallet, also called an e-wallet, stores the customer's payment credentials so they can pay without entering card data at checkout. Apple Pay, Google Pay, and Samsung Pay are examples of digital wallets supported by VTEX.

For an overview of how digital wallets work, see [What is an e-wallet](https://help.vtex.com/en/docs/tutorials/what-is-an-e-wallet) and the [Digital wallet (e-wallet)](https://help.vtex.com/en/docs/tracks/digital-wallet-e-wallet) track.

If you are building a connector that handles wallet transactions, see [Google Pay: processing information for payment providers and anti-fraud](https://developers.vtex.com/docs/guides/google-pay-processing-information-for-payment-providers-and-anti-fraud) and [Setting up merchant ID in Apple Pay](https://developers.vtex.com/docs/guides/setting-up-merchant-id-in-apple-pay).

## Custom payments

Custom payments are payment methods that do not follow standard market patterns. Their behavior is specific to each scenario where they apply.

VTEX supports three custom payment types: Notes payable, Private label, and Co-branded.

### Notes payable

The seller must manually approve each payment registered in the platform. After approval, the transaction proceeds normally. Notes payable payments are mostly used to facilitate cash payments.

For configuration steps, see [Setting up payments with Notes payable](https://help.vtex.com/docs/tutorials/setting-up-payments-with-notes-payable).

### Private label

A private label is a credit card created exclusively for a store, using the store's own brand.

For configuration steps, see [Setting up private label payments](https://help.vtex.com/en/docs/tutorials/setting-up-private-label-payments).

### Co-branded

A co-branded card is also created exclusively for a store. Unlike a private label, it results from a partnership between a card network, such as Mastercard or Visa, and the store's brand.

For configuration steps, see [Setting up payments with store card (co-branded)](https://help.vtex.com/en/docs/tutorials/setting-up-payments-with-store-card-cobranded).

## Regional payments

### Instant payments (Pix/Brazil)

Pix is the instant payments ecosystem implementation led by the Central Bank of Brazil (BCB) to enable online money transfers with reduced costs, increased safety, and 24/7 availability. Transfers occur directly from the payer’s account to the payee’s account, without the need for intermediaries, resulting in lower transaction costs. For more information, see [Pix: Instant Payments in Brazil](https://developers.vtex.com/docs/guides/payments-integration-pix-instant-payments-in-brazil).

### Bank invoice (boleto bancário/Brazil)

The boleto bancário is a popular payment method in Brazil. It is an official voucher that a customer can pay in cash at more than 200,000 locations, such as banks, post offices, and supermarkets, or electronically through internet banking. For more information, see [Bank invoice payment flow](https://help.vtex.com/en/docs/tutorials/boleto-bancario-registrado-fluxo-basico-de-um-pagamento).

Although bank invoices are easy to pay, the payment can take up to two business days to be processed.

To configure this payment method in a store, see [How to configure a bank slip](https://help.vtex.com/en/docs/tutorials/how-to-configure-a-bank-slip).

> ℹ️ In the Payment Provider Protocol manifest, this payment method is identified as `BankInvoice`.

### PSE (Colombia)

PSE (Pagos Seguros en Línea) is an online payment method in Colombia that lets customers pay directly from their bank account. For integration details, see [PSE payment method](https://developers.vtex.com/docs/guides/pse-payment-method). To configure it in a store, see [Setting up payments with PSE](https://help.vtex.com/en/docs/tutorials/setting-up-payments-with-pse).

> ℹ️ Every payment method has an associated payment condition. For more information, see [Configuring a payment condition](https://help.vtex.com/en/docs/tracks/configuring-a-payment-condition).
