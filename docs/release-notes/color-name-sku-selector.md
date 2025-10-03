---
title: Color name on SKU Selector 
excerpt: "Display the name of the SKU color above its image on the SKU Selector."
createdAt: "2019-09-08T14:47:00.000Z"
type: 'info'
---
Display the name of the SKU color above its image on the SKU Selector.

## What has changed

When the user had to select a product’s color from the Product Details page, he had to rely only on the product’s image to imagine how it looked. It is now possible to display the name of the SKU color in addition to the variation’s name, in order to help the user to choose from among the available options.

![](https://user-images.githubusercontent.com/12139385/62787485-309fff80-ba9b-11e9-85c5-e08528688f8f.png)

## Key advantage

By seeing the color’s name along with the product’s image, the user can more clearly understand the difference among variations and therefore make a better choice

## What you need to do

1. Make sure your store runs version __3.59.0__ or newer of the [Store Components](https://github.com/vtex-apps/store-components) app.
2. Ensure that the [SKU Selector](https://github.com/vtex-apps/store-components/tree/master/react/components/SKUSelector) component is available in your [Product Details](https://github.com/vtex-apps/product-details) page block.
3. Configure your SKU Selector block with the `showValueNameForImageVariation prop`. When set as `true`, the component shows the selected SKU variation’s color name. :eyes: Default value is set to `false`.
