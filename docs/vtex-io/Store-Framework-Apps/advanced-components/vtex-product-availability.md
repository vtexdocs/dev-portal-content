---
title: "Product Availability"
slug: "vtex-product-availability"
hidden: false
createdAt: "2020-06-03T15:19:17.857Z"
updatedAt: "2022-02-25T16:57:31.666Z"
---

The Product Availability app displays text messages regarding the in-stock quantity for products. 

![product-availability](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-product-availability-0.png)

## Configuration

1. Add the Product Availability app to your theme's dependencies in the `manifest.json` file:

```diff
 "dependencies": {
+  "vtex.product-availability": "0.x"
 }
```

2. Add the `product-availability` block to the desired theme block whose data is fetched from the [Product Context](https://developers.vtex.com/vtex-developer-docs/docs/vtex-product-context), such as the [Minicart](https://developers.vtex.com/vtex-developer-docs/docs/vtex-minicart). For example:

```json
"product-availability": {
  "props": {
    "threshold": "10",
    "lowStockMessage": "Only {quantity} left!",
    "highStockMessage": "Item in stock!"
  }
}
```

| Prop name           | Type      | Description                                                 | Default value | 
| ------------------- | --------- | ----------------------------------------------------------- | ------------- |
| `threshold`     | `number` | Minimum product quantity that makes the low stock message to be displayed (if any message is set in the `lowStockMessage` prop).   | `0` | 
| `lowStockMessage` | `string` | Message text to be displayed when the in-stock quantity is lower than the quantity defined in the `threshold` prop. This prop value must have `{quantity}` inside the string text in order to properly display the stock quantity according to the threshold. For example: `"Only {quantity} left!`. Notice: if this prop's value is left empty, no message will be shown. | `""` | 
| `highStockMessage`  | `string` | Message text to be displayed when the in-stock quantity is higher or equal than the quantity defined in the `threshold` prop. Notice: if this prop's value is left empty, no message will be shown. | `""` | 

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-css-handles-for-store-customization).

| CSS Handles |
| ----------- | 
| `container` | 
| `highStockText` | 
| `lowStockHighlight` | 
| `lowStockText` |
