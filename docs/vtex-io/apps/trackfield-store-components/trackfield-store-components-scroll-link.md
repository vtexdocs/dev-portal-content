---
title: "ScrollLink component"
slug: "trackfield-store-components-scroll-link"
excerpt: "trackfield.store-components@0.18.0"
hidden: true
createdAt: "2022-07-20T08:59:14.928Z"
updatedAt: "2022-08-04T10:48:21.290Z"
---
Render a button with an icon when clicked scroll the page to a target class.

## Getting Started

1. Add the `store-components` app to your theme's dependencies in the `manifest.json`, for example:

```diff
"dependencies": {
+  "trackfield.store-components": "0.x"
}
```

2. Now you can use the scroll component anywhere in your store

```json
{
  "scroll-link": {
    "props": {
      "refClass": "vtex-flex-layout-0-x-flexRow--whats-app-stripe",
      "refClassDesktop": "vtex-flex-layout-0-x-flexRow--whats-app-stripe"
    }
  }
}
```

## `scrollLink` props

| Prop name         | Type     | Description                                                                      | Default value |
| ----------------- | -------- | -------------------------------------------------------------------------------- | ------------- |
| `refClass`        | `string` | classe de referencia do mobile que determina até onde o scroll deverá acontecer  | ` `           |
| `offset`          | `number` | mobile scroll aditional px                                                       | 0             |
| `refClassDesktop` | `string` | classe de referencia do desktop que determina até onde o scroll deverá acontecer | ` `           |
| `offsetDesktop`   | `number` | desktop scroll aditional px                                                      | 0             |
| `IconCustom`      | `string` | icon's block that will render inside button                                      | ''            |

## Customization

The first thing that should be present in this section is the sentence below, showing users the recipe pertaining to CSS customization in apps:

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

Thereafter, you should add a single column table with the available CSS handles for the app, like the one below. Note that the Handles must be ordered alphabetically.

| CSS Handles  |
| ------------ |
| `scrollLink` |