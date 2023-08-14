---
title: "Adding payment information to the cart"
slug: "adding-payment-information-to-the-cart"
hidden: true
createdAt: "2022-11-28t18:26:30.450z"
updatedAt: "2022-11-28t18:32:23.152z"
---

The shopping cart gathers information on the products the customer chooses while browsing a store, such as prices, shipping costs, payment methods, delivery methods, etc. This data may include item prices, shipping value, payment, and delivery methods, among others.

This guide will describe how to add payment information to the shopping cart via API.

>⚠️ The payment information attached to the shopping cart does not determine the final order payment method. However, it allows the platform to update any relevant information that might be affected by the payment method.

## Getting shopping cart information

The first step is to get the `orderFormId` of the shopping cart to which you want to add the payment information. For more information, read the [Getting cart information by ID](https://developers.vtex.com/vtex-rest-api/docs/get-cart-information-by-id) guide.

## Adding payment information to the shopping cart

To add payment information to the shopping cart, you need to use the [Add payment data](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/attachments/paymentData) endpoint. In this request, you must send the `orderFormId` through the URL address, as in the example below:

`https://{accountName}.{environment.com.br}/api/checkout/pub/orderForm/ede846222cd44046ba6c638442c3505a/attachments/paymentData`

Additionally, you must send the request body containing the following payment information:

- `paymentSystem`: Payment system ID.
- `paymentSystemName`: Payment system name.
- `group`: Payment system group.
- `installments`: Number of installments.
- `installmentsInterestRate`: Installment interest rate.
- `installmentsValue`: Amount of each installment.
- `value`: Total payment amount.
- `referenceValue`: Base value used to calculate total order amount with interest.
- `hasDefaultBillingAddress`: Indicates whether the billing address for this order is the default address.

See a request body example below:

```json
{
     "payments": [
          {
              "paymentSysytem": 1,
              "paymentSystemName": "Boleto Bancário",
              "group": "bankInvoicePaymentGroup",
              "installments": 3,
              "installmentsInterestRate": 0,
              "installmentsValue": 100,
              "value": 300,
              "referenceValue": 300,
              "hasDefaultBillingAddress": false
          }
     ]
}
```
If you are using a gift card as a payment method, the request body can be similar to this:

```json
{
     "giftCards": [
          {
            "redemptionCode": "480030010012333619",
            "provider": "CartaoPresente",
            "value": 15289,
            "balance": 100000,
            "name": null,
            "caption": null,
            "id": "480030010012333619",
            "inUse": true,
            "isSpecialCard": false,
            "groupName": null
        }
     ]
}
```

 After sending the request, the endpoint will return the response body containing the payment information in the shopping cart, as in the example below:

```json
...
"paymentData": {
        "updateStatus": "updated",
        "installmentOptions": [
            {
                "paymentSystem": "1",
                "bin": null,
                "paymentName":  "Boleto Bancário",
                "paymentGroupName": "bankInvoicePaymentGroup",
                "value": 300,
                "installments": [
                    {
                        "count": 3,
                        "hasInterestRate": false,
                        "interestRate": 0,
                        "value": 300,
                        "total": 300,
                        "sellerMerchantInstallments": [
                            {
                                "id": "COSMETICS2",
                                "count": 3,
                                "hasInterestRate": false,
                                "interestRate": 0,
                                "value": 300,
                                "total": 300
                            }
                        ]
                    }
                ]
            }
...
```

> ℹ️️ For more information on the meaning of each field available in the shopping cart, see the [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) overview.

## Error codes

The following errors may appear as a message in the response body.

### 400 - Bad Request

- **Message error example (code ORD002)**: `"Invalid order form"`. The `orderFormId` information is not valid.

```json
{
    "fields": {},
    "error": {
        "code": "ORD002",
        "message": "Invalid order form",
        "exception": null
    },
    "operationId": "5d9f54e6-7db4-46d6-bca9-deeb278b8b98"
}
```

- **Message error example (code ORD020)**: `"Invalid payment"`. The `referenceValue` information has not been sent. [block:code]

```json
{
    "fields": {},
    "error": {
        "code": "ORD020",
        "message": "Invalid payment",
        "exception": null
    },
    "operationId": "9d14e7af-a63d-4c26-8974-bad734b758da"
}
```

### 404 - Not Found

- **Message error example**: `"The requested URL was not found on the server"`: Check if the URL is correct.

```html
<body>
	<h1>404 Not Found</h1>
	<p>The requested URL was not found on this server.</p>
</body>
```
