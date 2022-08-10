---
title: "outletespacohering-components"
slug: "heringhomolog-heringhomolog-components"
excerpt: "heringhomolog.heringhomolog-components@0.45.63"
hidden: true
createdAt: "2022-07-21T10:57:56.834Z"
updatedAt: "2022-08-05T19:16:18.951Z"
---
![OUTLET COMPONENTS STORE](https://static.hering.com.br/store/_ui/desktop/theme-outlet/images/square-logo-outlet.jpg)

## Description

- Here will be all the customized components of the Hering Outlet store

## Table of Contents

- [Usage](#usage)
  - [Styles API](#styles-api)
- [Components Specs](#components-specs)
- [Pattern](#Pattern)

## Usage

This app uses our store builder with the blocks architecture. To know more about Store Builder [click here.](https://help.vtex.com/en/tutorial/understanding-storebuilder-and-stylesbuilder#structuring-and-configuring-our-store-with-object-object)

To use this app, you need to import in your dependencies on `manifest.json`.

```json
  "dependencies": {
    "outletespacohering.outletespacohering-components": "0.x"
  }
```

Then, you can add a component block into your app theme.

### Styles API

This app provides some CSS classes as an API for style customization.

To use this CSS API, you must add the `styles` builder and create an app styling CSS file.

1. Add the `styles` builder to your `manifest.json`:

```json
  "builders": {
    "styles": "1.x"
  }
```

2. Create a file called `outletespacohering.outletespacohering-components.css` inside the `styles/css` folder. Add your custom styles:

```css
.containerBenefits {
  margin-top: 10px;
  display: flex;
}
```

## Components Specs

Below we have a README for each component of this project that explains how to use them.

- [Benefits bar](BenefitsBar.md)
- [Carousel custom](CarouselCustom.md)
- [Editable top bar](EditableTopBar.md)
- [Hot Spot](HotSpot.md)
- [Limited Offer](LimitedOffer.md)
- [List Items](ListItems.md)
- [Newsletter custom](ListItems.md)
- [Search Bar](SearchBarCustom.md)
- [Visibility layout](VisibilityLayout.md)
- [User name custom](ListItems.md)

## Pattern

- Files ending with JSX
- Dividing files by folders

<!-- DOCS-IGNORE:start -->

## Devs

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/Erislandio"><img src="https://avatars1.githubusercontent.com/u/34255207?v=4" width="100px;" alt=""/><br /><sub><b>Erislandio</b></sub></a><br /><a href="https://github.com/vtex-apps/store-components/commits?author=Erislandio" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->