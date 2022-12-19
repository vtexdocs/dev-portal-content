---
title: "Product Summary Buy Button"
slug: "vtex-product-summary-productsummarybuybutton"
excerpt: "vtex.product-summary@2.80.1-perftest.1"
hidden: false
createdAt: "2020-06-09T14:48:52.864Z"
updatedAt: "2022-07-02T00:50:32.936Z"
---
Product Summary Buy Button is the block exported by the [Product Summary app](https://developers.vtex.com/vtex-developer-docs/docs/vtex-product-summary) responsible for rendering a Buy Button in the [Product Summary Shelf](https://developers.vtex.com/vtex-developer-docs/docs/vtex-product-summary-productsummaryshelf) block.

![buy-button](https://user-images.githubusercontent.com/52087100/76864047-38006600-683f-11ea-8a4e-74dc91712984.png)

>⚠️ **The Product Summary Buy Button only effectively adds products to the Minicart if the store still uses the [Minicart v1](https://github.com/vtex-apps/minicart/blob/383d7bbd3295f06d1b5854a0add561a872e1515c/docs/README.md)**. If the store uses the [Minicart v2](https://vtex.io/docs/components/all/vtex.minicart/), please configure the [Add To Cart Button](https://developers.vtex.com/vtex-developer-docs/docs/vtex-add-to-cart-button/) in the `product-summary.shelf` block instead.

## Configuration

1. Import the `vtex.product-summary` app to your theme's dependencies in the `manifest.json`:

```json
  dependencies: {
    "vtex.product-summary": "2.x"
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

To apply CSS customizations in this and other blocks, follow the [Using CSS Handles for store customization](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-css-handles-for-store-customization) guide.

| CSS Handles |
| --- |
| `buyButtonContainer` |
| `buyButton` |
| `isHidden` |