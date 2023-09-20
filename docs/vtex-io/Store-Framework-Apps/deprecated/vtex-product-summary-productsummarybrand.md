---
title: "Product Summary Brand"
slug: "vtex-product-summary-productsummarybrand"
hidden: false
createdAt: "2020-06-09T14:48:53.038Z"
updatedAt: "2022-07-02T00:50:32.906Z"
---
![https://img.shields.io/badge/-Deprecated-red](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-product-summary-productsummarybrand-0.png)

> ⚠️ 
> 
> The Product Summary Brand block has been deprecated in favor of the [Product Brand](https://developers.vtex.com/docs/guides/vtex-store-components-productbrand) app from the [Store Components](https://developers.vtex.com/docs/guides/store-components) collection. Although support for this block is still granted, we strongly recommend updating your store theme with the Product Brand block.

Product Summary Brand is a block exported by the [Product Summary app](https://developers.vtex.com/docs/guides/vtex-product-summary) responsible for rendering the brand of the product.

![product-brand](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-product-summary-productsummarybrand-1.png)

## Before you begin

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