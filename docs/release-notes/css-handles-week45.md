---
title: CSS Handles
excerpt: "The Breadcrumb was not the only one to have been gifted Handles this week. `savingPriceValue` and `savingPriceLabel` also had a lucky week and gained their own CSS Handles."
createdAt: "2019-11-25T14:47:00.000Z"
type: 'info'
---
This improvement gives two Product Details Page components their own **CSS Handles**. The aforementioned components are `savingPriceValue` and `savingPriceLabel` . 

## What has changed

Previously, `savingPriceLabel` and `savingPriceValue` were the only [Product Price](https://github.com/vtex-apps/store-components/blob/master/docs/ProductPrice.md) components lacking Handles. 

This led to defective customization scenarios, as shown in the example below:

![saving-css-handles](https://user-images.githubusercontent.com/52087100/69572579-2f8bd300-0fa3-11ea-989e-cc9278b595e7.png)

_Notice that `savingPriceLabel` (`You Save:`) and `savingPriceValue`(`$3.80`) are the only ones not in bold._ 

## Main advantages 

Without CSS Handles, `savingPriceLabel` and `savingPriceValue`  customization depended on CSS Selectors, which looked to a page's HTML structure when selecting an element. 

This store customization practice, in addition to being vulnerable, will soon be [deprecated](https://vtex.io/docs/releases/2019-week-43-44/css-selectors-deprecation). Therefore, launching these Handles is of **strategic importance**.

## What you need to do

Make sure your store is running [**Store Components**](https://vtex.io/docs/app/vtex.store-components) on version **3.81.0** or higher. 

Don't forget to take a look at the recipe on [using CSS Handle for store customization](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-css-handles-for-store-customization).
