---
title: "Menu"
slug: "vtex-menu"
excerpt: "vtex.menu@2.34.26"
hidden: false
createdAt: "2020-06-03T15:19:15.904Z"
updatedAt: "2022-12-06T17:06:12.798Z"
---

VTEX Menu is a store component responsible for displaying a bar containing links and drop-down sub-menus.

![menu-app](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-menu-0.png)

## Configuration

1. Import the menu's app to your dependencies as `manifest.json`, for example:

```json
  "dependencies": {
    "vtex.menu": "2.x"
  }
```

2. Add the `vtex.menu@2.x:menu` block to the [store header](https://github.com/vtex-apps/store-header/blob/master/store/interfaces.json) template.

3. To build the store's menu options, you need to configure the `menu-item` blocks. These can be declared in two different ways in `vtex.menu@2.x:menu`: as children or as props. The advantage of this latest `menu-item` configuration compared is that Site Editor can be used to edit the blocks.

### `menu-item` as children

_Example:_

```json
"vtex.menu@2.x:menu#websites": {
  "children": [
    "menu-item#shop",
    "menu-item#about-us"
  ]
},
"menu-item#shop": {
  "props": {
    "id": "menu-item-shop",
    "type": "custom",
    "highlight": false,
    "itemProps": {
      "type": "internal",
      "href": "#",
      "noFollow": false,
      "tagTitle": "Shop",
      "text": "Shop"
    },
    "iconProps": {
      "id": "bnd-logo",
      "size": 16,
      "viewBox": "0 0 16 16",
      "activeClassName": "rebel-pink",
      "mutedClassName": "c-action-primary"
    },
    "iconToTheRight": true
  }
}
```

### `menu-item` as props

_Example:_

```json
"vtex.menu@2.x:menu#websites": {
  "props": {
    "items": [
      {
        "id": "menu-item-shop",
        "type": "custom",
        "highlight": false,
        "itemProps": {
          "type": "internal",
          "href": "#",
          "noFollow": false,
          "tagTitle": "Shop",
          "text": "Shop"
        }
      },
      {
        "id": "menu-item-about-us",
        "type": "custom",
        "highlight": false,
        "itemProps": {
          "type": "internal",
          "href": "/about-us",
          "noFollow": false,
          "tagTitle": "about-us",
          "text": "About Us"
        }
      }
    ]
  }
}
```

You can define a submenu for a menu-item:

```jsonc
"menu-item#shop": {
  "props": {
    "type": "custom",
    "highlight": false,
    "itemProps": {
      "type": "internal",
      "href": "#",
      "noFollow": false,
      "tagTitle": "Shop",
      "text": "Shop"
    },
  },
  "blocks": ["vtex.menu@2.x:submenu#shop"] // Defining a submenu
},
"vtex.menu@2.x:submenu#shop": {
  "children": [
    "vtex.menu@2.x:menu#submenushop"
  ]
},
"vtex.menu@2.x:menu#submenushop": {
  "children": [
    "menu-item#shop"
  ]
}
```

<div class="alert alert-info">
The Menu block has no prerequisite children. Therefore, any menu block implementation does not need to have any blocks declared within it to properly function.
</div>

The available `menu-item` block props are as follows:

| Prop name      | Type     | Description                                          | Default value |
| -------------- | -------- | ---------------------------------------------------- | ------------- |
| `type`         | `String` | Menu item type, either `category` or `custom`                                            | `category`           |
| `id`           | `String` | menu item ID                                         | `undefined`   |
| `highlight`         | `boolean` | Whether the item has highlight                                            | `undefined`           |
| `iconPosition`         | `String` | Icon position relative to the menu item text. Either to the `left` or `right`                                           | `left`          |
| `iconProps`         | `IconProps` | Icon props                                           | `undefined`           |
| `onMountBehavior` | `enum` | Whether the submenu should always be automatically displayed when its parent is hovered/clicked on (`open`) or not (`closed`). | `closed` |
| `itemProps`         | `CategoryItem` or `CustomItem` | Item props                                           | `undefined`           |
| `classes`         | `CustomCSSClasses` | Used to override default CSS handles. To better understand how this prop works, we recommend reading about it [here](https://github.com/vtex-apps/css-handles#usecustomclasses). Note that this is only useful if you're importing this block as a React component.                                      | `undefined`           |

- For icons in the menu items:

| Prop name      | Type     | Description                                          | Default value |
| -------------- | -------- | ---------------------------------------------------- | ------------- |
| `id`         | `String` | Icon ID  | N/A           |
| `isActive`         | `boolean` | Whether the item is active or not | `true`          |
| `size`         | `number` | Icon size | 16           |
| `viewBox`         | `String` | Icon view box   | `0 0 16 16`           |
| `activeClassName`         | `String` | Icon classname when `isActive` is true  | N/A           |
| `mutedClassName`         | `String` | Icon classname when `isActive` is false  | N/A           |

- For category related menu items:

| Prop name      | Type     | Description                                          | Default value |
| -------------- | -------- | ---------------------------------------------------- | ------------- |
| `categoryId`         | `number` | Item category ID  | N/A           |
| `text`         | `String` | Menu item text  | N/A          |

- For customized items:

| Prop name      | Type     | Description                                          | Default value |
| -------------- | -------- | ---------------------------------------------------- | ------------- |
| `type`         | `String` | Menu item type, either `internal` or `external` | `internal`           |
| `href`         | `String` |  Link to where the menu item leads  | N/A |
| `noFollow`         | `boolean` | No follow attribute  | N/A          |
| `tagTitle`         | `String` | Menu item tag  | N/A          |
| `text`         | `String` | Menu item text  | N/A          |

#### Customization

In order to apply CSS customizations on this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handle                 |
| -------------------------- |
| `accordionIcon--isClosed`  |
| `accordionIcon--isOpen`    |
| `accordionIcon`            |
| `container`                |
| `linkLeft`                 |
| `linkMiddle`               |
| `linkRight`                |
| `menuContainerNav`         |
| `menuContainer`            |
| `menuItemInnerDiv`         |
| `menuItem`                 |
| `menuItem--isOpen`         |
| `menuItem--isClosed`       |
| `menuLinkDivLeft`          |
| `menuLinkDivMiddle`        |
| `menuLinkDivRight`         |
| `menuLinkNav`              |
| `renderLink`               |
| `styledLinkContainer`      |
| `styledLinkContent`        |
| `styledLinkIcon`           |
| `styledLink`               |
| `submenuAccordion`         |
| `submenuColumn`            |
| `submenuContainer`         |
| `submenuWrapper--isClosed` |
| `submenuWrapper--isOpen`   |
| `submenuWrapper`           |
| `submenu`                  |

## Contributors

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore -->
<table><tr><td align="center"><a href="http://giovanapereira.com.br/"><img src="https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-menu-1.png"></img></a></td></tr></table>

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!