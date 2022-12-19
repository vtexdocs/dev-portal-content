---
title: "Product Summary SKU Selector"
slug: "vtex-product-summary-productsummaryskuselector"
excerpt: "vtex.product-summary@2.80.1-perftest.1"
hidden: false
createdAt: "2020-06-09T14:48:52.836Z"
updatedAt: "2022-07-02T00:50:32.998Z"
---
The `product-summary-sku-selector` is a VTEX block that's tasked with rendering the [SKU Selector](https://developers.vtex.com/vtex-developer-docs/docs/vtex-store-components-skuselector) component in a Product Summary component, such as the Shelf or the Search Results Page.

![product-summary-sku-selector](https://user-images.githubusercontent.com/52087100/68625690-87f9a580-04b8-11ea-835d-009ac768805f.gif)

## Configuration

1. Follow the [Product Summary](https://developers.vtex.com/vtex-developer-docs/docs/vtex-product-summary) app's configuration instruction.
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
 
 3. Below, declare the `product-summary-sku-selector` block. The props that it uses are the same that are available for the [SKU Selector](https://developers.vtex.com/vtex-developer-docs/docs/vtex-store-components-skuselector). For example:
 
 ```
  "product-summary-sku-selector": {
   "props":{
     "showVariationsLabels": ["false"]
   }
 },
 ```
>⚠️ The Product Summary SKU block can only be modified through the source code. It's not possible yet to edit it via the Site Editor. 


## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-css-handles-for-store-customization).

| CSS Handles        |
| ------------------ |
| `SKUSelectorContainer` |