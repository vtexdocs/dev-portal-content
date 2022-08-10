---
title: "Custom search title catalog"
slug: "clubdeamigos-custom-search-title"
excerpt: "clubdeamigos.custom-search-title@0.0.3"
hidden: true
createdAt: "2022-07-28T13:10:58.882Z"
updatedAt: "2022-07-28T13:10:58.882Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

To use into PLP to show some titles like h1, is based in especific url's catalog.

![Desktop](./title-catalog.png)

## Configuration-

1. Add the app as a dependency in your store theme

```
"autecocolombia.custom-search-title": "0.x"
```

2. Declare the app block in your store inside your porduct display page. Default is `product.jsonc`

```
{
   ...
   "children":[
      "search-title-custom"
   ]
}
```

## Considerations
All titles are declared into ./react/utils/catalogTitles.js if you wish change/add just edit the catalog.

## Contributors ✨

Thanks goes to these wonderful people:

- Manuel Castillo