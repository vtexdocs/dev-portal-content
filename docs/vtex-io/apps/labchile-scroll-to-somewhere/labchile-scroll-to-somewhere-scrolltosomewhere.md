---
title: "Count Down"
slug: "labchile-scroll-to-somewhere-scrolltosomewhere"
excerpt: "labchile.scroll-to-somewhere@0.0.1"
hidden: true
createdAt: "2022-08-09T01:33:22.269Z"
updatedAt: "2022-08-09T01:33:22.269Z"
---
The `scroll-to-somewhere` is the block responsible for scrolling to a specified element using the CSS class name.

## Configuration

1. Import the `blacksipqa.scroll-to-somewhere` app to your theme's dependencies in the `manifest.json`, for example:

```json
{
    "dependencies": {
        "blacksipqa.scroll-to-somewhere": "0.x"
    }
}
```

2. Add the `scroll-to-somewhere` block to any block. For example:

```json
{
    "store.home": {
        "blocks": ["scroll-to-somewhere"]
    },
    "scroll-to-somewhere":{
        "props":{
            "text":"Conocer más acerca del producto",
            "cssClassName":"vtex-store-components-3-x-productDescriptionContainer"
        }
    }
}
```

| Prop name      | Type                  | Description                            | Default value          |
| -------------- | --------------------- | -------------------------------------- | ---------------------- |
| `text`         | `String` | Text to display                            | `null` |
| `cssClassName`  | `String`              | Name of the CSS class that is wished to be scrolled to | `null`                  |

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles    |
| -------------- |
| `container`    |
| `text` |