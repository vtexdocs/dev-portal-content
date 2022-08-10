---
title: "Gradient Collapse"
slug: "vtex-store-components-gradientcollapse"
excerpt: "vtex.store-components@3.132.2"
hidden: false
createdAt: "2020-06-03T16:04:30.346Z"
updatedAt: "2022-01-04T23:11:39.554Z"
---
![https://img.shields.io/badge/-Deprecated-red](https://img.shields.io/badge/-Deprecated-red)

>⚠️ **Warning**
>
> **The Gradient Collapse block has been deprecated in favor of the [Disclosure Layout app](https://developers.vtex.com/vtex-developer-docs/docs/vtex-disclosure-layout).** Although support for this block is still granted, we strongly recommend you to update your store theme with the Disclosure Layout app.

`GradientCollapse` is a VTEX component that hides part of the children when it is bigger than the `collapseHeight` giving the user the _show more_ or _show less_ options. This Component can be imported and used by any VTEX app.

## Configuration

1. Import the `vtex.store-component` app to your theme's dependencies in the `manifest.json`;

```json
  "dependencies": {
    "vtex.store-components": "3.x"
  }
```

2. Import it into your code:

```js
import { GradientCollapse } from 'vtex.store-components'
```

You can use it in your code like a React component with the jsx tag: `<GradientCollapse />`.

```jsx
<GradientCollapse>
  I'm a text and I will collapse if I'm bigger than my collapseHeight!
</GradientCollapse>
```

| Prop name        | Type      | Description                   | Default Value |
| ---------------- | --------- | ----------------------------- | ------------- |
| `collapseHeight` | `Number!` | MaxHeight of the container    | `undefined`   |
| `children`       | `Node`    | The component to be collapsed | `null`        |

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles         |
| ------------------- |
| `container`         |
| `content`           |
| `fadeBottom`        |
| `pointerEventsAuto` |
| `pointerEventsNone` |
| `showMoreButton`    |