---
title: "Locale Switcher"
slug: "vtex-locale-switcher"
hidden: false
createdAt: "2020-06-03T15:19:32.977Z"
updatedAt: "2021-07-16T16:19:13.912Z"
---

The Locale Switcher app provides a component capable of changing the current language of your store.

![img-locale-switcher](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-locale-switcher-0.png)

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

> ⚠️ **\*Caution:** The third step is mandatory. If no ticket is opened requiring the desired languages, the selection list may not appear on the Locale Switcher component.\*

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-css-handles-for-store-customization).

|     CSS Handles     |
| :-----------------: |
|      `button`       |
|    `buttonText`     |
|     `container`     |
|       `list`        |
|    `listElement`    |
|   `localeIdText`    |
| `relativeContainer` |
