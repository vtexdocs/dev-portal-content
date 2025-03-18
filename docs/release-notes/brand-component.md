---
title: 'Brand component'
excerpt: "A new component which shows either the product brand name or product brand logo was released."
createdAt: "2019-07-03T14:47:00.000Z"
---

With the introduction of the Brand component, you can now display the product’s brand name independently and also showcase the brand logo, which was not possible before.

![brand-component](https://user-images.githubusercontent.com/52087100/60600980-a374d700-9d87-11e9-9f57-e10cbe371577.png)

## What has changed 

Previously, the product’s brand name could only be retrieved through the [Product Name component](https://developers.vtex.com/docs/apps/vtex.store-components@3.68.0/ProductName). This limitation meant that the brand name could not be displayed separately from the product name on the Product Details page.

## Why did we make this change?

The new component provides more flexibility in building your Product Details pages by showing the product brand name and/or the brand logo in any position on the page with its own CSS customization.

## What needs to be done?

1. Ensure your store is running [Store Components](https://developers.vtex.com/docs/apps/vtex.store-components) version 3.47.0 or later.
2. Add the component [Product Brand](https://developers.vtex.com/docs/apps/vtex.store-components@3.68.0/ProductBrand) to your Product Details Page (PDP).
3. Configure your PDP block with the following props:

| Property          | Type                | Description                                                                                                                |
|-------------------|---------------------|----------------------------------------------------------------------------------------------------------------------------|
| `displayMode`     | `string`            | Choose between `logo` or `text` to define how the product brand is displayed. |
| `fallbackToText`  | `boolean`           | Defines what should be done when no image is registered in the VTEX Catalog. Defaults to `true`, replacing the logo with the brand name. Set it to `false` to hide the brand if no logo is available. Only applicable when `displayMode` is `logo`. |
| `height`          | `number`            | Sets the brand logo height. Only applicable when `displayMode` is `logo`.                                            |
| `excludeBrands`   | `array of strings`  | List of brand names or brand IDs to exclude from being displayed. Useful for hiding test brands/logos. |


> ⚠️ The `displayMode` prop allows you to choose between `text` and `logo`. If you want to display both the brand name and logo, add the Brand component twice, setting `displayMode` to `text` in one instance and `logo` in the other.
