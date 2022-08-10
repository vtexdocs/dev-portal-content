---
title: "Custom Components"
slug: "alessaecuador-category-slider"
excerpt: "alessaecuador.category-slider@0.0.5"
hidden: true
createdAt: "2022-07-05T05:49:43.772Z"
updatedAt: "2022-07-05T05:49:43.772Z"
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
    "blacksipqa.slider-categories": "0.x"
  }
```

For example, now you can change the behavior of `slider-departaments` block that is in the product details. See an example of how to configure:

```json
{
    "store.home": {
        "blocks": ["slider-departaments"]
    }
}
```

## Components Specs

Below we have a README for each component of this project that explains how to use them.

-   [Slider categories](SliderCategories.md)
-   [Slider departaments](SliderDepartaments.md)