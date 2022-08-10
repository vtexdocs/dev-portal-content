---
title: "Expandable Menu"
slug: "levimx-landings"
excerpt: "levimx.landings@0.0.24"
hidden: true
createdAt: "2022-07-19T20:32:46.411Z"
updatedAt: "2022-08-02T02:32:47.135Z"
---
Vertically expanding menu to show submenu items.
Each menu item has an image that corresponds to the menu title.

![Media Placeholder](./expandable-menu.png)

## Configuration

Declare the block in your store theme with the following props

```
"mobile-menu":{
  "props":{
    "menu":[
      {
        "title": STRING,
        "href": STRING (eg. /charms),
        "items":[
          {
            "title": STRING,
            "href": STRING (eg. /charms/pandora-me)
          },
          {
            "title": STRING,
            "href": STRING (eg. /charms/pandora-me)
          },
          {...}
        ]
      },
      {...}
    ]
  }
}
```

Only the following `menu item TITLES` have images assigned to them

- Charms
- Aros
- Brazaletes
- Anillos
- Collares y Dijes
- Descubrir

Images are not dynamic. If a new different menu item is added/changed in the JSON declaration statement a new image must be declared. Otherwise a placeholder will be shown.

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles            |
| ---------------------- |
| `container`            |
| `menuItemContainer`    |
| `subMenuItemContainer` |

## Contributors ✨

- Kinich Barcelo