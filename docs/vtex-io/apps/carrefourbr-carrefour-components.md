---
title: "Description"
slug: "carrefourbr-carrefour-components"
excerpt: "carrefourbr.carrefour-components@0.128.2"
hidden: true
createdAt: "2022-07-07T03:47:18.909Z"
updatedAt: "2022-08-03T18:57:03.337Z"
---
Carrefour Apps

## Table of Contents

-   [Usage](#usage)
-   [Components Specs](#components-specs)

## Usage

This app uses our store builder with the blocks architecture. To know more about Store Builder
[click here.](https://help.vtex.com/en/tutorial/understanding-storebuilder-and-stylesbuilder#structuring-and-configuring-our-store-with-object-object)

To use this app, you need to import in your dependencies on `manifest.json`.

```json
  "dependencies": {
    "acupula.carrefour-components": "0.x"
  }
```

Then, you can add a component block into your app theme.
You can use all components declared at `interfaces.json`.

For example, now you can use the `card-installments` block that is in the carrefour-apps. See an example of how to configure:

```json
"flex-layout.row.carrefour#product-price": {
    "props": {
      "marginTop": 5,
      "marginBottom": 5,
      "colSizing": "auto",
      "blockClass": "product-price"
    },
    "children": ["product-price#product-details", "card-installments"]
  },
```

## Components Specs

Below we have a README for each component of this project that explains how to use them.

-   [card-installments](card-installments.md)