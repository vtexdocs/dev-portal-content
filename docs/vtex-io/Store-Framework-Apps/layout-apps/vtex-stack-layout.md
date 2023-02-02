---
title: "Stack Layout"
slug: "vtex-stack-layout"
hidden: false
createdAt: "2020-06-03T15:19:16.096Z"
updatedAt: "2020-06-23T20:27:17.252Z"
category: "VTEX IO Apps"
---

Use this layout component to show blocks on top of other blocks.

![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-stack-layout-0.png)

Each children passed to `stack-layout` will receive an increasingly higher value of `zIndex`.

This means `flex-layout.row#viewone` will appear on the bottom, `flex-layout.row#viewtwo` will appear over it with `zIndex` of value 2, and `flex-layout.row#viewthree` will appear over them both with `zIndex` of value 3. Another thing to notice is that you pass the `blockClass` prop to any children of the `stack-layout` it will apply the `blockClass` to the element that wraps child element.

## Configuration

1. Import the breadcrumb's app to your theme's dependencies in the `manifest.json`, for example:

```json
  "dependencies": {
    "vtex.stack-layout": "0.x"
  }
```

2. Add the `stack-layout` block to your template. For example:

```json
"stack-layout": {
  "children": ["flex-layout.row#viewone", "flex-layout.row#viewtwo", "flex-layout.row#viewthree]
}
```

| Prop name      | Type     | Description                                                                                                                                                                            | Default value |
| -------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `blockClass`   | `string` | Allows to pass a custom name to be added to component css classes                                                                                                                      | `null`        |
| `zIndexOffset` | `number` | An offset to be passed to the zIndex of the children of the stack layout. If you pass 3, the first children will have zIndex of 3 and the next layer will have zIndex of 4, and so on. | `0`           |

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization). 

| CSS Handles       |
| ------------------|
| `stackContainer`  |
| `stackItem`       |
| `stackItem--first`|