---
title: "Product Availability"
slug: "vtex-product-availability"
excerpt: "vtex.product-availability@0.3.1"
hidden: false
createdAt: "2020-06-03T15:19:17.857Z"
updatedAt: "2022-02-25T16:57:31.666Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/vtex-io/Store Framework Apps/advanced-components/#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

The Product Availability app displays text messages regarding the in-stock quantity for products. 

![product-availability](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-product-availability-0.png)

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

<!-- DOCS-IGNORE:start -->

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!

<!-- DOCS-IGNORE:end -->