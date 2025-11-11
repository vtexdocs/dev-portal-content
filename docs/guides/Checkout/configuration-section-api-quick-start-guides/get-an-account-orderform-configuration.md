---
title: "Getting an account orderForm configuration"
slug: "get-an-account-orderform-configuration"
hidden: true
createdAt: "2022-12-08t23:21:08.132z"
updatedAt: "2022-12-12t14:06:21.595z"
---

The orderForm is the main object processed by VTEX Checkout and one of the most important data structures in the architecture of every VTEX store. It stores a lot of contextual information about the order, which is essential for processing order information, such as order items, customer personal information, delivery address, and shipping information.

This guide describes how to check the following settings, which are currently applied to every orderForm in a specific account:

- `paymentConfiguration`: Payment configuration information.
  - `requiresAuthenticationForPreAuthorizedPaymentOption`: Determines whether pre-authorized payments require authentication.
  - `allowInstallmentsMerge`: In a multi-seller purchase scenario, it allows a flexible installment option that considers maximum installments for each seller according to their respective configuration options.
  - `paymentSystemToCheckFirstInstallment`: Option to apply a first installment discount to a particular payment system.

- `taxConfiguration`: External tax service configuration information.
  - `url`: Endpoint URL.
  - `authorizationHeader`: Authorization header.
  - `appId`: Custom data ID sent to the tax system.

- `minimumQuantityAccumulatedForItems`: Minimum SKU quantity per cart.
- `decimalDigitsPrecision`: Number of price digits.
- `minimumValueAccumulated`: Minimum cart value.
- `apps`: Apps configuration information.
  - `id`: App ID.
  - `fields`: App fields information.
  - `major`: App major version.

- `allowMultipleDeliveries`: Allows selecting items from several delivery channels in the same purchase.
- `allowManualPrice`: Allows editing SKU prices directly in the cart.
- `savePersonalDataAsOptIn`: Allows users to select whether they want the store to save their personal and payment information.
- `maxNumberOfWhiteLabelSellers`: Allows entering a limit of white label sellers in the cart.
- `maskFirstPurchaseData`: Allows masking the customer information in the first purchase. It may be useful when a shared cart is used and the customer does not want to share their information.
- `recaptchaValidation`: Configures reCAPTCHA verification status for the account.

## Getting an account orderForm configuration

To get an account orderForm configuration, you need to use the [Get orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/getorderformconfiguration) endpoint. In this request, you must send the `accountname` in the URL address, as in the example below:

`https://{accountName}.{environment.com.br}/api/checkout/pvt/configuration/orderForm`

After sending the request, the endpoint will return the response body containing the current account orderForm configuration, as in the example below:

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

If you need to update any of your account orderForm settings, see the [Update an account's orderForm configuration Dev. Guide](https://developers.vtex.com/vtex-rest-api/docs/update-an-account-orderform-configuration).

## Error codes

The following errors may appear as messages in the response body:

### 401 - Unauthorized

- **Message error example (code ORD062)**: `"Unauthorized"`. The credentials (API key and API token) used in this request are incorrect or not authorized to access this information.

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

- **Message error example**: `"The requested URL was not found on the server"`. Check if the URL is correct.

```html
<body>
    <h1>404 Not Found</h1>
    <p>The requested URL was not found on this server.</p>
</body>
```
