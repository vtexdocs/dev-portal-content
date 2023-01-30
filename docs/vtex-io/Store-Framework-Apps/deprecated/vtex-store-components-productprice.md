---
title: "Product Price"
slug: "vtex-store-components-productprice"
hidden: false
createdAt: "2020-06-25T18:52:51.079Z"
updatedAt: "2022-11-22T18:39:23.079Z"
---
![https://img.shields.io/badge/-Deprecated-red](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-store-components-productprice-0.png)

> ⚠️ **The Product Price block has been deprecated in favor of the [Product Price](https://developers.vtex.com/docs/guides/vtex-product-price) app**. Although support for this block is still granted, we strongly recommend you to update your store theme with the Product Price's blocks in order to keep up with the component's evolution.

The `product-price` component is responsible for **displaying the price** of a given product.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-store-components-productprice-1.png)

## Configuration

1. Import the `vtex.store-components` app to your theme's dependencies in the `manifest.json` file as in the following example:

```json
  "dependencies": {
    "vtex.store-components": "3.x"
  }
```

2. Add the `product-price` block to any child of the `store.product` template (Product Details Page template). For example:

```diff
  "store.product": {
    "children": [
      "flex-layout.row#product",
    ]
  },
  "flex-layout.row#product": {
    "children": [
+     "product-price"
    ]
  },
```

3. Then, declare the `product-price` block using the props stated in the [Props](#props) table. For example:

```json
   "product-price": {
    "props": {
      "showSavings": true,
      "showListPrice": false
    }
  },
```

### Props

| Prop name               | Type      | Description                           | Default value |
| ----------------------- | --------- | ------------------------------------- | ------------- |
| `blockClass`            | `String`  | The set value functions as a customization identifier for any CSS specified in the block | null | 
| `labelListPrice`        | `String`  | Product list price label              | null          |
| `labelSellingPrice`     | `String`  | Product selling price label           | null          |
| `sellingPrices`         | `Array`   | Product list of selling prices        | `[]`            |
| `showInstallments`      | `Boolean` | Set visibility of installments        | `false`         |
| `showLabels`            | `Boolean` | Set visibility of labels              | `true`          |
| `showListPrice`         | `Boolean` | Set visibility of list price          | `true`          |
| `showListPriceRange`    | `Boolean` | Set visibility of list price range    | `false`         |
| `showSavings`           | `Boolean` | Set visibility of savings             | `false`         |
| `showSellingPriceRange` | `Boolean` | Set visibility of selling price range | `false`         |

## Customization

To apply CSS customizations in this and other blocks, follow the [Using CSS handles for store customization](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-css-handles-for-store-customization) guide.

| CSS Handles                 |
| -------------------------- |
| `price_className` |
| `price_installment` |
| `price_installmentContainer` |
| `price_interestRate` |
| `price_listPrice` |
| `price_listPriceContainer` |
| `price_listPriceLabel` |
| `price_listPriceRange` |
| `price_loader` |
| `price_savings` |
| `price_savingsContainer` |
| `price_sellingPrice` |
| `price_sellingPriceContainer` |
| `price_sellingPriceLabel` |
| `price_sellingPriceRange` |