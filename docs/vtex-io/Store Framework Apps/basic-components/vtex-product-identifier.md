---
title: "Product Identifier"
slug: "vtex-product-identifier"
excerpt: "vtex.product-identifier@0.4.1"
hidden: false
createdAt: "2020-06-03T15:19:25.494Z"
updatedAt: "2022-08-18T10:57:35.113Z"
---
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/vtex-io/Store Framework Apps/basic-components/#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

Product Identifier app is responsible for showing a product identifier, such as: product reference, product ID, sku EAN or sku reference.

![reference](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-product-identifier-0.png)

## Configuration

Add the `vtex.product-identifier` app to your theme's dependencies in the `manifest.json` file, as in:

```
"dependencies": {
    "vtex.product-identifier": "0.x"
}
```

Add `product-identifier.product` block to your store as a child of `product-summary.shelf`.

```
"product-identifier.product": {
  "props": {
    "label": "default", //'default' | 'custom' | 'hide'
    "customLabel": "teste", // text if label is custom
    "idField": "skuReferenceId" //'itemId' | 'productId' | 'productReference' | 'skuEan' | 'skuReferenceId'
  }
},
```

The `product-identifier` interface is available is also available within the admin's CMS where you can configure this component to show other identifiers, such as:

- Product Reference
- Product ID
- SKU EAN
- SKU Reference ID
- Item ID

It's also possible to hide the component label or customize its text. Notice that, in the following example, the "Reference" text was substituted by "Foo".

![foo](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-product-identifier-1.png)

## Customization

To apply CSS customization in this and other blocks, follow the instructions given in the recipe on [Using  CSS  Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles |
| ----------- |
| `product-identifier`           | 
| `product-identifier__label`    | 
| `product-identifier__separator`| 
| `product-identifier__value`    | 

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="http://carafizi.com/"><img src="https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-product-identifier-2.png"></img></a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!