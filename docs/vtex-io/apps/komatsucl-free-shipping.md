---
title: "Store Components"
slug: "komatsucl-free-shipping"
excerpt: "komatsucl.free-shipping@0.0.2"
hidden: true
createdAt: "2022-07-05T18:18:51.588Z"
updatedAt: "2022-07-05T18:18:51.588Z"
---
## Description

Store Components is a collection of components that can be used to create/extend others VTEX apps.

## Table of Contents

- [Usage](#usage)
- [Components Specs](#components-specs)

## Usage

This app uses our store builder with the blocks architecture. To know more about Store Builder [click here.](https://help.vtex.com/en/tutorial/understanding-storebuilder-and-stylesbuilder#structuring-and-configuring-our-store-with-object-object)

To use this app, you need to import in your dependencies on `manifest.json`.

```json
  "dependencies": {
    "vtex.store-components": "3.x"
  }
```

For example, now you can change the behavior of `product-price` block that is in the product details. See an example of how to configure:

```json
"product-price": {
  "props": {
    "showListPrice": true,
    "showLabels": false,
  }
}
```

## Components Specs

Below we have a README for each component of this project that explains how to use them.

- [Store Locator](StoreLocator.md)