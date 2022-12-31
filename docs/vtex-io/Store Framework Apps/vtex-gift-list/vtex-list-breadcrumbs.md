---
title: "Breadcrumb"
slug: "vtex-list-breadcrumbs"
excerpt: "vtex.list@3.6.2"
hidden: false
createdAt: "2022-09-16T00:32:17.850Z"
updatedAt: "2022-12-01T16:44:24.277Z"
---
The `breadcrumbs` block displays the path to the user's navigation list.

![breadcrumbs](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-list-breadcrumbs-0.gif)

## Configuration

1. Import the `vtex.list` app to your theme's peer dependencies in the `manifest.json` file as in the following example:

```json
  "peerDependencies": {
    "vtex.list": "3.x"
  }
```

2. Add the `breadcrumbs` block to other theme block, such as the `flex-layout`. For example:

```diff
  "flex-layout.row": {
    "children": [
+     "breadcrumbs",
    ]
  }
```

## Customization

To apply CSS customizations in this and other blocks, follow the [Using CSS handles for store customization](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-css-handles-for-store-customization) guide.

| CSS Handles            |
| ---------------------- |
| `breadCrumbsContainer` |
| `breadLinkContainer`   |
| `biggerThenContainer`  |
| `lastRouteContainer`   |