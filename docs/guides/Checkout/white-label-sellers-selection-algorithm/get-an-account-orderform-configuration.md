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
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"paymentConfiguration\": {\n        \"requiresAuthenticationForPreAuthorizedPaymentOption\": false,\n        \"allowInstallmentsMerge\": null,\n        \"blockPaymentSession\": null,\n        \"paymentSystemToCheckFirstInstallment\": null,\n        \"defaultPaymentSystemToApplyOnUserOrderForm\": null\n    },\n    \"taxConfiguration\": null,\n    \"minimumQuantityAccumulatedForItems\": 1,\n    \"decimalDigitsPrecision\": 2,\n    \"minimumValueAccumulated\": 0,\n    \"apps\": [\n        {\n            \"fields\": [\n                \"cart-extra-context\",\n                \"cart-type\"\n            ],\n            \"id\": \"cart-extra-context\",\n            \"major\": 1\n        },\n        {\n            \"fields\": [\n                \"orderIdMarketplace\",\n                \"paymentIdMarketplace\"\n            ],\n            \"id\": \"marketplace-integration\",\n            \"major\": 1\n        },\n        {\n            \"fields\": [\n                \"marketplacePaymentMethod\"\n            ],\n            \"id\": \"cn-centauro-integration\",\n            \"major\": 1\n        },\n        {\n            \"fields\": [\n                \"quantity\",\n                \"deadlines_1\",              \n                \"interestRate\"\n            ],\n            \"id\": \"customer-credit\",\n            \"major\": 1\n        },\n        {\n            \"fields\": [\n                \"affiliateId\"\n            ],\n            \"id\": \"affiliates\",\n            \"major\": 1\n        }\n    ],\n    \"allowMultipleDeliveries\": false,\n    \"allowManualPrice\": true,\n    \"savePersonalDataAsOptIn\": false,\n    \"maxNumberOfWhiteLabelSellers\": null,\n    \"maskFirstPurchaseData\": null,\n    \"recaptchaValidation\": null,\n    \"maskStateOnAddress\": null\n}\n",
      "language": "json"
    }
  ]
}
[/block]
If you need to update any of your account's orderForm settings, access the [Update an account's orderForm configuration Dev. Guide](https://developers.vtex.com/vtex-rest-api/docs/update-an-account-orderform-configuration).

## Error codes

The following errors may appear as a message in the response body.

### 401 - Unauthorized
- **Message error example (code ORD062)**: `"Unauthorized"`. The credentials (API key and API token) used in this request are incorrect or not authorized to access this type of information.
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"fields\": {},\n    \"error\": {\n        \"code\": \"ORD062\",\n        \"message\": \"Unauthorized\",\n        \"exception\": null\n    },\n    \"operationId\": \"8ec4b686-435f-42ab-8cfd-89306f888c3c\"\n}",
      "language": "json"
    }
  ]
}
[/block]
### 404 - Not Found

- **Message error example**: `"The requested URL was not found on the server"`: check that the URL data is correct.
[block:code]
{
  "codes": [
    {
      "code": "<body>\n\t<h1>404 Not Found</h1>\n\t<p>The requested URL was not found on this server.</p>\n</body>",
      "language": "json"
    }
  ]
}
[/block]