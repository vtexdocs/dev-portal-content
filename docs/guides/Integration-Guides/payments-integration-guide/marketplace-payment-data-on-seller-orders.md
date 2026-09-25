---
title: "Marketplace payment data on seller orders"
slug: "marketplace-payment-data-on-seller-orders"
hidden: false
createdAt: "2026-09-10T00:00:00.000Z"
updatedAt: "2026-09-10T00:00:00.000Z"
excerpt: "How native paymentData on marketplace seller orders carries NT 2025.001 fiscal fields without creating a VTEX Gateway transaction on the seller account."
---

When a marketplace processes the customer's payment, the seller order can include native `paymentData` with the method used on the marketplace. Use this object to issue invoices. In Brazil, it carries the fields required by [NT 2025.001](https://developers.vtex.com/updates/release-notes/2025-08-29-orders-api-support-for-nt-2025-001-fields).

> ⚠️ This `paymentData` isn't a payment transaction on the seller’s [VTEX Payment Gateway](https://help.vtex.com/en/tutorial/what-is-a-payment-gateway--2KH9Wdi7F6swOU4amECSOk). Don't use it to authorize, settle, refund, or capture a payment on the seller account.

This behavior applies to VTEX sellers and to external sellers that receive the [Authorize fulfillment](https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-seller-fulfillment#post-/pvt/orders/-sellerOrderId-/fulfill) payload. It doesn't replace [Split Payouts on Payment Provider Protocol](https://developers.vtex.com/docs/guides/split-payouts-on-payment-provider-protocol), which describes split processing on the marketplace Gateway.

## Identifying a marketplace-assumed payment

In the VTEX Admin, open the order and go to **Payment**. The section can show the real method, such as **Credit card** and **Mastercard**. The signal that the marketplace assumed the payment is the **Transaction ID** `PAYMENT-FROM-AFFILIATE`.

The same value is stored as `transactionId` in the order. The date in **Gateway authorization** doesn't mean that the Gateway of the seller account authorized the payment.

Older integrations may still show `paymentSystemName` as *Assumed value by affiliate*. Use `transactionId = "PAYMENT-FROM-AFFILIATE"` as the identifier going forward.

## Reading the payload

Read `paymentData` from the [Get order](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/oms/pvt/orders/-orderId-) endpoint. External sellers can also receive it in [Authorize fulfillment](https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-seller-fulfillment#post-/pvt/orders/-sellerOrderId-/fulfill) after `placeOrder`.

```json
{
  "transactionId": "PAYMENT-FROM-AFFILIATE",
  "payments": [
    {
      "paymentSystem": "21",
      "paymentSystemName": "JCB",
      "value": 100000,
      "installments": 1,
      "referenceValue": 100000,
      "group": "creditCard",
      "connectorResponses": {
        "acquirerCnpj": "01425787000104",
        "authId": "01010202"
      }
    }
  ]
}
```

`connectorResponses` may also include a `Message` that states the value was assumed by the affiliate. Don't treat that text as a Gateway operation result.

## NT 2025.001 fields

Nota Técnica (NT) 2025.001 fields were previously stored in `customData.customApps`. Native `paymentData` maps them as follows:

| NT / `customApps` field | Native `paymentData` field |
| --- | --- |
| `marketplacePaymentMethods` | `group`, `paymentSystem`, and `paymentSystemName` |
| `marketplacePaymentCreditCardBrands` | `paymentSystemName` (card brand, when applicable) |
| `marketplacePaymentAuthorizationCodes` | `connectorResponses.authId` |
| `marketplacePaymentCnpjAcquirers` | `connectorResponses.acquirerCnpj` |

Some connectors still send `customApps` in addition to `paymentData`. Prefer the native fields for new invoice integrations. Not every marketplace connector uses this payload yet.

## Mapping payment systems

When the marketplace method matches a VTEX payment system by name, the order uses that system's catalog `id` (`paymentSystem`) and `groupName` (`group`). Examples:

| Marketplace method (matched by name) | `paymentSystem` | `paymentSystemName` | `group` |
| --- | --- | --- | --- |
| JCB | `"21"` | `JCB` | `creditCard` |
| Débito Itau | `"22"` | `Débito Itau` | `debit` |

If there is no match:

- `paymentSystem` is `"0"`.
- `paymentSystemName` keeps the label sent by the marketplace.
- `group` is promissory.

Marketplace labels aren't standardized. `CARD`, `Credit Card`, and `credit_card` can all arrive for the same method. Unmapped values must not block the order.

## Avoiding Gateway actions

- Don't call [Payments Gateway API](https://developers.vtex.com/docs/api-reference/payments-gateway-api) endpoints such as the Get transaction endpoint on the seller account and expect a transaction only because `paymentData` is present.
- Don't send NT field names (`marketplacePaymentMethods`, `marketplacePaymentCnpjAcquirers`, and similar) inside `connectorResponses`. Use `acquirerCnpj` and `authId`.
- Don't use `tid` or `nsu` in this flow. Use `acquirerCnpj`, `authId`, and, when present, `Message`.

## See also

- [Payments in VTEX marketplaces](https://help.vtex.com/en/docs/tutorials/payments-in-vtex-marketplaces)
- [Fetching marketplace information with the Orders API](https://developers.vtex.com/docs/guides/get-marketplace-data-orders-api)
- [External seller processing payments](https://developers.vtex.com/docs/guides/external-seller-processing-payments)
- [Orders API: support for NT 2025.001 fields](https://developers.vtex.com/updates/release-notes/2025-08-29-orders-api-support-for-nt-2025-001-fields)
