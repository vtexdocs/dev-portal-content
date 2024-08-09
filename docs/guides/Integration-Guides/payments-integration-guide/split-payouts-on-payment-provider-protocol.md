---
title: "Split Payouts on Payment Provider Protocol"
slug: "split-payouts-on-payment-provider-protocol"
hidden: false
createdAt: "2021-11-09T14:21:42.226Z"
updatedAt: "2021-11-09T19:35:35.998Z"
---
Split payouts are a common requirement for payment providers used by marketplaces, since it allows marketplaces to not only process the payment for an order, but also collect their commission and pay sellers for their products. This leads to improved operational efficiency when managing payouts for a large marketplace.

The VTEX platform allows the merchant to register sellers, configure commission percentages (total order and freight values), and specific commissions by seller category. Check on [Adding a Seller](https://help.vtex.com/tutorial/configurando-seller--tutorials_392).

## Cart Scenarios

When an order is placed, one of three scenarios are present in the cart:

1. Products only from the Marketplace.
2. Products from the Marketplace, and one or more sellers.
3. Products only from seller(s).

### Marketplace Products only

As the order contains products only from the Marketplace, there is no split of payment, calculation of commissioning, or split payload to be sent. The Marketplace will receive the full order payment value.

### Marketplace and Sellers Products only

When an order contains products from the Marketplace and sellers (or only from sellers), a split payout is required.
In this scenario, the VTEX gateway is responsible for:

* Calculate commissioning per seller of each order.
* Send split payload data to the payment processor.
* Process the complete or partial refund in split operations, if required.

> ⚠️ The split payload is sent only if the payment provider supports this scenario.

An illustrative example is shown below to explain how a **calculation breakdown** for split is performed:

1. The registered commission is:
   a. 16% for the marketplace when buying the product from seller X.
   b. 20% for the marketplace when buying products from seller Y.
2. The cart is made up of products from sellerX, sellerY, and the Marketplace itself.
3. An Order with the value of 199.62 is registered. See below:

```json
"items": [
      {
        "id": "25807",
        "name": "marketplace product",
        "sellerId": "markeplace",
        "value": 69.90,
        "comission": 0
      },
      {
        "id": "29052",
        "name": "SellerX product",
        "sellerId": "sellerX",
        "value": 87.12,
        "comission": 13.94
      },
      {
        "id": "48760",
        "name": "SellerY product",
        "sellerId": "sellerY",
        "value": 42.60,
        "comission": 8.52
      }
]
```

4. The following containers will be sent with these values:
   a. 92.36 for the marketplace.
   b. 73.18 for seller X.
   c. 34.08 for seller Y.

**Calculation Breakdown**
[block:parameters]
{
  "data": {
    "h-0": "ID",
    "h-1": "Item Value",
    "h-2": "Marketplace Comission",
    "h-3": "Recipient",
    "0-0": "**SellerX**",
    "1-0": "**SellerY**",
    "2-0": "**Marketplace**",
    "0-1": "87.12",
    "1-1": "42.60",
    "2-1": "69.90",
    "0-2": "13.94",
    "1-2": "8.52",
    "2-2": "-",
    "0-3": "73.18",
    "1-3": "34.08",
    "2-3": "(69.90+13.94+8.52) = 92.36"
  },
  "cols": 4,
  "rows": 3
}
[/block]

## Split Time Settings

It is also possible to configure the following characteristics of the split process:

* **Automatic Capture Time**: The payment processor has the permission to control if the automatic capture will occur before or after approval of anti-fraud (setting the fields as `delayToAutoSettle` or `delayToAutoSettleAfterAntifraud`).
* **Split Payload Sending Time**: This moment can be set according to each method of payment associated with the transaction. For processors within the PPP (Payment Provider Protocol), it can be done through setting the field on the manifest as `onAuthorize`, `onCapture` or `disabled`.

  If not specified by the processor, the default behavior is:

  * **Credit card transaction**: The sending of the split is in the capture call.
  * **Transaction with boleto**: The sending of the split is in the authorization call.

## Split Payout Solution for Payment Provider Protocol

Our Split Payout solution consists of adding an array of objects in the Payment Provider Protocol that we call **recipients**.

Each item of this array informs the necessary data so that the provider can perform the split between the recipients involved in that transaction (marketplace/sellers). The following fields are part of the recipient’s object:
[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "`id`",
    "0-1": "string",
    "0-2": "Recipient identifier",
    "1-0": "`name`",
    "1-1": "string",
    "1-2": "Recipient name",
    "2-0": "`documentType`",
    "2-1": "string",
    "2-2": "Recipient document type",
    "3-0": "`document`",
    "3-1": "string",
    "3-2": "Recipient document number",
    "4-0": "`role`",
    "4-1": "string",
    "4-2": "Indicates if the recipient is the seller or the marketplace",
    "5-0": "`chargeProcessingFee`",
    "5-1": "boolean",
    "5-2": "Indicates whether or not this recipient is charged for processing fees",
    "6-0": "`chargebackLiable`",
    "6-1": "boolean",
    "6-2": "Indicates whether or not this recipient is liable to chargebacks",
    "7-0": "`amount`",
    "7-1": "float",
    "7-2": "Amount due to this recipient",
    "8-0": "`comissionAmount`",
    "8-1": "float",
    "8-2": "Amount received by the Marketplace"
  },
  "cols": 3,
  "rows": 9
}
[/block]

## Payment Protocol modifications

In this section, we will describe modifications applied to our payment protocol at each stage (e.g., authorization, capture, etc.) when the split payout is active.

### Authorization Stage

For transactions where the split in _authorization_ is enabled, we send the _recipients_ in the authorization payload. The _“recipient’s”_ object array contains data on the values to be passed on to each seller and the Marketplace involved in the order.

See below an example of the authorization request:

```json
curl --location --request POST 'https://{{providerApiEndpoint}}/payments' \\
--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\
--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\
--header 'Content-Type: application/json' \\
--header 'Accept: application/json' \\
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
      "complement": "10tth Floor",
      "neighborhood": "Itaim Bibi",
      "postalCode": "04538132",
      "city": "Rio de Janeiro",
      "state": "RJ"
    },
    "items": [
      {
        "id": "25807",
        "name": "SellerX product",
        "price": 71.2,
        "quantity": 1,
        "discount": 0,
        "categoryId": "1000097",
        "sellerId": "sellerX"
      },
      {
        "id": "29052",
        "name": "marketplace product",
        "price": 69.9,
        "quantity": 1,
        "discount": 0,
        "categoryId": "1000148",
        "sellerId": "1"
      },
      {
        "id": "48760",
        "name": "SellerY product",
        "price": 19.2,
        "quantity": 1,
        "discount": 0,
        "categoryId": "1000104",
        "sellerId": "SellerY"
      }
    ],
    "shippingValue": 39.32,
    "taxValue": 0,
    "url": "<https://admin.mystore.example.com/admin/checkout/#/orders?q=v22590454abc>"
  },
  "callbackUrl": "<https://api.example.com/some-path/to-notify/status-changes?an=mystore>",
  "returnUrl": "<https://mystore.example.com/checkout/order/v22590454abc>",
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
      "commissionAmount": 13.94
    },
    {
      "id": "sellerY",
      "name": "Company Y",
      "documentType": "CNPJ",
      "document": "99.999.999/0001-26",
      "role": "seller",
      "chargeProcessingFee": false,
      "chargebackLiable": false,
      "amount": 34.08,
      "commissionAmount": 8.52
    }
  ]
}'

```

> ℹ️ For transactions where the split in _authorization_ is disabled, there are no changes in the normal authorization payload.

### Capture Stage

The list of _recipients_ involved in the transaction will be sent in this stage when the split is configured for the capture step (according to the payment method).

Split example:

1. The registered commission is 16% for the Marketplace when buying the product from sellerA.
2. The cart is made up of products from sellerA.
3. An order with the value of 45.00 is registered.
4. The following containers will be sent with these values:
   a. 7.2 for the Marketplace.
   b. 37.8 for sellerA.

> ℹ️ For transactions where the split in _authorization_ is disabled, there are no changes in the normal catch payload.

See below the capture request for this split example:

```json
curl --location --request POST 'https://{{providerApiEndpoint}}/payments/{{paymentId}}/settlements' \\
--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\
--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\
--header 'Content-Type: application/json' \\
--header 'Accept: application/json' \\
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

### Complete Refund Stage

> ℹ️ There is no change in the normal complete refund payload.

See below an example of the complete refund request:

```json
curl --location --request POST 'https://{{providerApiEndpoint}}/payments/{{paymentId}}/refunds' \\
--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\
--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\
--header 'Content-Type: application/json' \\
--header 'Accept: application/json' \\
--data-raw '{
    "paymentId": "F5C1A4E20D3B4E07B7E871F5B5BC9F91",
    "transactionId": "D3AA1FC8372E430E8236649DB5EBD08E",
    "settleId": "Q5C1A4E20D3B4E07B7E871F5B5BC9F91",
    "value": 45.0,
    "requestId": "LA4E20D3B4E07B7E871F5B5BC9F91"
}'
```

### Partial Refund Stage

> ⚠️ To allow the use of the split partial refund functionality, you must request the Partner Support team to enable the `acceptSplitPartialRefund` parameter as `true` during the payment provider homologation process.

The _“recipient’s”_ object array will contain the sellers involved in the chargeback. If the chargeback is only applicable for Marketplace items, the _“recipient’s”_ object array will be sent containing only the Marketplace data.

Split example of a partial refund of a seller item:

1. Sending the array of recipient objects with the Marketplace value to be refunded and the seller value to be refunded.
2. The registered commission is 16% for the Marketplace when buying the product from sellerA.
3. The cart was made up of items from sellerA.
4. The value to be refunded from sellerA item is 20.00.
5. The following containers will be sent with these values:
   a. 3.2 for the Marketplace.
   b. 16.8 for sellerA.

See below the partial refund request for this split example:

```json
curl --location --request POST 'https://{{providerApiEndpoint}}/payments/{{paymentId}}/refunds' \\
--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\
--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\
--header 'Content-Type: application/json' \\
--header 'Accept: application/json' \\
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

Split example of a partial refund of a Marketplace item:

1. Sending the array of _recipient_ objects with the Marketplace value to be refunded.
2. The value to be refunded from the Marketplace item is 20.00.
3. A _recipient_ object with a value of 20.00 will be sent to the Marketplace.

See below the partial refund request for this split example:

```json
curl --location --request POST 'https://{{providerApiEndpoint}}/payments/{{paymentId}}/refunds' \\
--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\
--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\
--header 'Content-Type: application/json' \\
--header 'Accept: application/json' \\
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

### Cancellation Stage

> ℹ️ In this version of the Split Payouts, there is no change in the normal Cancellation payload.

See below an example of the cancellation request:

```json
curl --location --request POST 'https://{{providerBaseUrl}}/payments/{{paymentId}}/cancellations' \\
--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\
--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\
--header 'Content-Type: application/json' \\
--header 'Accept: application/json' \\
--data-raw '{
    "paymentId": "F5C1A4E20D3B4E07B7E871F5B5BC9F91",
    "requestId": "D12D9B80972C462980F5067A3A126837"
}'
```

For more information about payment splits on VTEX, see [Split Payment](https://help.vtex.com/en/tutorial/split-de-pagamento--6k5JidhYRUxileNolY2VLx?&utm_source=autocomplete#).
