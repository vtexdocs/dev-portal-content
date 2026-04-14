---
title: "Processing DPAN cards in external connectors"
slug: "processing-dpan-cards-in-external-connectors"
excerpt: "Configure your external payment connector to correctly process DPAN card transactions, ensuring secure and compliant payment flows."
hidden: false
createdAt: "2026-04-14T00:00:00.000Z"
---

This guide explains how external connectors integrated with the VTEX [Payment Provider Protocol (PPP)](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-protocol) must handle [DPAN](https://help.vtex.com/docs/tutorials/dpan-and-fpan-understanding-security-in-the-online-tokenized-payment-flow) card transactions via a `POST` request to the connector's route (`https://{providerServiceUrl}/payments`). See the [Create payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments) endpoint documentation for more information.

> ℹ️ External connectors are payment connectors that are not built with the **Payment Provider Framework (PPF)**. If your connector uses PPF, refer to the [PPF-specific documentation](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-framework).

## DPAN fields in the payment payload

VTEX Payments Gateway sends card payment requests through the [Create payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments) endpoint following the standard PPP contract. For DPAN transactions, the `card` object can include additional fields that your connector must support:

- **`cryptogram`:** 3DS cryptogram data. This field is used in DPAN transactions for 3DS authentication and must be forwarded to the acquirer when required.
- **`eci`:** Optional Electronic Commerce Indicator. This field is sent in specific scenarios, such as some Visa DPAN transactions.
- **`paymentOrigin`:** Optional field that identifies the wallet used in the transaction, such as `Apple Pay` or `Google Pay`.

The remaining card fields keep the same structure used in standard card transactions, including `number`, `holder`, and `csc`.


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
        "paymentOrigin": "Apple Pay",
        "eci": null,
        "expiration": {
            "month": "12",
            "year": "2031"
        },
        "document": "",
        "token": null
    }
}
```

## Connector requirements

External connectors must meet the following requirements to process DPAN card transactions:

- **Compatibility with DPAN fields:** The [Create payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments) endpoint must accept DPAN-specific fields such as `cryptogram`, `eci`, and `paymentOrigin` when they are included in the `card` object. The presence of these fields must not cause validation errors, request rejection, or unexpected failures in the connector flow.

- **Secure Proxy support:** If the connector environment isn't PCI DSS compliant, sensitive card data won't be sent in plain text. In these cases, fields such as `holder`, `number`, and `csc` can be `null`, and the connector must use tokenized values such as `holderToken` and `numberToken` through the [Secure Proxy](https://developers.vtex.com/docs/guides/payments-integration-secure-proxy) flow. Sensitive data must not be handled outside a PCI-compliant environment.

- **Forwarding data to the acquirer:** When the acquirer or gateway requires DPAN-specific data, the connector must forward the fields received from VTEX, such as `cryptogram`, `eci`, and `paymentOrigin`, using the format expected by the acquirer integration.

- **Backward compatibility:** The [Create payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments) endpoint must continue to process standard card transactions normally. If DPAN-specific fields aren't present, the connector must keep the existing card flow unchanged.
