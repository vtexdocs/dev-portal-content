---
title: "Petcamp - Buy Together"
slug: "petcamp-buy-together"
excerpt: "petcamp.buy-together@0.1.2"
hidden: true
createdAt: "2022-07-22T12:57:21.184Z"
updatedAt: "2022-07-25T20:50:38.232Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

⚠️ This App was built to work just with **Buy Together Promotion**, so make sure you have set up that and that it matches all requirements for a Default Buy Together VTEX promotion. It will return just two products with the "Buy Together" promotion.

It'll render the usual buy together structure to show the user the discount he'll get if he buy the products together.

![Media Placeholder](https://i.imgur.com/0AjqG8S.png)

## Configuration 

1. Install the `petcamp.buy-together` app to the desire account with the command `vtex install petcamp.buy-together`.

2. Import the `petcamp.buy-together` app to your theme's peerDependencies in the `manifest.json`:

```json
  "peerDependencies": {
    "petcamp.buy-together": "0.x"
  }
```

Now, you are able to use all blocks exported by the `buy-together` app. Check out the example below:

```json
{
  "buy-together": {
    "blocks": [
      "product-summary.shelf",
      "add-to-cart-button"
    ],
    "props": {
      "title": "Buy Together",
      "label": "You save {discount} buying together"
    }
  }
}
```

### `buy-together` props

| Prop name | Type   | Description                         | Default Value |
|-----------|--------|-------------------------------------|---------------|
| `Title`     | `String` | A title text for the component      | `""`            |
| `Label`     | `String` | Custom text to show off the savings | `""`            |

<!-- ## Modus Operandi *(not mandatory)*

There are scenarios in which an app can behave differently in a store, according to how it was added to the catalog, for example. It's crucial to go through these **behavioral changes** in this section, allowing users to fully understand the **practical application** of the app in their store.

If you feel compelled to give further details about the app, such as it's **relationship with the VTEX admin**, don't hesitate to use this section.  -->

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles |
| ----------- | 
| `buyContainer` |
| `buyOutterWrapper` |
| `buyInnerWrapper` |
| `summaryContainer` | 
| `priceContainer` | 
| `cardsContainer` |
| `totalPrice` | 
| `discountText` | 
| `discountValue` |
| `title` |
| `verticalLine` |
| `iconWrapper` |
| `plusIcon` |

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

----