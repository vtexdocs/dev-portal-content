---
title: "My account styles component"
slug: "trackfield-store-components-myaccountstyle"
excerpt: "trackfield.store-components@0.18.0"
hidden: true
createdAt: "2022-07-05T22:31:25.061Z"
updatedAt: "2022-08-04T10:48:21.252Z"
---
Component to add styles to vtex my-account app, when page is equal 'store.account'.

## Configuration

1. Add the `store-components` app to your theme's dependencies in the `manifest.json`, for example:

```diff
"dependencies": {
+  "trackfield.store-components": "0.x"
}
```
2. You are now able to use the my-account styles component.

```json
{
  "store.product": {
    "children": ["my-account-style"]
  }
}
```