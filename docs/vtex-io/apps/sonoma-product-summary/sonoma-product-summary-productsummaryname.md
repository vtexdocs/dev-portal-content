---
title: "Product Summary Name"
slug: "sonoma-product-summary-productsummaryname"
excerpt: "sonoma.product-summary@0.0.22"
hidden: true
createdAt: "2022-07-26T02:31:27.836Z"
updatedAt: "2022-08-09T01:24:15.997Z"
---
_Product Summary Name_ renders the product name.

## Configuration

You should follow the usage instruction in the main [README](https://github.com/vtex-apps/product-summary/blob/master/README.md#usage).

Then, add `product-summary-name` block into your app theme as children of `product-summary.shelf`, as we do in our [Product Summary app](https://github.com/vtex-apps/product-summary/blob/master/store/blocks.json).

```diff
   "product-summary.shelf": {
    "children": [
      "product-summary-image",
+     "product-summary-name",
      "product-summary-space",
      "product-summary-column#1"
    ]
  },
```

| Prop name | Type | Description | Default value |
| ----------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------- |
| `showFieldsProps` | `object` | Defines the visibility on certain properties. | `{ showProductReference: false, showBrandName: false, showSku: false }` |
| `tag` | `string` | HTML tag used. It can be: `div`, `h1`, `h2`, `h3`. | `h1` |

- `showFieldsProps` object:

| Prop name | Type | Description | Default value |
| --- | --- | --- | ---| 
| `showSku` | `Boolean` | Show product SKU | `false` |
| `showProductReference` | `Boolean` | Show product reference | `false`| 
| `showBrandName` | `Boolean` | Show brand name | `false`| 

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles        |
| ------------------ |
| `nameContainer` |
| `nameWrapper` |
| `brandName` |
| `skuName` |
| `productReference` |
| `productNameLoader` |