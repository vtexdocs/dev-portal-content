---
title: "Count Down"
slug: "ebeauty-timer-countdown"
excerpt: "ebeauty.timer@0.0.4"
hidden: true
createdAt: "2022-07-28T20:14:42.966Z"
updatedAt: "2022-08-02T18:30:06.132Z"
---
The `count-down` is the block is responsible show count down

![image](https://user-images.githubusercontent.com/17678382/153967625-29dd776c-6087-4827-b25d-1d92d9bd7afc.png)

## Configuration

1. Import the `blacksipqa.timer` app to your theme's dependencies in the `manifest.json`, for example:

```json
{
    "dependencies": {
        "blacksipqa.timer": "0.x"
    }
}
```

2. Add the `count-down` block to any block below `store.home`. For example:

```json
{
    "store.home": {
        "blocks": ["count-down"]
    }
}
```

| Prop name      | Type                  | Description                            | Default value          |
| -------------- | --------------------- | -------------------------------------- | ---------------------- |
| `date`         | `String 'yyyy-mm-dd'` | date event                             | `date actual + 2 days` |
| `sizeSegment`  | `Number`              | size of the each element of count down | `100`                  |
| `colorDays`    | `String`              | code color in exa for days             | `7E2E84`               |
| `colorHours`   | `String`              | code color in exa for hours            | `D14081`               |
| `colorMinutes` | `String`              | code color in exa for minutes          | `EF798A`               |
| `colorSeconds` | `String`              | code color in exa for seconds          | `218380`               |

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles    |
| -------------- |
| `container`    |
| `timerWrapper` |
| `time`         |
| `timeLabel`    |