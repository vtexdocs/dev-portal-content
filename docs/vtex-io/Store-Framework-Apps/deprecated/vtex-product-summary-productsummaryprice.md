---
title: "Product Summary Price"
slug: "vtex-product-summary-productsummaryprice"
hidden: false
createdAt: "2020-06-26T14:55:49.118Z"
updatedAt: "2022-07-02T00:50:33.015Z"
---
![https://img.shields.io/badge/-Deprecated-red](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-product-summary-productsummaryprice-0.png)

>⚠️ **The Product Summary Price block has been deprecated in favor of the [Product Price](https://developers.vtex.com/vtex-developer-docs/docs/vtex-product-price) app**. Although support for this block is still available, we strongly recommend that you update your store theme with the Product Price app to stay up with the component's evolution.

`ProductSummaryPrice` is a block exported by the [Product Summary app](https://developers.vtex.com/vtex-developer-docs/docs/vtex-product-summary) responsible for rendering the product's price.

![price-example](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-product-summary-productsummaryprice-1.png)

### Configuration

1. Import the `vtex.product-summary` app to your theme's dependencies in the `manifest.json`:

```json
  dependencies: {
    "vtex.product-summary": "2.x"
  }
```

2. Add the `product-summary-price` block to your store theme as a child of the `product-summary.shelf` block. For example:

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
3. Then, declare the `product-summary-price` and configure its behavior using the props stated below.

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

To apply CSS customizations in this and other blocks, follow the [Using CSS Handles for store customization](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-css-handles-for-store-customization) guide.

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