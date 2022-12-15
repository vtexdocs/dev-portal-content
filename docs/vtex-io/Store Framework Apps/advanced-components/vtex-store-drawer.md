---
title: "Store Drawer"
slug: "vtex-store-drawer"
excerpt: "vtex.store-drawer@0.16.2"
hidden: false
createdAt: "2020-06-03T15:19:47.724Z"
updatedAt: "2022-06-13T17:20:27.990Z"
---
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-3-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

This component allows you to have a sliding drawer for your menus. This is specially handy for mobile layouts.

## Configuration

Add the app to your theme's dependencies on the `manifest.json`, for example:

```json
"dependencies": {
  "vtex.store-drawer": "0.x"
}
```

Then, you need to add the `drawer` block into your app. The following is an example taken from [Store Theme](https://github.com/vtex-apps/store-theme).

```json
"drawer": {
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
"drawer": {
  "children": [
    "menu#drawer"
  ],
  "blocks": ["drawer-trigger"]
},

"drawer-trigger": {
  "children": ["rich-text#open-drawer"]
},

"rich-text#open-drawer": {
  "props": {
    "text": "Open drawer"
  }
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
  "drawer": {
    "blocks": ["drawer-header#my-drawer"]
  },
  "drawer-header#my-drawer": {
    "children": [
      // you need to include the block `drawer-close-button` somewhere inside here
      "flex-layout.row#something",
      // ...
      "drawer-close-button"
    ]
  }
}
```

If you're using this component by itself, you just need to import it inside the component you want to use it in. Here's an example:

```tsx
import { Drawer, DrawerHeader, DrawerCloseButton } from 'vtex.store-drawer'

const Menu = () => (
  <Drawer
    header={
      <DrawerHeader>
        <DrawerCloseButton />
      </DrawerHeader>
    }
  >
    <ul>
      <li>Link 1</li>
      <li>Link 2</li>
      <li>Link 3</li>
      <li>Link 4</li>
      <li>Link 5</li>
      <li>Link 6</li>
    </ul>
  </Drawer>
)
```

## Configuration

The `drawer` block accepts a few props that allow you to customize it.

| Prop name            | Type                                                                       | Description                                                                           | Default value  |
| -------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | -------------- |
| `maxWidth`           | `number` or `string`                                                       | Define the open Drawer's maximum width.                                               | `450`          |
| `isFullWidth`        | `Boolean`                                                                  | Control whether or not the open Drawer should occupy the full available width.        | `false`        |
| `slideDirection`     | `'horizontal'`&#124;`'vertical'`&#124;`'rightToLeft'`&#124;`'leftToRight'` | Controls the opening animation's direction.                                           | `'horizontal'` |
| `backdropMode`       | `'default'`&#124;`'none'`                                                  | Controls if it should display the backdrop when the Drawer is open                    |
| `renderingStrategy`       | `'lazy'`&#124;`'eager'`                                                  | Controls if it should render the children only when clicked (`lazy`) or as soon as the page loads (`eager`). Enabling the `eager` strategy may increase SEO performance, but the page may be rendered slower                   | `'lazy'`
| `customPixelEventId` | `string`   | Store event ID responsible for triggering the `drawer` to automatically open itself on the interface. | `undefined`    |
| `customPixelEventName` | `string`                                                                   | Store event name responsible for triggering the `drawer` to automatically open itself on the interface. Some examples are: `'addToCart'` and `'removeFromCart'` events. Notice that using this prop will make the drawer open in **every** event with the specified name if no `customPixelEventId` is specified. | `undefined`    |

The `drawer-close-button` block accepts the following props to customize it:

| Prop name | Type                     | Description                                   | Default value |
| --------- | ------------------------ | --------------------------------------------- | ------------- |
| `size`    | `Number`                 | Define the size of the icon inside the button | `30`          |
| `type`    | `'filled'`&#124;`'line'` | Define the type of the icon                   | `'line'`      |
| `text`    | `String`                 | Define the text inside the button. If `text` is defined, the icon will not be rendered.             | `undefined`   |

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
    <td align="center"><a href="https://github.com/Radu1749"><img src="https://avatars2.githubusercontent.com/u/51535501?v=4" width="100px;" alt=""/><br /><sub><strong>Radu1749</strong></sub></a><br /><a href="https://github.com/vtex-apps/drawer/commits?author=Radu1749" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/rayra-alencar"><img src="https://avatars0.githubusercontent.com/u/28907161?v=4" width="100px;" alt=""/><br /><sub><strong>rayra-alencar</strong></sub></a><br /><a href="https://github.com/vtex-apps/drawer/commits?author=rayra-alencar" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/renanguerraa1"><img src="https://avatars2.githubusercontent.com/u/69531548?v=4" width="100px;" alt=""/><br /><sub><strong>Renan Guerra</strong></sub></a><br /><a href="https://github.com/vtex-apps/drawer/commits?author=renanguerraa1" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!