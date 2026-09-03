---
title: "Google Pay: Processing information for payment providers and anti-fraud"
slug: "google-pay-processing-information-for-payment-providers-and-anti-fraud"
excerpt: "Answers to common questions from payment providers and anti-fraud providers about how VTEX processes Google Pay transactions, including the additional card fields sent in the payment payload."
hidden: false
createdAt: "2022-06-22T00:00:00.000Z"
updatedAt: "2026-09-03T00:00:00.000Z"
---

Google Pay is a digital wallet that allows customers to pay with a card saved to their Google account or provisioned to their mobile device. When a customer pays with Google Pay, VTEX sends the transaction to your connector through the [Create payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments) endpoint, including card fields that standard card transactions don't have.

This guide answers common questions from payment providers and anti-fraud providers about these transactions.

## What is the difference between DPAN and FPAN?

Google Pay transactions use a tokenized card number instead of the number printed on the card, which is the Primary Account Number (PAN). There are two types of tokenized number:

- **DPAN (Device Primary Account Number):** Tokenized version of the PAN linked to a specific device of the customer, such as a smartphone, smartwatch, or tablet.
- **FPAN (Funding Primary Account Number):** Identifies the account charged for the transaction. Wallets use it when the customer can choose between more than one payment method, such as different cards or bank accounts.

For more information, see [DPAN and FPAN: Understanding security in the online tokenized payment flow](https://help.vtex.com/docs/tutorials/dpan-and-fpan-understanding-security-in-the-online-tokenized-payment-flow).

## What are the differences between a standard card payload and a Google Pay DPAN payload?

Besides the standard fields of a card transaction, the `card` object of a Google Pay DPAN transaction can include the following fields:

| Field | Description |
| ----- | ----------- |
| `cryptogram` | 3-D Secure (3DS) cryptogram data, available only for transactions with DPAN cards. Forward this value to the acquirer when the acquirer requires it. This field was previously called `3DS_criptogram`. |
| `eci` | Electronic Commerce Indicator (ECI), which indicates the result of the authentication attempt made by the 3DS system. VTEX sends it in specific scenarios, such as some Visa DPAN transactions. This field was previously called `ECI_Indicador`. |
| `paymentOrigin` | Wallet used in the payment, such as `Google Pay`. |

> ⚠️ VTEX sends `cryptogram`, `eci`, and `paymentOrigin` only when these fields are enabled for your account. To enable them, [open a ticket to VTEX support](https://help.vtex.com/en/docs/tutorials/opening-tickets-to-vtex-support).

The following example shows the `card` object of a Create payment request for a Google Pay DPAN transaction. In this example, the card data is tokenized because the connector environment isn't PCI DSS compliant:

```json
{
  "merchantName": "mystore",
  "card": {
    "holder": null,
    "number": null,
    "csc": null,
    "holderToken": "#vtex#token#fd10ce5#holder#",
    "bin": "489725",
    "numberToken": "#vtex#token#fd40ce5#number#",
    "numberLength": 16,
    "cryptogram": "/gAAAAwAZWJqaw4AAAAAgIRgE4A=",
    "paymentOrigin": "Google Pay",
    "eci": null,
    "expiration": {
      "month": "12",
      "year": "2031"
    },
    "document": ""
  }
}
```

The example shows only the fields related to the wallet and the card. For the complete request body, see the [Create payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments) endpoint.

Standard credit and debit card transactions made without a digital wallet don't include these fields, so your connector must keep processing payloads that omit them. For the complete list of requirements, see [Processing DPAN cards in external connectors](https://developers.vtex.com/docs/guides/processing-dpan-cards-in-external-connectors).

## What are the possible values for the `paymentOrigin` field in the payload?

The `paymentOrigin` field identifies the wallet used in the payment. In Google Pay transactions, VTEX sends the value `Google Pay`. Transactions made with other wallets carry their own values, such as `Apple Pay`, and transactions made without a wallet don't include this field.

## How can I check whether a transaction used Google Pay?

In the VTEX Admin, go to **Orders > Transactions**, or type **Transactions** in the search bar at the top of the page, and open the transaction you want to check. Transactions made with a digital wallet display the following fields:

| Field | Description |
| ----- | ----------- |
| `paymentOrigin` | Wallet used in the payment, such as `Google Pay`. |
| `panType` | Type of tokenized card number used in the transaction, either `DPAN` or `FPAN`. |
| `cryptogram` | 3DS cryptogram data of the transaction. |

![Transaction details in the VTEX Admin, displaying the paymentOrigin field with the value Google Pay, the panType field with the value DPAN, and the cryptogram field.](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Integration-Guides/payments-integration-guide/dpan-transaction-fields-1.png)

> ℹ️ The VTEX Admin displays `panType` in the transaction details, but the Create payment request that VTEX sends to your connector doesn't include this field. To identify the wallet in the payload, use `paymentOrigin`.

## Is the Card Verification Value (CVV) sent in Google Pay transactions?

No. Transactions with DPAN cards don't require the CVV, because the device tokenization identifies the cardholder. VTEX sends the CVV in certain transactions with FPAN cards.

> ℹ️ Subscription and recurring transactions also don't use the CVV.

## How can I simulate a DPAN test transaction?

A DPAN is linked to a specific device, so you need a mobile device with the card provisioned in Google Pay. On desktop browsers, Google Pay uses a card saved to the Google account, which results in an FPAN transaction.

To run a DPAN test transaction, follow these instructions:

1. On an Android device, add a card to the Google Pay app, or add it through the redirect from the app of your bank.
2. On the same Android device, open the Chrome browser and access your store.
3. Add a product to the cart and, at checkout, select Google Pay as the payment method.
4. Select the card displayed with the card image.
5. Complete the payment.
6. In the VTEX Admin, go to **Orders > Transactions** and confirm that the transaction details display `panType` as `DPAN`.

> ⚠️ In step 4, select the card displayed with the card image, which results in a DPAN transaction. Selecting the card displayed with the logo of the card network results in an FPAN transaction.

## Learn more

- [Processing DPAN cards in external connectors](https://developers.vtex.com/docs/guides/processing-dpan-cards-in-external-connectors)
- [Create payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments)
- [DPAN and FPAN: Understanding security in the online tokenized payment flow](https://help.vtex.com/docs/tutorials/dpan-and-fpan-understanding-security-in-the-online-tokenized-payment-flow)
