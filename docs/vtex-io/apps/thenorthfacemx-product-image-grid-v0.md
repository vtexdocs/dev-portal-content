---
title: "Product Image Grid"
slug: "thenorthfacemx-product-image-grid-v0"
excerpt: "thenorthfacemx.product-image-grid@0.3.3"
hidden: true
createdAt: "2022-07-19T22:05:43.000Z"
updatedAt: "2022-07-19T22:05:43.000Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

For use inside the Product detail page.
On desktop displays it shows the product images arranged in a responsive grid format with zoom on hover.
On mobile displays it shows the product images in an 'Intagram-like' slider with pinch to zoom, dots and total image count.

It displays a maximum of 6 images.

![Desktop](desktop-screenshot.png)
![Mobile](mobile-screenshot.png)

## Configuration

1. Add the app as a dependency in your store theme

```
"thenorthfacemx.product-image-grid":"0.x"
```

2. Declare the app block in your store inside your porduct display page. Default is `product.jsonc`

```
image-grid
```

3. Change the color of the dots in the mobile slider in Vtex Admin.
   Go to `Store Setup > CMS > Site Editor` and navigate to a page that contains this block.
   You will find it under the name `Slider Image Dots`. Colors must be correct hex values starting wwith `#` otherwise the system will revert to the defualt colors.

## Customization

`No CSS Handles are available yet for the app customization.`

Only customization is done thorugh the admin section as mentioned above

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

- Eduardo Cervantes
- Kinich Barcelo

<!-- DOCS-IGNORE:end -->