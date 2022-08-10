---
title: "Custom Components"
slug: "blacksipqa-store-locator"
excerpt: "blacksipqa.store-locator@2.0.2"
hidden: true
createdAt: "2022-08-04T16:41:16.023Z"
updatedAt: "2022-08-04T16:41:16.023Z"
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
    "blacksipqa.store-locator": "0.x"
  }
```

For example, now you can change the behavior of `product-price` block that is in the product details. See an example of how to configure:

```json
{
    "store.custom#store-locator": {
        "blocks": ["blacksipqa.store-locator:store-locator"]
    }
}
```

## Components Specs

Below we have a README for each component of this project that explains how to use them.

-   [Store Locator](StoreLocator.md)