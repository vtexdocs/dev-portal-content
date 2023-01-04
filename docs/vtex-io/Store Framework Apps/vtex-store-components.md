---
title: "VTEX Store Components"
slug: "vtex-store-components"
excerpt: "vtex.store-components@3.163.4"
hidden: true
createdAt: "2020-06-03T15:19:50.043Z"
updatedAt: "2022-11-22T18:39:22.812Z"
---
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-17-orange.svg?style=flat-square)](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/vtex-io/Store Framework Apps/#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

VTEX Store Components is a collection of components that can be used to create/extend others VTEX apps.


- [VTEX Store Components](#vtex-store-components)
  - [Usage](#usage)
  - [Styles API](#styles-api)
  - [Components](#components)
  - [Creating a new component](#creating-a-new-component)
    - [Project structure](#project-structure)
  - [Troubleshooting](#troubleshooting)
  - [Contributing](#contributing)
  - [Tests](#tests)
    - [Travis CI](#travis-ci)
  - [Contributors](#contributors)

## Usage

The Store Components collection uses the `store` builder with the blocks architecture. Please refer to our [Builder](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-builders) documentation to learn more about the `store` builder. 

To use this app, you must import it as dependency of your project in the `manifest.json` file.

```json
  "dependencies": {
    "vtex.store-components": "3.x"
  }
```

Then, you can start adding components to your store theme app.

## Styles API

The Store Components collection provides some CSS classes as an API for style customization.

To use this CSS API, you must add the `styles` builder and create an app styling CSS file.

1. Add the `styles` builder to your `manifest.json`:

```json
  "builders": {
    "styles": "2.x"
  }
```

2. Create a file called `vtex.store-components.css` inside the `styles/css` folder. Add your custom styles:

```css
.container {
  margin-top: 10px;
}
```

## Components

For more information, check the documentation of all components of the Store Components collection.

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


> ⚠️ **The following blocks have been deprecated:** `Animation`, `Categories Highlights`, `Collection Badges`, `Container`, `Discount Badge`, `Gradient Collapse`, `Greeting`, `Slider`. Despite this, support for them is still granted.

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

[![Build Status](https://api.travis-ci.org/vtex-apps/store-components.svg?branch=master)](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-store-components-0.png)

<!-- DOCS-IGNORE:start -->
## Contributors

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/hapoza"><img src="https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-store-components-1.png"></img></a></td>
    <td align="center"><a href="https://github.com/JNussens"><img src="https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-store-components-2.png"></img></a></td>
    <td align="center"><a href="https://github.com/lucasayb"><img src="https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-store-components-3.png"></img></a></td>
    <td align="center"><a href="https://t.co/LTjWBxRnqE"><img src="https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-store-components-4.png"></img></a></td>
    <td align="center"><a href="https://github.com/Erislandio"><img src="https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-store-components-5.png"></img></a></td>
    <td align="center"><a href="https://github.com/BeatrizMiranda"><img src="https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-store-components-6.png"></img></a></td>
    <td align="center"><a href="https://github.com/Jayendra88"><img src="https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-store-components-7.png"></img></a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/pgrimaud"><img src="https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-store-components-8.png"></img></a></td>
    <td align="center"><a href="https://www.linkedin.com/in/igorpoubel"><img src="https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-store-components-9.png"></img></a></td>
    <td align="center"><a href="http://www.hugoccosta.com"><img src="https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-store-components-10.png"></img></a></td>
    <td align="center"><a href="https://github.com/MatheusR42"><img src="https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-store-components-11.png"></img></a></td>
    <td align="center"><a href="https://github.com/LuisaFCorrea"><img src="https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-store-components-12.png"></img></a></td>
    <td align="center"><a href="https://github.com/pmarignan"><img src="https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-store-components-13.png"></img></a></td>
    <td align="center"><a href="https://github.com/rcmuniz1994"><img src="https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-store-components-14.png"></img></a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/ovio224"><img src="https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-store-components-15.png"></img></a></td>
    <td align="center"><a href="https://github.com/LucasCastroJussi"><img src="https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-store-components-16.png"></img></a></td>
    <td align="center"><a href="https://razvanudrea.com"><img src="https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-store-components-17.png"></img></a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

<!-- DOCS-IGNORE:end -->

**Upcoming documentation:**

 - [Render logo as amp-img if in AMP page](https://github.com/vtex-apps/store-components/pull/580)
 - [Update CSS handles on ProductSpecification](https://github.com/vtex-apps/store-components/pull/599)

 - [Including classes on searchBar to identify when is open and/or filled](https://github.com/vtex-apps/store-components/pull/792)