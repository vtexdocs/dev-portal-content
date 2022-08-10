---
title: "Carousel Custom"
slug: "hering-hering-components-carouselcustom"
excerpt: "hering.hering-components@0.45.64"
hidden: true
createdAt: "2022-07-05T23:59:30.443Z"
updatedAt: "2022-08-08T11:42:33.076Z"
---
## Description

- Carousel of videos and customized images

![desktop](https://res.cloudinary.com/acct/image/upload/v1600198530/acct/banner_bsra4t.png)

### Table of Contents

- [Usage](#usage)
  - [Configuration](#configuration)
  - [Styles API](#styles-api)
    - [CSS Namespaces](#css-namespaces)

## Usage

You should follow the usage instruction in the main [README](/README.md#usage).

To import it into your code:

```JSON
{
   "list-context.custom-carousel#home": {
        "children": [
            "slider-layout#carousel-images"
        ],
        "props": {
            "images": [
                {
                    "price": "59,99",
                    "title": "Blusas",
                    "priceLabel": "a partir de",
                    "subTitle": "Perfeitas para você",
                    "descriptionBanner": "* Válido nesse link para loja virtual Hering Outlet.",
                    "video": "",
                    "image": "https://outletespacohering.vteximg.com.br/arquivos/banner-mobile-home.jpg",
                    "mobileImage": "https://outletespacohering.vteximg.com.br/arquivos/banner-mobile-home.jpg",
                    "imgLink": "",
                    "buttons": [
                        {
                            "buttonLabel": "Feminino",
                            "buttonLink": "#"
                        },
                        {
                            "buttonLabel": "Masculino",
                            "buttonLink": "#"
                        }
                    ]
                },
                {
                    "price": "59,99",
                    "title": "Blusas",
                    "priceLabel": "a partir de",
                    "subTitle": "Perfeitas para você",
                    "descriptionBanner": "* Válido nesse link para loja virtual Hering Outlet.",
                    "video": "",
                    "": "https://outletespacohering.vteximg.com.br/arquivos/banner-mobile-home.jpg",
                    "mobileImage": "https://outletespacohering.vteximg.com.br/arquivos/banner-mobile-home.jpg",
                    "imgLink": "",
                    "buttons": [
                        {
                            "buttonLabel": "Feminino",
                            "buttonLink": "#"
                        },
                        {
                            "buttonLabel": "Masculino",
                            "buttonLink": "#"
                        }
                    ]
                }
            ],
            "displayIcons": true
        }
    }
```

### Configuration

| Prop name      | Type        | Description |
| -------------- | ----------- | ----------- |
| `images`       | `images[]!` | Image list  |
| `displayIcons` | `Boolean`   | Show icons? |

- Possible values of `images`:

| Prop name     | Type        | Description       |
| ------------- | ----------- | ----------------- |
| `image`       | `String!`   | Desktop image     |
| `mobileImage` | `String!`   | Mobile image      |
| `buttons`     | `buttons[]` | Action Buttons    |
| `priceLabel`  | `String`    | Label above price |
| `title`       | `String`    | Banner title      |
| `subTitle`    | `String`    | Banner subtitle   |
| `video`       | `String`    | Video URL         |

- Possible values of `buttons`:

### Styles API

You should follow the Styles API instruction in the main [README](/README.md#styles-api).

### Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles                     |
| ------------------------------- |
| `carouselActionContainerMobile` |
| `carouselActionContent`         |
| `anchorButtonContainer`         |
| `anchorButtonContent`           |
| `anchorButtonText`              |
| `carouselImage`                 |
| `descriptionContainer`          |
| `descriptionTextBottom`         |
| `titleBanner`                   |
| `subTitleBanner`                |
| `priceContainer`                |
| `priceLabel`                    |
| `priceContent`                  |
| `video`                         |
| `currencyBanner`                |