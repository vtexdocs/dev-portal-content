---
title: "Editable Top Bar"
slug: "hering-hering-components-hotspot"
excerpt: "hering.hering-components@0.45.64"
hidden: true
createdAt: "2022-07-05T23:59:30.474Z"
updatedAt: "2022-08-08T11:42:33.031Z"
---
## Description

- This component allows the customer to place markings above an image, when clicked it displays a product

![desktop](https://res.cloudinary.com/acct/image/upload/v1600199434/acct/topbar_bkeg1g.png)

- [Usage](#usage)
  - [Configuration](#configuration)
  - [Styles API](#styles-api)
    - [CSS Namespaces](#css-namespaces)

## Usage

You should follow the usage instruction in the main [README](/README.md#usage).

To import it into your code:

```JSON
{
    "hotspot-desktop#default": {
        "blocks": ["product-summary.shelf#shelf-content--default"],
        "props": {
            "activeHotspot": true,
            "areas": [
                {
                    "areaName": "1",
                    "image": "/arquivos/post4.png",
                    "spots": [
                        {
                            "name": "shorts-saia-cintura-alta-com-fenda-frontal---laranja-copy-3-",
                            "eixoX": 10,
                            "eixoY": 10
                        },
                        {
                            "name": "shorts-saia-cintura-alta-com-fenda-frontal---laranja-copy-3-",
                            "eixoX": 20,
                            "eixoY": 20
                        }
                    ]
                }
            ]
        },
        "title": "shop the look desktop"
    }
  }
```

### Configuration

| Prop name       | Type       | Description                            |
| --------------- | ---------- | -------------------------------------- |
| `activeHotspot` | `Boolean!` | Should you show the hotspot?           |
| `areas`         | `areas[]!` | Areas of each banner with the markings |

- Possible values of `areas`:

| Prop name  | Type       | Description                                                                         |
| ---------- | ---------- | ----------------------------------------------------------------------------------- |
| `areaName` | `String!`  | Name of the banner area, remember that the names must be different for each section |
| `image`    | `String!`  | Banner image                                                                        |
| `spots`    | `Spots[]!` | Spots are the markings of each axis                                                 |

- Possible values of `Spots[]`:

| Prop name | Type      | Description                                                               |
| --------- | --------- | ------------------------------------------------------------------------- |
| `name`    | `String!` | product slug name, must be the same name as the `product` graphql request |
| `eixoX`   | `Number`  | Spot Y axis position                                                      |
| `eixoY`   | `Number`  | Spot X axis position                                                      |

### Styles API

You should follow the Styles API instruction in the main [README](/README.md#styles-api).

### Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles                    |
| ------------------------------ |
| hotspotContainer               |
| galleryContainer               |
| hotspotProductSummary          |
| hotspotContainer               |
| activeImageContainer           |
| gallery--inactive              |
| hotspotProductSummaryTitle     |
| hotspotProductSummaryHeader    |
| hotspotProductSummaryComponent |
| hotspotProductSummaryTitle     |
| hotspotProductSummaryText      |
| hotspotProductSummaryLink      |
| activeImageContainer           |
| actionButtonDefault            |
| noActiveImageContainer         |
| noActiveImages                 |
| imgActiverContainer            |
| gallery                        |
| gallery--inactive              |
| areaImage                      |
| activeAreaButton               |
| MobileGalleryContainer         |
| arrowContainerClass            |
| smallSpinner                   |
| spotCard                       |