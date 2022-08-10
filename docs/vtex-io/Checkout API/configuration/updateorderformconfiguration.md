---
title: "Update orderForm configuration"
slug: "updateorderformconfiguration"
excerpt: "Determines settings that will apply to every orderForm in the account.\n\r\n\rFor example, if you create an app using this request, every orderForm of this account will have the custom fields created though it.\n\r\n\r**Important**: always retrieve the current configuration before performing an update to ensure that you are modifying only the properties you want. Otherwise, old values can be overwritten. To retrieve the current configuration, use the request [Get orderForm configuration](https://developers.vtex.com/reference#getorderformconfiguration)."
hidden: false
createdAt: "2020-02-05T23:27:53.590Z"
updatedAt: "2020-11-12T14:22:46.081Z"
---
**Example of request body:** 
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"paymentConfiguration\": {\n        \"requiresAuthenticationForPreAuthorizedPaymentOption\": false,\n        \"allowInstallmentsMerge\": null\n    },\n    \"taxConfiguration\": {\n        \"url\": \"https://master--qausa.myvtex.com/avalara/checkout/order-tax\",\n        \"authorizationHeader\": \"99b9935b048dfd86893d0bf9gas628849\",\n        \"allowExecutionAfterErrors\": false,\n        \"integratedAuthentication\": false,\n        \"appId\": null\n    },\n    \"minimumQuantityAccumulatedForItems\": 1,\n    \"decimalDigitsPrecision\": 2,\n    \"minimumValueAccumulated\": 0,\n    \"apps\": [\n        {\n            \"fields\": [\n                \"cart-extra-context\",\n                \"cart-type\"\n            ],\n            \"id\": \"cart-extra-context\",\n            \"major\": 1\n        },\n        {\n            \"fields\": [\n                \"age\",\n                \"sex\"\n            ],\n            \"id\": \"profile\",\n            \"major\": 1\n        },\n        {\n            \"fields\": [\n                \"manufacturer\",\n                \"model\",\n                \"year\"\n            ],\n            \"id\": \"car\",\n            \"major\": 1\n        }\n    ],\n    \"allowMultipleDeliveries\": false,\n    \"allowManualPrice\": true,\n    \"maxNumberOfWhiteLabelSellers\": null,\n    \"maskFirstPurchaseData\": null\n}",
      "language": "json"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "info",
  "title": "Turning off your tax provider",
  "body": "If you need to turn off your tax provider, fetch your current orderForm configuration and update it with an empty object in the `taxConfiguration` field (`\"taxConfiguration\": {}`)."
}
[/block]