---
title: "Background Color"
slug: "trackfield-store-components-background"
excerpt: "trackfield.store-components@0.18.0"
hidden: true
createdAt: "2022-07-05T22:31:25.046Z"
updatedAt: "2022-08-04T10:48:21.346Z"
---
the component allows the client to change the background color of the stripe section

![Media Placeholder](https://gitlab.com/acct.global/program-04/track-and-field-io/trackandfield.store-theme/uploads/49dba0d7e0dff4f1c9ba3beda1b86719/image.png)

## Configuration

1. Add the `store-components` app to your theme's dependencies in the `manifest.json`, for example:

```diff
"dependencies": {
+  "trackfield.store-components": "0.x"
}
```

2. you are now able to use the background

```json
{
  "background": {
    "children": ["rich-text#stripe-text"]
  }
}

```

### `background` props

| Prop name  | Type     | Description                                                                      | Default value |
| ---------- | -------- | -------------------------------------------------------------------------------- | ------------- |
| `color`    | `string` | saves the value corresponding to the hexadecimal number of the background color. | `""`          |
| `children` | `any`    | set the vtex block as a child.                                                   | `""`          |

## Customization

The first thing that should be present in this section is the sentence below, showing users the recipe pertaining to CSS customization in apps:

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

Thereafter, you should add a single column table with the available CSS handles for the app, like the one below. Note that the Handles must be ordered alphabetically.

| CSS Handles  |
| ------------ |
| `background` |