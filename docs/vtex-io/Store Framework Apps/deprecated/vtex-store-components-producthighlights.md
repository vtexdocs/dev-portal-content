---
title: "Product Highlights"
slug: "vtex-store-components-producthighlights"
excerpt: "vtex.store-components@3.163.4"
hidden: false
createdAt: "2020-06-03T16:04:30.385Z"
updatedAt: "2022-11-22T18:39:23.175Z"
---
![https://img.shields.io/badge/-Deprecated-red](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-store-components-producthighlights-0.png)

> ⚠️ Warning
>
> **The Product Highlights block has been deprecated in favor of the [Product Specifications app](https://developers.vtex.com/vtex-developer-docs/docs/vtex-product-specifications/).** Although support for this block is still granted, we strongly recommend you to update your store theme with the Product Specification's blocks in order to keep up with the component's evolution.


The `product-highlights` block shows the general specifications of a product.

## Configuration

1. Import the `vtex.store-components` app to your theme's dependencies in the `manifest.json` file as in the following example:

```json
  "dependencies": {
    "vtex.store-components": "3.x"
  }
```

2. Add the `product-highlights` block to any child of the `store.product` or `product-summary` templates. For example:

```diff
  "store.product": {
    "children": [
+     "product-highlights",
    ]
  },
```

3. Then, declare the `product-highlights` block using the props stated in the [Props](#props) table.

### Props

| Prop name    | Type                | Description             | Default value |
| ------------ | ------------------- | ----------------------- | ------------- |
| `highlights` | `Array(Highlights)` | Highlights of a product. | `[]`          |

#### `highlights` props

| Prop name | Type             | Description       |
| --------- | ---------------- | ----------------- |
| `name`    | `String!`        | Highlights name.   |
| `values`  | `Array(String)!` | Highlights values. |

## Customization

To apply CSS customizations in this and other blocks, follow the [Using CSS handles for store customization](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-css-handles-for-store-customization) guide.

| CSS Handles                     |
| ------------------------------- |
| `highlightContent` |
| `itemHighlight` |
| `highlightTitle` |
| `highlightValue` |