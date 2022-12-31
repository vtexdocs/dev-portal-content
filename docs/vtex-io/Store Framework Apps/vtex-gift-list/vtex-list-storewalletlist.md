---
title: "Store Wallet List"
slug: "vtex-list-storewalletlist"
excerpt: "vtex.list@3.6.2"
hidden: false
createdAt: "2022-09-16T00:32:45.126Z"
updatedAt: "2022-12-01T16:44:24.275Z"
---
The `store-wallet-list` renders the virtual wallet that contains the user's credit and gift card information.

![StoreWalletList](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-list-storewalletlist-0.gif)

## Configuration

1. Import the `vtex.list` app to your theme's peer dependencies in the `manifest.json` file as in the following example:

```json
  "peerDependencies": {
    "vtex.list": "3.x"
  }
```

2. Add the `store-wallet-list` block to other theme block inside an authentication context, such as the `flex-layout.col`. For example:

```diff
  "store.home": {
    "blocks": ["auth-condition#search-list"],
    "parent": { "storeWrapper": "storeWrapper#home" }
  },

  "auth-condition#search-list": {
    "props": {
      "Then": "flex-layout.row#home-with-user",
      "Else": "flex-layout.row#home-without-user"
    }
  },

  "flex-layout.row#home-with-user": {
    "children": ["flex-layout.col#home-with-user-col"],
    "props": {
      "blockClass": "home-with-user"
    }
  },

  "flex-layout.col#home-with-user-col": {
    "children": [
      "flex-layout.row#user-list",
+     "store-wallet-list",
      "flex-layout.row#search-list",
      "flex-layout.row#advantages"
    ]
  }
```