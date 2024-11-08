---
title: "FAQ - Google Pay: processing information for payment providers and anti-fraud"
slug: "google-pay-processing-information-for-payment-providers-and-anti-fraud"
hidden: false
createdAt: "2022-06-22T00:00:00.000Z"
updatedAt: ""
---
Here are some answers to questions you may have about transactions with Google Pay:

## What are the differences between the payload used for a standard credit card payment and the one used for Google Pay [DPAN](https://help.vtex.com/en/tutorial/dpan-and-fpan-understanding-security-in-the-online-tokenized-payment-flow--3RM7RvhKZ057wja5xVEOqb)?

Besides the original fields for a credit or debit card payment transaction, the Google Pay DPAN transaction has three additional fields:

- `cryptogram`: 3DS cryptogram information (previously called `3DS_criptogram`).
- `eci`: Electronic Commerce Indicator (previously called `ECI_Indicador`). This field is sent only for Visa transactions and indicates the result of the authentication attempt made by the 3DS system.
- `paymentOrigin` (optional): Identifies the type of card used for payment. To enable this field in Google Pay (DPAN) transactions or FPAN transactions and receive the information in the [Create payment endpoint](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments) payload, open a ticket with [VTEX Support](https://help.vtex.com/support).

In the VTEX Admin, go to **Orders > Transactions** to check if a transaction has been made with Google Pay.

![DPAN transaction fields](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Integration-Guides/payments-integration-guide/dpan-transaction-fields-1.png)

> ℹ️ The `paymentOrigin`, `panType`, and `cryptogram` fields aren't sent in standard credit or debit card transactions (without using a digital wallet).

## What are the possible values for the `paymentOrigin` field in the payload?

The `paymentOrigin` field is always sent with the "Google Pay" value. Payment transactions using other payment methods don't have the `paymentOrigin` field in the payload.

## Is the Card Verification Value (CVV) sent in Google Pay transactions?

No. The card CVV is sent in certain FPAN-type transactions. DPAN payment transactions do not require the card CVV number.

> ℹ️ Transactions processed in subscription or recurring operations do not use the card CVV as well.

## How can I simulate a DPAN test transaction?

To run a DPAN test transaction, follow these steps:

1. Add a new card in the Google Pay digital wallet app or via redirection from the bank app (Android).
2. Open the Chrome browser using the same Android device you used to add the card.
3. Simulate buying a product, and on the checkout screen, select the option to pay using Google Pay.

    > ⚠️ Make sure to select the card that displays the actual card image, as it defines the transaction will use DPAN. If you select the card displaying the flag image, the transaction will use the FPAN method.

4. Complete the payment and check the DPAN transaction data in your system.
