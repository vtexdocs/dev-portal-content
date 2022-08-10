---
title: "CUSTOM CURRENT YEAR COPYRIGHT"
slug: "ninaherrera-custom-current-year-copyright"
excerpt: "ninaherrera.custom-current-year-copyright@0.0.3"
hidden: true
createdAt: "2022-07-07T22:57:27.124Z"
updatedAt: "2022-07-08T19:44:49.093Z"
---
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)

Custom current year copyright that shows the current year established by the machine and the copyrights.

![Media Placeholder](./custom-current-year-copyright.jpg)

## Installation 
1. Clone the repository and change the app manifest:
```
{
  "vendor": "<your-vendor>",
  "name": "custom-current-year-copyright",
  "version": "0.0.0",
  .
  .
  .
}
```
2. Login to your vtex account:
```
> vtex login <development-environment>
```
3. Select your workspace and use `vtex link`:
```
> vtex use <workspace>
> vtex link
```

## Block ⚙
1. Adding the app as a theme dependency in the `manifest.json` file:
```
<your-vendor>.custom-current-year-copyright: "0.x"
```
2. Create a new file named `<your-vendor>.custom-current-year-copyright.css` in the css folder and add the following styles.
```
.container  {
    text-align: center;
    color: white;
    font-size: .7rem;
    line-height: 1.3rem;
}
```
3. Declare the main application block in a given theme template or within another theme block. For example:
```
{
  "flex-layout.row#copyright": {
    "children": [
      "custom-current-year-copyright#footer"
    ]
  },
  "custom-current-year-copyright#footer": {
    "props": {
      "brand": "Coca-Cola",
      "copyright": "Todos los derechos reservados.",
      "endText": "Ecommerce implementado y operado por Ecomsur"
    }
  },
}
```

## Props

| Prop name    | Type            | Description    | Default value                                                                                                                               |
| ------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | 
| `brand` | `String` |  Brand name  | `undefined`   |
| `year`      | `String` |  If you don't want the year to be actomatic, you can enter one.  |    `undefined`    |
| `copyright`      | `String` |  Text representing copyright  |    `undefined`     |
| `endText`      | `String` |  Text located in the lower area  |    `undefined`     |

## Modus Operandi

The app receives the props and represents them in Span and P tags.

 ** The app can be edited from the site editor. **

## Customization

| CSS Handles |
| ----------- |
| `container` |
| `brand` |
| `copyrightText` |
| `endText` |

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

- **Fabian Toro**