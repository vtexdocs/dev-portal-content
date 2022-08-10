---
title: "MinicartCheckoutButton"
slug: "sicredi-login-components-minicartcheckoutbutton"
excerpt: "sicredi.login-components@0.1.0"
hidden: true
createdAt: "2022-08-08T17:41:04.598Z"
updatedAt: "2022-08-08T17:41:04.598Z"
---
## Description

This component is responsable to send the user to the checkout, but, this will only occur if the user is logged in the VTEX and in the Sicredi system. Otherwise, it will open the respective login (respecting the procedence which is first VTEX and last Sicredi).

## Modus Operandi

1. Not logged in VTEX & Sicredi
    - Open the modal of Associated for the user log in

2. Logged VTEX and not Sicredi
    - Open the Sicredi modal

3. Logged VTEX and Sicredi (with the flag of associated)
    - Go to checkout

## Configuration

1. Add the `sicredi.login-components` app to your theme's dependencies in the `manifest.json`, for example:

```diff
"dependencies": {
+  "sicredi.login-components": "0.x"
}
```

2. The component can be called inside another component as `<MinicartCheckoutButton />` or using the the json `minicart-checkout-button-custom`

## Customization

Below are the classes available for customization. For more information access: [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles                  |
| ---------------------------- |
| `minicart-checkout__wrapper` |
| `minicart-checkout__button`  |