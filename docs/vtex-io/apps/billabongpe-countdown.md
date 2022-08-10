---
title: "Countdown"
slug: "billabongpe-countdown"
excerpt: "billabongpe.countdown@0.0.1"
hidden: true
createdAt: "2022-07-08T18:47:48.923Z"
updatedAt: "2022-07-08T18:47:48.923Z"
---
The `countdown` is the block responsible for showing a countdown block.

## Configuration

1. Import the `catcol.countdown` app to your theme's dependencies in the `manifest.json`, for example:

```json
{
    "dependencies": {
        "catcol.countdown": "0.x"
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
| `secondTitle`   | `String` | Text  | `null` |
| `targetDate`   | `String` | Final Date  | `null` |
| `showOnPage`   | `Boolean` | The block should be visible? | `false` |


## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles             |
| ----------------------- |
| `container`             |
| `countdown`             |
| `title`                 |
| `secondTitle`           |
| `dateContainer`         | 
| `timeContainer`         |
| `timeValue`             | 
| `timeType`              |