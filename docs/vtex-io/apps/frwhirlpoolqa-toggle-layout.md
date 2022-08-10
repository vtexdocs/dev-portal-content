---
title: "Toggle Layout"
slug: "frwhirlpoolqa-toggle-layout"
excerpt: "frwhirlpoolqa.toggle-layout@0.0.5"
hidden: true
createdAt: "2022-08-08T15:27:11.228Z"
updatedAt: "2022-08-08T15:27:11.228Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

A layout that renders it's content, on demand, controlled via site editor

⚠️ This app works not as visibility, but as displaying it's content passed

![Site editor example](../img/toggleLayout.png)

## Configuration

- Add this app as a theme dependency in the `manifest.json` file

```json
"dependencies": {
    "vtex.toggle-layout": "0.x"
}
```

- Add `toggle-layout` block and declare it's content via the children prop

```json
"toggle-layout": {
    "children": [
      "rich-text#title",
      "info-card#example"
      ]
  }
```

Now the user has access to a `Toggle Layout` block inside site editor, that can manipulate on demand

## Customization

`No CSS Handles are available yet for the app customization.`

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