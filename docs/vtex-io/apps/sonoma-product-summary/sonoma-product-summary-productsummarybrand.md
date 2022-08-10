---
title: "Product Summary Brand"
slug: "sonoma-product-summary-productsummarybrand"
excerpt: "sonoma.product-summary@0.0.22"
hidden: true
createdAt: "2022-07-26T02:31:27.832Z"
updatedAt: "2022-08-09T01:24:15.908Z"
---
![https://img.shields.io/badge/-Deprecated-red](https://img.shields.io/badge/-Deprecated-red)

> ⚠️ The Product Summary Brand block has been deprecated in favor of the Product Brand from the app vtex.store-components. Although support for this block is still granted, we strongly recommend you to update your store theme with the Product Brand block in order to keep up with the component's evolution.

_Product Summary Brand_ renders the brand of the product.

## Configuration

You should follow the usage instruction in the main [README](https://github.com/vtex-apps/product-summary/blob/master/README.md#usage).

Then, add `product-summary-brand` block into your app theme as children of `product-summary.shelf`, as we do in our [Product Summary app](https://github.com/vtex-apps/product-summary/blob/master/store/blocks.json).

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