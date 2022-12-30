---
title: "List Info"
slug: "vtex-list-listinfo"
excerpt: "vtex.list@3.6.2"
hidden: false
createdAt: "2022-09-16T00:32:17.866Z"
updatedAt: "2022-12-01T16:44:24.318Z"
---
The list information is made up of three blocks `list-info.name` , `list-info.event-date` and `list-info.owner` and each one represents a type of information associated with the list, which are the name of the list, date of the event and name of the owner of the list respectively.

![ListInfo](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-list-listinfo-0.gif)

## Configuration

1. Import the `vtex.list` app to your theme's peer dependencies in the `manifest.json` file as in the following example:

```json
  "peerDependencies": {
    "vtex.list": "3.x"
  }
```

2. Add any `list-info` block to other theme block using a list context, such as the `store.guest`. For example:

```diff
  "store.guest": {
    "blocks":[
      "flex-layout.row#breadcrumbs-guest",
      "responsive-layout.desktop#guest",
      "responsive-layout.mobile#guest",
      "flex-layout.col"
    ]
  }

  "flex-layout.col": {
    "children": [
+     "list-info.name",
    ]
  }
```

## Customization - "list-info.name"

To apply CSS customizations in this and other blocks, follow the [Using CSS handles for store customization](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-css-handles-for-store-customization) guide.

| CSS Handles    |
| -------------- |
| `listName`     |
| `listNameText` |

## Customization - "list-info.event-date"

To apply CSS customizations in this and other blocks, follow the [Using CSS handles for store customization](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-css-handles-for-store-customization) guide.

| CSS Handles          |
| -------------------- |
| `eventDateContainer` |
| `eventDateText`      |

## Customization - "list-info.owner"

To apply CSS customizations in this and other blocks, follow the [Using CSS handles for store customization](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-css-handles-for-store-customization) guide.

| CSS Handles       |
| ----------------- |
| `ownersContainer` |
| `ownersParagraph` |
| `ownerNameText`   |
| `divisorText`     |
| `otherNameText`   |