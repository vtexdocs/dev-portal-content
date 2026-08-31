---
title: "Cardholder document configuration"
slug: "cardholder-document-configuration"
excerpt: "Learn how anti-fraud providers use the cardholderDocument field in the manifest to define whether the checkout requests an identification document from the cardholder."
hidden: false
createdAt: "2022-04-19T17:14:08.281Z"
updatedAt: "2026-08-26T00:00:00.000Z"
---

When a customer pays with a credit or debit card, the store may request an identification document from the cardholder, such as a CPF or a Social Security Number, in addition to the card number, cardholder name, expiration date, and CVV. Some payment providers use this document to authorize the transaction, and some anti-fraud providers use it to analyze the risk of fraud.

This document is not always necessary. Some anti-fraud providers analyze transactions without it, the legislation of some countries discourages collecting this data, and some customers don't have a document that proves they own the card.

To give anti-fraud providers and merchants control over this behavior, the [Anti-fraud Provider Protocol](https://developers.vtex.com/docs/guides/how-the-integration-protocol-between-vtex-and-antifraud-companies-works) offers the `cardholderDocument` field in the provider manifest. This field defines whether the checkout requests the cardholder document, and whether merchants can change that behavior.

Configuring this field involves two roles:

- **Anti-fraud providers** declare `cardholderDocument` in the connector manifest, as described in this guide.
- **Merchants** choose whether to display the field at checkout, when the provider allows it. See [Cardholder document configuration](https://developers.vtex.com/docs/guides/how-the-integration-protocol-between-vtex-and-antifraud-companies-works#cardholder-document-configuration).

## Before you begin

Your connector must be integrated through the [Anti-fraud Provider Protocol](https://developers.vtex.com/docs/guides/how-the-integration-protocol-between-vtex-and-antifraud-companies-works), so that you can edit the manifest returned by the [List anti-fraud provider manifest](https://developers.vtex.com/docs/api-reference/antifraud-provider-protocol#get-/manifest) endpoint.

> ℹ️ When the manifest doesn't declare `cardholderDocument`, VTEX requires the cardholder document in card transactions. To keep this behavior, you don't need to follow this guide.

## Declaring the cardholder document field

To define how the checkout handles the cardholder document, follow these instructions:

1. In the connector manifest, add the `cardholderDocument` field with one of the values described in [Accepted values](#accepted-values).
2. [Open a ticket to VTEX support](https://help.vtex.com/en/docs/tutorials/opening-tickets-to-vtex-support) requesting the update of your connector on VTEX.

The following example declares a manifest that requires the cardholder document:

```json
{
  "cardholderDocument": "required",
  "customFields": [
    {
      "name": "AnalysisMode",
      "type": "text"
    }
  ]
}
```

> ⚠️ The manifest requires the `customFields` array, so keep it in the response even when your connector has no custom fields to declare.

### Accepted values

| Value | Behavior at checkout and in [My Cards](https://help.vtex.com/en/docs/tutorials/how-my-account-works#credit-cards) | Merchants can change it |
| ----- | ---------------------------------------------------------------------------------------------------------------- | ----------------------- |
| `required` | The cardholder document field is displayed, and the customer must fill it in to complete the order. | No |
| `optional` | The cardholder document field is displayed according to the merchant configuration. Your connector uses the document in the analysis when the customer provides it. | Yes |
| `unused` | The cardholder document field is not displayed, and your connector analyzes transactions without this document. | No |

Only the `optional` value gives merchants the **Cardholder document field** option in the VTEX Admin. With `required` and `unused`, the behavior you declare in the manifest applies to every store that uses your connector.

## Next steps

After VTEX updates your connector, validate the result:

1. Confirm that the [List anti-fraud provider manifest](https://developers.vtex.com/docs/api-reference/antifraud-provider-protocol#get-/manifest) endpoint returns the expected `cardholderDocument` value.
2. Place a test order in a store that uses your connector and confirm that the checkout requests the cardholder document as expected. Changes may take up to 10 minutes to appear at the checkout.
3. If you declared `optional`, ask the merchant to set the **Cardholder document field** option, as described in [Cardholder document configuration](https://developers.vtex.com/docs/guides/how-the-integration-protocol-between-vtex-and-antifraud-companies-works#cardholder-document-configuration).

## Learn more

- [Anti-fraud Provider Protocol](https://developers.vtex.com/docs/guides/how-the-integration-protocol-between-vtex-and-antifraud-companies-works)
- [Anti-fraud Provider Protocol API reference](https://developers.vtex.com/docs/api-reference/antifraud-provider-protocol)
- [Configuring the anti-fraud](https://help.vtex.com/en/docs/tutorials/how-to-configure-the-anti-fraud)
