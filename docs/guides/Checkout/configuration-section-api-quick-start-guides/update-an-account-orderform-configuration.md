---
title: "Updating an account orderForm configuration"
slug: "update-an-account-orderform-configuration"
hidden: true
createdAt: "2022-12-09T18:51:21.877Z"
updatedAt: "2022-12-12T13:58:26.358Z"
---

The orderForm is the main object processed by VTEX Checkout and one of the most important data structures in the architecture of every VTEX store. It stores a lot of contextual information about the order, which is essential for processing order information, such as order items, customer personal information, delivery address, and shipping information.

This guide will describe how to update settings currently applied to every orderForm in a specific account.
> ⚠️ Always retrieve the current orderForm configuration before performing an update to ensure you modify only the properties you want. Otherwise, old values can be overwritten. To get the current orderForm configuration for a specific account, read the [Get an account's orderForm configuration Dev. Guide](https://developers.vtex.com/docs/guides/get-an-account-orderform-configuration).

## Updating an account orderForm configuration

To update an account orderForm configuration, you must use the [Update orderForm configuration](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pvt/configuration/orderForm) endpoint. In this request, you must send the `accountname` in the URL address, as in the example below:

`https://{accountName}.{environment.com.br}/api/checkout/pvt/configuration/orderForm`

Additionally, you can send the configuration information below that you want to modify in your account’s orderForm:

- `paymentConfiguration`: Payment configuration information. -  `requiresAuthenticationForPreAuthorizedPaymentOption`: Determines whether pre-authorized payments require authentication. - `allowInstallmentsMerge`: In a multi-seller purchase scenario, it allows a flexible installment option that considers maximum installments for each seller according to their respective configuration options. - `paymentSystemToCheckFirstInstallment`: Option to apply a first installment discount to a particular payment system.

- `taxConfiguration`: External tax service configuration information. - `url`: Endpoint URL. - `authorizationHeader`: Authorization header. - `appId`: Custom data ID sent to the tax system.

- `minimumQuantityAccumulatedForItems`: Minimum SKU quantity per cart.
- `decimalDigitsPrecision`: Number of price digits.
- `minimumValueAccumulated`: Minimum cart value.
- `apps`: Apps configuration information. - `id`: App ID. - `fields`: App fields information. - `major`: App major version.

- `allowMultipleDeliveries`: Allows selecting items from several delivery channels in the same purchase.
- `allowManualPrice`: Allows editing SKU prices directly in the cart.
- `savePersonalDataAsOptIn`: Allows users to select whether they want the store to save their personal and payment information.
- `maxNumberOfWhiteLabelSellers`: Allows entering a limit of white label sellers in the cart.
- `maskFirstPurchaseData`: Allows masking the customer information in the first purchase. It can be useful when a shared cart is used and the customer does not want to share their information.
- `recaptchaValidation`: Configures reCAPTCHA verification status for the account.

See a request body example below:

```json
{
     "paymentConfiguration": {
          "requiresAuthenticationForPreAuthorizedPaymentOption": true
     },
     "recaptchaValidation": "vtexCriteria",
     "minimumValueAccumulated": 5,
     "maxNumberOfWhiteLabelSellers": 2,
     "maskFirstPurchaseData": false,
     "decimalDigitsPrecision": 2,
     "minimumQuantityAccumulatedForItems": 8
}
```

After sending the request, the endpoint will return `code 204 (No Content)` and an empty response body.

To confirm that the new orderForm settings have been applied to your account, please access the [Get orderForm configuration](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pvt/configuration/orderForm) endpoint again.

## Error codes

The errors below may appear as messages in the response body.

### 401 - Unauthorized
- `Message error example (code ORD062): "Unauthorized"`: The credentials (API key and API token) used in this request are incorrect or do not have authorization to access this type of information.

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

- `Message error example: "The requested URL was not found on the server"`. Check if the URL is correct.

```json
<body>
    <h1>404 Not found</h1>
    <p>The requested URL was not found on this server.</p>
</body>
```
