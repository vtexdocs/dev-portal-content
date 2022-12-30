---
title: "Share List"
slug: "vtex-list-sharelist"
excerpt: "vtex.list@3.6.2"
hidden: false
createdAt: "2022-09-16T00:32:17.848Z"
updatedAt: "2022-12-01T16:44:24.336Z"
---
The `share-list` block displays a button to automatically copy the URL to send the list to guests.

![ShareList](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-list-sharelist-0.gif)

## Configuration

1. Import the `vtex.list` app to your theme's peer dependencies in the `manifest.json` file as in the following example:

```json
  "peerDependencies": {
    "vtex.list": "3.x"
  }
```

2. Add the `share-list` block to other theme block inside a list context, such as the `store.list`. For example:

```diff
  "store.list": {
    "children": [
      "flex-layout.row
    ]
  },

  "flex-layout.row": {
    "children": [
      "list-info.name",
+     "share-list",
    ]
  }
```

## Customization

To apply CSS customizations in this and other blocks, follow the [Using CSS handles for store customization](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-css-handles-for-store-customization) guide.

| CSS Handles             |
| ----------------------- |
| `shareListContainer`    |
| `shareListIcon`         |
| `shareListNotification` |