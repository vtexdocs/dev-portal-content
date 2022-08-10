---
title: "Interfaces"
slug: "vtex-io-documentation-interface"
excerpt: "vtex.io-documentation@0.88.5"
hidden: false
createdAt: "2021-04-07T19:00:37.442Z"
updatedAt: "2022-08-02T00:03:05.816Z"
---
Interfaces establish a relation between a block and a React component, allowing the Store Builder to build the store's front end. They can be found within an app's `interfaces.json` file.

For example:

```jsonc
// product-summary/store/interfaces.json
{
  "product-summary": {
    "component": "ProductSummary",
    "composition": "children",
    "content": {
      "$ref": "app:vtex.product-summary#/definitions/ProductSummary"
    }
  }
}
```

In general, front-end apps export different blocks, which are declared and configured in the store theme's code, and React components related to these blocks. These components are then rendered on the store's front end. 

To sum up, for every exported block, the app also defines a React component linked to that block.