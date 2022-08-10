---
title: "Helpdesk component"
slug: "trackfield-store-components-helpdesk"
excerpt: "trackfield.store-components@0.18.0"
hidden: true
createdAt: "2022-07-05T22:31:25.043Z"
updatedAt: "2022-08-04T10:48:21.275Z"
---
Helpdesk component with two floating whatsapp and sac buttons to facilitate user interaction.

![Media Placeholder](https://gitlab.com/acct.global/program-04/track-and-field-io/trackandfield.store-theme/uploads/96a963d9df9fbaa76283f38b4feea948/image.png)

## Configuration

1. Add the `store-components` app to your theme's dependencies in the `manifest.json`, for example:

```diff
"dependencies": {
+  "trackfield.store-components": "0.x"
}
```

2. You are now able to use the help desk component entering the necessary props.

```json
{
  "helpdesk": {
    "props": {
      "whatsappTitle": "Compre pelo Whatsapp",
      "linkWhatsapp": "https://api.whatsapp.com/send?phone={{phone-number}}"
    }
  }
}
```

# `Helpdesk` Props

| Prop name       | Type     | Description                                       | Default value |
| --------------- | -------- | ------------------------------------------------- | ------------- |
| `whatsappTitle` | `string` | title for whatsapp for example 'buy by whatsapp'. | `""`          |
| `linkWhatsapp`  | `string` | page redirect, for exemple "https://localhost".   | `""`          |

## Customization

The first thing that should be present in this section is the sentence below, showing users the recipe pertaining to CSS customization in apps:

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

Thereafter, you should add a single column table with the available CSS handles for the app, like the one below. Note that the Handles must be ordered alphabetically.

| CSS Handles         |
| ------------------- |
| `helpdesk`          |
| `helpdesk__content` |
| `helpdesk__link`    |
| `helpdesk__icon`    |
| `helpdesk__title`   |