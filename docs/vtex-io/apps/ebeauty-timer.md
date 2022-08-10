---
title: "Custom Components"
slug: "ebeauty-timer"
excerpt: "ebeauty.timer@0.0.4"
hidden: true
createdAt: "2022-07-28T20:13:04.498Z"
updatedAt: "2022-08-02T18:30:05.930Z"
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
    "blacksipqa.timer": "0.x"
  }
```

For example, now you can change the behavior of `timer` block that is in the product details. See an example of how to configure:

```json
{
    "store.home": {
        "blocks": ["count-down"]
    }
}
```

## Components Specs

Below we have a README for each component of this project that explains how to use them.

-   [count-down](CountDown.md)