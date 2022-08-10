---
title: "Product Description Acoordion"
slug: "timberlandmx-product-description-accordion"
excerpt: "timberlandmx.product-description-accordion@0.1.17"
hidden: true
createdAt: "2022-07-20T03:31:28.492Z"
updatedAt: "2022-08-03T17:07:33.238Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

To use within the product details page. Drop-down component in which it shows the properties of the product such as description, characteristics, advantages, product details.
In the case of properties, it shows an image related to each of the properties that the product has.
In the other properties of the product shows a list with each of them.

![Desktop](./product-description.png)

## Configuration

1. Add the app as a dependency in your store theme

```
"thenorthfacemx.product-description-accordion":"0.x"
```

2. Declare the app block in your store inside your porduct display page. Default is `product.jsonc`

```
{
   ...
   "children":[
      "poduct-description-accordion"
   ]
}
```

## Customization

In the store-theme create a file the north face mx.product-description-accordion inside the css folder and you can change css properties through the defined useCssHandles classes.

## Contributors ✨

Thanks goes to these wonderful people:

- Mario Rodriguez