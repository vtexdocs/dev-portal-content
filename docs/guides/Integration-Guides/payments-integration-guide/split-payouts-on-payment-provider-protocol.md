---
title: "Split payouts on Payment Provider Protocol"
slug: "split-payouts-on-payment-provider-protocol"
excerpt: "Learn how the VTEX Gateway calculates commissions and sends the recipients array to your connector at each stage of the Payment Provider Protocol."
hidden: false
createdAt: "2021-11-09T14:21:42.226Z"
updatedAt: "2026-08-2600:00:00.000Z"
---

Split payouts are a common requirement for payment providers used by marketplaces. They allow a marketplace to process the payment for an order, collect its commission, and pay sellers for their products in a single transaction, which improves operational efficiency when managing payouts at scale.

The VTEX platform allows merchants to register sellers, configure commission percentages for the total order and freight values, and set specific commissions by seller category. For more information, see [Adding a seller](https://help.vtex.com/en/docs/tutorials/adding-a-seller).

This guide describes how the VTEX Gateway calculates the split and what changes in each [Payment Provider Protocol](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-protocol) request when split payouts are active.

## Before you begin

Check the following requirements:

- Your connector must be integrated through the [Payment Provider Protocol](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-protocol).
- The manifest returned by the [Get manifest](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#get-/manifest) endpoint must declare the `allowsSplit` property for each payment method that supports split payouts.
- To support partial refunds in split transactions, the `acceptSplitPartialRefund` parameter must be enabled for your connector. Request this during the [payment provider homologation](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-homologation) process.
- The merchant must have sellers and commission percentages registered in the marketplace, as described in [Adding a seller](https://help.vtex.com/en/docs/tutorials/adding-a-seller).

## Cart scenarios

When an order is placed, the cart falls into one of three scenarios:

| Scenario | Split behavior |
| -------- | -------------- |
| Products only from the marketplace | No split payout, commission calculation, or split payload. The marketplace receives the full order payment value. |
| Products from the marketplace and one or more sellers | Split payout required. |
| Products only from sellers | Split payout required. |

When a split payout is required, the VTEX Gateway is responsible for:

- Calculating the commission per seller of each order.
- Sending the split payload data to the payment processor.
- Processing the complete or partial refund in split operations, when required.

> ⚠️ The VTEX Gateway sends the split payload only if the payment provider supports this scenario.

### Commission calculation example

Consider an order of 199.62 with the following registered commissions: 16% for the marketplace when the product comes from seller X, and 20% for the marketplace when the product comes from seller Y. The cart contains products from seller X, seller Y, and the marketplace itself.

The VTEX Gateway calculates the following breakdown:

| Item | Seller | Item value | Marketplace commission | Amount sent to recipient |
| ---- | ------ | ---------- | ---------------------- | ------------------------ |
| SellerX product | `sellerX` | 87.12 | 13.94 | 73.18 |
| SellerY product | `sellerY` | 42.60 | 8.52 | 34.08 |
| Marketplace product | Marketplace | 69.90 | - | 92.36, that is 69.90 + 13.94 + 8.52 |

The marketplace receives the value of its own products plus the commission collected from both sellers, and each seller receives the value of its products minus the marketplace commission.

## Split timing settings

You can configure the following characteristics of the split process:

- **Automatic settlement time:** The payment processor controls whether the automatic settlement occurs before or after the anti-fraud analysis, through the `delayToAutoSettle` and `delayToAutoSettleAfterAntifraud` fields of the authorization response.
- **Split payload sending time:** Set per payment method through the `allowsSplit` property of each item in the `paymentMethods` array of the manifest.

The `allowsSplit` property accepts the following values:

| Value | Behavior |
| ----- | -------- |
| `onAuthorize` | The VTEX Gateway sends the `recipients` array in the authorization request. |
| `onCapture` | The VTEX Gateway sends the `recipients` array in the settlement request. |
| `disabled` | The VTEX Gateway doesn't send the `recipients` array for this payment method. |

When the processor doesn't specify a value, the default behavior is:

- **Credit card transactions:** The split is sent in the settlement call.
- **Transactions with boleto:** The split is sent in the authorization call.

## The recipients array

The split payout solution adds an array of objects called `recipients` to the Payment Provider Protocol. Each item of this array carries the data your connector needs to split the transaction between the recipients involved, meaning the marketplace and the sellers.

The recipient object contains the following fields:

| Field | Type | Required | Description |
| ----- | ---- | -------- | ----------- |
| `id` | String | Yes | Recipient identifier. |
| `name` | String | Yes | Recipient name. |
| `documentType` | String | Yes | Recipient document type, such as `CNPJ`. |
| `document` | String | Yes | Recipient document number. |
| `role` | String | Yes | Indicates whether the recipient is the `seller` or the `marketplace`. |
| `chargeProcessingFee` | Boolean | No | Indicates whether this recipient is charged for processing fees. |
| `chargebackLiable` | Boolean | No | Indicates whether this recipient is liable for chargebacks. |
| `amount` | Number | Yes | Amount due to this recipient. |
| `comissionAmount` | Number | No | Amount of commission due to the marketplace. Sent only for recipients whose `role` is `seller`. |

> ⚠️ The commission field is spelled `comissionAmount`, with a single `m`, in the [Create payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments) and [Refund payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/refunds) schemas, and `commissionAmount`, with a double `m`, in the [Settle payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/settlements) schema. Handle both spellings in your connector to avoid losing commission data.

## Protocol changes by stage

The following sections describe the changes applied to each stage of the Payment Provider Protocol when split payouts are active.

### Authorization

For transactions where the split on authorization is enabled, the VTEX Gateway sends the `recipients` array in the authorization payload, containing the values to be passed on to each seller and to the marketplace involved in the order.

The following example shows the authorization request for the order described in [Commission calculation example](#commission-calculation-example):

```sh
curl --location --request POST 'https://{providerApiEndpoint}/payments' \
--header 'X-VTEX-API-AppKey: {appKey}' \
--header 'X-VTEX-API-AppToken: {appToken}' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data-raw '{
  "value": 199.62,
  "reference": "22590454",
  "orderId": "v22590454abc",
  "transactionId": "888EC956B26A4F53B3A8F2D420271195",
  "paymentId": "FAD57B4061034026A78545DD3FC6A85D",
  "paymentMethod": "Visa",
  "merchantName": "mystore",
  "card": {
    "holder": "John Doe",
    "number": "4682185088924788",
    "csc": "021",
    "expiration": {
      "month": "06",
      "year": "2029"
    }
  },
  "currency": "BRL",
  "installments": 1,
  "deviceFingerprint": "12ade389087fe",
  "miniCart": {
    "buyer": {
      "id": "3287c060-2e43-4dc7-b730-4b8d2a9bd114",
      "firstName": "Mary",
      "lastName": "Rose",
      "document": "11112222333",
      "documentType": "cpf",
      "email": "mary.rose@example.com",
      "phone": "+5521978888888"
    },
    "shippingAddress": {
      "country": "BRA",
      "street": "Praia de Botafogo",
      "number": "300",
      "complement": "3rd Floor",
      "neighborhood": "Botafogo",
      "postalCode": "22250040",
      "city": "Rio de Janeiro",
      "state": "RJ"
    },
    "billingAddress": {
      "country": "BRA",
      "street": "Brigadeiro Faria Lima Avenue",
      "number": "4440",
      "complement": "10th Floor",
      "neighborhood": "Itaim Bibi",
      "postalCode": "04538132",
      "city": "Rio de Janeiro",
      "state": "RJ"
    },
    "items": [
      {
        "id": "25807",
        "name": "SellerX product",
        "price": 87.12,
        "quantity": 1,
        "discount": 0,
        "categoryId": "1000097",
        "sellerId": "sellerX"
      },
      {
        "id": "29052",
        "name": "Marketplace product",
        "price": 69.90,
        "quantity": 1,
        "discount": 0,
        "categoryId": "1000148",
        "sellerId": "1"
      },
      {
        "id": "48760",
        "name": "SellerY product",
        "price": 42.60,
        "quantity": 1,
        "discount": 0,
        "categoryId": "1000104",
        "sellerId": "sellerY"
      }
    ],
    "shippingValue": 0,
    "taxValue": 0,
    "url": "https://admin.mystore.example.com/admin/checkout/#/orders?q=v22590454abc"
  },
  "callbackUrl": "https://api.example.com/some-path/to-notify/status-changes?an=mystore",
  "returnUrl": "https://mystore.example.com/checkout/order/v22590454abc",
  "recipients": [
    {
      "id": "mystore",
      "name": "Company XPTO",
      "documentType": "CNPJ",
      "document": "01239313000160",
      "role": "marketplace",
      "chargeProcessingFee": true,
      "chargebackLiable": true,
      "amount": 92.36
    },
    {
      "id": "sellerX",
      "name": "Company X",
      "documentType": "CNPJ",
      "document": "88888888000173",
      "role": "seller",
      "chargeProcessingFee": false,
      "chargebackLiable": false,
      "amount": 73.18,
      "comissionAmount": 13.94
    },
    {
      "id": "sellerY",
      "name": "Company Y",
      "documentType": "CNPJ",
      "document": "99999999000126",
      "role": "seller",
      "chargeProcessingFee": false,
      "chargebackLiable": false,
      "amount": 34.08,
      "comissionAmount": 8.52
    }
  ]
}'
```

> ℹ️ For transactions where the split on authorization is disabled, there are no changes in the authorization payload.

### Settlement

The VTEX Gateway sends the list of recipients involved in the transaction in the settlement request when the split is configured for the settlement step of that payment method.

Consider a cart made up of products from seller A, with an order value of 45.00 and a registered commission of 16% for the marketplace. The VTEX Gateway sends 7.2 to the marketplace and 37.8 to seller A:

```sh
curl --location --request POST 'https://{providerApiEndpoint}/payments/{paymentId}/settlements' \
--header 'X-VTEX-API-AppKey: {appKey}' \
--header 'X-VTEX-API-AppToken: {appToken}' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data-raw '{
  "transactionId": "D3AA1FC8372E430E8236649DB5EBD08E",
  "requestId": "2019-02-04T22:53:42-40000",
  "paymentId": "F5C1A4E20D3B4E07B7E871F5B5BC9F91",
  "value": 45.00,
  "authorizationId": "5784589",
  "tid": "5784589",
  "recipients": [
    {
      "id": "mystore",
      "name": "Company XPTO",
      "documentType": "CNPJ",
      "document": "05314972000174",
      "role": "marketplace",
      "chargeProcessingFee": true,
      "chargebackLiable": true,
      "amount": 7.2
    },
    {
      "id": "sellerA",
      "name": "Company ABC",
      "documentType": "CNPJ",
      "document": "24830098000172",
      "role": "seller",
      "chargeProcessingFee": true,
      "chargebackLiable": true,
      "amount": 37.8,
      "commissionAmount": 7.2
    }
  ]
}'
```

> ℹ️ For transactions where the split on settlement is disabled, there are no changes in the settlement payload.

### Complete refund

The complete refund payload has no changes when split payouts are active, because the refund covers the whole transaction:

```sh
curl --location --request POST 'https://{providerApiEndpoint}/payments/{paymentId}/refunds' \
--header 'X-VTEX-API-AppKey: {appKey}' \
--header 'X-VTEX-API-AppToken: {appToken}' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data-raw '{
  "paymentId": "F5C1A4E20D3B4E07B7E871F5B5BC9F91",
  "transactionId": "D3AA1FC8372E430E8236649DB5EBD08E",
  "settleId": "Q5C1A4E20D3B4E07B7E871F5B5BC9F91",
  "value": 45.0,
  "requestId": "LA4E20D3B4E07B7E871F5B5BC9F91"
}'
```

### Partial refund

> ⚠️ To use the split partial refund functionality, request the Partner Support team to enable the `acceptSplitPartialRefund` parameter as `true` during the payment provider homologation process.

The `recipients` array contains the sellers involved in the refund. When the refund applies only to marketplace items, the array contains only the marketplace data.

#### Partial refund of a seller item

Consider a cart made up of items from seller A, with a registered commission of 16% for the marketplace, where 20.00 must be refunded. The VTEX Gateway sends 3.2 for the marketplace and 16.8 for seller A:

```sh
curl --location --request POST 'https://{providerApiEndpoint}/payments/{paymentId}/refunds' \
--header 'X-VTEX-API-AppKey: {appKey}' \
--header 'X-VTEX-API-AppToken: {appToken}' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data-raw '{
  "requestId": "LA4E20D3B4E07B7E871F5B5BC9F91",
  "settleId": "Q5C1A4E20D3B4E07B7E871F5B5BC9F91",
  "paymentId": "F5C1A4E20D3B4E07B7E871F5B5BC9F91",
  "tid": "10022005181543584603",
  "value": 20.00,
  "transactionId": "D3AA1FC8372E430E8236649DB5EBD08E",
  "recipients": [
    {
      "id": "mystore",
      "name": "Company XPTO",
      "documentType": "CNPJ",
      "document": "05314972000174",
      "role": "marketplace",
      "amount": 3.2
    },
    {
      "id": "sellerA",
      "name": "Company ABC",
      "documentType": "CNPJ",
      "document": "24830098000172",
      "role": "seller",
      "amount": 16.8
    }
  ]
}'
```

#### Partial refund of a marketplace item

When 20.00 must be refunded for a marketplace item, the VTEX Gateway sends a single recipient object with the marketplace data:

```sh
curl --location --request POST 'https://{providerApiEndpoint}/payments/{paymentId}/refunds' \
--header 'X-VTEX-API-AppKey: {appKey}' \
--header 'X-VTEX-API-AppToken: {appToken}' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data-raw '{
  "requestId": "LA4E20D3B4E07B7E871F5B5BC9F91",
  "settleId": "Q5C1A4E20D3B4E07B7E871F5B5BC9F91",
  "paymentId": "F5C1A4E20D3B4E07B7E871F5B5BC9F91",
  "tid": "10022005181543584603",
  "value": 20.00,
  "transactionId": "D3AA1FC8372E430E8236649DB5EBD08E",
  "recipients": [
    {
      "id": "mystore",
      "name": "Company XPTO",
      "documentType": "CNPJ",
      "document": "05314972000174",
      "role": "marketplace",
      "amount": 20.00
    }
  ]
}'
```

### Cancellation

The cancellation payload has no changes in this version of the split payouts feature:

```sh
curl --location --request POST 'https://{providerApiEndpoint}/payments/{paymentId}/cancellations' \
--header 'X-VTEX-API-AppKey: {appKey}' \
--header 'X-VTEX-API-AppToken: {appToken}' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data-raw '{
  "paymentId": "F5C1A4E20D3B4E07B7E871F5B5BC9F91",
  "requestId": "D12D9B80972C462980F5067A3A126837"
}'
```

## Connector responses

Split payouts don't change the response bodies your connector must return. Answer each request with the standard Payment Provider Protocol response for that operation.

A successful settlement returns the status code `200 OK`:

```json
{
  "paymentId": "F5C1A4E20D3B4E07B7E871F5B5BC9F91",
  "settleId": "2EA354989E7E4BBC9F9D7B66674C2574",
  "value": 45.00,
  "code": null,
  "message": "Successfully settled",
  "requestId": "DCEAA1FC8372E430E8236649DB5EBD08E"
}
```

A successful refund also returns the status code `200 OK`:

```json
{
  "paymentId": "F5C1A4E20D3B4E07B7E871F5B5BC9F91",
  "refundId": "2EA354989E7E4BBC9F9D7B66674C2574",
  "value": 20.00,
  "code": null,
  "message": "Successfully refunded",
  "requestId": "LA4E20D3B4E07B7E871F5B5BC9F91"
}
```

## Error handling

Report failures through the status code and the `code` and `message` fields of the response, so that the VTEX Gateway can register the result of the operation:

| Status code | When to use it | Response fields |
| ----------- | -------------- | --------------- |
| `500 Internal Server Error` | Your connector or the payment processor couldn't complete the split operation. | Set `settleId` or `refundId` to `null`, `value` to `0`, and describe the failure in `code` and `message`. |
| `501 Not Implemented` | Your connector can't refund the payment automatically and the merchant must refund it outside VTEX. | Set `code` to `refund-manually` and explain the limitation in `message`. |

The following example shows a settlement that failed:

```json
{
  "paymentId": "F5C1A4E20D3B4E07B7E871F5B5BC9F91",
  "settleId": null,
  "value": 0,
  "code": "ERR123",
  "message": "Settlement has failed due to an internal error",
  "requestId": "DCEAA1FC8372E430E8236649DB5EBD08E"
}
```

When validating a split request, consider the following:

- The sum of the `amount` values of all recipients matches the `value` field of the request.
- The `recipients` array is absent when the payment method sets `allowsSplit` as `disabled`, or when the order contains marketplace products only. Treat the absence of this array as a transaction without split.
- Partial refund requests only include the recipients involved in that refund, so don't assume that the array repeats every recipient of the authorization.

## Learn more

- [Payment Provider Protocol](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-protocol)
- [Payment provider homologation](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-homologation)
- [Split payment](https://help.vtex.com/en/docs/tutorials/split-payment)
- [Adding a seller](https://help.vtex.com/en/docs/tutorials/adding-a-seller)
