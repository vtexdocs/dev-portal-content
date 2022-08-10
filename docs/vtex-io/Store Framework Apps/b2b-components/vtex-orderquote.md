---
title: "Order Quote"
slug: "vtex-orderquote"
excerpt: "vtex.orderquote@1.6.0"
hidden: false
createdAt: "2020-06-03T15:19:21.542Z"
updatedAt: "2022-08-02T15:36:46.582Z"
---
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->

The Order Quote app provides **B2B** capabilities to save a shopping cart (its items, product quantities and prices) for further use.

> ⚠️ The Order Quote app is not compatible with the [B2B Suite](https://developers.vtex.com/vtex-developer-docs/docs/vtex-b2b-suite) solution. Therefore, these instructions do not apply to stores using the B2B Suite. If you are using the B2B Suite, refer to the [B2B Quotes & Carts](https://developers.vtex.com/vtex-developer-docs/docs/vtex-b2b-quotes) documentation instead.

The user can also print the quotation information containing the cart information along with expiration date which is defined at **Admin > Apps**.

![quick-order](https://user-images.githubusercontent.com/52087100/94163217-f5f35500-fe5d-11ea-8ac1-b1fd3c717ae5.png)

## Configuration

1. [Install](https://vtex.io/docs/recipes/development/installing-an-app/) the Order Quote app by running `vtex install vtex.orderquote@1.x`.
2. Head over to your VTEX account's admin and access the **Apps** section.
3. Select the **Order Quote** app and click on **Settings**.
4. Fill out the **Lifespan** and **Store logo URL** fields.
5. Click on **Save**.
6. Add the Order Quote app as a `peerDependency` in your `store-theme`'s `manifest.json` file:

```diff
 "peerDependencies": {
+  "vtex.orderquote": "1.x"
 }
```

Once declared as a [Peer Dependency](https://vtex.io/docs/concepts/peerdependencies/), the app will generate a few routes under the `/orderquote` path in order to create the Order Quote custom page. Namely, they are:

| Route                  | Description                                                                                   |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| `/orderquote`          | Lists all saved cart quotations.                                                              |
| `/orderquote/create`   | Retrieves the current cart information, allowing you to create cart quotations as you desire. |
| `/orderquote/view/:ID` | Details page, displayed when you click on a quote from the listing page (`/orderquote`).      |

The new routes already contain a default template with all blocks automatically exported by the `orderquote` app, meaning that the Order Quote pages are ready to be rendered and no further actions are required from you.

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles               |
| ------------------------- |
| `buttonDelete`            |
| `buttonPrint`             |
| `buttonSave`              |
| `buttonsContainer`        |
| `buttonUse`               |
| `checkboxClear`           |
| `containerCreate`         |
| `containerFields`         |
| `containerList`           |
| `containerView`           |
| `refreshButton`           |
| `refreshLoading`          |
| `field`                   |
| `inputCreate`             |
| `inputCreate`             |
| `listContainer`           |
| `logo`                    |
| `notAuthenticatedMessage` |
| `printingArea`            |
| `totalizerContainer`      |
| `itemNameContainer`       |
| `itemName`                |
| `itemSkuName`             |

<!-- DOCS-IGNORE:start -->

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!

<!-- DOCS-IGNORE:end -->