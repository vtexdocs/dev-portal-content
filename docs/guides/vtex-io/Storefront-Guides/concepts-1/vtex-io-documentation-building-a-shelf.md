---
title: "Building a Shelf"
slug: "vtex-io-documentation-building-a-shelf"
hidden: false
createdAt: "2021-10-28T00:08:33.278Z"
updatedAt: "2024-05-29T13:00:00.565Z"
---

The Shelf component is a product list that helps you to build your own shop window and work on your store's visual merchandising.

![shelf](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-building-a-shelf-0.png)

To create a product list, you can configure the Shelf component to use the [Product Summary List](https://developers.vtex.com/docs/apps/vtex.product-summary/productsummarylist), the [Product Summary Shelf](https://developers.vtex.com/docs/apps/vtex.product-summary), and the [Slider Layout](https://developers.vtex.com/docs/apps/vtex.slider-layout) blocks.

>ℹ️ Refer to the [**Product Summary**](https://developers.vtex.com/docs/apps/vtex.product-summary) and [**Slider-Layout**](https://developers.vtex.com/docs/apps/vtex.slider-layout) documentation to explore the available props for configuring their behavior. Use this information to adjust the Shelf behavior accordingly.

Check out the instructions below for how it can be done.

## Instructions

1. Add the `product-summary` and the `slider-layout` apps to your theme's dependencies in the `manifest.json` file:

```json
  "dependencies": {
    "vtex.product-summary": "2.x",
    "vtex.slider-layout": "0.x"
  }
```

2. Add the `list-context.product-list` into your `store.home` theme template and add in its blocks list the `product-summary.shelf` block. Also, add as its children the `slider-layout` block. For example:

```json
{
  "product-summary.shelf#demo1": {
    "children": [
      "stack-layout#prodsum",
      "product-summary-name",
      "product-rating-inline",
      "product-summary-space",
      "product-summary-price",
      "product-summary-buy-button"
    ]
  },
  "list-context.product-list#demo1": {
    "blocks": ["product-summary.shelf#demo1"],
    "children": ["slider-layout#demo-products"]
  }
}
```

3. Declare the `product-summary.shelf` block and add the desired blocks as children, as shown in the example below. If you have any questions about structuring the block, check its [documentation](https://developers.vtex.com/docs/guides/vtex-product-summary).

```diff
{
  "list-context.product-list#demo1": {
    "blocks": ["product-summary.shelf#demo1"],
    "children": ["slider-layout#demo-products"]

  },

+ "product-summary.shelf#demo1": {
+   "children": [
+    "product-summary-name",
+    "product-summary-description",
+    "product-summary-image",
+    "product-summary-price",
+    "product-summary-sku-selector",
+    "product-summary-buy-button"
+   ]
+ }
}
```

4. Declare the `slider-layout` block, adding as desired child blocks and props. If you have any questions about structuring the block, check its [documentation](https://developers.vtex.com/docs/guides/vtex-slider-layout).

```diff
{
  "list-context.product-list#demo1": {
    "blocks": ["product-summary.shelf#demo1"],
    "children": ["slider-layout#demo-products"]

  },

    "product-summary.shelf#demo1": {
     "children": [
      "product-summary-name",
      "product-summary-description",
      "product-summary-image",
      "product-summary-price",
      "product-summary-sku-selector",
      "product-summary-buy-button"
    ]
  },

+ "slider-layout#demo-products": {
+    "props": {
+      "itemsPerPage": {
+        "desktop": 1,
+        "tablet": 1,
+        "phone": 1
+      },
+      "infinite": true,
+      "showNavigationArrows": "desktopOnly",
+      "blockClass": "carousel"
+    },
+    "children": ["rich-text#1", "rich-text#2", "rich-text#3"]
+  },
}
```

After the last step, you now have a functioning Shelf for your store.
