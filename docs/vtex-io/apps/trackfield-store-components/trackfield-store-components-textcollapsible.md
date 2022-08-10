---
title: "Text Collapsible"
slug: "trackfield-store-components-textcollapsible"
excerpt: "trackfield.store-components@0.18.0"
hidden: true
createdAt: "2022-08-04T10:48:21.336Z"
updatedAt: "2022-08-04T10:48:21.336Z"
---
Component renders a collapsible text.

## Configuration

1. Add the `store-components` app to your theme's dependencies in the `manifest.json`, for example:

```diff
"dependencies": {
+  "trackfield.store-components": "0.x"
}
```

2. You are now able to use Text Collapsible component entering the necessary props.

```json
{
  "text-collapsible": {
    "props": {
      "text": "texto",
      "charQuantityMobile": 200,
      "charQuantityDesktop": 550
    }
  }
}
```

# `Text Collapsible` Props

| Prop name             | Type     | Description                                                      | Default value |
| ---------------       | -------- | --------------------------------------------------------------   | ------------- |
| `text`                | `string` | Text to be displayed.                                            | `""`          |
| `charQuantityMobile`  | `number` | Number of characters that will be displayed layout on mobile.    | `200`         |
| `charQuantityDesktop` | `number` | Number of characters that will be displayed layout on desktop.   | `550`         |

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles                               |
| ----------------------------------------  |
| `text-collapsible`                        |
| `text-collapsible__content`               |
| `text-collapsible__description`           |
| `text-collapsible__icon`                  |
| `text-collapsible__description--isOpen`   |
| `text-collapsible__description--isClosed` |