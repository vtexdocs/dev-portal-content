---
title: "Product Summary Buy Button"
slug: "cea-cea-product-summary-productsummarybuybutton"
excerpt: "cea.cea-product-summary@0.23.0"
hidden: true
createdAt: "2022-07-14T17:15:53.806Z"
updatedAt: "2022-08-09T12:32:19.726Z"
---
## Description

`ProductSummaryBuyButton` is a VTEX Component that renders the buy button.
This Component can be imported and used by any VTEX App.

:loudspeaker: **Disclaimer:** Don't fork this project; use, contribute, or open issue with your feature request.

## Table of Contents
- [Usage](#usage)
  - [Blocks API](#blocks-api)
  - [Configuration](#configuration)
  - [Styles API](#styles-api)

## Usage

You should follow the usage instruction in the main [README](https://github.com/vtex-apps/product-summary/blob/master/README.md#usage).

Then, add `product-summary-buy-button` block into your app theme, as we do in our [Product Summary app](https://github.com/vtex-apps/product-summary/blob/master/store/blocks.json).

### Blocks API

This component has an interface that describes which rules must be implemented by a block when you want to use the `ProductSummaryBuyButton`.

```json
  "product-summary-buy-button": {
    "component": "ProductSummaryBuyButton"
  }
```

### Configuration

Through the Storefront, you can change the `ProductSummaryBuyButton`'s behavior and interface. However, you also can make in your theme app.

| Prop name           | Type      | Description                                                                                 | Default value         |
| ------------------- | --------- | ------------------------------------------------------------------------------------------- | --------------------- |
| `isOneClickBuy`     | `Boolean` | Should redirect to checkout after clicking on buy                                           | `false`               |
| `buyButtonText`     | `String`  | Custom buy button text                                                                      |                       |
| `displayBuyButton`  | `Enum`    | Set display mode of buy button (displayButtonAlways, displayButtonHover, displayButtonNone) | `displayButtonAlways` |
| `customToastURL`  | `String`    | Set the link associated with the Toast created when adding an item to your cart.  | `/checkout/#/cart` |
| `buyButtonBehavior` | `Enum` | What the buy button should do when you click it, if you pass `default` it will add to cart only if there is only one SKU of that product (default, alwaysGoToProduct) | `default`

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
.buyButtonContainer {
  margin-top: 10px;
}
```

#### CSS Handles

| CSS Handles   | Description                                          | Component Source                     |
| ------------ | ---------------------------------------------------- | ------------------------------------ |
| `buyButtonContainer` | The main container of buy button | [index](/react/components/ProductSummaryBuyButton/ProductSummaryBuyButton.js) |
| `buyButton` | Class right before buy button | [index](/react/components/ProductSummaryBuyButton/ProductSummaryBuyButton.js) |
| `isHidden` | Class when button is hidden | [index](/react/components/ProductSummaryBuyButton/ProductSummaryBuyButton.js) |