---
title: "CROSS DEVICE CART"
slug: "vtex-cross-device-cart"
excerpt: "vtex.cross-device-cart@1.4.6"
hidden: true
createdAt: "2022-07-22T10:34:43.569Z"
updatedAt: "2022-07-22T10:34:43.569Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

The main feature users are looking for is to keep an up-to-date shopping cart through different devices; one of the most important experiences of a truly unified commerce.

To do so, this app was created to enable `logged in` users to retrieve their cart from their last session.

## Configuration

1.  Install the app and then import it to your theme's peer dependencies in `manifest.json`,

```json
  "peerDependencies": {
    // ...
    "vtex.cross-device-cart": "1.x"
  }
```

2. Add the `cross-device-cart` block as a children of your store header, desktop and mobile, for i.e:

   ```diff
   "header-layout.desktop": {
       "children": [
   +     "cross-device-cart",
         "flex-layout.row#1-desktop",
         "flex-layout.row#2-desktop",
         "flex-layout.row#3-desktop",
         "sticky-layout#4-desktop"
       ]
     },
     "header-layout.mobile": {
       "children": [
   +     "cross-device-cart",
         "flex-layout.row#1-mobile",
         "sticky-layout#2-mobile"
       ]
     },
   ```

3. (Optional) You can tailor the default experience by accesing the admin app settings.  
   By default, the app handles the replacement automatically. But it you set it to manual, a challenge block will be rendered as an action bar, for the user to interact with.

## Customization

| CSS Handles     |
| --------------- |
| `actionBar`     |
| `challengeText` |

<!-- DOCS-IGNORE:start -->

## Contributors

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!

<!-- DOCS-IGNORE:end -->