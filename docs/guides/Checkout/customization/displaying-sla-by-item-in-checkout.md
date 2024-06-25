---
title: "Displaying SLA by item in Checkout"
slug: "displaying-sla-by-item-in-checkout"
hidden: true
createdAt: ""
updatedAt: ""
excerpt: "This guide describes how to display individual shipping estimates for items in a customer's cart on an ecommerce platform using the Checkout API."
hidePaginationPrevious: false
hidePaginationNext: false
---

To enhance the customer experience, some stores may want to display precise shipping estimates for each item in the customer's cart. This can be particularly useful for ecommerce platforms that have sellers with different shipping capabilities and delivery times. This guide will walk through the process of displaying the Service Level Agreement (SLA) by item using the [Checkout API](https://developers.vtex.com/docs/api-reference/checkout-api).

<CH.Scrollycoding>

## Enable the `useIndividualShippingEstimates` flag

First, it is necessary to enable the [Checkout API](https://developers.vtex.com/docs/api-reference/checkout-api) behavior to fill the `shippingEstimateDate` with the SLA information. To do so, you must update the store's `orderForm` with the [Update orderForm configuration](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pvt/configuration/orderForm) endpoint. You must include the flag `useIndividualShippingEstimates` to `true` as in the example shown.

```json Request mark=23
{
    "paymentConfiguration": {
    ...
    },
    "taxConfiguration": null,
    "minimumQuantityAccumulatedForItems": 1,
    "decimalDigitsPrecision": 2,
    "minimumValueAccumulated": null,
    "apps": [
    ...
    ],
    "allowMultipleDeliveries": true,
    "allowManualPrice": null,
    "savePersonalDataAsOptIn": false,
    "maxNumberOfWhiteLabelSellers": null,
    "recaptchaValidation": "vtexcriteria",
    "recaptchaMinScore": null,
    "recaptchaKeys": null,
    "maskStateOnAddress": true,
    "enableSecureCookies": true,
    "useOwnershipCookie": true,
    "ignoreProfileData": null,
    "useIndividualShippingEstimates": true
}
```

By enabling this flag, the `shippingEstimateDate` will be updated with the SLA information configured by the sellers.

---

## Add items to cart

Once you enable the `useIndividualShippingEstimates`, test if the configuration is correct by adding items to a shopping cart using the [Add cart items](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/items) endpoint. See the request body example presented.

```json Request
{
  "orderItems": [
    {
      "seller": "1",
      "id": 6,
      "quantity": 1
    },
    {
      "seller": "1",
      "id": 11,
      "quantity": 1
    }
  ]
}
```

---

## Send shipping data attachment

Send the item shipping data to the `orderForm` using the [Add shipping address and select delivery option](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/attachments/shippingData) endpoint as in the example shown.

Once configured, the `orderForm` will retrieve the variable `shippingEstimateDate`, which will display the shipping estimate date instead of only the shipping estimate in business days.

<CH.Code>

```json Request
{
  "selectedAddresses": [
    {
      "addressId": "5139683010323",
      "addressType": "search",
      "city": null,
      "complement": null,
      "country": "BRA",
      "neighborhood": null,
      "number": null,
      "postalCode": "08391705",
      "receiverName": "Jane Doe",
      "reference": null,
      "street": null,
      "addressQuery": "",
      "isDisposable": null
    }
  ],
  "expectedOrderFormSections": [
    "items",
    "totalizers",
    "clientProfileData",
    "shippingData",
    "paymentData",
    "sellers",
    "messages",
    "marketingData",
    "clientPreferencesData",
    "storePreferencesData",
    "giftRegistryData",
    "ratesAndBenefitsData",
    "openTextField",
    "commercialConditionData",
    "customData"
  ]
}
```

---

```json Response
{
"slas": [
    "id": "SEDEX 1",
    "deliveryChannel": "delivery",
    "name": "SEDEX_1",
    "deliveryIds":[1],
    "courierId": "1aafbd3",
    "warehouseId": "estoqueA",
    "dockId": "01",
    "courierName": "Correios DistanceLevel Sedex1_Test",
    "quantity": 1,
    "kitItemDetails": []
    "shippingEstimate": "3bd",
    "shippingEstimateDate": "2023-07-12T14:52:00+00:00",
    "lockTTL": null,
    "availableDeliveryWindows": 0,
    "deliveryWindow": null,
    "price": 31,
    "listPrice": 31,
    "tax":0,
    "pickupStoreInfo": {
        "isPickupStore": false,
        "friendlyName": null,
        "address": null,
        "additionalInfo": null,
        "dockId": null
    }
]}
```

</CH.Code>

</CH.Scrollycoding>
