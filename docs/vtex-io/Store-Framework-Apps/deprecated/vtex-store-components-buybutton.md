---
title: "Buy Button"
slug: "vtex-store-components-buybutton"
hidden: false
createdAt: "2020-06-03T16:04:30.375Z"
updatedAt: "2022-11-22T18:39:23.054Z"
---
> ⚠️ **The Buy Button block has been deprecated in favor of the [Add To Cart Button app](https://developers.vtex.com/vtex-developer-docs/docs/vtex-add-to-cart-button/).** Although support for this block is still granted, we strongly recommend you to update your store theme with the Add to Cart Button's blocks in order to keep up with the component's evolution.

![https://img.shields.io/badge/-Deprecated-red](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-store-components-buybutton-0.png)

The `buy-button` block displays a button that allows users to add products in the [Minicart](https://developers.vtex.com/vtex-developer-docs/docs/vtex-minicart) (`minicart.v1`).

> ⚠️ **The Buy Button block only works for stores using the Minicart v1**. If your store uses the Minicart v2, please refer to the [Add To Cart Button](https://developers.vtex.com/vtex-developer-docs/docs/vtex-add-to-cart-button) instead.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-store-components-buybutton-1.png)

## Configuration

1. Import the `vtex.store-components` app to your theme's dependencies in the `manifest.json` file as in the following example:

```diff
  "dependencies": {
+   "vtex.store-components": "3.x"
  }
```

2. Add the `buy-button` to other theme block using the product context, such as the `product-summary.shelf`. In the following example, the `buy-button` component was added to the `flex-layout.row` block from the `store.product` template (which uses the product context):

```diff
  "store.product": {
    "children": [
      "flex-layout.row#product",
    ]
  },
  "flex-layout.row#product": {
    "children": [
+      "buy-button#product"
    ]
  },
```

3. Then, declare the `buy-button` block using the props stated in the [Props](#props) table. For example:

```json
  "buy-button#product": {
    "props": {
      "isOneClickBuy": true,
      "showTooltipOnSkuNotSelected": false
    }
  },
```

### Props

| Prop name            | Type      | Description                                                                      | Default value      |
| -------------------- | --------- | -------------------------------------------------------------------------------- | ------------------ |
| `available`          | `boolean` | Whether the Buy Button block is available for using (`true`) or not (`false`). | `true` |
| `customToastURL`     | `string`  | Defines the link to where users will be redirected when the Buy Button is clicked on and the `isOneClickBuy` prop is set to `true`. | `/checkout/#/cart` |
| `isOneClickBuy`      | `boolean` | Whether the user should be redirected to the checkout page (`true`) or not (`false`) when the Add To Cart Button is clicked on.        |  `false`              |
| `large`              | `boolean` | Whether the Buy Button should fill its whole width (`true`) or not (`false`). | `false`    |
| `shouldOpenMinicart` | `boolean` | Whether the Minicart should be opened when the Buy Button is clicked on (`true`) or not (`false`).                              | `false`              |
| `shouldAddToCart`    | `boolean` | Whether the Buy Button should add products to the minicart when clicked on (`true`) or not (`false`).         | `true`          |
| `showItemsPrice`     | `boolean` | Whether the total price of items added to the cart should be displayed (`true`) or not (`false`).                 | `false`              |
| `showToast`          | `boolean` | Whether a Toast (pop-up notification) should be displayed when adding an item to the minicart (`true`) or not (`false`)    | `false`                 |
| `showTooltipOnSkuNotSelected` | `boolean` | Whether a tooltip should be displayed when the Buy Button is clicked on with no SKU was selected (`true`) or not (`false`). | `true` |

## Customization

To apply CSS customizations in this and other blocks, follow the [Using CSS handles for store customization](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-css-handles-for-store-customization) guide.

| CSS Handles |
| --- |
| `buttonDataContainer` |
| `buttonItemsPrice`    |
| `buyButtonText`       |