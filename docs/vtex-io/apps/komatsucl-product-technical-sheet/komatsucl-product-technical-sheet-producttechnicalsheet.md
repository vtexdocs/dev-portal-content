---
title: "Technical Sheet"
slug: "komatsucl-product-technical-sheet-producttechnicalsheet"
excerpt: "komatsucl.product-technical-sheet@0.0.2"
hidden: true
createdAt: "2022-07-29T20:33:00.431Z"
updatedAt: "2022-07-29T22:05:58.842Z"
---
The `product-technical-sheet` is the block is responsible print a button to access the specification corresponding to the technical data in PDF

![image](https://user-images.githubusercontent.com/17678382/132425433-8b874dde-1f60-4549-9b0d-9f1e02c6df23.png)

## Configuration

1. Import the `blacksipqa.product-technical-sheet` app to your theme's dependencies in the `manifest.json`, for example:

```json
{
    "dependencies": {
        "blacksipqa.product-technical-sheet": "0.x"
    }
}
```

2. Add the `product-technical-sheet` block in the product page or block whit this contex. For example:

```json
{
    "store.product": {
        "blocks": ["product-technical-sheet"]
    }
}
```

| Prop name                | Type     | Description                                     | Default value |
| ------------------------ | -------- | ----------------------------------------------- | ------------- |
| `specificationGroupName` | `String` | Group containing the specification              | `null`        |
| `specificationName`      | `String` | Specification that contains the technical sheet | `null`        |

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles |
| ----------- |
| `container` |