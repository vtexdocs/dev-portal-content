---
title: "copy-url-app"
slug: "cosmo-copy-url"
excerpt: "cosmo.copy-url@0.0.3"
hidden: true
createdAt: "2022-07-27T19:52:16.556Z"
updatedAt: "2022-07-27T19:52:16.556Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

the `copy-url-app` is a custom VTEX block that allows wrapping children and giving them an id

![Media Placeholder](http://iglesialocoamor.com/wp-content/uploads/2021/07/copy-url-app-image.jpg)

## Configuration 

1. Import the `cosmo.copy-url-app` to your theme's dependencies in the `manifest.json`;  

```
  "dependencies": {
    "cosmo.copy-url-app": "0.x"
  }
```

2. Add the `copy-url-app` block in any template from your theme. For example:

```
 "copy-url-app#example":{
        "children": ["rich-text#example"],
        "props": {
          "wrapperId": "example"
        }
      },
```

Finally you will have a wrapper with an id that you could use in different scenarios, for example call it as an anchor point with markdown like this:

`[Text example](#idexample)`
 

### `copy-url-app` props

| Prop name    | Type            | Description    | Default value                                                                                                                               |
| ------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | 
| `wrapperId`      | `string`       | `id` that will be assigned to the wrapper         | `undefined`        |

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