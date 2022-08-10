---
title: "Custom Section"
slug: "ebeauty-store-components-customsection"
excerpt: "ebeauty.store-components@0.0.3"
hidden: true
createdAt: "2022-07-21T13:58:59.860Z"
updatedAt: "2022-07-21T13:58:59.860Z"
---
The `section-custom` is the block is responsible for insert a parent div with id.

## Configuration

1. Import the `ebeauty.store-components` app to your theme's dependencies in the `manifest.json`, for example:

```json
{
    "dependencies": {
        "ebeauty.store-components": "0.x"
    }
}
```

2. Add the `section-custom` block to any block below `store.home`. For example:

```json
{
    "store.home": {
        "blocks": ["section-custom"]
    }
}
```

| Prop name | Type     | Description | Default value  |
| --------- | -------- | ----------- | -------------- |
| `id`      | `String` | id Text     | `""`           |

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles             |
| ----------------------- |
| `sectionContent`        |