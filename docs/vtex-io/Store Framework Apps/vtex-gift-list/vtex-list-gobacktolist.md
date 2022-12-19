---
title: "Go Back To List"
slug: "vtex-list-gobacktolist"
excerpt: "vtex.list@3.6.2"
hidden: false
createdAt: "2022-09-16T00:32:17.827Z"
updatedAt: "2022-12-01T16:44:24.218Z"
---
The `go-back-to-list` block allows the user to return to the list.

![GoBackToList](https://user-images.githubusercontent.com/67066494/190467457-ae896809-26ae-4979-8427-160982c02e90.gif)

## Configuration

1. Import the `vtex.list` app to your theme's peer dependencies in the `manifest.json` file as in the following example:

```json
  "peerDependencies": {
    "vtex.list": "3.x"
  }
```

2. Add the `go-back-to-list` block to other theme block inside a search context, such as the `store.search`. For example:

```diff
  "search-result-layout.desktop":{
    "children": [
      flex-layout.row
    ]
  },

  "flex-layout.row": {
    "children": [
      "flex-layout.col#searchinfo",
      "flex-layout.col#search-product",
+     "go-back-to-list",
    ]
  }
```