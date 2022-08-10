---
title: "DidYouMean"
slug: "lojacaos-search-didyoumean"
excerpt: "lojacaos.search@2.10.0"
hidden: true
createdAt: "2022-08-02T20:10:35.271Z"
updatedAt: "2022-08-02T20:30:43.162Z"
---
`DidYouMean` is a component used to suggest a possible misspelling correction to the current query.

## Usage

Add the `did-you-mean` block to the `search-result-layout.desktop` or `search-result-layout.mobile`. For example:

```json
"search-result-layout.desktop": {
    "children": [
        "flex-layout.row#didyoumean",
    ],
    "flex-layout.row#didyoumean": {
        "children": ["did-you-mean"]
    }
}
```

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles        |
| ------------------ |
| `didYouMeanPrefix` |
| `didYouMeanTerm`   |