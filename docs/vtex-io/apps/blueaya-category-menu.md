---
title: "Category Menu"
slug: "blueaya-category-menu"
excerpt: "blueaya.category-menu@2.20.0"
hidden: true
createdAt: "2022-07-14T10:59:06.773Z"
updatedAt: "2022-07-14T10:59:06.773Z"
---
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

Category Menu app is a store component that shows a department list of the store on an customizable menu, and this app is used by store theme.

## Configuration

1. Add the app to your theme's dependencies on the `manifest.json`, for example:

```json
  dependencies: {
    "vtex.category-menu": "2.x"
  }
```

2. Add the `category-menu` block into your theme.

```json
{
  "category-menu": {
    "props": {
      "showAllDepartments": true,
      "showSubcategories": true,
      "menuDisposition": "center",
      "departments": []
    }
  }
}
```

Blocks: 

| Block | Description | 
| `category-menu`| render department list |
| `category-menu.mobile`| render drawer menu with department list |
| `category-menu-custom-item` | custom item block to be show in menu department list |


`category-menu` props:

| Prop name            | Type           | Description                                                                                     | Default Value |
| -------------------- | -------------- | ----------------------------------------------------------------------------------------------- | ------------- |
| `showAllDepartments` | `Boolean`      | Shows all departments category in menu                                                          | `true`        |
| `menuDisposition`    | `Enum`         | Indicates the disposition of the menu on the screen. Possible values: `left`, `center`, `right` | `center`      |
| `showSubcategories`  | `Boolean`      | Decides if the subcategories will be displayed                                                  | `true`        |
| `departments`        | `Array(items)` | List of departments `items` to be displayed on the menu                                         | `[]`          |
| `mobileMode`         | ![https://img.shields.io/badge/-Deprecated-red](https://img.shields.io/badge/-Deprecated-red) `Boolean`      | Use this as `true` to render the category menu in a sidebar                                      | `false`       |

Items:

| Prop name | Type     | Description                                   |
| --------- | -------- | --------------------------------------------- |
| `id`      | `Number` | The department Id to be displayed on the menu |
| `imgUrl` | `path` | Path to img to render in department |


`category-menu.mobile` props:

| Prop name            | Type           | Description                                                                                     | Default Value |
| -------------------- | -------------- | ----------------------------------------------------------------------------------------------- | ------------- |
| `showAllDepartments` | `Boolean`      | Shows all departments category in menu                                                          | `true`        |
| `menuDisposition`    | `Enum`         | Indicates the disposition of the menu on the screen. Possible values: `left`, `center`, `right` | `center`      |
| `showSubcategories`  | `Boolean`      | Decides if the subcategories will be displayed                                                  | `true`        |
| `departments`        | `Array(items)` | List of departments `items` to be displayed on the menu                                         | `[]`          |
| `MenuTrigger` | `Block` | block to render in menu trigger |
| `showMenuLabel` | `Boolean` | witch menu label should be render |

Items:

| Prop name | Type     | Description                                   |
| --------- | -------- | --------------------------------------------- |
| `id`      | `Number` | The department Id to be displayed on the menu |
| `imgUrl` | `path` | Path to img to render in department |

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles                 |
| --------------------------- |
| `container`                 |
| `departmentLink`            |
| `departmentList`            |
| `firstLevelLink`            |
| `firstLevelLinkContainer`   |
| `firstLevelList`            |
| `itemContainer`             |
| `itemContainer--category`   |
| `itemContainer--department` |
| `menuContainer`             |
| `secondLevelLink`           |
| `secondLevelLinkContainer`  |
| `secondLevelList`           |
| `section--category`         |
| `section--department`       |
| `sidebar`                   |
| `sidebarContainer`          |
| `sidebarContent`            |
| `sidebarHeader`             |
| `sidebarItem`               |
| `sidebarItemContainer`      |
| `sidebarOpen`               |
| `sidebarScrim`              |
| `submenuItem`               |
| `submenuList`               |

<!-- DOCS-IGNORE:start -->
## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!
<!-- DOCS-IGNORE:end -->