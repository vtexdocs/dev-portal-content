---
title: "Hide And Show"
slug: "trackfield-store-components-hideandshow"
excerpt: "trackfield.store-components@0.18.0"
hidden: true
createdAt: "2022-07-05T22:31:25.054Z"
updatedAt: "2022-08-04T10:48:21.279Z"
---
## Description

This component was developed to the customer can disable or enable any content on the site-editor

## Configuration

1. Add the `store-components` app to your theme's dependencies in the `manifest.json`, for example:

```diff
"dependencies": {
+  "trackfield.store-components": "0.x"
}
```

2. You are now able to use the hide-and-show in any part of your store, inserting as a children, the component to which you want to hide.
```json
{
   "hide-and-show#mini-banner": {
    "title": "ON/OFF - Mini banner",
    "props": {
      "visible": true
    },
    "children": ["flex-layout.row#mini-banner"]
  },
}
```