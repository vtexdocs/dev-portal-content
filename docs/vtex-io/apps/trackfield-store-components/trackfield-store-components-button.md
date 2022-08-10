---
title: "Button"
slug: "trackfield-store-components-button"
excerpt: "trackfield.store-components@0.18.0"
hidden: true
createdAt: "2022-07-05T22:31:25.129Z"
updatedAt: "2022-08-04T10:48:21.308Z"
---
## Description

This is a button (or Call to Action) that have all of it components editable by site-editor, including hover effect for `background-color` and `color`.

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
  "button#example": {
    "props": {
      "text": "VER MAIS",
      "color": "#d0e588",
      "backgroundColor": "#9F316E",
      "borderColor": "#9F316E",
      "hoverBackgroundColor": "#d0e588",
      "hoverColor": "#9F316E"
    }
  }
}
```

## `button` props

| Prop name              | Type      | Description                                                | Default value |
| ---------------------- | --------- | ---------------------------------------------------------- | ------------- |
| `text`                 | `string`  | text that will be show inside the button                   | `ver mais`    |
| `color`                | `string`  | color for the text                                         | `#000`        |
| `backgroundColor`      | `string`  | color for the background                                   | `#fff`        |
| `hoverBackgroundColor` | `string`  | color for the hover effect on background                   | `#fff`        |
| `hoverColor`           | `string`  | color for the hover effect on text                         | `#000`        |
| `link`                 | `string`  | link for when the button is clicked                        | `#`           |
| `hasPseudoClasses`     | `boolean` | if it has the pseudo-class `:after` and `:before` as lines | `false`       |
| `activate`             | `boolean` | activate the component                                     | `true`        |
| `borderColor`          | `string`  | the color of the border                                    | `transparent` |

## Customization

The first thing that should be present in this section is the sentence below, showing users the recipe pertaining to CSS customization in apps:

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

Thereafter, you should add a single column table with the available CSS handles for the app, like the one below. Note that the Handles must be ordered alphabetically.

| CSS Handles |
| ----------- |
| `button`    |
| `after`     |
| `before`    |