---
title: "Product Summary Name"
slug: "kaueplussize-product-summary-productsummaryname"
excerpt: "kaueplussize.product-summary@2.81.2"
hidden: true
createdAt: "2022-08-01T18:04:09.488Z"
updatedAt: "2022-08-03T19:26:10.753Z"
---
Product Summary Name is a block exported by the [Product Summary app](https://developers.vtex.com/vtex-developer-docs/docs/vtex-product-summary) responsible for rendering the product name.

![name-example](https://user-images.githubusercontent.com/67270558/156374478-42cc320d-8aa9-432a-95c1-cf884534cbb1.png)
## Configuration

1. Import the `vtex.product-summary` app to your theme's dependencies in the `manifest.json`:

```json
  dependencies: {
    "vtex.product-summary": "2.x"
  }
```

2. Add the `product-summary-name` block to your store theme as a child of `product-summary.shelf`. For example:

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
3. Then, declare the `product-summary-name` and configure its behavior using the props stated below.


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

To apply CSS customizations in this and other blocks, follow the [Using CSS Handles for store customization](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-css-handles-for-store-customization) guide.

| CSS Handles        |
| ------------------ |
| `nameContainer` |
| `nameWrapper` |
| `brandName` |
| `skuName` |
| `productReference` |
| `productNameLoader` |