---
title: "Product Summary Image"
slug: "cea-cea-product-summary-productsummaryimage"
excerpt: "cea.cea-product-summary@0.23.0"
hidden: true
createdAt: "2022-07-14T17:15:53.812Z"
updatedAt: "2022-08-09T12:32:19.371Z"
---
## Description

`ProductSummaryImage` is a VTEX Component that renders the product's image.
This Component can be imported and used by any VTEX App.

:loudspeaker: **Disclaimer:** Don't fork this project; use, contribute, or open issue with your feature request.

## Table of Contents

- [Product Summary Image](#product-summary-image)
  - [Description](#description)
  - [Table of Contents](#table-of-contents)
  - [Usage](#usage)
    - [Blocks API](#blocks-api)
    - [Configuration](#configuration)
    - [Styles API](#styles-api)
      - [CSS namespaces](#css-namespaces)

## Usage

You should follow the usage instruction in the main [README](https://github.com/vtex-apps/product-summary/blob/master/README.md#usage).

Then, add `product-summary-image` block into your app theme, as we do in our [Product Summary app](https://github.com/vtex-apps/product-summary/blob/master/store/blocks.json).

### Blocks API

This component has an interface that describes which rules must be implemented by a block when you want to use the `ProductSummaryImage`.

```json
  "product-summary-image": {
    "component": "ProductSummaryImage"
  }
```

### Configuration

Through the Storefront, you can change the `ProductSummaryImage`'s behavior and interface. However, you also can make in your theme app.

| Prop name         | Type      | Description                                                                                                                                                              | Default value |
| ----------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------- |
| `showBadge`       | `Boolean` | Set the discount badge's visibility                                                                                                                                      | `true`        |
| `badgeText`       | `String`  | Text shown on badge                                                                                                                                                      |               |
| `showCollections` | `Boolean` | Set collection badges' visibility                                                                                                                                        | `false`       |
| `displayMode`     | `Enum`    | Set display mode of product summary (normal, inline)                                                                                                                     | `normal`      |
| `hoverImageLabel` | `String`  | Set this value to match the value of the `imageLabel` field of a product image, so this "secondary" image will be showed when user hovers its mouse over this component. | `""`          |
| `mainImageLabel` | `String` | Works the same way as `hoverImageLabel` but to set the main image to display. If you pass a label and no image has that label, it will show the main image of the product | `""`|
| `width` | `[ResponsiveInput<Number>](https://github.com/vtex-apps/responsive-values#vtexresponsive-values)`  | Sets the image width. | `undefined`          |
| `height` | `[ResponsiveInput<Number>](https://github.com/vtex-apps/responsive-values#vtexresponsive-values)`  | Sets the image height. | `undefined`          |

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
.imageContainer {
  margin-top: 10px;
}
```

#### CSS Handles

| CSS Handles           | Description                                                             | Component Source                                                      |
| --------------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `imageContainer`      | The main container of image                                             | [index](/react/components/ProductSummaryImage/ProductSummaryImage.js) |
| `imageNormal`         | Class when display mode is normal                                       | [index](/react/components/ProductSummaryImage/ProductSummaryImage.js) |
| `imageInline`         | Class when display mode is inline                                       | [index](/react/components/ProductSummaryImage/ProductSummaryImage.js) |
| `imageStackContainer` | Class for container with product images to be shown                     | [index](/react/components/ProductSummaryImage/ProductSummaryImage.js) |
| `hoverImage`          | Class for image that appears when user hovers mouse                     | [index](/react/components/ProductSummaryImage/ProductSummaryImage.js) |
| `hoverEffect`         | Class that applies hover effect and changes images. Override carefully. | [index](/react/components/ProductSummaryImage/ProductSummaryImage.js) |