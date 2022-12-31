---
title: "Product Summary Description"
slug: "vtex-product-summary-productsummarydescription"
excerpt: "vtex.product-summary@2.80.1-perftest.1"
hidden: false
createdAt: "2020-06-09T14:48:52.918Z"
updatedAt: "2022-07-02T00:50:33.068Z"
---
Product Summary Description is a block exported by the [Product Summary app](https://developers.vtex.com/vtex-developer-docs/docs/vtex-product-summary) responsible for rendering the description of the product.

![product-description-example](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-product-summary-productsummarydescription-0.png)
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