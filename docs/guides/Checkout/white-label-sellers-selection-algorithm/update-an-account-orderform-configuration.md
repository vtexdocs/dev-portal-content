---
title: "Update an account's orderForm configuration"
slug: "update-an-account-orderform-configuration"
hidden: true
createdAt: "2022-12-09T18:51:21.877Z"
updatedAt: "2022-12-12T13:58:26.358Z"
---
The orderForm is the main object processed by VTEX checkout, and one of the most important data structures in the architecture of every VTEX store. It stores a lot of contextual information about the order which is important to the processing of the order: order items, client's personal data, delivery address, freight information, etc.

This guide will describe how to update settings applied currently to every orderForm in a specific account.

>⚠️ Always retrieve the current orderForm configuration before performing an update to ensure that you are modifying only the properties you want. Otherwise, old values can be overwritten. To get the current orderForm configuration for a specific account, check the [Get orderForm configuration developer's guide](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pvt/configuration/orderForm).

## Updating an account's orderForm configuration

To update an account orderForm configuration, you need to use the [Update orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/updateorderformconfiguration) endpoint. In this request, you must send the `accountname` through the URL address, as shown by the example below:

`https://{accountName}.{environment.com.br}/api/checkout/pvt/configuration/orderForm`

Additionally, you can submit the following information to modify your account's orderForm configuration:

- `paymentConfiguration`: payment configuration information.
         - `requiresAuthenticationForPreAuthorizedPaymentOption`: determines whether pre-authorized payments require authentication. This field is mandatory and must be sent in all requests.
         - `allowInstallmentsMerge`: when in a multi-seller purchase scenario, it allows a flexible installment option that considers maximum installments for each seller, according to their respective configuration options.
         - `paymentSystemToCheckFirstInstallment`: option to apply a first installment discount to a particular payment system.

- `taxConfiguration`: external tax service configuration information.
         - `url`: endpoint URL.
         - `authorizationHeader`: authorization header.
         - `appId`: custom data ID sent to the tax system.

- `minimumQuantityAccumulatedForItems`: minimum SKU quantity by cart. This field is mandatory and must be sent in all requests.
- `decimalDigitsPrecision`: number of price digits.
- `minimumValueAccumulated`: minimum cart value.
- `apps`: apps configuration information.
         - `fields`: app fields information.
         - `id`: app ID.
         - `major`: app major version.

- `allowMultipleDeliveries`: allows the selection of items from several delivery channels in the same purchase.
- `allowManualPrice`: allows the editing of SKU prices directly in the cart.
- `savePersonalDataAsOptIn`: allows users to select whether they want the store to keep their personal and payment data saved.
- `maxNumberOfWhiteLabelSellers`: allows the input of a limit of white label sellers involved on the cart.
- `maskFirstPurchaseData`: allows, on a first purchase, masking client's data. It could be useful when a shared cart is used and the client doesn't want to share its data.
- `recaptchaValidation`: configures reCAPTCHA validation status for the account.
- `requiresLoginToPlaceOrder`: indicates whether authentication is required for completing purchases.
- `minimumPurchaseDowntimeSeconds`: minimum interval (in seconds) between successive purchases.
- `cartAgeToUseNewCardSeconds`: minimum cart existence period (in seconds) before allowing the use of a new credit card.

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
    "minimumQuantityAccumulatedForItems": 8,
    "requiresLoginToPlaceOrder": true,
    "minimumPurchaseDowntimeSeconds": 90,
    "cartAgeToUseNewCardSeconds": 30,
    "apps": [
        {
            "fields": [
                "gender",
                "age"
            ],
            "id": "profile",
            "major": 1
        },
        {
            "fields": [
                "address"
            ],
            "id": "address",
            "major": 1
        }
  ]
}
```

After sending the request, the endpoint will return `code 204 (No Content)` and an empty response body.

To confirm that the new orderForm settings have been applied to your account, access the [Get orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/getorderformconfiguration) endpoint again.

## Error codes

The following errors may appear as a message in the response body.

### 401 - Unauthorized
- **Message error example (code ORD062)**: `"Unauthorized"`. The credentials (API key and API token) used in this request are incorrect or not authorized to access this type of information.

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

```html
<body>
 <h1>404 Not Found</h1>
 <p>The requested URL was not found on this server.</p>
</body>
```
