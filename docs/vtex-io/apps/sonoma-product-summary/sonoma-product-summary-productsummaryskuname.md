---
title: "Product Summary SKU Name"
slug: "sonoma-product-summary-productsummaryskuname"
excerpt: "sonoma.product-summary@0.0.22"
hidden: true
createdAt: "2022-07-26T02:31:27.810Z"
updatedAt: "2022-08-09T01:24:15.938Z"
---
_Product Summary SKU Name_ renders the selected SKU's name.

## Configuration

You should follow the usage instruction in the main [README](https://github.com/vtex-apps/product-summary/blob/master/README.md#usage).

Then, add `product-summary-sku-name` block into your app theme as children of `product-summary.shelf`, as we do in our [Product Summary app](https://github.com/vtex-apps/product-summary/blob/master/store/blocks.json).

```diff
   "product-summary.shelf": {
    "children": [
      "product-summary-image",
      "product-summary-name",
+     "product-summary-sku-name",
      "product-summary-attachment-list",
      "product-summary-space",
      "product-summary-column#1"
    ]
  },
```

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles        |
| ------------------ |
| `skuNameContainer` |