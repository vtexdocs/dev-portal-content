---
title: "CUSTOM LINK CARD"
slug: "americaneaglecl-link-card-custom"
excerpt: "americaneaglecl.link-card-custom@0.0.2"
hidden: true
createdAt: "2022-08-03T20:01:16.443Z"
updatedAt: "2022-08-03T20:01:16.443Z"
---
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)

Custom Image Gallery to display a series of images specifying their URL, alt text, redirect, maximum width, styles, and if it triggers an modal or not for desktop and mobile.

Desktop:

![Media Placeholder](./custom-link-card.jpg)

Mobile:

![Media Placeholder](./custom-link-card-mobile.jpg)

## Installation
1. Clone the repository and change the app manifest:
```
{
  "vendor": "<your-vendor>",
  "name": "custom-link-card",
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
<your-vendor>.custom-link-card: "0.x"
```
2. Create a new file named `<your-vendor>.custom-link-card.css` in the css folder and add the following styles.
```
.img {
  width: 100%;
  height: 100%;
}

@media only screen and (max-width: 639px) {
 .containerLinkCards__nowrap {
    overflow-x: auto;
    flex-flow: row nowrap;
 }
}

```
3. Declare the main application block in a given theme template or within another theme block. For example:
```
{
    "flex-layout.row#link-card-licores": {
        "title": "Link card: licores",
        "children": [
            "custom-link-card#licores"
        ]
    },
    "custom-link-card#licores": {
        "props": {
            "images": [
              {
                  "imgDesktop": {
                      "urlImgDesktop": "https://andina.micoca-cola.cl/arquivos/ENE21_licores_licores_760x400-DESK.png?v=637764045784670000",
                      "widthDesktop": "48.5"
                  },
                  "imgMobile": {
                      "urlImgMobile": "https://andina.micoca-cola.cl/arquivos/ENE22_licores_licores_300x500-MOB.png?v=637764046023070000",
                      "widthMobile": "45"
                  },
                  "alt": "",
                  "title": "",
                  "link": "",
                  "imgText": "",
                  "customPixelEventId": "",
                  "linkCardStyles": "center ph3",
                  "imageStyles": "br4",
                  "blockClass": ""
              },
              .
              .
              .
            ],
            "containerStyles": {
              "desktop": "",
              "tablet": "",
              "mobile": ""
            },
            "containerLinkCardsStyles": "",
            "containerLinkCardsStylesDefault": true,
            "carouselOnMobile": true,
            "visible": true
        }
    },
}
```

4. OPTIONAL: You can pass a component as a child to be rendered before the images. (Applies to use in PLPs that use customQuerys with slider-layout and then the image listing.). For example:

```
{
"custom-link-card#custom-search-licores": {
        "title": "Banner licores",
        "children": [
            "list-context.image-list#landing-licores"
        ],
        "props": {
            "images": [
                {
                  "imgDesktop": {
                      "urlImgDesktop": "http://micocacola.vteximg.com.br/arquivos/LandingLicores2021-categorias-piscos.jpg?v=637650735665670000",
                      "widthDesktop": 15
                  },
                  "imgMobile": {
                      "urlImgMobile": "http://micocacola.vteximg.com.br/arquivos/LandingLicores2021-categorias-piscos.jpg?v=637650735665670000",
                      "widthMobile": 30
                  },
                  "alt": "",
                  "title": "",
                  "link": "",
                  "imgText": "Pisco",
                  "linkCardStyles": "center ph3",
                  "imageStyles": "br4",
                  "blockClass": ""
                },
                .
                .
                .
            ],
            "containerStyles": {
              "desktop": "mt7",
              "tablet": "",
              "mobile": ""
            },
            "containerLinkCardsStyles": "",
            "containerLinkCardsStylesDefault": true,
            "carouselOnMobile": true,
            "visible": true
        }
    },
    "list-context.image-list#landing-licores": {
        "children": [
          "slider-layout#landing-licores"
        ],
        .
        .
        .
    },
    "slider-layout#landing-licores": {
        .
        .
        .
    }
}
```

**Result**: 

![Media Placeholder](./custom-link-card-customQuery.jpg)

## Props

| Prop name    | Type            | Description    | Default value                                                                                                                               |
| ------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | 
| `images` | `Array of Objects` |  Array of objects that defines the properties of each image and indicates whether it is a trigger for an event or not.  | `undefined`   |
| `containerStyles`      | `Object` |  It is the container that wraps the entire component. This container contains tachyon classes for `desktop`, `tablet` and `mobile` properties. Each property is a `string`  | `undefined`       |
| `containerLinkCardsStyles` | `String` | CSS tachyon styles for the container that wraps the parent container of the linkcard | `undefined`|
| `containerLinkCardsStylesDefault` | `Boolean` | CSS tachyon styles by default for the container that wraps the main container of the link card. These default styles are: `flex flex-wrap items-center justify-between` | `true`|
| `carouselOnMobile`      | `Boolean` |  Determines if the order of the images displayed in mobile will be in carousel mode with `nowrap` or ordered as `wrap` style.   | `true`       |
| `visible` | `Boolean` | Determines if the component should be shown or hidden | `true` |
| `blockClass` | `string Array` | blockClass Native from VTEX IO | `undefined` |

###  - `images` Array of objects:

| Prop name    | Type            | Description    | Default value                                                                                                                               |
| ------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | 
| `imgDesktop`      | `Object`       | Contains the properties for the desktop image       | `undefined`         |
| `imgMobile`      | `Object`       | Contains the properties for the mobile image        | `undefined`         |
| `link`      | `String`       | Link that will redirect to a URL when clicked         | `undefined`        |
| `alt`      | `String`       | Image SEO alt text         | `undefined`        |
| `title`      | `String`       | Image SEO title text         | `undefined`        |
| `imgText`      | `String`       | Informative text under the image       | `undefined`        |
| `customPixelEventId`      | `String`       | Name of the event which execute a specific event from the 'vtex.pixel-manager'  | `undefined`        |
| `linkCardStyles`      | `String`       | Classes of tachyons for linkCard | `undefined`        |
| `imageStyles`      | `String`       | Classes of tachyons for image inside linkcard  | `undefined`        |
| `blockClass`      | `String`       | Class that differentiates the element from the others  | `undefined`        |
| `analytics`      | `Object`       | Allows to trigger events to the dataLayer of google tag manager, when clicking on one of the images.  | `undefined`        |

- `imgDesktop` object:

| Prop name    | Type            | Description    | Default value                                                                                                                               |
| ------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | 
| `urlImgDesktop`      | `String`  | Contains the URL of the image for desktop using ui:widget from site-editor         | `undefined`        |
| `widthDesktop`      | `String or number`       | Width used by the image in %. It is not necessary to include the % sign. It can be number or text  | `undefined`        |

- `imgMobile` object:

| Prop name    | Type            | Description    | Default value                                                                                                                               |
| ------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | 
| `urlImgMobile`      | `String`  | Contains the URL of the image for mobile using ui:widget from site-editor    | `undefined`        |
| `widthMobile`      | `String or number`       | Maximum width used by the image in%. It is not necessary to include the % sign. It can be number or text  | `undefined`        |

- `analytics` object:

| Prop name    | Type            | Description    | Default value                                                                                                                               |
| ------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | 
| `analyticsToggle`      | `String`  | Determines if events should be logged by GTM. Possible values [ 'none', 'provide' ]    | `none`        |
| `promotionId`      | `String`       | Promotion Id for Google Tag Manager  | `undefined`        |
| `promotionName`      | `String`       | Promotion name for Google Tag Manager  | `undefined`        |
| `creativePosition`      | `String`       | Creative position for Google Tag Manager  | `undefined`        |


## Modus Operandi

When the application receives an array of objects, these must be mapped to represent the images with their corresponding props. Images will render for mobile and desktop devices based on the configured URL and % width the image will use.

The most important factor is defining whether the image contains the customPixelEventId attribute that defines whether to run an event or redirect to a URL.

Optionally, a VTEX component can be sent as a child to be rendered before the images.

For mobile styles you can change the way images are displayed in `phone`. They can be in carousel mode (no wrap and with overflow-x: auto to make a carousel effect) or in wrap mode so that they go down and are ordered according to the established % width.

Important: 

- The app can be edited from the site editor.
- For device phone, the `justify-between` style will be applied in the following condition: If device = `phone` and `carouselOnMobile` = true.

  This fixes a bug where certain elements disappear if `carouselOnMobile` is true.

## Customization

| CSS Handles |
| ----------- |
| `container` |
| `containerLinkCards` |
| `containerLinkCards__nowrap` |
| `containerChild` |
| `linkCard` |
| `img` |
| `link` |
| `imgText` |

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

- **Fabian Toro**