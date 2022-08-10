---
title: "Countdown"
slug: "ebeauty-countdown"
excerpt: "ebeauty.countdown@0.0.1"
hidden: true
createdAt: "2022-07-28T17:55:25.859Z"
updatedAt: "2022-07-28T17:55:25.859Z"
---
The `countdown` is the block responsible for showing a countdown block.

## Configuration

1. Import the `blacksipqa.countdown` app to your theme's dependencies in the `manifest.json`, for example:

```json
{
    "dependencies": {
        "blacksipqa.countdown": "0.x"
    }
}
```

2. Add the `countdown` block to any block below `store.home`. For example:

```json
{
    "store.home": {
        "blocks": [
            "countdown"
        ]
    }
}
```

| Prop name | Type     | Description | Default value  |
| --------- | -------- | ----------- | -------------- |
| `title`   | `String` | Text  | `null` |
| `targetDate`   | `String` | Final Date  | `null` |
| `showOnPage`   | `Boolean` | The block should be visible? | `false` |

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles             |
| ----------------------- |
| `container`           |
| `countdown`            |
| `title` |