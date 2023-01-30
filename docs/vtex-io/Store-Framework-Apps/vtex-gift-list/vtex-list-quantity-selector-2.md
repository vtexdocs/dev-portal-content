---
title: "Quantity Selector"
hidden: false
createdAt: "2022-09-16T12:16:38.317Z"
updatedAt: "2022-09-21T13:14:31.287Z"
---
The quantity selector is made up of three blocks `quantity-selector-minicart`, `quantity-selector-shelf-guest` and `quantity-selector-shelf-owner-list` and each of them represents a quantity selector for different contexts which are use in mini-cart, guest shelf, list owner shelf and selection modal on search page.

![QuantitySelector](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-list-quantity-selector-2-0.gif)

## Configuration

1. Import the `vtex.list` app to your theme's peer dependencies in the `manifest.json` file as in the following example:

```json
  "peerDependencies": {
    "vtex.list": "2.x"
  }
```

2. Add the `quantity-selector` block to other theme block using a product context, such as the `product-summary.shelf`. For example:

```diff
  "product-summary.shelf":{
    "children":[
      "flex-layout.col"
    ]
  },
  
  "flex-layout.col": {
    "children": [      
      "product-summary-price#desktopPriceGuest",
+     "quantity-selector-shelf-guest",
    ]
  }
```

## Customization - "quantity-selector-minicart"

To apply CSS customizations in this and other blocks, follow the [Using CSS handles for store customization](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-css-handles-for-store-customization) guide.

| CSS Handles |
| --- |
| `quantitySelectorWrapper` |
| `quantitySelectorButton`    |
| `quantitySelectorDecrease`    |
| `quantitySelectorIncrease`    |

## Customization - "quantity-selector-shelf-guest"

To apply CSS customizations in this and other blocks, follow the [Using CSS handles for store customization](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-css-handles-for-store-customization) guide.

| CSS Handles |
| --- |
| `quantitySelectorContainer` |
| `quantitySelectorTitle`    |
| `availableQuantityContainer`    |

## Customization - "quantity-selector-shelf-owner-list"

To apply CSS customizations in this and other blocks, follow the [Using CSS handles for store customization](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-css-handles-for-store-customization) guide.

| CSS Handles |
| --- |
| `summaryContainer` |
| `quantitySelectorContainer`    |
| `quantitySelectorTitle`    |
| `availableQuantityContainer`    |
| `quantitySelectorStepper`    |