---
title: "Checkout UI Settings With Cross Selling"
slug: "levimx-checkout-ui-settings"
excerpt: "levimx.checkout-ui-settings@0.2.53"
hidden: true
createdAt: "2022-07-06T14:13:53.996Z"
updatedAt: "2022-08-08T16:39:13.308Z"
---
The Checkout UI Settings app is responsible for **customizing your store's Checkout UI through scripts**.

The main advantage of using the app instead of the [store's admin](https://help.vtex.com/tutorial/configure-template-in-smartcheckout-update--ToTE5XB39t0SwtHgpgwSv?locale=en) for this customization is that your Checkout scripts will behave as configurations for platform apps.

In practice, it means that Checkout UI Settings allows A/B testing in your store's scripts, in addition to the possibility of quick rollbacks for old scripts (i.e. scripts pertaining to older Checkout UI Settings app's versions).

Also this application allows to show the Cross Selling or a product collection.

## Configuration

1.  Using your terminal and the [VTEX IO Toolbelt](https://vtex.io/docs/recipes/development/vtex-io-cli-installment-and-command-reference), log into the desired account;
2.  In the `manifest.json` file, change the predefined default value `vendor` to the name of the account in which you want to install the app;
3.  Run the `npm run dev` command and keeping it running to copy any change to route /checkout-ui-custom, that you working in the files in /src.;
4.  Run `vtex link` to syncs the app in the current directory with the development workspace in use.;
5.  When you are done making changes, you must run the `npm run build` command to obfuscate the source code. Now you can publish the app;

## Remember 🚨

Just you must <mark>work</mark> files like in /src and not in /checkout-ui-custom;

<br>

### `shelfProps` props

| Prop name                 | Type      | Description                                                                                                                      | Default value                                    |
| ------------------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| `suggestionsContainer`    | `string`  | JQuery selector of element in which the content will be inserted (can use class or id selector)                                  | `.cart-template.full-cart .cart-template-holder` |
| `suggestionsInsertMethod` | `emun`    | Method to be used to insert the suggestions container. Possible values are: `append`, `prepend`, `insertBefore` or `insertAfter` | `append`                                         |
| `collectionId`            | `string`  | Collection to show in carousel. This setting will ignore if useCrosseling is true                                                |
| `shelfOrdenation`         | `enum`    | Decides which order products must follow when displayed.                                                                         | `1`                                              |
| `suggestionsTitle`        | `string`  | Header for cross selling section                                                                                                 |
| `currency`                | `string`  | Currency to format prices.                                                                                                       | `MXN`                                            |
| `btnDefaultText`          | `string`  | Add to cart button default text.                                                                                                 |
| `btnLoadingText`          | `string`  | Add to cart button loading element or text                                                                                       |
| `successText`             | `string`  | Item to cart success message text                                                                                                |
| `useCrossSelling`         | `boolean` | If method to get items use cross selling apis                                                                                    | `false`                                          |
| `crossSellingStrategy`    | `enum`    | Type of recommendations that will be displayed in the Shelf.                                                                     |
| `showWithoutStock`        | `boolean` | If the items without stock should be displayed                                                                                   |
| `showSkusWithoutStock`    | `boolean` | If the sku selector button without stock should be displayed                                                                     | `false`                                          |
| `resolution`              | `number`  | Resolution to change slider                                                                                                      | `550`                                            |
| `sliderConfig`            | `object`  | Carousel config props                                                                                                            |

<br>

### `shelfOrdenation` enum values

ℹ️ _Only works with collectionId fetch items method._

| Value | Description                        |
| ----- | ---------------------------------- |
| `1`   | Order By Price DESC                |
| `2`   | Order By Price ASC                 |
| `3`   | Order By Top Sale DESC             |
| `4`   | Order By Release Date DESC         |
| `5`   | Order By Best Discount DESC        |
| `6`   | Order By Order By Review Rate DESC |

<br>

### `crossSellingStrategy` enum values

ℹ️ _This setting will ignore if useCrosseling is false_

| Value | Description            |
| ----- | ---------------------- |
| `1`   | Who Saw Also Saw       |
| `2`   | Who Saw Also Bought    |
| `3`   | Who Bought Also Bought |
| `4`   | Accessories            |
| `5`   | Similars               |
| `6`   | Suggestions            |

<br>

### `sliderConfig` props

| Prop name        | Type      | Description                                                                                                                                                                                                                                                                                    | Default value |
| ---------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `accessibility`  | `boolean` | Enables tabbing and arrow key navigation                                                                                                                                                                                                                                                       | `true`        |
| `appendArrows`   | `string`  | Change where the navigation arrows are attached (Selector, htmlString, Array, Element, jQuery object)                                                                                                                                                                                          | `$(element)`  |
| `dots`           | `boolean` | Show dot indicators                                                                                                                                                                                                                                                                            | `false`       |
| `arrows`         | `boolean` | If the carousel should show arrows                                                                                                                                                                                                                                                             | `true`        |
| `infinite`       | `boolean` | Infinite loop sliding                                                                                                                                                                                                                                                                          | `true`        |
| `slidesToShow`   | `int`     | Number of slides to show                                                                                                                                                                                                                                                                       | `1`           |
| `slidesToScroll` | `number`  | Number of slides to scroll                                                                                                                                                                                                                                                                     | `1`           |
| `lazyLoad`       | `emun`    | Set lazy loading technique. Accepts 'ondemand' or 'progressive'                                                                                                                                                                                                                                | `ondemand`    |
| `responsive`     | `object`  | Object containing breakpoints and settings objects (see demo). Enables settings sets at given screen width. Set settings to "unslick" instead of an object to disable slick at a given breakpoint. This prop object must contain the [responsive](/https://kenwheeler.github.io/slick/) props. | `none`        |

### Example:

```json
 responsive: [
      {
        breakpoint: 980,
        settings: { slidesToShow: 4, slidesToScroll: 4 },
      },
      {
        breakpoint: 750,
        settings: { slidesToShow: 2.5, centerMode: true, arrows: false, swipeToSlide: true },
      },
      {
        breakpoint: 550,
        settings: { slidesToShow: 1.5, centerMode: true, arrows: false, swipeToSlide: true },
      },
  ]
```

## Modus Operandi

Once the app is deployed and installed in the account, every scripts contained in it will be automatically linked to your store and used to [build the templates](https://help.vtex.com/tutorial/configure-template-in-smartcheckout-update--ToTE5XB39t0SwtHgpgwSv?locale=en#configuring-templates-from-the-code-menu) to customize your Checkout.

:warning: **Scripts used by Checkout are linked to the Checkout UI Settings version that's installed in your store**. If a prior app version was already installed and your want to change the scripts linked to it, you'll need to repeat the already existing code and thereafter launch the app's new version containing the changes you just did. Housekeeper is responsible for updating app versions in the accounts it's installed in.