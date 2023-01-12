---
title: "Get an account's orderForm configuration"
slug: "get-an-account-orderform-configuration"
hidden: true
createdAt: "2022-12-08T23:21:08.132Z"
updatedAt: "2022-12-12T14:06:21.595Z"
---

The orderForm is the main object processed by VTEX checkout, and one of the most important data structures in the architecture of every VTEX store. It stores a lot of contextual information about the order which is important to the processing of the order: order items, client's personal data, delivery address, freight information, etc.

This guide will describe how to check the following settings applied currently to every orderForm in a specific account:
- `paymentConfiguration`: payment configuration information.
         -  ` requiresAuthenticationForPreAuthorizedPaymentOption`: determines whether pre-authorized payments require authentication.
         - `allowInstallmentsMerge`: when in a multi-seller purchase scenario, it allows a flexible installment option that considers maximum installments for each seller, according to their respective configuration options.
         - `paymentSystemToCheckFirstInstallment`: option to apply a first installment discount to a particular payment system.

- `taxConfiguration`: external tax service configuration information.
         - `url`: endpoint URL.
         - `authorizationHeader`: authorization header.
         - `appId`: custom data ID sent to the tax system.

- `minimumQuantityAccumulatedForItems`: minimum SKU quantity by cart.
- `decimalDigitsPrecision`: number of price digits.
- `minimumValueAccumulated`: minimum cart value.
- `apps`: apps configuration information.
         - `id`: app ID.
         - `fields`: app fields information.
         - `major`: app major version.

- `allowMultipleDeliveries`: allows the selection of items from several delivery channels in the same purchase.
- `allowManualPrice`: allows the editing of SKU prices directly in the cart.
- `savePersonalDataAsOptIn`: allows users to select whether they want the store to keep their personal and payment data saved.
- `maxNumberOfWhiteLabelSellers`: allows the input of a limit of white label sellers involved on the cart.
- `maskFirstPurchaseData`: allows, on a first purchase, masking client's data. It could be useful when a shared cart is used and the client doesn't want to share its data.
- `recaptchaValidation`: configures reCAPTCHA validation status for the account.

## Getting an account's orderForm configuration

To get an account orderForm configuration, you need to use the [Get orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/getorderformconfiguration) endpoint. In this request, you must send the `accountname` through the URL address, as shown by the example below:

`https://{accountName}.{environment.com.br}/api/checkout/pvt/configuration/orderForm`

After sending the request, the endpoint will return the response body containing the current account orderForm configuration, as shown in the example below:

```json
{
    "paymentConfiguration": {
        "requiresAuthenticationForPreAuthorizedPaymentOption": false,
        "allowInstallmentsMerge": null,
        "blockPaymentSession": null,
        "paymentSystemToCheckFirstInstallment": null,
        "defaultPaymentSystemToApplyOnUserOrderForm": null
    },
    "taxConfiguration": null,
    "minimumQuantityAccumulatedForItems": 1,
    "decimalDigitsPrecision": 2,
    "minimumValueAccumulated": 0,
    "apps": [
        {
            "fields": [
                "cart-extra-context",
                "cart-type"
            ],
            "id": "cart-extra-context",
            "major": 1
        },
        {
            "fields": [
                "orderIdMarketplace",
                "paymentIdMarketplace"
            ],
            "id": "marketplace-integration",
            "major": 1
        },
        {
            "fields": [
                "marketplacePaymentMethod"
            ],
            "id": "cn-centauro-integration",
            "major": 1
        },
        {
            "fields": [
                "quantity",
                "deadlines_1",              
                "interestRate"
            ],
            "id": "customer-credit",
            "major": 1
        },
        {
            "fields": [
                "affiliateId"
            ],
            "id": "affiliates",
            "major": 1
        }
    ],
    "allowMultipleDeliveries": false,
    "allowManualPrice": true,
    "savePersonalDataAsOptIn": false,
    "maxNumberOfWhiteLabelSellers": null,
    "maskFirstPurchaseData": null,
    "recaptchaValidation": null,
    "maskStateOnAddress": null
}
```

If you need to update any of your account's orderForm settings, access the [Update an account's orderForm configuration Dev. Guide](https://developers.vtex.com/vtex-rest-api/docs/update-an-account-orderform-configuration).

## Error codes

The following errors may appear as a message in the response body.

### 401 - Unauthorized
- **Message error example (code ORD062)**: `"Unauthorized"`. The credentials (Application Key and Application Token) used in this request are incorrect or not authorized to access this type of information.

```json
{
    "fields": {},
    "error": {
        "code": "ORD062",
        "message": "Unauthorized",
        "exception": null
    },
    "operationId": "8ec4b686-435f-42ab-8cfd-89306f888c3c"
}
```


### 404 - Not Found

- **Message error example**: `"The requested URL was not found on the server"`: check that the URL data is correct.

```json
<body>
	<h1>404 Not Found</h1>
	<p>The requested URL was not found on this server.</p>
</body>
```
