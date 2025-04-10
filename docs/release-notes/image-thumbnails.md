---
title: Image thumbnails 
excerpt: "The Product Images component now allows a product’s thumbnails to be displayed either vertically or horizontally on the page."
createdAt: "2019-08-22T14:47:00.000Z"
---

Thanks to the new `thumbnailsOrientation` prop, the [Product Images](https://developers.vtex.com/docs/apps/vtex.store-components@3.70.0/ProductImages) component now allows a product’s thumbnails to be displayed either vertically or horizontally on the page.

## What has changed?

Previously, it was not possible to choose how a product’s thumbnail images were set on a store’s page. The only possible behavior was to have them vertically.

The `thumbnailsOrientation` prop now allows a product’s page thumbnail images to be positioned according to your store’s needs:

- **Vertical** (default value)

![](https://user-images.githubusercontent.com/52087100/63535192-4378f200-c4e7-11e9-8f27-17280583a1af.png)

- **Horizontal**

![](https://user-images.githubusercontent.com/52087100/63535269-74592700-c4e7-11e9-813e-b873164666b9.png)

## Why did we make this change?

The new prop allows the retailer to choose the best way to position thumbnails for its users, avoiding forcing an unwanted default behavior onto the product’s page layout.

## What needs to be done?

To customize your store’s thumbnail position, you must have installed version 3.61.0 or higher of [Store Components](https://github.com/vtex-apps/store-components).
