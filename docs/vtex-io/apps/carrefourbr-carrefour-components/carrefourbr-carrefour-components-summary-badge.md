---
title: "Carrefour Search Bar"
slug: "carrefourbr-carrefour-components-summary-badge"
excerpt: "carrefourbr.carrefour-components@0.128.2"
hidden: true
createdAt: "2022-07-07T03:54:09.180Z"
updatedAt: "2022-08-03T18:57:03.665Z"
---
## Description

`Summary Badge` is a component that uses the `product-summary-context` to check all the clusters that will appear on product summary and display a badge.

- [Usage](#usage)
  - [CSS Namespaces](#css-namespaces)

## Usage

Add `carrefour-summary-badge` block into your app theme, add the cluster id.

Example:

```
"carrefour-summary-badge": {
  "props": {
    "collections": "142"
  }
},
```

#### CSS Namespaces

Below, we describe the namespace that are defined in the `Summary Badge`.

| Class name                  |
| --------------------------- |
| `summaryHighlight`          |
| `summaryHighlightContainer` |