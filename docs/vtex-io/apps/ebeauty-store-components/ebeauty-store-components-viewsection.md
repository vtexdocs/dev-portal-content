---
title: "View Section"
slug: "ebeauty-store-components-viewsection"
excerpt: "ebeauty.store-components@0.0.3"
hidden: true
createdAt: "2022-07-21T13:58:59.899Z"
updatedAt: "2022-07-21T13:58:59.899Z"
---
The `observe-view-section` is the block is responsible for change color in Links when scroll on specific section.

## Configuration

1. Import the `ebeauty.store-components` app to your theme's dependencies in the `manifest.json`, for example:

```json
{
    "dependencies": {
        "ebeauty.store-components": "0.x"
    }
}
```

2. Add the `observe-view-section` block to any block below `store.home`. For example:

```json
{
    "store.home": {
        "blocks": ["observe-view-section"]
    }
}
```

| Prop name  | Type     | Description | Default value  |
| ---------  | -------- | ----------- | -------------- |
| `idSection`| `String` | id Text     | `""`           |
| `threshold`| `Number` | thresHold   | `0`            |
| `itemLink` | `String` | id Link     | `""`           |