---
title: "Enable the Save user data opt-in"
slug: "enable-the-save-user-data-opt-in"
hidden: false
createdAt: "2022-06-13T19:32:17.594Z"
updatedAt: "2022-10-20T17:36:55.171Z"
---

To comply with GDPR (General Data Protection Regulation - Europe) and LGPD - Lei Geral de Proteção de Dados (General Data Protection Law - Brazil), among other solutions, VTEX offers the **Save User Data opt-in** functionality. Through it, users can select whether they want the store to keep their personal and payment data saved.
[block:callout]
{
  "type": "warning",
  "body": "The **Save user data opt-in** feature is only available for Checkout v6."
}
[/block]

## Save user data opt-in activation

To use the **Save user data opt-in** functionality in your store, you must first enable it. Then, follow the settings below:

1. Make a `GET` request using the endpoint [Get orderForm configuration](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pvt/configuration/orderForm).
2. Make a `POST` request using the endpoint [Update orderForm configuration](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pvt/configuration/orderForm) with the same data obtained in the GET request, just modifying the value of the `savePersonalDataAsOptIn` parameter from `null` to `true`.
3. Make a new `GET` request using the endpoint [Get orderForm configuration](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pvt/configuration/orderForm) to confirm activation. This will be indicated by the presence of the `savePaymentData` and `savePersonalData` fields under the `clientPreferencesData` object in the `orderForm`.

![savePersonalData](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/enable-the-save-user-data-opt-in-0.PNG)

> ℹ️ Under the `storePreferencesData` object, the `saveUserData` field may be indicated as `true`. This field is ignored, and kept in this configuration for backwards compatibility only.

![savePersonalData2](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/enable-the-save-user-data-opt-in-1.PNG)

## Saving personal and payment data

Once the **Save user data opt-in** is enabled, the user will have access to checkboxes on the Checkout page to select whether their personal and payment data should be kept by the store and used in future orders.

Checkbox for saving personal data:

![Contact Information](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/enable-the-save-user-data-opt-in-2.png)

> ℹ️ Previously, it was possible to display this checkbox by modifying the `display` property of the `.save-data` element, via CSS. However, with the **Save user data opt-in** enabled, the method through CSS is no longer recommended.

Checkbox for saving payment data:

![Pagamento](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/enable-the-save-user-data-opt-in-3.PNG)

[block:callout]
{
  "type": "warning",
  "body": "The checkbox for saving payment data will only be shown if the user has already selected the option to save their personal data."
}
[/block]
Checkbox not available to save payment data if (the user has not previously selected the option to save personal data):

![Payment\_No Checkbox](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/enable-the-save-user-data-opt-in-4.png)

If the user chooses to use two cards to pay for the purchase, when selecting the option to save payment data, the data of both cards will be saved. There is no option to save only one of the cards.

Checkbox to save payment data from both cards:

![Payment two cards](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/enable-the-save-user-data-opt-in-5.png)
