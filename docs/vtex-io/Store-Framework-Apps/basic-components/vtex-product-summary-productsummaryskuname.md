---
title: "Product Summary SKU Name"
slug: "vtex-product-summary-productsummaryskuname"
hidden: false
createdAt: "2020-09-24T16:36:08.010Z"
updatedAt: "2022-07-02T00:50:32.861Z"
---
Product Summary SKU Name is a block exported by the [Product Summary app](https://developers.vtex.com/docs/guides/vtex-product-summary) responsible for rendering the selected SKU's name.

## Configuration

1. Import the `vtex.product-summary` app to your theme's dependencies in the `manifest.json`:

```json
  "dependencies": {
    "vtex.product-summary": "2.x"
  }
```

2. Add the `product-summary-sku-name` block to your store theme as a child of `product-summary.shelf`. For example:

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

To apply CSS customizations in this and other blocks, follow the [Using CSS Handles for store customization](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-css-handles-for-store-customization) guide.

| CSS Handles        |
| ------------------ |
| `skuNameContainer` |