---
title: "DISPOSITION LAYOUT - 1.x"
slug: "shoulder-disposition-layout"
excerpt: "shoulder.disposition-layout@3.0.0"
hidden: true
createdAt: "2022-08-01T20:51:56.101Z"
updatedAt: "2022-08-04T13:26:09.631Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

A layout capable of ordering sections/blocks/components by **dragging** them on the site editor's interface, and choosing which of them are visible.

✅ SEO-FRIENDLY

![ordering-example](https://user-images.githubusercontent.com/50715158/128493726-ebdbca35-292e-4bd3-84a1-ac01005843ec.gif)

## Configuration

1. Add `vtex.disposition-layout` 1.x as a theme dependency in the `manifest.json` file
2. Declare your orderable components as children of `disposition-layout`
3. Add, as prop, an array of objects with the numerical assigment of the given components; always start from `1`
4. Controlling the visibility is done via site editor, inside each item of the array list

### `disposition-layout` props

| Prop name     | Type    | Description                                                                     | Default value |
| ------------- | ------- | ------------------------------------------------------------------------------- | ------------- |
| `disposition` | `array` | An array of objects describing, with integers, the numerical asigment and order | `undefined`   |

- `disposition` array:

| Prop name | Type     | Description                               | Default value |
| --------- | -------- | ----------------------------------------- | ------------- |
| `order`   | `number` | The numerical assigment for each children | `undefined`   |

## Modus Operandi

A good implementantion is to declare the array length and numerical values corresponding to the length and order of the children array.

⚠️ Always use an ascending pattern starting from 1, as this array is correlated with the indices of the children

```json
"disposition-layout": {
    "children": [
      "flex-layout.row#one",
      "info-card#example",
      "flex-layout.row#two"
    ],
    "props": {
      "disposition": [
        {
          "order": 1
        },
        {
          "order": 2
        },
        {
          "order": 3
        }
      ]
    }
  },
```

Per example,

- 1 -> "flex-layout.row#one"
- 2 -> "info-card#example"
- 3 -> "flex-layout.row#two"

If by mistake you delete an item from the list, in site editor, remember that you can go to `configuration` and restore the original theme settings. 

![configuration](https://user-images.githubusercontent.com/50715158/128494098-6d5dff5d-c909-48a7-84de-d1578544cf93.png)

## App not working

Some users reported changing the app content via site editor while not seeing them reflected in the storefront.  
A potential fix was introduced in the `major 2.x`. You can test it by declaring the dependency as such, or installing it directly.

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