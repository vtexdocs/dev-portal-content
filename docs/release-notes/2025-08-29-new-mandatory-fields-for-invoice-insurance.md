---
title: "Orders API: support for NT 2025.001 fields"
slug: "2025-08-29-orders-api-support-for-nt-2025-001-fields"
hidden: false
type: "added"
createdAt: "2025-08-29T00:00:00.219Z"
updatedAt: ""
excerpt: "The Orders API now supports the NT 2025.001 fields, ensuring tax compliance and preventing invoice rejections. These updates introduce new fields within `customApps`, with variations depending on the marketplace. The changes apply only to stores in Brazil."
---

>ℹ️ The following changes apply only to stores in Brazil.

To ensure tax compliance for all orders and avoid rejections during invoice issuance, the Orders API now includes new fields in the `customApps` object.
The new fields are listed below:

- `marketplacePaymentMethods`: Payment methods used.
- `marketplacePaymentCnpjAcquirers`: CNPJ of the acquirer.
- `marketplacePaymentAuthorizationCodes`: Authorization code.
- `marketplacePaymentCreditCardBrands`: Credit card brand. This field will be empty for other payment methods.

The new fields can be retrieved using the [Get order](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/oms/pvt/orders/-orderId-) endpoint, as in the example below:

```shell
"customData": {
  {
    "customApps": [
      {
        "id": "integration-marketplace-[marketplace name]",
        "major": 1,
        "fields": {
          "marketplacePaymentCnpjAcquirers": "11.222.333/0001-44",
          "marketplacePaymentAuthorizationCodes": "XYZ",
          "marketplacePaymentCreditCardBrands": "",
          "marketplacePaymentMethods": "Pix"
        }
      }
    ]
  }
}
```

>ℹ️ Values may vary between marketplaces, as they are passed as is (without standardization) from the marketplace. For example: `Credit Cards`, `Credit`, `Credit Card`, `credit-card`).

## Dafiti marketplace

For the [Dafiti](https://help.vtex.com/pt/tracks/configurar-integracao-da-dafiti--4wF4RBx9ygEkimW6SsKw8i/5lAIj7OCqizD5EisLJvatx) marketplace, the fields are in singular form:

- `marketplacePaymentMethod`
- `marketplacePaymentCnpjAcquirer`
- `marketplacePaymentAuthorizationCode`

The field `marketplacePaymentCreditCardBrands` is not available, as this information is already included in the `marketplacePaymentMethod` field.

For more information, read the [New mandatory fields for invoice issuance announcement]().
