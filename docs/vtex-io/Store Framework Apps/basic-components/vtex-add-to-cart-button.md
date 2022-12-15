---
title: "Add To Cart Button"
slug: "vtex-add-to-cart-button"
excerpt: "vtex.add-to-cart-button@0.28.1-hkignore.0"
hidden: false
createdAt: "2020-06-03T15:19:30.080Z"
updatedAt: "2022-04-11T12:41:12.534Z"
---
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-3-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

The `add-to-cart-button` is a block responsible for adding products in the [Minicart](https://vtex.io/docs/components/all/vtex.minicart/) (`minicart.v2`). 

![image](https://user-images.githubusercontent.com/284515/70233985-69e13700-173e-11ea-91f7-6675a6a0e73b.png)

:warning: **The Add To Cart Button only effectively function i.e. only adds products to the Minicart if the store uses the Minicart v2**. In this scenario, it successfully works in the Shelf component as well as in the Product Details page. **When using the [Minicart v1](https://github.com/vtex-apps/minicart/blob/383d7bbd3295f06d1b5854a0add561a872e1515c/docs/README.md), you should configure the [Buy Button block](https://vtex.io/docs/components/all/vtex.store-components/buybutton/) in the Product Details page, and the [Product Summary Buy Button](https://vtex.io/docs/components/all/vtex.product-summary/product-summary-buy-button/) in the Shelf component instead**.

## Configuration

1. Import the `vtex.add-to-cart-button` app to your theme's dependencies in the manifest.json, for example:

```json
"dependencies": {
  "vtex.add-to-cart-button": "0.x"
}
```

2. Add the `add-to-cart-button` to other theme block using the product context, such as the `product-summary.shelf`. In the example below, the `add-to-cart-button` is added to the `flex-layout.row` block from the `store.product` template (which uses the product context):

```json
  "store.product": {
    "children": [
      "flex-layout.row#product",
    ]
  },
  "flex-layout.row#product": {
    "children": [
      "add-to-cart-button"
    ]
  }
```

| Prop name               | Type      | Description                                                                       | Default value        |
| ----------------------- | --------- | --------------------------------------------------------------------------------- | -------------------- |
| `onClickBehavior`       | `enum` | Controls what happens when users click on the button. Possible values are: `go-to-product-page`, `add-to-cart`, and `ensure-sku-selection` (if multiple SKUs are available, users will be redirected to the product page to select the desired one. If the product only has 1 SKU available, it will be added to the cart once the button is clicked on). | `add-to-cart`              |
| `onClickEventPropagation` | `enum` | Controls whether the 'onClick' event (triggered upon user clicks) should be spread to the page's parent elements. Possible values are: `disabled` and `enabled`. | `disabled` |
| `isOneClickBuy`         | `boolean` | Whether the user should be redirected to the checkout page (`true`) or not (`false`) when the Add To Cart Button is clicked on.  | `false`              |
| `customOneClickBuyLink` | `string`  | Defines the link to where users will be redirected when the Add To Cart Button is clicked on and the `isOneClickBuy` prop is set to `true`. | `/checkout/#/cart` |
| `customToastUrl`        | `string`  | Defines the link to where users will be redirected when the Toast (pop-up notification displayed when adding an item to the minicart) is clicked on.  | `/checkout/#/cart`   |
| `text` | `string` | Defines a custom text message to be displayed on the Add To Cart Button. | `Add to cart` *( automatic translation will be applied according to your store's default language)* | 
| `unavailableText` | `string` | Defines a custom text message to be displayed on the Add To Cart Button when a product is unavailable. | `Unavailable` *(automatic translation will be applied according to your store's default language)* |
| `customPixelEventId` | `string` | Define the `id` for the event that will be sent by the the button upon user interaction. | `undefined`   |

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles           |
| --------------------- |
| `buttonText`          |
| `buttonDataContainer` |
| `tooltipLabelText`    |

<!-- DOCS-IGNORE:start -->

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/JNussens"><img src="https://avatars0.githubusercontent.com/u/7662734?v=4" width="100px;" alt=""/><br /><sub><strong>Jean Nussenzveig</strong></sub></a><br /><a href="https://github.com/vtex-apps/add-to-cart-button/commits?author=JNussens" title="Code">💻</a></td>
    <td align="center"><a href="http://ygorneves.com"><img src="https://avatars1.githubusercontent.com/u/39542011?v=4" width="100px;" alt=""/><br /><sub><strong>Ygor Neves</strong></sub></a><br /><a href="https://github.com/vtex-apps/add-to-cart-button/commits?author=ygorneves10" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/lucaspacheco-acct"><img src="https://avatars0.githubusercontent.com/u/59736416?v=4" width="100px;" alt=""/><br /><sub><strong>Lucas Pacheco</strong></sub></a><br /><a href="https://github.com/vtex-apps/add-to-cart-button/commits?author=lucaspacheco-acct" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!

<!-- DOCS-IGNORE:end -->