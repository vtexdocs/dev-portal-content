---
title: "APP NAME"
slug: "casaideasperu-custom-plp"
excerpt: "casaideasperu.custom-plp@0.1.118"
hidden: true
createdAt: "2022-07-04T21:20:28.085Z"
updatedAt: "2022-08-02T14:49:10.577Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

Custom component that shows a slider with the subcategories of each category, and the title tag of each category.

![Desktop](.docs/slider-category.PNG)

![Desktop](.docs/icon-category.PNG)

## Configuration

1. Adding the app as a theme dependency in the `manifest.json` file;

"store-theme.custom-plp":"0.x"

2. Declaring the app's main block in a given theme template or inside another block from the theme.

{
...
"children":[
"slider-category"
]
}

{
...
"children":[
"icon-category"
]
}

## Customization

In the store-theme create a file store-theme.store-finder inside the css folder and you can change css properties through the defined useCssHandles classes.

slider-category

| CSS Handles       |
| ----------------- |
| `sliderContainer` |
| `cardContainer`   |
| `bannerImage`     |
| `image`           |
| `infoContainer`   |
| `categoryLink`    |

icon-category

| CSS Handles        |
| ------------------ |
| `itemIcon`         |
| `tagTitle`         |
| `categoryContaine` |

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

---

Check out some documentation models that are already live:

- [Breadcrumb](https://github.com/vtex-apps/breadcrumb)
- [Image](https://vtex.io/docs/components/general/vtex.store-components/image)
- [Condition Layout](https://vtex.io/docs/components/all/vtex.condition-layout@1.1.6/)
- [Add To Cart Button](https://vtex.io/docs/components/content-blocks/vtex.add-to-cart-button@0.9.0/)
- [Store Form](https://vtex.io/docs/components/all/vtex.store-form@0.3.4/)