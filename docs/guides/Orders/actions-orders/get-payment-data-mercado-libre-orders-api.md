---
title: "Fetching payment details from a Mercado Libre order with Orders API"
slug: "get-payment-data-mercado-libre-orders-api"
hidden: false
createdAt: "2020-10-28T23:22:25.245Z"
updatedAt: "2020-11-25T01:11:12.441Z"
---
When [setting up order integration](https://developers.vtex.com/docs/guides/erp-integration-set-up-order-integration ) for your ERP middleware or similar integration, you may need additional payment details from orders placed in external marketplaces. 

This article explains where our [native Mercado Libre connector](https://help.vtex.com/pt/tracks/mercado-libre-integration-set-up--2YfvI3Jxe0CGIKoWIGQEIq/51oWBHvVxSs8eAwLQhSbSd) stores this information in the orderForm data structure and how to fetch this data for your integration.

## Understanding customData

Checkout API allows integrators to [create customizable fields in the shopping cart](/docs/guides/creating-customizable-fields-in-the-cart-with-checkout-api) through the `customData` object. Their middleware can create extra fields in the orderForm and set the value of each of these fields when placing an order, so that this additional information can be retrieved when fetching order details with Orders API.

## Custom fields created by Mercado Libre connector

Our native Mercado Libre connector leverages this functionality to add custom fields to orders, as seen in the code snippet below. Note: the actual orders data structure is much larger - we are omitting everything else and highlighting only `customData` in this example.
[block:code]
{
  "codes": [
    {
      "code": "{\n ...\n    \"customData\": {\n        \"customApps\": [\n            {\n                \"fields\": {\n                    \"orderIdMarketplace\": \"4113970696\",\n                    \"paymentIdMarketplace\": \"12040787637\",\n                    \"authorization_code\": \"1234567\",\n                    \"currency_id\": \"BRL\",\n                    \"first_six_digits\": \"0\",\n                    \"installments\": \"1\",\n                    \"last_four_digits\": \"0\",\n                    \"payment_method_id\": \"hipercard\",\n                    \"payment_type\": \"credit_card\"\n                },\n                \"id\": \"marketplace-integration\",\n                \"major\": 1\n            }\n        ]\n    },\n ...\n}",
      "language": "json",
      "name": "Example - customData for Mercado Libre connector"
    }
  ]
}
[/block]
The table below lists the `customData` fields created by the Mercado Libre connector.
[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Description",
    "0-0": "`orderIdMarketplace`",
    "1-0": "`paymentIdMarketplace`",
    "2-0": "`authorization_code`",
    "3-0": "`currency_id`",
    "4-0": "`first_six_digits`",
    "5-0": "`installments`",
    "6-0": "`last_four_digits`",
    "7-0": "`payment_method_id`",
    "8-0": "`payment_type`",
    "0-1": "Order identifier in Mercado Libre",
    "1-1": "Payment identifiers in Mercado Libre",
    "2-1": "Authorization code for Mercado Libre payments",
    "3-1": "[ISO 4127](https://en.wikipedia.org/wiki/ISO_4217) currency code",
    "4-1": "[Issuer Identification Number (IIN)](https://en.wikipedia.org/wiki/Payment_card_number#Issuer_identification_number_(IIN)) of credit cards used in Mercado Libre payments",
    "5-1": "Number of installments for Mercado Libre order",
    "6-1": "Last four digits of credit cards used in Mercado Libre payments",
    "7-1": "Payment method identifier in Mercado Libre",
    "8-1": "Payment type identifier in Mercado Libre"
  },
  "cols": 2,
  "rows": 9
}
[/block]

[block:callout]
{
  "type": "warning",
  "title": "Some fields may be missing from Mercado Libre",
  "body": "The default value returned is `0` if the payment method does not offer any data for `authorization_code`, `first_six_digits`, `last_four_digits`"
}
[/block]
## Multiple payments

If there is an order that was payed for with more than one payment method, the data returned by [Mercado Libre's Orders API](https://developers.mercadolivre.com.br/en_us/manage-sales#How-can-I-know-if-there-are-two-payments) is split by vertical bars (`|`) in the following fields:

- `paymentIdMarketplace`
- `authorization_code`
- `first_six_digits`
- `last_four_digits`
- `payment_method_id`
- `payment_type`


[block:code]
{
  "codes": [
    {
      "code": "{\n ...\n    \"customData\": {\n        \"customApps\": [\n            {\n                \"fields\": {\n                    \"orderIdMarketplace\": \"893431118\",\n                    \"paymentIdMarketplace\": \"885920310 | 885920410\",\n                    \"authorization_code\": \"008877 | 211118\",\n                    \"currency_id\": \"BRL\",\n                    \"first_six_digits\": \"402360 | 512106\",\n                    \"installments\": \"1\",\n                    \"last_four_digits\": \"1001 | 2002\",\n                    \"payment_method_id\": \"visa | master\",\n                    \"payment_type\": \"credit_card | credit_card\"\n                },\n                \"id\": \"marketplace-integration\",\n                \"major\": 1\n            }\n        ]\n    },\n ...\n}",
      "language": "json",
      "name": "Example - customData for Multiple payments"
    }
  ]
}
[/block]