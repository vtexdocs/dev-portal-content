---
title: "Test - VTEX Store components"
slug: "test-vtex-store-components"
hidden: true
createdAt: "2021-10-04T13:37:00.677Z"
updatedAt: "2021-10-25T14:03:06.461Z"
---

## Usage

This app uses our store builder with the blocks architecture. To know more about Store Builder [click here.](https://help.vtex.com/en/tutorial/understanding-storebuilder-and-stylesbuilder#structuring-and-configuring-our-store-with-object-object)

To use this app, you need to import in your dependencies on `manifest.json`.

```json
  "dependencies": {
    "vtex.store-components": "3.x"
  }
```

Then, you can add a component block into your app theme as we do with `product-price` in our [Product Details app](https://github.com/vtex-apps/product-details/blob/master/store/blocks.json).

For example, now you can change the behavior of `product-price` block that is in the product details. See an example of how to configure:

```json
"product-price": {
  "props": {
    "showListPrice": true,
    "showLabels": false,
  }
}
```

### Styles API

This app provides some CSS classes as an API for style customization.

To use this CSS API, you must add the `styles` builder and create an app styling CSS file.

1. Add the `styles` builder to your `manifest.json`:

```json
  "builders": {
    "styles": "1.x"
  }
```

2. Create a file called `vtex.store-components.css` inside the `styles/css` folder. Add your custom styles:

```css
.container {
  margin-top: 10px;
}
```

## Components Specs

Below we have a documentation for each component of this project that explains how to use them.

- [Availability Subscriber](https://developers.vtex.com/vtex-developer-docs/docs/vtex-store-components-availabilitysubscriber)
- [Back To Top Button](https://developers.vtex.com/vtex-developer-docs/docs/vtex-store-components-backtotopbutton)
- [Buy Button](https://developers.vtex.com/vtex-developer-docs/docs/vtex-store-components-buybutton)
- [Image](https://developers.vtex.com/vtex-developer-docs/docs/vtex-store-components-image)
- [InfoCard](https://developers.vtex.com/vtex-developer-docs/docs/vtex-store-components-infocard)
- [Logo](https://developers.vtex.com/vtex-developer-docs/docs/vtex-store-components-logo)
- [Newsletter](https://developers.vtex.com/vtex-developer-docs/docs/vtex-store-components-newsletter)
- [Product Brand](https://developers.vtex.com/vtex-developer-docs/docs/vtex-store-components-productbrand)
- [Product Description](https://developers.vtex.com/vtex-developer-docs/docs/vtex-store-components-productdescription)
- [Product Images](https://developers.vtex.com/vtex-developer-docs/docs/vtex-store-components-productimages)
- [Product Name](https://developers.vtex.com/vtex-developer-docs/docs/vtex-store-components-productname)
- [Product SKU Attributes](https://developers.vtex.com/vtex-developer-docs/docs/vtex-store-components-productskuattributes)
- [Product Price](https://developers.vtex.com/vtex-developer-docs/docs/vtex-store-components-productprice)
- [Product Specifications](https://developers.vtex.com/vtex-developer-docs/docs/vtex-store-components-productspecifications)
- [SKU Selector](https://developers.vtex.com/vtex-developer-docs/docs/vtex-store-components-skuselector)
- [Search Bar](https://developers.vtex.com/vtex-developer-docs/docs/vtex-store-components-searchbar)
- [Share](https://developers.vtex.com/vtex-developer-docs/docs/vtex-store-components-share)
- [Shipping Simulator](https://developers.vtex.com/vtex-developer-docs/docs/vtex-store-components-shippingsimulator)
- [Notification](https://developers.vtex.com/vtex-developer-docs/docs/vtex-store-components-notification)


> ⚠️ **The following blocks have been deprecated:** `Animation`, `Categories Highlights`, `Collection Badges`, `Container`, `Discount Badge`, `Gradient Collapse`, `Greeting`, `Slider`. 
> Despite this, support for them is still granted.

## Creating a new component

To start your development, create a new folder on react/components. That's where your source code will be stored. Also create a new js file on /react, this file should be used to expose your component, like:

### Project structure

Inside your `react/components/<component_name>` you should have:

- index.js
- README.md
- [Optional] components/
- [Optional] constants/
- [Optional] utils/
- [Optional] queries/
- [Optional] mutations/
- [Optional] styles.css

Next, inside of `react/` folder you need to export your component, such as:

```js
import ProductPrice from './components/ProductPrice/index'

export default ProductPrice
```

Also, all dependencies needed should be inserted inside the react/package.json.

## Troubleshooting

You can check if others are passing through similar issues [here](https://github.com/vtex-apps/store-components/issues). Also feel free to [open issues](https://github.com/vtex-apps/store-components/issues/new) or contribute with pull requests.

## Contributing

Check it out [how to contribute](https://github.com/vtex-apps/awesome-io#contributing) with this project.

## Tests

To execute our tests go to `react/` folder and run `yarn test`

### Travis CI

[![Build Status](https://api.travis-ci.org/vtex-apps/store-components.svg?branch=master)](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/test-vtex-store-components-0.png)
