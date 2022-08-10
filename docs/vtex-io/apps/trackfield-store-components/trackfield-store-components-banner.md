---
title: "Full Banner"
slug: "trackfield-store-components-banner"
excerpt: "trackfield.store-components@0.18.0"
hidden: true
createdAt: "2022-07-05T22:31:25.107Z"
updatedAt: "2022-08-04T10:48:21.299Z"
---
Banner with call to action, a solution to have texts and call to action button inside the banners, and editables.

![Media Placeholder](https://gitlab.com/acct.global/program-04/track-and-field-io/trackandfield.store-components/uploads/22608fb8027b4600a949a6856e9d818c/image.png)

## Configuration

1. Add the `store-components` app to your theme's dependencies in the `manifest.json`, for example:

```diff
"dependencies": {
+  "trackfield.store-components": "0.x"
}
```

2. you are now able tu use the banner, inside the banner-list-context or on a single banner

```json
{
  "banner#colection-banner": {
    "props": {
      "image": "https://trackfield.vteximg.com.br/arquivos/ids/240286/1596x485%20(2).jpg?v=637709469601870000",
      "mobileImage": "https://trackfield.vteximg.com.br/arquivos/ids/239897/banner_ilha_475_445.jpg?v=637702750481930000"
    }
  }
}
```

3. You are now able to use the `list-context.banner-list` block, exported by the bannerFull app. The block allows you to display banner itens in your store with a higher degree of composability, since you can use it along with other `list-context` blocks to create a more flexible and customizable banner slider. In any desired theme template, add the `list-context.banner-list` block, declaring inside the [slider-layout](https://vtex.io/docs/app/vtex.slider-layout) block as child. For example:

```json
{
  "list-context.banner-list": {
    "children": ["slider-layout#banner"],
    "props": {
      "banners": [
        {
          "image": "https://trackfield.vteximg.com.br/arquivos/ids/239890/banner_ilha_1920_768.jpg?v=637702747738670000",
          "mobileImage": "https://trackfield.vteximg.com.br/arquivos/ids/239897/banner_ilha_475_445.jpg?v=637702750481930000"
        },
        {
          "image": "https://trackfield.vteximg.com.br/arquivos/ids/238748/banner_home_principal_1920_768_b",
          "mobileImage": "https://trackfield.vteximg.com.br/arquivos/ids/239494/banner_cores_475_445a.jpg?v=637690336493100000"
        }
      ]
    }
  },
  "slider-layout#banner": {
    "props": {
      "itemsPerPage": {
        "desktop": 1,
        "tablet": 1,
        "phone": 1
      },
      "infinite": true,
      "showNavigationArrows": "desktopOnly",
      "blockClass": "banners"
    }
  }
}
```

### `banner` props

| Prop name                 | Type     | Description                                                                                         | Default value |
| ------------------------- | -------- | --------------------------------------------------------------------------------------------------- | ------------- |
| `titleText`               | `string` | a principal text to show on banner                                                                  | `Headline`    |
| `titleTextColor`          | `string` | color for a title on callToAction                                                                   | `#000`        |
| `subtitleText`            | `string` | a sub text to show on banner                                                                        | `Headline`    |
| `subtitleTextColor`       | `string` | color for a sub text on callToAction                                                                | `#000`        |
| `helpText`                | `string` | a support text to show on banner                                                                    | `Headline`    |
| `helpTextColor`           | `string` | color for a help text on callToAction                                                               | `#000`        |
| `textAlignment`           | `enum`   | this is an align the call to action text. Possible values are: `LEFT`, `CENTER`,`RIGHT`             | `LEFT`        |
| `verticalAlignment`       | `enum`   | this align the call to action on vertical possible values are: `TOP`, `CENTER`,`BOTTOM`             | `TOP`         |
| `horizontalAlignment`     | `enum`   | this align the call to action on horizontal possible values are: `TOP`, `CENTER`,`BOTTOM`           | `LEFT`        |
| `imageLink`               | `string` | banner redirect link                                                                                | `#`           |
| `bannerTitle`             | `string` | title attribute for the link                                                                        | `""`          |
| `image`                   | `string` | a image to be uploaded                                                                              | `undefined`   |
| `mobileImage`             | `string` | a imagem rendered only on mobile                                                                    | `undefined`   |
| `title`                   | `string` | `title` and `alt` atribute to the image                                                             | `""`          |
| `videoFile`               | `string` | a video to be uploaded rendered on desktop, OBS: video has a priority against images                | `undefined`   |
| `videoFileMobile`         | `string` | a video rendered only on mobile OBS: video has a priority against images                            | `undefined`   |


### `button` props


| Prop name              | Type     | Description                              | Default value |
|------------------------|----------|------------------------------------------|---------------|
| `link`                 | `string` | link for when the button is clicked      | `""`          |
| `text`                 | `string` | text that will be show inside the button | `""`          |
| `color`                | `string` | color for the text                       | `""`          |
| `backgroundColor`      | `string` | color for the background                 | `""`          |
| `hoverBackgroundColor` | `string` | color for the hover effect on background | `""`          |
| `hoverColor`           | `string` | color for the hover effect on text       | `""`          |



### `list-context.bannerList` props

| Prop name | Type    | Description                 | Default value |
| --------- | ------- | --------------------------- | ------------- |
| `banners` | `array` | The same of `banner` blocks | `[]`          |

## Data-layer events

This banner will dispatch events to the data-layer, named `promotionClick` and have the following attributes:
the id will be the ID in the banner image source, parsed by this component.
and the name will be the props BannerTitle

```javascript
{
  event: 'promotionClick',
  ecommerce: {
    currencyCode: 'BRL',
    promoClick: { promotions: [{ name: bannerTitle id: parsedBannerUrlImage }] },
  },
}
```

## Customization

The first thing that should be present in this section is the sentence below, showing users the recipe pertaining to CSS customization in apps:

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

Thereafter, you should add a single column table with the available CSS handles for the app, like the one below. Note that the Handles must be ordered alphabetically.

| CSS Handles                        |
| ---------------------------------- |
| `banner__calltoaction`             |
| `banner__button-wrapper`           |
| `banner__image`                    |
| `banner__video`                    |
| `banner__container`                |
| `banner__container--title-text`    |
| `banner__container--subtitle-text` |
| `banner__container--support-text`  |