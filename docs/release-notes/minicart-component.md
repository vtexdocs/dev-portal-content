---
title: Minicart component 
excerpt: "The new Minicart component prop 'linkButtonFinishShopping' redirects the user to any page the retailer wants when clicking the Finish Shopping Button."
createdAt: "2019-08-22T14:47:00.000Z"
type: 'info'
---
The new Minicart component prop `linkButtonFinishShopping` redirects the user to any page the retailer wants when clicking the Finish Shopping Button.

## What has changed

Prior to having the  `linkButtonFinishShopping` prop, the Minicart Finish Shopping Button would always make the user proceed to checkout.

![](https://user-images.githubusercontent.com/52087100/63535533-0a8d4d00-c4e8-11e9-8e37-28e5990e8b5d.png)

> ℹ️ The “__GO TO CHECKOUT__” text shown on the Finish Shopping Button of the example above is set by the `labelButtonFinishShopping` prop.

Thanks to this improvement, you can now set a different address to redirect the user to, without necessarily having to be the checkout. The address may be any page the retailer wants.

## Main advantages

The retailer may have wanted to change the default redirect and choose another page to where the user would land, for example one with special buy&win promotions or extended warranty options.

The new prop makes the Minicart component behavior more flexible and gives the retailer greater control over user browsing.

## What you need to do

To use the new component prop, ensure that [__Minicart__](https://github.com/vtex-apps/minicart) version __2.24.0__ or higher is installed in your store.
