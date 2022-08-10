---
title: "Product Summary SKU Selector"
slug: "cea-cea-product-summary-productsummaryskuselector"
excerpt: "cea.cea-product-summary@0.23.0"
hidden: true
createdAt: "2022-07-14T17:15:53.834Z"
updatedAt: "2022-08-09T12:32:19.169Z"
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

#### Customization

| CSS Handles   | Description                                          | Component Source                     |
| ------------ | ---------------------------------------------------- | ------------------------------------ |
| `SKUSelectorContainer` | SKU Selector main container | [index](/react/components/ProductSummarySKUSelector/index.js) |