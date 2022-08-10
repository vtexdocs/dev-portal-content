---
title: "Product Summary Brand"
slug: "landerfit-product-summary-productsummarybrand"
excerpt: "landerfit.product-summary@2.80.3"
hidden: true
createdAt: "2022-07-14T16:32:57.561Z"
updatedAt: "2022-07-14T16:32:57.561Z"
---
![https://img.shields.io/badge/-Deprecated-red](https://img.shields.io/badge/-Deprecated-red)

> ⚠️ 
> 
> The Product Summary Brand block has been deprecated in favor of the [Product Brand](https://developers.vtex.com/vtex-developer-docs/docs/vtex-store-components-productbrand) app from the [Store Components](https://developers.vtex.com/vtex-developer-docs/docs/store-components) collection. Although support for this block is still granted, we strongly recommend updating your store theme with the Product Brand block.

Product Summary Brand is a block exported by the [Product Summary app](https://developers.vtex.com/vtex-developer-docs/docs/vtex-product-summary) responsible for rendering the brand of the product.

![product-brand](https://user-images.githubusercontent.com/52087100/70259346-bb081f80-176c-11ea-84db-5785c45829ce.png)

## Before you start

Ensure that you have registered [brands](https://help.vtex.com/en/tutorial/what-is-a-brand--QU07yhHoaWcEYseEucOQW) in your store. To do so, follow the [How to register brands](https://help.vtex.com/en/tutorial/registering-brands--tutorials_1414) guide.

## Configuration

1. Import the `vtex.product-summary` app to your theme's dependencies in the `manifest.json`:

```json
  "dependencies": {
    "vtex.product-summary": "2.x"
  }
```

2. Add the `product-summary-brand` block to your store theme as a child of the `product-summary.shelf` block. For example:


```diff
   "product-summary.shelf": {
    "children": [
      "product-summary-image",
      "product-summary-name",
+     "product-summary-brand",
      "product-summary-attachment-list",
      "product-summary-space",
      "product-summary-column#1"
    ]
  },
```