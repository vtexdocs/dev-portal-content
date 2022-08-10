---
title: "Custom Mobile Menu"
slug: "autecocolombia-custom-mobile-menu"
excerpt: "autecocolombia.custom-mobile-menu@0.1.9"
hidden: true
createdAt: "2022-07-19T17:45:31.223Z"
updatedAt: "2022-07-19T17:45:31.223Z"
---
To use into the store theme, This component allows you to create a page with options that when selected will send you to a menu with submenus accordions that correspond to the selected option. It can also receive components of vtex as children

![Desktop](/1.png)
![Desktop](/2.png)

## Configuration

Add the app to your theme's dependencies on the `manifest.json`, for example:

```json
"dependencies": {
  "autecocolombia.custom-mobile-menu": "0.x"
}
```

Declare the custom-mobile-menu block and send the props and children.
```json
"custom-mobile-menu": {
    "props": {
      "menu": [
        //MENU Repuestos
        {
          "id": 1,
          "title": "REPUESTOS",
          "href": "/",
          "active": true,
          "items": [
            {
              //menus internos
              "title": "Entradas de aire",
              "href": "",
              "active": true,
              "items": [
                {
                  "title": "Filtros",
                  "href": "/"
                },
                {
                  "title": "Item 1",
                  "href": "/"
                },
                {
                  "title": "Entradas de aire",
                  "href": "/"
                },
                {
                  "title": "Item 1",
                  "href": "/"
                }
              ]
            },
            {
              //menus internos
              "title": "Otro submenu",
              "href": "",
              "active": true,
              "items": [
                {
                  "title": "Mas Filtros",
                  "href": "/"
                },
                {
                  "title": "Item 1",
                  "href": "/"
                },
                {
                  "title": "Entradas de aire",
                  "href": "/"
                },
                {
                  "title": "Item 1",
                  "href": "/"
                }
              ]
            }
          ]
        },

        //MENU Limpieza y cuidado
        {
          "id": 2,
          "title": "LIMPIEZA Y CUIDADO",
          "href": "/",
          "active": true,
          "items": []
        },
        //MENU Aceites y lubricantes
        {
          "id": 3,
          "title": "ACEITES Y LUBRICANTES",
          "href": "/",
          "active": true,
          "items": []
        },
        //MENU Accesorios
        {
          "id": 4,
          "title": "ACCESORIOS",
          "href": "/",
          "active": true,
          "items": []
        }
      ]
    },
    "children": [
      "flex-layout.row#mobile-drawer-landing-husqvarna-row-banner-2",
      "flex-layout.row#footer-redes-sociales"
    ]
}
```

3. Declare the app block in your store inside your porduct display page.

```json
{
   ...
   "children":[
      "custom-mobile-menu"
   ]
}
```

## Customization

In the store-theme create a file theme-name.custom-mobile-menu.css inside the css folder and you can change css properties through the defined useCssHandles classes.



# Store Drawer Custom

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->

This component allows you to have a sliding drawer for your menus. This is specially handy for mobile layouts.

## Configuration

Add the app to your theme's dependencies on the `manifest.json`, for example:

```json
"dependencies": {
  "autecocolombia.custom-mobile-menu": "0.x"
}
```

Then, you need to add the `drawer` block into your app. The following is an example taken from [Store Theme](https://github.com/vtex-apps/store-theme).

```json
"autecocolombia.custom-mobile-menu:drawer": {
  "children": [
    "menu#drawer"
  ]
},

"menu#drawer": {
  "children": [
    "menu-item#category-clothing",
    "menu-item#category-decoration",
    "menu-item#custom-sale"
  ],
  "props": {
    "orientation": "vertical"
  }
},
```

There is also a block that can be used for customizing the icon that triggers the opening of the drawer, it's called `"drawer-trigger"` and can be used as follows:

```json
"autecocolombia.custom-mobile-menu:drawer": {
  "children": [
    "menu#drawer"
  ],
  "blocks": ["drawer-trigger"]
},

"autecocolombia.custom-mobile-menu:drawer-trigger": {
  "children": ["rich-text#open-drawer"]
},

"rich-text#open-drawer": {
  "text": "Open drawer"
}

"menu#drawer": {
  "children": [
    "menu-item#category-clothing",
    "menu-item#category-decoration",
    "menu-item#custom-sale"
  ],
  "props": {
    "orientation": "vertical"
  }
},
```

And there is a block that enables customization of the header that contains the button which closes the drawer.
It's called `"drawer-header"` and can be used in a similar way as `"drawer-trigger"`, here is an example:

```jsonc
// inside blocks.json
{
  "autecocolombia.custom-mobile-menu:drawer": {
    "blocks": ["drawer-header#my-drawer"]
  },
  "autecocolombia.custom-mobile-menu:drawer-header#my-drawer": {
    "children": [
      // you need to include the block `drawer-close-button` somewhere inside here
      "flex-layout.row#something",
      // ...
      "drawer-close-button"
    ]
  }
}
```


## Configuration

The `drawer` block accepts a few props that allow you to customize it.

| Prop name            | Type                                                                       | Description                                                                           | Default value  |
| -------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | -------------- |
| `maxWidth`           | `number` or `string`                                                       | Define the open Drawer's maximum width.                                               | `450`          |
| `isFullWidth`        | `Boolean`                                                                  | Control whether or not the open Drawer should occupy the full available width.        | `false`        |
| `slideDirection`     | `'horizontal'`&#124;`'vertical'`&#124;`'rightToLeft'`&#124;`'leftToRight'` | Controls the opening animation's direction.                                           | `'horizontal'` |
| `backdropMode`       | `'default'`&#124;`'none'`                                                  | Controls if it should display the backdrop when the Drawer is open                    |
| `customPixelEventId` | `string`   | Store event ID responsible for triggering the `drawer` to automatically open itself on the interface. | `undefined`    |
| `customPixelEventName` | `string`                                                                   | Store event name responsible for triggering the `drawer` to automatically open itself on the interface. Some examples are: `'addToCart'` and `'removeFromCart'` events. Notice that using this prop will make the drawer open in **every** event with the specified name if no `customPixelEventId` is specified. | `undefined`    |

The `drawer-close-button` block accepts the following props to customize it:

| Prop name | Type                     | Description                                   | Default value |
| --------- | ------------------------ | --------------------------------------------- | ------------- |
| `size`    | `Number`                 | Define the size of the icon inside the button | `30`          |
| `type`    | `'filled'`&#124;`'line'` | Define the type of the icon                   | `'line'`      |

The `drawer-trigger` block accepts the following prop to customize it:

| Prop name            | Type     | Description                                                           | Default value |
| -------------------- | -------- | --------------------------------------------------------------------- | ------------- |
| `customPixelEventId` | `string` | Defines the event ID to be sent whenever users interact with the Drawer component. | `undefined`   |

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles              |
| ------------------------ |
| `drawer`                 |
| `opened`                 |
| `overlay`                |
| `overlay--visible`       |
| `closed`                 |
| `moving`                 |
| `drawerContent`          |
| `drawerHeader`           |
| `drawerTriggerContainer` |
| `openIconContainer`      |
| `closeIconContainer`     |
| `closeIconButton`        |
| `childrenContainer`      |

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/Radu1749"><img src="https://avatars2.githubusercontent.com/u/51535501?v=4" width="100px;" alt=""/><br /><sub><b>Radu1749</b></sub></a><br /><a href="https://github.com/vtex-apps/drawer/commits?author=Radu1749" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/rayra-alencar"><img src="https://avatars0.githubusercontent.com/u/28907161?v=4" width="100px;" alt=""/><br /><sub><b>rayra-alencar</b></sub></a><br /><a href="https://github.com/vtex-apps/drawer/commits?author=rayra-alencar" title="Code">💻</a></td>
    <td align="center"><a href="https://gitlab.com/fbailon"><img src="https://secure.gravatar.com/avatar/0186704106dc8ba25b228e5a1d2257e1?s=800&d=identicon" width="100px;" alt=""/><br /><sub><b>Fernando Bailon</b></sub></a><br />💻</td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!