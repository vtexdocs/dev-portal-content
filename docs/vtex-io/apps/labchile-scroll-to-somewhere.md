---
title: "Custom Components"
slug: "labchile-scroll-to-somewhere"
excerpt: "labchile.scroll-to-somewhere@0.0.1"
hidden: true
createdAt: "2022-08-09T01:31:44.301Z"
updatedAt: "2022-08-09T01:31:44.301Z"
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
    "blacksipqa.scroll-to-somewhere": "0.x"
  }
```

For example, now you can change the behavior of `scroll-to-somewhere` block that is in the product details. See an example of how to configure:

```json
{
    "store.product": {
        "blocks": ["scroll-to-somewhere"]
    }
}
```

## Components Specs

Below we have a README for each component of this project that explains how to use them.

-   [scroll-to-somewhere](scrollToSomewhere.md)