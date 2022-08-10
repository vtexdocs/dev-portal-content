---
title: "Title"
slug: "trackfield-store-components-title"
excerpt: "trackfield.store-components@0.18.0"
hidden: true
createdAt: "2022-07-05T22:31:25.072Z"
updatedAt: "2022-08-04T10:48:21.239Z"
---
## Description

This is a title component where can hava a background image or not and is editable in site-editor.

## Configuration

1. Add the `store-components` app to your theme's dependencies in the `manifest.json`, for example:

```diff
"dependencies": {
+  "trackfield.store-components": "0.x"
}
```

2. you are now able tu use the button in any part of your store

```json
{
  "title#sale-shelf": {
    "props": {
      "text": "Sale",
      "color": "#9F316E",
      "hasBackground": true,
      "backgroundImage": "assets/images/banners/banner_sale_title.png"
    }
  }
}
```

## `title` props

| Prop name         | Type      | Description                              | Default value |
| ----------------- | --------- | ---------------------------------------- | ------------- |
| `text`            | `string`  | text that will be show inside the button | `ver mais`    |
| `color`           | `string`  | color for the text                       | `#000`        |
| `hasBackground`   | `boolean` | if has a background image                | `false`       |
| `backgroundImage` | `string`  | background image url                     | `undefined`   |

## Customization

The first thing that should be present in this section is the sentence below, showing users the recipe pertaining to CSS customization in apps:

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

Thereafter, you should add a single column table with the available CSS handles for the app, like the one below. Note that the Handles must be ordered alphabetically.

| CSS Handles |
| ----------- |
| `title`     |