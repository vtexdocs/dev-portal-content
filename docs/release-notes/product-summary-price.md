---
title: Product Summary Price
excerpt: "Learn how to build and custom a Product Details Page with our flexible components"
createdAt: "2019-11-11T14:47:00.000Z"
---

The Product Summary Price component gained a new prop, `showDiscountValue`, which allows users to see a product's absolute savings. 

![absolute-saving-release](https://user-images.githubusercontent.com/52087100/68611939-13177300-049a-11ea-8601-8191fca590fb.png)

## What has changed?

Previously, it wasn't possible to display a product's savings using the Product Summary Price component.

The only way to show users what they were saving on a specific product was using the `discountBadge`. However, it only displayed that saving in percentage points.

## Why did we make these changes? 

In addition to clearly showing users the economic advantages of buying a specific product at a sale price, this release eliminates complications that arose from this process for retailers. 

Since we're dealing with a prop, this configuration can be performed directly in the block itself without resorting to other components or customizations.  

## What needs to be done?

To configure this new prop, use [Product Summary](https://developers.vtex.com/docs/apps/vtex.product-summary@2.43.0) version **2.43.0** or higher in your store.
