---
title: "Custom image with Analytics"
slug: "philipsmx-custom-image-analytics"
excerpt: "philipsmx.custom-image-analytics@0.0.5"
hidden: true
createdAt: "2022-07-19T23:51:28.796Z"
updatedAt: "2022-07-19T23:51:28.796Z"
---
custom image with props to track campaigns in Analytics.

## Configuration

Declare the block in the theme of your store with the following accessories 

```
  "one-block-image#withAnalyticsProps": {
    "props": {
      "blockClass": "mainBannerItem",
      "image": {
        "desktop": "https://philipsmx.vtexassets.com/arquivos/BANNER_COLLAGE_SINGLE_2_desktop.jpg",
        "mobile": "https://philipsmx.vteximg.com.br/arquivos/BANNER_COLLAGE_SINGLE_2_mobile.jpg",
        "altText": "Banner 1"
      },
      "link": {
        "url": "/singles-month"
      },
      "analytics": {
        "analyticsProperties": true,
        "promotionId": "12345",
        "promotionName": "test_image_analytics",
        "promotionPosition": "bannerPrincipal"
      }
    }
  }
```

Description props

```
  "one-block-image#withAnalyticsProps": {
    "props": {
      "blockClass": "Your custom class",
      "image": {
        "desktop": "Desktop image",
        "mobile": "Mobile image",
        "altText": "Alt text to show when image doesn't load"
      },
      "link": {
        "url": "Url to redirect when user click in image"
      },
      "analytics": {
        "analyticsProperties": "Add analytics properties or not",
        "promotionId": "Id to track promotion",
        "promotionName": "Name to analytics promotion",
        "promotionPosition": "Promotion position"
      }
    }
  }
```

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles            |
| ---------------------- |
| `imageContainer` |
| `imageLink`    |
| `image` |

## Contributors ✨

- Jorge Luis Aguilar Rodarte


### Copyright Ecomsur 2021