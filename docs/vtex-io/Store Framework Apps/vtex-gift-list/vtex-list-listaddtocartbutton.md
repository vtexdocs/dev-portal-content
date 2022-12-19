---
title: "Add To Cart Button"
slug: "vtex-list-listaddtocartbutton"
excerpt: "vtex.list@3.6.2"
hidden: false
createdAt: "2022-09-16T00:32:17.824Z"
updatedAt: "2022-12-01T16:44:24.156Z"
---
The `add-to-cart-button-list` block displays a button that allows users to add products in the Minicart from a guest page if the quantity purchased has not yet reached the limit.

![AddToCartButton](https://user-images.githubusercontent.com/67066494/190247953-58f73d99-008f-432b-8cdf-cb2970e51df0.gif)

## Configuration

1. Import the `vtex.list` app to your theme's peer dependencies in the `manifest.json` file as in the following example:

```json
  "peerDependencies": {
    "vtex.list": "3.x"
  }
```

2. Add the `add-to-cart-button-list` block to other theme block using the product context, such as the `product-summary.shelf`. For example:

```diff
  "product-summary.shelf": {
    "children": [
      "product-summary-image",
      "flex-layout.row",
      "flex-layout.col",
+     "add-to-cart-button-list",
      "gifted-button"
    ]
  }
```