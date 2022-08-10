---
title: "MZ Buy Collection"
slug: "jequiti-product-spec-video"
excerpt: "jequiti.product-spec-video@0.0.3"
hidden: true
createdAt: "2022-07-31T03:37:44.150Z"
updatedAt: "2022-07-31T03:37:44.150Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

This app provides a custom store template and elements to build special shelves related a products' collection according to a filter defined by the seller. The pages and /or shelves built using these blocks allow for purchase of all products in a collection at once.

:heavy_exclamation_mark: **The products shown must be part of a Collection. The user must specify the collection search term via Site Editor**

![Media Placeholder](https://user-images.githubusercontent.com/27385566/157740384-fc400754-c1aa-4ae1-8725-48fb48000420.png)

## Setup

### Step 1 - Add this app to your dependencies

Add `maeztraio.buy-collection` to your theme's dependencies `manifest.json` file:

```json
  "dependencies": {
    "maeztraio.buy-collection": "0.x",
  }
```

Now, you are able to use all blocks/page templates exported by the `buy-collection` app. Check out the full list below:

| Block name           | Type        | Description                                                                           |     |
| -------------------- | ----------- | ------------------------------------------------------------------------------------- | --- |
| `buy-collection-cta` | `mandatory` | This block renders a Call-To-Action in the PDP with a link to the Collection kit page |

### `buy-together` props

| Prop name    | Type     | Description      | Default value                                                               |
| ------------ | -------- | ---------------- | --------------------------------------------------------------------------- |
| `title`      | `string` | Section title    | Acessórios sugeridos                                                        |
| `subtitle`   | `string` | Section subtitle | Compre também os acessórios abaixo e não deixe de levar o seu kit completo! |
| `buttonText` | `string` | Buy button text  | Comprar junto                                                               |

:warning: **This app should be used only in product page**.

## Example

```
"store.product": {
    "blocks": [
      "flex-layout.row"
    ]
},
"flex-layout.row": {
  "children": ["accessories"]
}
```

## Customization

`In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).`

| CSS Handles |
| ----------- |
| `WIP`       |

<!-- DOCS-IGNORE:start -->

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/lokinmodar"><br /><sub><b>Douglas Dantas</b></sub></a><br /><a href="" title="Code">💻</a></td>
  </tr>
</table>
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

<!-- This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome! -->

<!-- DOCS-IGNORE:end -->