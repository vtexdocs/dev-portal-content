---
title: "Product List"
slug: "zonasul-product-list"
excerpt: "zonasul.product-list@0.8.2"
hidden: true
createdAt: "2022-07-28T13:27:33.611Z"
updatedAt: "2022-08-04T19:46:43.087Z"
---
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

The Product List displays all items in the user's cart and informs the user when some of them are unavailable. Currently, the Product List only works out of the box within the [Minicart](https://github.com/vtex-apps/minicart) and the [Checkout Cart](https://github.com/vtex-apps/checkout-cart).

![image](https://user-images.githubusercontent.com/8902498/71035787-03bfc100-20fb-11ea-914e-51301b3bedf4.png)

## Configuration

1. Add the Product List app to your theme's dependencies in `manifest.json`. For example:

```json
  "dependencies": {
    "vtex.product-list": "0.x"
  }
```

2. Add the `product-list` block to the `minicart-product-list` block of the Minicart or to the `product-list-wrapper` block of the Checkout Cart. For example:

```json
  "minicart-product-list#example": {
    "blocks": ["product-list"]
  }
```

### Advanced Configuration

The `product-list` block is made up of other smaller blocks. Currently, its default implementation is as follows (props omitted):

```json
{
  "product-list": {
    "blocks": [
      "product-list-content-desktop",
      "product-list-content-mobile"
    ]
  },
  "flex-layout.col#product-description": {
    "children": [
      "flex-layout.row#product-brand",
      "flex-layout.row#product-name",
      "flex-layout.row#product-variations"
    ],
    "props": { (...) }
  },
  "flex-layout.row#product-brand": {
    "children": ["product-brand"],
    "props": { (...) }
  },
  "flex-layout.row#product-name": {
    "children": ["product-name"]
  },
  "flex-layout.row#product-variations": {
    "children": ["product-variations"],
    "props": { (...) }
  }
}
```

#### Desktop layout

```json
{
  "product-list-content-desktop": {
    "children": ["flex-layout.row#list-row.desktop"]
  },
  "flex-layout.row#list-row.desktop": {
    "children": [
      "flex-layout.col#image.desktop",
      "flex-layout.col#main-container.desktop"
    ],
    "props": { (...) }
  },
  "flex-layout.col#image.desktop": {
    "children": ["product-list-image"],
    "props": { (...) }
  },
  "flex-layout.col#main-container.desktop": {
    "children": [
      "flex-layout.row#sub-container.desktop",
      "flex-layout.row#message.desktop"
    ],
    "props": { (...) }
  },
  "flex-layout.row#sub-container.desktop": {
    "children": [
      "flex-layout.col#product-description",
      "flex-layout.col#quantity.desktop",
      "flex-layout.row#price-remove"
    ],
    "props": { (...) }
  },
  "flex-layout.col#quantity.desktop": {
    "children": [
      "flex-layout.row#quantity-selector.desktop",
      "flex-layout.row#unit-price.desktop"
    ],
    "props": { (...) }
  },
  "flex-layout.row#price-remove": {
    "children": [
      "flex-layout.col#price.desktop",
      "flex-layout.col#remove-button.desktop"
    ],
    "props": { (...) }
  },
  "flex-layout.row#quantity-selector.desktop": {
    "children": ["quantity-selector"],
    "props": { (...) }
  },
  "flex-layout.row#unit-price.desktop": {
    "children": ["unit-price#desktop"],
    "props": { (...) }
  },
  "unit-price#desktop": {
    "props": { (...) }
  },
  "flex-layout.col#price.desktop": {
    "children": ["price#desktop"],
    "props": { (...) }
  },
  "price#desktop": {
    "props": { (...) }
  },
  "flex-layout.col#remove-button.desktop": {
    "children": ["remove-button"],
    "props": { (...) }
  },
  "flex-layout.row#message.desktop": {
    "children": ["message#desktop"],
    "props": { (...) }
  },
  "message#desktop": {
    "props": { (...) }
  }
}
```

#### Mobile layout

```json
{
  "product-list-content-mobile": {
    "children": ["flex-layout.row#list-row.mobile"]
  },
  "flex-layout.row#list-row.mobile": {
    "children": [
      "flex-layout.col#image.mobile",
      "flex-layout.col#main-container.mobile"
    ],
    "props": { (...) }
  },
  "flex-layout.col#image.mobile": {
    "children": ["product-list-image"],
    "props": { (...) }
  },
  "flex-layout.col#main-container.mobile": {
    "children": [
      "flex-layout.row#top.mobile",
      "flex-layout.row#quantity-selector.mobile",
      "flex-layout.row#unit-price.mobile",
      "flex-layout.row#price.mobile",
      "flex-layout.row#message.mobile"
    ],
    "props": { (...) }
  },
  "flex-layout.row#top.mobile": {
    "children": [
      "flex-layout.col#product-description",
      "flex-layout.col#remove-button.mobile"
    ],
    "props": { (...) }
  },
  "flex-layout.row#quantity-selector.mobile": {
    "children": ["quantity-selector"],
    "props": { (...) }
  },
  "flex-layout.row#unit-price.mobile": {
    "children": ["unit-price"],
    "props": { (...) }
  },
  "flex-layout.row#price.mobile": {
    "children": ["price#mobile"],
    "props": { (...) }
  },
  "price#mobile": {
    "props": { (...) }
  },
  "flex-layout.col#remove-button.mobile": {
    "children": ["remove-button"],
    "props": { (...) }
  },
  "flex-layout.row#message.mobile": {
    "children": ["message#mobile"],
    "props": { (...) }
  },
  "message#mobile": {
    "props": { (...) }
  }
}
```

By default implementation we mean that whenever you use `product-list` in your store you're actually using the `json` above behind the scenes.

Therefore, in order to customize the Product List configuration, you can simply use the default implementation in your code and change it as you wish.

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles                          |
| ------------------------------------ |
| `availabilityMessageContainer`       |
| `availabilityMessageTextContainer`   |
| `availabilityMessageText`            |
| `productBrandName`                   |
| `productImageAnchor`                 |
| `productImageContainer`              |
| `productImage`                       |
| `productListAvailableItemsMessage`   |
| `productListItem`                    |
| `productListUnavailableItemsMessage` |
| `productName`                        |
| `productPriceContainer`              |
| `productPriceCurrency`               |
| `productPrice`                       |
| `productQuantityLabel`               |
| `productVariationsContainer`         |
| `productVariationsItem`              |
| `quantityDropdownContainer`          |
| `quantityDropdownMobileContainer`    |
| `quantityInputContainer`             |
| `quantityInputMobileContainer`       |
| `quantitySelectorContainer`          |
| `removeButtonContainer`              |
| `removeButton`                       |
| `unitPriceContainer`                 |
| `unitPriceMeasurementUnit`           |
| `unitPricePerUnitCurrency`           |

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!