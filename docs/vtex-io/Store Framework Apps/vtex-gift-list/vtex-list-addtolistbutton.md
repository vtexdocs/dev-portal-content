---
title: "Add To List Button"
slug: "vtex-list-addtolistbutton"
excerpt: "vtex.list@3.6.2"
hidden: false
createdAt: "2022-09-16T00:32:17.835Z"
updatedAt: "2022-12-01T16:44:24.282Z"
---
The `add-to-list-button` block displays a button that allows owners of the list to add products and remove products inside their list.

![AddToListButton](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-list-addtolistbutton-0.gif)

## Configuration

1. Import the `vtex.list` app to your theme's peer dependencies in the `manifest.json` file as in the following example:

```json
  "peerDependencies": {
    "vtex.list": "3.x"
  }
```

2. Add the `add-to-list-button` block to other theme block using the product context, such as the `product-summary.shelf`. For example:

```diff
  "product-summary.shelf": {
    "children": [
      "product-summary-image",
      "flex-layout.row",
      "flex-layout.col",
+     "add-to-list-button",
      "gifted-button"
    ]
  }
```

## Customization

To apply CSS customizations in this and other blocks, follow the [Using CSS handles for store customization](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-css-handles-for-store-customization) guide.

| CSS Handles                |
| -------------------------- |
| `addToListButtonText`      |
| `addToListButtonContainer` |