---
title: "CUSTOM CONDITIONAL"
slug: "philipsmx-custom-conditional"
excerpt: "philipsmx.custom-conditional@1.0.10"
hidden: true
createdAt: "2022-07-18T22:35:09.544Z"
updatedAt: "2022-07-19T15:00:15.061Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

The **Custom Conditional** app provides blocks that can help you to render a childrens blocks if the browser path is included in the indicated urls.

## Configuration 

To use this component you need:

1. Add the custom badges app to your theme's dependencies in the `manifest.json`:

```diff
"dependencies": {
+   "philipsmx.custom-conditional": "0.x"
}
```

Now, you are able to use all blocks exported by the `custom-badges` app. Check out the full list below:

| Block name | Description | 
| --------  | ------------ | 
| `custom-conditional` | Defines the block that renders content if the browser path is included in the indicated urls. |

### `custom-conditional`

Declare the app block in your store theme.

```jsonc
"...": {
  "children": [
    "custom-conditional",
  ]
}
```

```jsonc
"custom-conditional" {
  "props": {
    "urls": ["/foo", "/bar"]
  },
  "children": [
    "...",
  ]
}
```

### `custom-conditional` props

| Prop name | Type | Description | Default value |
| --- | --- | --- | --- |
| `urls` | `string[]` | ![https://img.shields.io/badge/-Mandatory-red](https://img.shields.io/badge/-Mandatory-red) Array of strings against which the browser path will be compared to determine if content is rendered or not. | `undefined` |

<!-- DOCS-IGNORE:start -->

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://gitlab.com/AguilarJorge"><img src="https://gitlab.com/uploads/-/system/user/avatar/8848520/avatar.png?width=100" width="100px;" alt=""/><br /><sub><b>Jorge Aguilar</b></sub></a><br /><a href="https://gitlab.com/vtex/philipsmx-io/cross-selling/-/commits/master?author=Jorge%20Aguilar" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!

<!-- DOCS-IGNORE:end -->
### Copyright Ecomsur 2021