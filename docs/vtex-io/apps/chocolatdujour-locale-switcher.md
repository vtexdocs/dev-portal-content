---
title: "Locale Switcher"
slug: "chocolatdujour-locale-switcher"
excerpt: "chocolatdujour.locale-switcher@0.6.0"
hidden: true
createdAt: "2022-07-21T18:46:41.443Z"
updatedAt: "2022-07-21T18:46:41.443Z"
---
The Locale Switcher app provides a component capable of changing the current language of your store.

![img-locale-switcher](https://user-images.githubusercontent.com/27777263/74359290-c2b5f700-4da1-11ea-8612-c05ccf1988d5.png)

## Configuration

1. Add the Locale Switcher app to your theme's dependencies in the `manifest.json` file:

```diff
 "dependencies": {
+  "vtex.locale-switcher": "0.x"
 }
```

2. Add the `locale-switcher` block to your header. For example:

```jsonc
"header-row#desktop": {
  "children": [
    // (...)
    "locale-switcher",
    "login",
    "minicart.v2"
  ]
},
```

3. Open a ticket to our support team in order to adjust your store's binding with the desired languages. 

> ⚠️ ***Caution:** The third step is mandatory. If no ticket is opened requiring the desired languages, the selection list may not appear on the Locale Switcher component.*

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles         |
| :-----------------: |
| `button`            |
| `buttonText`        |
| `container`         |
| `list`              |
| `listElement`       |
| `localeIdText`      |
| `relativeContainer` |

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!