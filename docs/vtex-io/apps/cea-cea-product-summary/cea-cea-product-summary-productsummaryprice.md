---
title: "Product Summary Price"
slug: "cea-cea-product-summary-productsummaryprice"
excerpt: "cea.cea-product-summary@0.23.0"
hidden: true
createdAt: "2022-07-14T17:15:53.814Z"
updatedAt: "2022-08-09T12:32:19.196Z"
---
## Description

`ProductSummaryPrice` is a VTEX Component that renders the product's price.
This Component can be imported and used by any VTEX App.

:loudspeaker: **Disclaimer:** Don't fork this project; use, contribute, or open issue with your feature request.

## Table of Contents
- [Product Summary Price](#product-summary-price)
  - [Description](#description)
  - [Table of Contents](#table-of-contents)
  - [Usage](#usage)
    - [Blocks API](#blocks-api)
    - [Configuration](#configuration)
    - [Styles API](#styles-api)
      - [CSS namespaces](#css-namespaces)

## Usage

You should follow the usage instruction in the main [README](https://github.com/vtex-apps/product-summary/blob/master/README.md#usage).

Then, add `product-summary-price` block into your app theme, as we do in our [Product Summary app](https://github.com/vtex-apps/product-summary/blob/master/store/blocks.json).

### Blocks API

This component has an interface that describes which rules must be implemented by a block when you want to use the `ProductSummaryPrice`.

```json
  "product-summary-price": {
    "component": "ProductSummaryPrice"
  }
```

### Configuration

Through the Storefront, you can change the `ProductSummaryPrice`'s behavior and interface. However, you also can make in your theme app.

| Prop name           | Type      | Description                      | Default value |
| ------------------- | --------- | -------------------------------- | ------------- |
| `showListPrice`     | `Boolean` | Shows the product list price     | `true`        |
| `showInstallments`  | `Boolean` | Set installments' visibility     | `true`        |
| `showDiscountValue`  | `Boolean` | Set discount value's visibility     | `false`        |
| `showLabels`        | `Boolean` | Set pricing labels' visibility   | `true`        |
| `labelSellingPrice` | `String`  | Text of selling price's label    |               |
| `labelListPrice`    | `String`  | Text of list price's label       |               |   
| `showBorders`       | `Boolean` | Set product's borders visibility | `false`       |
| `showListPriceRange`       | `Boolean` | Set if you want to see list price as range (lowest - highest) when available | `false`       |
| `showSellingPriceRange`       | `Boolean` | Set if you want to see selling price as range (lowest - highest) when available | `false`       |

### Styles API

This app provides some CSS classes as an API for style customization.

To use this CSS API, you must add the `styles` builder and create an app styling CSS file.

1. Add the `styles` builder to your `manifest.json`:

```json
  "builders": {
    "styles": "1.x"
  }
```

2. Create a file called `vtex.product-summary.css` inside the `styles/css` folder. Add your custom styles:

```css
.priceContainer {
  margin-top: 10px;
}
```

#### CSS Handles

| CSS Handles           |
| ------------------- |
| `priceContainer` |
| `productPriceClass` |
| `listPriceContainer` |
| `listPriceLabel` |
| `listPrice` |
| `sellingPriceContainer` |
| `sellingPriceLabel` |
| `sellingPrice` |
| `savingsContainer` |
| `savings` |
| `interestRate` |
| `installmentContainer` |
| `listPriceRange` |
| `sellingPriceRange` |
| `priceLoading` |