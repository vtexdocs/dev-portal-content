---
title: "Product Summary Price"
slug: "umbrale-product-summary-productsummaryprice"
excerpt: "umbrale.product-summary@2.77.4"
hidden: true
createdAt: "2022-08-03T20:43:34.348Z"
updatedAt: "2022-08-04T15:16:50.516Z"
---
![https://img.shields.io/badge/-Deprecated-red](https://img.shields.io/badge/-Deprecated-red)

:warning: **The Product Summary Price block has been deprecated in favor of the [Product Price](https://vtex.io/docs/components/all/vtex.product-price/) app**. Although support for this block is still granted, we strongly recommend you to update your store theme with the Product Price's blocks in order to keep up with the component's evolution.

`ProductSummaryPrice` renders the product's price.

### Configuration

You should follow the usage instruction in the main [README](https://github.com/vtex-apps/product-summary/blob/master/README.md#usage).

Then, add `product-summary-price` block into your app theme as children of `product-summary.shelf`, as we do in our [Product Summary app](https://github.com/vtex-apps/product-summary/blob/master/store/blocks.json).

```diff
   "product-summary.shelf": {
    "children": [
      "product-summary-image",
      "product-summary-name",
+     "product-summary-price",
      "product-summary-attachment-list",
      "product-summary-space",
      "product-summary-column#1"
    ]
  },
```

| Prop name           | Type      | Description                      | Default value |
| ------------------- | --------- | -------------------------------- | ------------- |
| `showListPrice`     | `Boolean` | Shows the product list price     | `true`        |
| `showInstallments`  | `Boolean` | Set installments' visibility     | `true`        |
| `showDiscountValue`  | `Boolean` | Set discount value's visibility     | `false`        |
| `showLabels`        | `Boolean` | Set pricing labels' visibility   | `true`        |
| `labelSellingPrice` | `String`  | Text of selling price's label    |               |
| `labelListPrice`    | `String`  | Text of list price's label       |               |   
| `showBorders`       | `Boolean` | Set product's borders visibility | `false`       |
| `showListPriceRange`       | `Boolean` | Set if you want to see list price as range (lowest - highest) when available | `false`       |
| `showSellingPriceRange`       | `Boolean` | Set if you want to see selling price as range (lowest - highest) when available | `false`       |

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles           |
| ------------------- |
| `priceContainer` |
| `productPriceClass` |
| `listPriceContainer` |
| `listPriceLabel` |
| `listPrice` |
| `sellingPriceContainer` |
| `sellingPriceLabel` |
| `sellingPrice` |
| `savingsContainer` |
| `savings` |
| `interestRate` |
| `installmentContainer` |
| `listPriceRange` |
| `sellingPriceRange` |
| `priceLoading` |