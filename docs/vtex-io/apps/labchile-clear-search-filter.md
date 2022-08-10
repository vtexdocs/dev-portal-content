---
title: "Custom Components"
slug: "labchile-clear-search-filter"
excerpt: "labchile.clear-search-filter@0.0.1"
hidden: true
createdAt: "2022-07-22T02:44:06.665Z"
updatedAt: "2022-07-22T02:44:06.665Z"
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
    "blacksipqa.clear-search-filter": "0.x"
  }
```

For example, now you can change the behavior of `product-price` block that is in the product details. See an example of how to configure:

```json
{
    "store.custom#clear-search-filter": {
        "blocks": ["blacksipqa.clear-search-filter:clear-search-filter"]
    }
}
```

## Components Specs

Below we have a README for each component of this project that explains how to use them.

-   [Clear Search Filter](ClearSearchFilter.md)