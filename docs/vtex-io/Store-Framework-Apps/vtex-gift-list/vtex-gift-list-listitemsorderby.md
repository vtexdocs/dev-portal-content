---
title: "List Items Order By"
slug: "vtex-gift-list-listitemsorderby"
hidden: false
createdAt: "2022-09-29T00:01:36.992Z"
updatedAt: "2022-09-29T00:01:36.992Z"
---
The `list-items-orderby` block allows the user order by the items of an list. The options for order is alphabetically or addition date.

![ListItemsOrderBy](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-gift-list-listitemsorderby-0.gif)

## Configuration

1. Import the `vtex.list` app to your theme's peer dependencies in the `manifest.json` file as in the following example:

```json
  "peerDependencies": {
    "vtex.list": "3.x"
  }
```

2. Add the `list-items-orderby` block to other theme block inside a list context, such as the `store.list` or `store.guest`. For example:

```diff
  "store.list":{
    "children": [
      flex-layout.col
    ]
  },

  "flex-layout.col": {
    "children": [
+     "list-items-orderby"
    ],
  }
```