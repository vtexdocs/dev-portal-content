---
title: "Wrappers"
slug: "vtex-gift-list-wrappers"
hidden: false
createdAt: "2022-09-20T22:32:12.493Z"
updatedAt: "2022-09-20T22:32:12.493Z"
---
The wrappers are used to call the context Provider for other components and they are made of three blocks `owner-list-wrapper` , `guest-list-wrapper` and `user-lists-wrapper` and each one represents a context, which are owners, guests and users respectively.

## Configuration

1. Import the `vtex.list` app to your theme's peer dependencies in the `manifest.json` file as in the following example:

```json
  "peerDependencies": {
    "vtex.list": "2.x"
  }
```

1. Add a wrapper like the `owner-list-wrapper` block to other theme block, such as the `store.search`. For example:

```diff
// .store/blocks/wrappers.jsonc

  "searchWrapper#default": {
    "props": {
+      "CustomContext": "owner-list-wrapper"
    }
  }

// .store/blocks/search/search.jsonc
  "store.search": {
    "parent": {
      "searchWrapper": "searchWrapper#default"
    },
```