---
title: "Product Summary Buy Button"
slug: "sonoma-product-summary-productsummarybuybutton"
excerpt: "sonoma.product-summary@0.0.22"
hidden: true
createdAt: "2022-07-26T02:31:27.836Z"
updatedAt: "2022-08-09T01:24:15.939Z"
---
Product Summary Buy Button is a block exported by the Product Summary app responsible for rendering a Buy Button in the Product Summary Shelf block.

![](https://user-images.githubusercontent.com/52087100/76864047-38006600-683f-11ea-8a4e-74dc91712984.png)

:warning: **The Product Summary Buy Button only effectively function i.e. only adds products to the Minicart if the store still uses the [Minicart v1](https://github.com/vtex-apps/minicart/blob/383d7bbd3295f06d1b5854a0add561a872e1515c/docs/README.md)**. When using the [Minicart v2](https://vtex.io/docs/components/all/vtex.minicart/), you should configure the [Add To Cart Button](https://vtex.io/docs/components/all/vtex.add-to-cart-button/) in the `product-summary.shelf` block instead.

## Configuration

1. Add the [Product Summary app](https://vtex.io/docs/components/content-blocks/sonoma.product-summary/) to your theme's dependencies on the `manifest.json`, for example:

```json
  dependencies: {
    "sonoma.product-summary": "0.x"
  }
```

2. Add the `product-summary-buy-button` block as a children of the `product-summary.shelf` block:

```diff
 {
   "product-summary.shelf": {
       "children": [
           "product-summary-image",
           "product-summary-name",
           "product-rating-inline",
           "product-summary-space",
           "product-summary-price",
+          "product-summary-buy-button"
       ]
   },
 }
```

3. Then, declare the `product-summary-buy-button` and configure its behavior using the props stated below.

```json
{
  "product-summary-buy-button": {
    "props": {
      "isOneClickBuy": false
    }
  }
}
```

### Props

| Prop name           | Type      | Description                                                                                 | Default value         |
| ------------------- | --------- | ------------------------------------------------------------------------------------------- | --------------------- |
| `isOneClickBuy`     | `boolean` | Whether the user should be redirected to Checkout after clicking on the Buy Button (`true`) or not (`false`). | `false` |
| `buyButtonText`     | `string`  | Custom text that overwrites the default Buy Button text.                                     | `undefined`           |
| `displayBuyButton`  | `enum`    | Sets the Buy Button display mode. Possivle values are: `displayButtonAlways` (it will always be displayed), `displayButtonHover` (only displayed on hover), or `displayButtonNone` (it will be hidden for users). | `displayButtonAlways` |
| `customToastURL`    | `string`  | Defines a redirect link to the Toast displayed when an item is added to your cart. | `/checkout/#/cart` |
| `buyButtonBehavior` | `enum`    | Sets the Buy Button behavior when it is clicked on. Possible values are: `alwaysGoToProduct` (redirect users to the product page), `default` (redirect users to the minicart), or `alwaysAddToTheCart` (add the selected SKU to the minicart). When choosing this last option, be careful: use it only if there are SKU Selectors for each product variation. This way, users can properly select their desired SKU. | `default` |

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles |
| --- |
| `buyButtonContainer` |
| `buyButton` |
| `isHidden` |