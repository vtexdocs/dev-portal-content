---
title: "Size bay global styles component"
slug: "trackfield-store-components-sizebay"
excerpt: "trackfield.store-components@0.18.0"
hidden: true
createdAt: "2022-07-05T22:31:25.101Z"
updatedAt: "2022-08-04T10:48:21.301Z"
---
Component to add global styles to size-bay app.

## Configuration

1. Add the `store-components` app to your theme's dependencies in the `manifest.json`, for example:

```diff
"dependencies": {
+  "trackfield.store-components": "0.x"
}
```

2. You are now able to use the size-bay styles component entering the necessary props.

```json
{
  "store.product": {
    "children": ["sizebay-global-styles"]
  }
}
```

## Modus Operandi

Add the component just in the blocks off the pages that u need that CSS to be applied, this component is used just to customize CSS's from size-bay, and do not replace the store-theme CSS, please try first using the CSS From the store-theme.