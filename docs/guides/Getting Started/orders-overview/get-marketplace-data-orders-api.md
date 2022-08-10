---
title: "Fetching marketplace information with the Orders API"
slug: "get-marketplace-data-orders-api"
hidden: false
createdAt: "2021-03-26T15:48:23.320Z"
updatedAt: "2021-10-01T21:55:54.778Z"
---
The information contained in ecommerce invoices may vary according to business laws in each country. It is possible, for example, that you are required to include payment method information in case a sale is made through an intermediator.

VTEX stores this data during checkout and makes it available to sellers integrated with different types of marketplaces.

It is possible to see who the marketplace is by checking the order object with the [Get order API request](https://developers.vtex.com/vtex-developer-docs/reference/orders#getorder), in the `affiliateId` field, like in the example below.

```json
{
  "emailTracked": "a27499cad31f42b7a771ae34f57c8358@ct.vtex.com.br",
  "approvedBy": null,
  "cancelledBy": null,
  "cancelReason": null,
  "orderId": "v5195004lux-01",
  "sequence": "502556",
  "marketplaceOrderId": "880102018018-01",
  "marketplaceServicesEndpoint": "http://oms.vtexinternal.com.br/api/oms?an=luxstore",
  "sellerOrderId": "00-v5195004lux-01",
  "origin": "Fulfillment",
  "affiliateId": "ABC",
  "salesChannel": "1",
  "merchantName": null,
  "status": "handling",
  "statusDescription": "Preparando Entrega",
  "value": 1160,
  "creationDate": "2019-01-28T20:09:43.8999580+00:00",
  "lastChange": "2019-02-06T20:46:11.7010747+00:00",
…
```
[block:callout]
{
  "type": "warning",
  "body": "In case of sellers using the [Multilevel Omnichannel Inventory](https://help.vtex.com/en/tutorial/multilevel-omnichannel-inventory--7M1xyCZWUyCB7PcjNtOyw4#) feature, the `affiliateId` field identifies the marketplace in the level directly above it. This means that if a seller on the third level receives a fulfillment order made in a marketplace in the first level, the order’s `affiliateId` will refer to the second level marketplace."
}
[/block]
Payment method information can be accessed in two different ways depending on the type of marketplace.


## VTEX marketplaces

VTEX clients who are sellers of other VTEX clients can access intermediator payment method data in the order object, in the `userPaymentInfo.paymentMethod` array, within the `invoiceData` object. See the example below.

```json
...
"invoiceData": {
    "userPaymentInfo": {
        "paymentMethod": [
            "creditCardPaymentGroup"
        ]
    }
}
...
```

The `paymentMethod` array includes strings which follow this pattern `{payment-group-name}PaymentGroup`. There are dozens of possible values, depending on the payment groups used by the marketplace. These are some examples:

*   `"creditCardPaymentGroup"`
*   `"debitCardPaymentGroup"`
*   `"instantPaymentPaymentGroup"`
*   `"promissoryPaymentGroup"`
*   `"PayPalPlusPaymentGroup"`
*   `"OneBuyPaymentGroup"`
*   `"virtualDebitEloPaymentGroup"`
*   `"foodCardPaymentGroup"`
*   `"giftCardPaymentGroup"`
*   `"debitPaymentGroup"`
*   `"PaymentHubPaymentGroup"`
*   `"PagosNetPaymentGroup"`
*   `"bankInvoicePaymentGroup"`
*   `"PagosWebPaymentGroup"`
*   `"cardPromissoryPaymentGroup"`
*   `"SamsungPayPaymentGroup"`
[block:callout]
{
  "type": "info",
  "body": "For external sellers connected to VTEX marketplaces this data is also sent in the `invoiceData` object, in the format described above."
}
[/block]
## Natively integrated external marketplaces

VTEX provides native connectors that allow our clients to connect to external marketplaces. We store intermediator data and make it available to sellers integrating with:
*   B2W
*   Via Varejo
*   Magazine Luiza
*   Mercado Libre
*   Amazon
*   Carrefour
*   Netshoes
*   Centauro
*   Dafiti
*   Wish

In this scenario, marketplace payment method information is stored in the `customData` object in the [`orderForm`](https://developers.vtex.com/vtex-developer-docs/reference/checkout-api-overview) data structure.

### Fetching external marketplace payment method data

This is an example of what you might find in the `customData` object of the order object when using the Get order request:

```json
{
  ...
  "customData": {
    "customApps": [
      {
        "id": "CN-Viavarejo-Integration",
        "fields": {
          "marketplacePaymentMethod": "credit_card"
        }
      }
    ]
  }
  ...
}
```
[block:callout]
{
  "type": "info",
  "body": "The Checkout API allows integrators to create customizable fields in the shopping cart through the `customData` object. Their middleware can create extra fields in the `orderForm` data structure and set the value of each of these fields when placing an order, so that this additional information can be retrieved when fetching order details with the Orders API."
}
[/block]
For orders made in marketplaces with native VTEX connectors, payment method will be available in the `marketplacePaymentMethod` field. These are the possible values for this field:
*   `"credit_card"`
*   `"debit_card"`
*   `"bank_slip"`
*   `"bank_deposit"`
*   `"pix"`
*   `"digital_wallet"`
*   `"gift_card"`
*   `"virtual_credit"`
*   `"payment_method_not_informed"`