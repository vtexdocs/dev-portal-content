---
title: "Product Shipping Calculator"
slug: "autecocolombia-custom-landings"
excerpt: "autecocolombia.custom-landings@0.0.11"
hidden: true
createdAt: "2022-07-12T00:00:16.859Z"
updatedAt: "2022-07-27T19:45:33.387Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

To use into PDP to show a calculator prices for a product

![Desktop](./product-description.png)

## Configuration

1. Add the app as a dependency in your store theme

```
"shuremx.product-shipping-price":"0.x"
```

2. Declare the app block in your store inside your porduct display page. Default is `product.jsonc`

```
{
   ...
   "children":[
      "product-shipping-calculator"
   ]
}
```

## Customization

In the store-theme create a file the north face mx.product-description-accordion inside the css folder and you can change css properties through the defined useCssHandles classes.

## Contributors ✨

Thanks goes to these wonderful people:

- Manuel Castillo