---
title: "Script WoowUp"
slug: "flexicolombia-woowup"
excerpt: "flexicolombia.woowup@0.0.3"
hidden: true
createdAt: "2022-07-22T14:01:42.930Z"
updatedAt: "2022-07-22T14:01:42.930Z"
---
## Description

Script WoowUp is an component that allows us to carry out email marketing with the best-selling products according to their productReference.

## Table of Contents

-   [Usage](#usage)
-   [Components Specs](#components-specs)

## Usage

This app uses our store builder with the blocks architecture. To know more about Store Builder [click here.](https://help.vtex.com/en/tutorial/understanding-storebuilder-and-stylesbuilder#structuring-and-configuring-our-store-with-object-object)

To use this app, you need to import in your dependencies on `manifest.json`.

```json
  "dependencies": {
    "blacksipqa.script-woowup": "0.x"
  }
```

For example, now you can change the behavior of `example-1` block that is in the product details. See an example of how to configure:

```json
{
    "store.home": {
        "blocks": ["woow-up-track-product"]
    }
}
```

## Components Specs

Below we have a README for each component of this project that explains how to use them.

-   [example-1](Example.md)