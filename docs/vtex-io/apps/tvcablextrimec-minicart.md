---
title: "Minicart"
slug: "tvcablextrimec-minicart"
excerpt: "tvcablextrimec.minicart@2.60.1"
hidden: true
createdAt: "2022-07-12T04:35:34.198Z"
updatedAt: "2022-07-12T04:35:34.198Z"
---
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-3-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

:information_source: **Minicart v1 block has been deprecated in favor of Minicart v2** which can be customized using the blocks defined by [Product List](https://vtex.io/docs/app/vtex.product-list) and [Checkout Summary](https://vtex.io/docs/app/vtex.checkout-summary). If you’re still using the former version, you can find its documentation here: [Minicart v1 documentation](https://github.com/vtex-apps/minicart/blob/383d7bbd3295f06d1b5854a0add561a872e1515c/docs/README.md)

The VTEX Minicart is a block that displays a summary list of all items added by customers in their shopping cart. Its data is fetched from the Checkout OrderForm API.

![minicart-v2-gif](https://user-images.githubusercontent.com/52087100/73321194-7f477e80-4220-11ea-844b-f24d1c10363c.gif)

## Configuration

1. Import the Minicart app to your theme's dependencies in the `manifest.json` as shown below:

```json
"dependencies": {
  "vtex.minicart": "2.x"
}
```

2. Add the `minicart.v2` block to your `header`. For example:

```json
"header.full": {
   "blocks": ["header-layout.desktop", "header-layout.mobile"]
 },

 "header-layout.desktop": {
   "children": [
     "header-row#1-desktop",
   ]
 },

 "header-row#1-desktop": {
   "children": ["minicart.v2"],
 },
```

:warning: **The Minicart v2 will only effectively function if the store uses the** [**Add To Cart Button**](https://vtex.io/docs/components/content-blocks/vtex.add-to-cart-button/) **instead of the** [**Buy Button**](https://vtex.io/docs/components/content-blocks/vtex.store-components/buybutton/) in blocks such as the Shelf and the Product Details Page. This is because Minicart v2 was built based on an indirect dependency with the Add To Cart button. That means that any other shopping buttons, as the Buy Button, are unable to render Minicart v2, even if it was correctly configured in the code. `

| Prop name              | Type                      | Description                                                                                                                                                                                                                                     | Default value |
| ---------------------- | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `variation`            | `enum`                    | Minicart behavior when rendered. Possible values are: `popup` (it pops up on the Homepage in a minitab window) , `drawer` (it is rendered through a side bar) or `link` (when clicked on, it redirects the user to the Checkout page). | `drawer`    |
| `drawerSlideDirection` | `enum`                    | Slide direction for the `drawer` Minicart opening. Possible values are: `rightToLeft` or `leftToRight`).                                                                                                                                               | `rightToLeft` |
| `linkVariationUrl`     | `string`                  | Link associated to the `link` Minicart.                                                                                                                                                                                                       |   `undefined`            |
| `maxDrawerWidth`       | `number`                  | Maximum width (in pixels) for the `drawer` Minicart when opened.                                                                                                                                                                             | `440`         |
| `openOnHover`          | `boolean`                 | Whether the `popup` minicart should open when the user hovers over it.                                                                                                                                                                       | `false`         |
| `quantityDisplay`      | `enum`                    | Shows the quantity badge even when the amount of products in the cart is zero. Possible values are: `always` or `not-empty` or `never`).                                                                                                                | `not-empty` |
| `itemCountMode` | `enum` | Quantity badge behavior when displaying the number of total items added in Minicart. Possible values are: `total`  (quantity badge displays the number of items added to the cart), `distinct` (only displays the number of different products added to the cart), `totalAvailable`  (displays the number of available items added to the cart), and `distinctAvailable` (displays the number of different *and* available products added to the cart). | `distinct` |
| `backdropMode`         | `enum` | Controls whether the backdrop should be displayed when the `drawer` Minicart is opened or not. Possible values are: `visible` (rendering the backdrop) or `none` (rendering the `drawer` without backdrop).  | `none` |
| `MinicartIcon` | `block` | Icon displayed in the Minicart button. This prop's value must match the name of the block responsible for rendering the desired icon. | `icon-cart` (from [Store Icons](https://vtex.io/docs/components/all/vtex.store-icons/) app) |
| `customPixelEventId` | `string`   | Store event ID responsible for triggering the `minicart.v2` to automatically open itself on the interface. | `undefined`    |
| `customPixelEventName` | `string`   | Store event name responsible for triggering the `minicart.v2` to automatically open itself on the interface. Some examples are: `'addToCart'` and `'removeFromCart'`. Notice that using this prop will make the `minicart.v2` open in **every** event with the specified name if no `customPixelEventId` is specified. | `undefined`    |
| `classes`         | `CustomCSSClasses` | Used to override default CSS handles. To better understand how this prop works, we recommend reading about it [here](https://github.com/vtex-apps/css-handles#usecustomclasses). Note that this is only useful if you're importing this block as a React component.                                      | `undefined`           |

### Advanced Configuration

According to the `minicart.v2` composition, it can be highly customizable using other blocks. Currently, its default implementation is as follows:

```jsonc
// This is the default blocks implementation for the minicart-layout
{
  "minicart.v2": {
    "props": {
      "MinicartIcon": "icon-cart#minicart-icon"
    },
    "children": ["minicart-base-content"]
  },
  "icon-cart#minicart-icon": {
    "props": {
      "size": 24
    }
  },
  "minicart-base-content": {
    "blocks": ["minicart-empty-state"],
    "children": ["minicart-product-list", "flex-layout.row#minicart-footer"]
  },
  "flex-layout.row#minicart-footer": {
    "props": {
      "blockClass": "minicart-footer"
    },
    "children": ["flex-layout.col#minicart-footer"]
  },
  "flex-layout.col#minicart-footer": {
    "children": ["minicart-summary", "minicart-checkout-button"]
  },
  "minicart-product-list": {
    "blocks": ["product-list#minicart"]
  },
  "product-list#minicart": {
    "blocks": ["product-list-content-mobile"]
  },
  "minicart-summary": {
    "blocks": ["checkout-summary.compact#minicart"]
  },

  "checkout-summary.compact#minicart": {
    "children": ["summary-totalizers#minicart"],
    "props": {
      "totalizersToShow": ["Items", "Discounts"]
    }
  },
  "summary-totalizers#minicart": {
    "props": {
      "showTotal": true,
      "showDeliveryTotal": false
    }
  },
  "minicart-empty-state": {
    "children": ["flex-layout.row#empty-state"]
  },
  "flex-layout.row#empty-state": {
    "children": ["flex-layout.col#empty-state"]
  },
  "flex-layout.col#empty-state": {
    "children": [
      "icon-cart#minicart-empty-state",
      "rich-text#minicart-default-empty-state"
    ],
    "props": {
      "horizontalAlign": "center",
      "verticalAlign": "middle",
      "rowGap": 5
    }
  },
  "icon-cart#minicart-empty-state": {
    "props": {
      "size": 64,
      "blockClass": "minicart-empty-state"
    }
  },
  "rich-text#minicart-default-empty-state": {
    "props": {
      "text": "Your cart is empty."
    }
  }
}
```

By default implementation we mean that whenever you use `minicart.v2` in your store you're actually using the `json` above behind the scenes.

Therefore, in order to customize the Minicart configuration, you can simply copy the code above and change it as you wish.

For further information on how to configure each of the blocks used to compose `minicart.v2`, check out [Product List](https://vtex.io/docs/app/vtex.product-list) and [Checkout Summary](https://vtex.io/docs/app/vtex.checkout-summary).

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles                     |
| ------------------------------- |
| `arrowUp`                       |
| `minicartCheckoutButton`        |
| `minicartContainer`             |
| `minicartContentContainer`      |
| `minicartFooter`                |
| `minicartIconContainer`         |
| `minicartProductListContainer`  |
| `minicartQuantityBadge`         |
| `minicartSideBarContentWrapper` |
| `minicartTitle`                 |
| `minicartWrapperContainer`      |
| `popupChildrenContainer`        |
| `popupContentContainer`         |
| `popupWrapper`                  |

## Contributors

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/lucasayb"><img src="https://avatars2.githubusercontent.com/u/17356081?v=4" width="100px;" alt=""/><br /><sub><b>Lucas Antônio Yamamoto Borges</b></sub></a><br /><a href="https://github.com/vtex-apps/minicart/commits?author=lucasayb" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/lucaspacheco-acct"><img src="https://avatars0.githubusercontent.com/u/59736416?v=4" width="100px;" alt=""/><br /><sub><b>lucaspacheco-acct</b></sub></a><br /><a href="https://github.com/vtex-apps/minicart/commits?author=lucaspacheco-acct" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/gustavopvasconcellos"><img src="https://avatars1.githubusercontent.com/u/49173685?v=4" width="100px;" alt=""/><br /><sub><b>gustavopvasconcellos</b></sub></a><br /><a href="https://github.com/vtex-apps/minicart/commits?author=gustavopvasconcellos" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!