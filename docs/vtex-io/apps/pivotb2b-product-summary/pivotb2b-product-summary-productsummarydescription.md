---
title: "Product Summary Description"
slug: "pivotb2b-product-summary-productsummarydescription"
excerpt: "pivotb2b.product-summary@2.80.2"
hidden: true
createdAt: "2022-07-20T18:39:44.205Z"
updatedAt: "2022-07-20T18:53:08.492Z"
---
Product Summary Description is a block exported by the [Product Summary app](https://developers.vtex.com/vtex-developer-docs/docs/vtex-product-summary) responsible for rendering the description of the product.

![product-description-example](https://user-images.githubusercontent.com/67270558/156373901-36a7a33d-9b32-4e0d-8798-ee4ddd01982d.png)
## Configuration

1. Import the `vtex.product-summary` app to your theme's dependencies in the `manifest.json`:

```json
  dependencies: {
    "vtex.product-summary": "2.x"
  }
```

2. Add the `product-summary-description` block to your store theme as a child of `product-summary.shelf`. For example:

```diff
   "product-summary.shelf": {
    "children": [
      "product-summary-image",
      "product-summary-name",
+     "product-summary-description",
      "product-summary-attachment-list",
      "product-summary-space",
      "product-summary-column#1"
    ]
  },
```

## Customization

To apply CSS customizations in this and other blocks, follow the [Using CSS Handles for store customization](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-css-handles-for-store-customization) guide.

| CSS Handles        |
| ------------------ |
| `description` |