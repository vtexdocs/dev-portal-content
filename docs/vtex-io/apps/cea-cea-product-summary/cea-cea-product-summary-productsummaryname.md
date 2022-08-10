---
title: "Product Summary Name"
slug: "cea-cea-product-summary-productsummaryname"
excerpt: "cea.cea-product-summary@0.23.0"
hidden: true
createdAt: "2022-07-14T17:15:53.796Z"
updatedAt: "2022-08-09T12:32:19.199Z"
---
## Description

`ProductSummaryName` is a VTEX Component that renders the product's name.
This Component can be imported and used by any VTEX App.

:loudspeaker: **Disclaimer:** Don't fork this project; use, contribute, or open issue with your feature request.

## Table of Contents
- [Usage](#usage)
  - [Blocks API](#blocks-api)
  - [Configuration](#configuration)
  - [Styles API](#styles-api)

## Usage

You should follow the usage instruction in the main [README](https://github.com/vtex-apps/product-summary/blob/master/README.md#usage).

Then, add `product-summary-name` block into your app theme, as we do in our [Product Summary app](https://github.com/vtex-apps/product-summary/blob/master/store/blocks.json).

### Blocks API

This component has an interface that describes which rules must be implemented by a block when you want to use the `ProductSummaryName`.

```json
  "product-summary-name": {
    "component": "ProductSummaryName"
  }
```

### Configuration

Through the Storefront, you can change the `ProductSummaryName`'s behavior and interface. However, you also can make in your theme app.

You can find all options available in [Store Components Product Name app](https://github.com/vtex-apps/store-components/blob/master/react/components/ProductName/README.md).

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
.nameContainer {
  margin-top: 10px;
}
```

#### CSS Handles

| CSS Handles   | Description                                          | Component Source                     |
| ------------ | ---------------------------------------------------- | ------------------------------------ |
| `nameContainer` | The main container of name | [index](/react/components/ProductSummaryName/ProductSummaryName.js) |