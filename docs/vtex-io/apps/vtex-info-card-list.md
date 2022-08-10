---
title: "INFO CARD LIST"
slug: "vtex-info-card-list"
excerpt: "vtex.info-card-list@1.0.2"
hidden: true
createdAt: "2022-07-15T11:05:23.303Z"
updatedAt: "2022-07-15T11:05:23.303Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

An extension to [List Context](https://github.com/vtex-apps/list-context) that enables users to create lists of info cards that can be editable via Site Editor

![Screen Shot 2021-07-07 at 23 19 56](https://user-images.githubusercontent.com/50715158/124839073-fdfd2b00-df7f-11eb-8ebd-a009e3fd34b8.png)

## Configuration 

- Add this app as a theme dependency in the `manifest.json` file

```json
"dependencies": {
    "vtex.info-card-list": "0.x"
}
```

- Declare the app's main block `list-context.info-card-list`
```json
"list-context.info-card-list#demo": {
    "children": [
      "slider-layout#demo-infocards"
    ],
    "props": {
      "infoCards": [
        {
          ...props
        },
        {
          ...props
        }
      ]
    }
  },
```
- For this list to work, you must now declare the app who will consume the list context, for i.e `slider-layout`

```json
"slider-layout#demo-infocards": {
    "props": {
      "itemsPerPage": {
        "desktop": 1,
        "tablet": 1,
        "phone": 1
      },
      "infinite": true
    }
  },
```

### `list-context.info-card-list` props

| Prop name    | Type            | Description    | Default value     |
| ------------ | --------------- | -------------- | ---------- | 
| `infoCards`      | `array`       | Array of `objects` declaring info cards        | null        |


- `infoCards` array:

This array is composed of objects with the properties defined in [Info Card](https://github.com/vtex-apps/store-components/blob/master/docs/InfoCard.md)

## Customization

### ⚠️ blockClass workaround

If you assign the prop `blockClass` to an info-card, it will be assigned as a CSS HANDLE to a `div` wrapper.  
For i.e: If you give the first info-card the blockClass `first-info-card`, a parent div will be rendered as such:  
```html
<div class="vtex-info-card-list-0-x-first-info-card">
```
This will give you the option to style each info-card individually  

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