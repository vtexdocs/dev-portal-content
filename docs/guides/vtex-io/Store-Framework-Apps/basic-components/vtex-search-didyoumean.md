---
title: "DidYouMean"
slug: "vtex-search-didyoumean"
hidden: false
createdAt: "2021-02-23T17:09:08.617Z"
updatedAt: "2022-09-15T11:39:24.346Z"
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

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-css-handles-for-store-customization).

| CSS Handles        |
| ------------------ |
| `didYouMeanPrefix` |
| `didYouMeanTerm`   |
