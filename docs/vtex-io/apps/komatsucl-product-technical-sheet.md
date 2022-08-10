---
title: "Custom Components"
slug: "komatsucl-product-technical-sheet"
excerpt: "komatsucl.product-technical-sheet@0.0.2"
hidden: true
createdAt: "2022-07-29T20:30:52.252Z"
updatedAt: "2022-07-29T22:05:58.700Z"
---
## Description

Custom Components is a collection of components that can be used to create/extend others VTEX apps.

## Table of Contents

-   [Usage](#usage)
-   [Components Specs](#components-specs)

## Usage

This app uses our store builder with the blocks architecture. To know more about Store Builder [click here.](https://help.vtex.com/en/tutorial/understanding-storebuilder-and-stylesbuilder#structuring-and-configuring-our-store-with-object-object)

To use this app, you need to import in your dependencies on `manifest.json`.

```json
  "dependencies": {
    "blacksipqa.product-technical-sheet": "0.x"
  }
```

For example, now you can change the behavior of `product-technical-sheet` block that is in the product details. See an example of how to configure:

```json
{
    "store.home": {
        "blocks": ["product-technical-sheet"]
    }
}
```

## Components Specs

Below we have a README for each component of this project that explains how to use them.

-   [product-technical-sheet](ProductTechnicalSheet.md)