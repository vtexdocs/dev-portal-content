---
title: "VTEX Sticky Layout"
slug: "vtex-sticky-layout"
excerpt: "vtex.sticky-layout@0.3.5-hkignore.ibk0"
hidden: false
createdAt: "2020-06-03T15:19:18.052Z"
updatedAt: "2022-05-02T08:51:37.588Z"
---
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

The Sticky Layout app provides layout structures to help building elements that should be fixed relative to the viewport in certain contexts.

> Sticky positioning is a hybrid of relative and fixed positioning. The element is treated as relative positioned until it crosses a specified threshold, at which point it is treated as fixed positioned.
>
> You can understand more by reading about in the [MDN `position` documentation](https://developer.mozilla.org/en-US/docs/Web/CSS/position#Sticky_positioning).

<!-- @import "[TOC]" {cmd="toc" depthFrom=3 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [`sticky-layout`](#sticky-layout)
- [`sticky-layout.stack-container`](#sticky-layoutstack-container)

<!-- /code_chunk_output -->

## Blocks

### `sticky-layout`

The `sticky-layout` block is responsible for making its children _stick_ to a certain position on the page when exiting the viewport while scrolling.

**Props:**

| Prop name         | Type           | Description                                                                      | Default value |
| ----------------- | -------------- | -------------------------------------------------------------------------------- | ------------- |
| `blockClass`      | `String`       | Unique class name to be appended to the container class                          | `""`          |
| `position`        | `PositionEnum` | Indicates where the component should stick                                       | `N/A`         |
| `verticalSpacing` | `Number`       | Indicates the distance in pixels from the position chosen in the `position` prop | `0`           |

`PositionEnum` options:

| Enum name | Enum value | Description                                  |
| --------- | ---------- | -------------------------------------------- |
| `TOP`     | `'top'`    | Component will stick to the top of screen    |
| `BOTTOM`  | `'bottom'` | Component will stick to the bottom of screen |

**CSS Handles:**

| Prop name        | Description                                                                                                   |
| ---------------- | ------------------------------------------------------------------------------------------------------------- |
| `container`      | Sticky layout container                                                                                       |
| `wrapper`        | Wrapper element that takes up the space previously used by the stuck element to prevent the page from jumping |
| `wrapper--stuck` | Sticky layout wrapper when stuck to a position on the page                                                    |

**Example usage:**

```jsonc
{
  "store.product": {
    "children": [
      "flex-layout.row#product-breadcrumb",
      "flex-layout.row#product-main",
      "sticky-layout#buy-button"
    ],
    "parent": {
      "challenge": "challenge.address"
    }
  },
  "sticky-layout#buy-button": {
    "props": {
      "position": "bottom"
    },
    "children": ["flex-layout.row#buy-button"]
  },
  "flex-layout.row#buy-button": {
    "props": {
      "marginTop": 4,
      "marginBottom": 7,
      "paddingBottom": 2
    },
    "children": ["buy-button"]
  }
}
```

### `sticky-layout.stack-container`

The `sticky-layout.stack-container` block can be used to orchestrate multiple `sticky-layout`s to have a stack behavior instead of one being on top of the other.

**Props:**

| Prop name  | Type           | Description                                                                                               | Default value |
| ---------- | -------------- | --------------------------------------------------------------------------------------------------------- | ------------- |
| `position` | `PositionEnum` | Indicates where the component should stick. _It overrides the `position` of its children `sticky-layout`_ | `N/A`         |

`PositionEnum` options:

| Enum name | Enum value | Description                                  |
| --------- | ---------- | -------------------------------------------- |
| `TOP`     | `'top'`    | Component will stick to the top of screen    |
| `BOTTOM`  | `'bottom'` | Component will stick to the bottom of screen |

**Example usage:**

Imagine three blocks: the first and the last being a `sticky-layout` and the second being any other block. A gap between both `sticky-layout`s will appear the moment the user starts scrolling the page. By defining those blocks inside a `sticky-layout.stack-container`, the second `sticky-layout` block will stick to the first `sticky-layout` instead of respecting the aformetioned gap or being one on top of the other.

```jsonc
{
  "header": {
    "blocks": ["header-layout.desktop"]
  },
  "header.full": {
    "blocks": ["header-layout.desktop"]
  },
  "header-layout.desktop": {
    // define a stack-container
    "children": ["sticky-layout.stack-container#header"]
  },
  "sticky-layout.stack-container#header": {
    "props": {
      "position": "top"
    },
    "children": [
      "sticky-layout#links-menu",
      // this notification.bar is not sticky, it will be scrolled away
      "notification.bar#home",
      "sticky-layout#main-menu"
    ]
  },
  "notification.bar#home": {
    "props": {
      "content": "SELECTED ITEMS ON SALE! CHECK IT OUT!"
    }
  },
  "sticky-layout#links-menu": {
    "children": ["vtex.menu@2.x:menu#websites"]
  },
  "sticky-layout#main-menu": {
    "children": ["vtex.menu@2.x:menu#category-menu"]
  }
}
```

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!