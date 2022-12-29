---
title: "Gifted Button"
slug: "vtex-list-giftedbutton"
excerpt: "vtex.list@3.6.2"
hidden: false
createdAt: "2022-09-16T00:32:17.853Z"
updatedAt: "2022-12-01T16:44:24.220Z"
---
The `gifted-button` block displays the counter of purchases that have already been made for a product within the list.

![GiftedButton](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-list-giftedbutton-0.gif)

## Configuration

1. Import the `vtex.list` app to your theme's peer dependencies in the `manifest.json` file as in the following example:

```json
  "peerDependencies": {
    "vtex.list": "3.x"
  }
```

2. Add the `gifted-button` block to other theme block inside a product context, such as the `product-summary.shelf`. For example:

```diff
  "product-summary.shelf": {
    "children": [
      "product-summary-image"#OwnerListDesktopImage"",
      "flex-layout.row",
      "flex-layout.col",
      "add-to-list-button",
+     "gifted-button",
    ]
  }
```