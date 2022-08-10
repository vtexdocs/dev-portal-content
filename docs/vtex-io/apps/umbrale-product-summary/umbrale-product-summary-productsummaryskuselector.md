---
title: "Product Summary SKU Selector"
slug: "umbrale-product-summary-productsummaryskuselector"
excerpt: "umbrale.product-summary@2.77.4"
hidden: true
createdAt: "2022-08-03T20:43:34.930Z"
updatedAt: "2022-08-04T15:16:50.651Z"
---
The `product-summary-sku-selector` is a VTEX block that's tasked with rendering the [SKU Selector](https://vtex.io/docs/app/vtex.store-components/sku-selector) component in a Product Summary component, such as the Shelf or the Search Results Page.

![product-summary-sku-selector](https://user-images.githubusercontent.com/52087100/68625690-87f9a580-04b8-11ea-835d-009ac768805f.gif)

## Configuration

1. Follow the [Product Summary](https://vtex.io/docs/app/vtex.product-summary) app's configuration instruction.
2. Add the `product-summary-sku-selector` to the Product Summary's desired block. In the following example, we'll use a Shelf:

```
"product-summary.shelf": {
   "children": [
     "product-summary-add-to-list-button",
     "stack-layout#prodsum",
     "product-summary-name",
     "product-rating-inline",
     "product-summary-space",
     "product-summary-sku-selector",
     "product-summary-price",
     "product-identifier.summary",
     "product-summary-buy-button"
   ]
 },
 ```
 
 3. Below, declare the `product-summary-sku-selector` block. The props that it uses are the same that are available for the [SKU Selector](https://vtex.io/docs/app/vtex.store-components/sku-selector). For example:
 
 ```
  "product-summary-sku-selector": {
   "props":{
     "showVariationsLabels": ["false"]
   }
 },
 ```
:warning: This block can only be configured through the source code. You're not yet able to edit using the Site Editor. 


## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles        |
| ------------------ |
| `SKUSelectorContainer` |