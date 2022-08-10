---
title: "Countdown"
slug: "trackfield-store-components-countdown"
excerpt: "trackfield.store-components@0.18.0"
hidden: true
createdAt: "2022-07-05T22:31:25.093Z"
updatedAt: "2022-08-04T10:48:21.302Z"
---
## Description

this is a countdown component that needs a target date to render.

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
  "countdown#landing-page": {
    "props": {
      "backgroundColor": "#fff",
      "textColor": "#000",
      "targetDate": "2022/03/20 09:00:00",
      "textDays": "Dias",
      "textHours": "Horas",
      "textMinutes": "Minutos",
      "textSeconds": "Segundos",
      "labelBottom": "Texto superior",
      "labelTop": "Texto inferior",
      "horizontalAlign": "LEFT"
    }
  }
}
```

## `countdown` props

| Prop name          | Type     | Description                                                                | Default value |
| ------------------ | -------- | -------------------------------------------------------------------------- | ------------- |
| `backgroundColor`  | `string` | color for the background container                                         | `transparent` |
| `textColor`        | `string` | color for the text numbers and label top and down                          | `#000`        |
| `targetDate`       | `string` | date as target to init countdown                                           | ''            |
| `textDays`         | `string` | text used as label below day's number                                      | `Dia`         |
| `textDaysColor`    | `string` | color used on textDays                                                     | `#000`        |
| `textHours`        | `string` | text used as label below hour's number                                     | `Horas`       |
| `textHoursColor`   | `string` | color used on textHours                                                    | `#000`        |
| `textMinutes`      | `string` | text used as label below minute's number                                   | `Minutos`     |
| `textMinutesColor` | `string` | color used on textMinutes                                                  | `#000`        |
| `textSeconds`      | `string` | text used as label below second's number                                   | `Segundos`    |
| `textSecondsColor` | `string` | color used on textSeconds                                                  | `#000`        |
| `labelBottom`      | `string` | text used as label below countdown block                                   | ''            |
| `labelTop`         | `string` | text used as label above countdown block                                   | ''            |
| `horizontalAlign`  | `enum`   | align the countdown content, possible values are: `TOP`, `CENTER`,`BOTTOM` | `LEFT`        |

## Customization

The first thing that should be present in this section is the sentence below, showing users the recipe pertaining to CSS customization in apps:

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

Thereafter, you should add a single column table with the available CSS handles for the app, like the one below. Note that the Handles must be ordered alphabetically.

| CSS Handles                         |
| ----------------------------------- |
| `countdown__container`              |
| `countdown__content`                |
| `countdown__content--title`         |
| `countdown__divider`                |
| `countdown__divider--up`            |
| `countdown__divider--down`          |
| `countdown__title`                  |
| `countdown__title--up`              |
| `countdown__title--down`            |
| `countdown__timer`                  |
| `countdown__timer--days-content`    |
| `countdown__timer--days`            |
| `countdown__timer--days-label`      |
| `countdown__timer--hours-content`   |
| `countdown__timer--hours`           |
| `countdown__timer--hours-label`     |
| `countdown__timer--minutes-content` |
| `countdown__timer--minutes`         |
| `countdown__timer--minutes-label`   |
| `countdown__timer--seconds-content` |
| `countdown__timer--seconds`         |
| `countdown__timer--seconds-label`   |