---
title: "Store Icons"
slug: "vtex-store-icons"
hidden: false
createdAt: "2020-06-03T15:19:30.629Z"
updatedAt: "2020-10-05T18:52:00.018Z"
---

All Store icons components.

## Table of Contents

- [Store Icons](#store-icons)
  - [Description](#description)
  - [Release schedule](#release-schedule)
  - [Table of Contents](#table-of-contents)
  - [Concept](#concept)
  - [Usage](#usage)
    - [Dedicated Icon](#dedicated-icon)
    - [Generic Icon](#generic-icon)
  - [Icons](#icons)
    - [Props](#props)
    - [Icons List](#icons-list)
      - [Brand](#brand)
      - [High Priority Actions](#high-priority-actions)
      - [Middle Priority Actions](#middle-priority-actions)
      - [Informational](#informational)
      - [Navigation](#navigation)
      - [Status Indicators](#status-indicators)
  - [Customize](#customize)
    - [Overwriting the default IconPack](#overwriting-the-default-iconpack)
    - [Nomenclature](#nomenclature)
      - [Icon Intention](#icon-intention)
  - [Troubleshooting](#troubleshooting)
  - [Contributing](#contributing)
  - [Tests](#tests)

## Concept

This project is based on [SVG fragment identifiers](https://css-tricks.com/svg-fragment-identifiers-work/). All store icons are served by Render SDK, and with HTML tag `<use>` we can render a fragment from our icon pack. If you want to know the complete list of fragment SVG's, [see here](https://github.com/vtex-apps/store-icons/blob/master/docs/ICONPACK.md)

## Usage

First of all, add into the dependencies of your `manifest.tsxon` and use it as an npm module:

```json
"dependencies": {
  "vtex.store-icons": "0.x"
}
```

There are two different ways to use the icons available here. If you're developing a store's theme, you should use the `icon` block for the icon you want to render, which behaves just like any other block and expects to receive the props exposed by its [API](#props). But if you're developing custom components and want to use icons defined here, just follow the instructions below.

### Dedicated Icon

Import the desired icon and use it into your code, for example:

```js
import { IconMenu } from 'vtex.store-icons'

const YourComponent = (props) => <IconMenu />
```

You can see [here](#icon-list) a list of every available icon.

### Generic Icon

The API provides a generic icon, The `Icon` component. You can choose from any other icon passing only the `id` from the respective one you want to add.

For example:

```js
import { Icon } from 'vtex.store-icons'

const YourComponent = (props) => <Icon id="hpa-cart" />
```

⚠️ This component is meant to be used on icons there aren't common throughout the store. Choose [`dedicated`](#dedicated-icon) components whenever possible.

## Icons

### Props

Any icon can receive the following props:

| Property        | Description                                | Type      | Default value |
| --------------- | ------------------------------------------ | --------- | ------------- |
| id              | The ID for the desired icon                | `String`  | ''            |
| size            | Desired size                               | `Number`  | 16            |
| isActive        | desc                                       | `Boolean` | true          |
| activeClassName | The className it should have if active     | `String`  | 🚫            |
| mutedClassName  | The className it should have if not active | `String`  | 🚫            |

Obs: **...props**: It is important to notice that any other `<svg>` prop passed will work with an icon as well.

#### Enhanced Props

Some components support modifiers. These are props that define the icon type, orientation, state or shape.

| Modifier    | Possible values             |
| ----------- | --------------------------- |
| type        | `filled` `line` `outline`   |
| orientation | `up` `down` `left` `right`  |
| state       | `on` `off`                  |
| shape       | `square` `rounded` `circle` |

### Icon List

#### Brand

| Component                                                                                    | id       | Type | Orientation | State | Shape                       |
| -------------------------------------------------------------------------------------------- | -------- | ---- | ----------- | ----- | --------------------------- |
| [IconSocial](https://github.com/vtex-apps/store-icons/tree/master/react/IconSocial.tsx) | `social` | 🚫   | 🚫          | 🚫    | square \| rounded \| circle |

#### High Priority Actions

| Component                                                                                                    | id                | Type | Orientation | State | Shape |
| ------------------------------------------------------------------------------------------------------------ | ----------------- | ---- | ----------- | ----- | ----- |
| [IconArrowBack](https://github.com/vtex-apps/store-icons/tree/master/react/IconArrowBack.tsx)           | `arrow-back`      | 🚫   | 🚫          | 🚫    | 🚫    |
| [IconAssistantSales](https://github.com/vtex-apps/store-icons/tree/master/react/IconAssistantSales.tsx) | `assistant-sales` | 🚫   | 🚫          | 🚫    | 🚫    |
| [IconProfile](https://github.com/vtex-apps/store-icons/tree/master/react/IconProfile.tsx)               | `profile`         | 🚫   | 🚫          | 🚫    | 🚫    |
| [IconCart](https://github.com/vtex-apps/store-icons/tree/master/react/IconCart.tsx)                     | `cart`            | 🚫   | 🚫          | 🚫    | 🚫    |
| [IconSearch](https://github.com/vtex-apps/store-icons/tree/master/react/IconSearch.tsx)                 | `search`          | 🚫   | 🚫          | 🚫    | 🚫    |
| [IconDelete](https://github.com/vtex-apps/store-icons/tree/master/react/IconDelete.tsx)                 | `delete`          | 🚫   | 🚫          | 🚫    | 🚫    |
| [IconMenu](https://github.com/vtex-apps/store-icons/tree/master/react/IconMenu.tsx)                     | `menu`            | 🚫   | 🚫          | 🚫    | 🚫    |
| [IconLocationMarker](https://github.com/vtex-apps/store-icons/tree/master/react/IconLocationMarker.tsx) | `location-marker` | 🚫   | 🚫          | 🚫    | 🚫    |

#### Medium Priority Actions

| Component                                                                                            | id            | Type                      | Orientation | State     | Shape |
| ---------------------------------------------------------------------------------------------------- | ------------- | ------------------------- | ----------- | --------- | ----- |
| [IconEyesight](https://github.com/vtex-apps/store-icons/tree/master/react/IconEyesight.tsx)     | `eyesight`    | filled \| outline         | 🚫          | on \| off | 🚫    |
| [IconMinus](https://github.com/vtex-apps/store-icons/tree/master/react/IconMinus.tsx)           | `minus`       | filled \| outline \| line | 🚫          | 🚫 brands |
| [IconPlus](https://github.com/vtex-apps/store-icons/blobrandseact/IconPlus.tsx)                       | `plus`        | filled \| outline \| line | 🚫          | 🚫        | 🚫    | brands |
| [IconSingleItem](https://github.com/vtex-apps/store-icons/tree/master/react/IconSingleItem.tsx) | `single-item` | 🚫                        | 🚫          | 🚫        | 🚫    |
| [IconList](https://github.com/vtex-apps/store-icons/tree/master/react/IconList.tsx)             | `list`        | 🚫                        | 🚫          | 🚫        | 🚫    |
| [IconGallery](https://github.com/vtex-apps/store-icons/tree/master/react/IconGallery.tsx)       | `gallery`     | 🚫                        | 🚫          | 🚫        | 🚫    |
| [IconRemove](https://github.com/vtex-apps/store-icons/tree/master/react/IconRemove.tsx)         | `remove`      | 🚫                        | 🚫          | 🚫        | 🚫    |
| [IconSwap](https://github.com/vtex-apps/store-icons/tree/master/react/IconSwap.tsx)             | `swap`        | 🚫                        | 🚫          | 🚫        | 🚫    |
| [IconHeart](https://github.com/vtex-apps/store-icons/tree/master/react/IconHeart.tsx)           | `heart`       | 🚫                        | 🚫          | 🚫        | 🚫    |
| [IconGlobe](https://github.com/vtex-apps/store-icons/tree/master/react/IconGlobe.tsx)           | `globe`       | 🚫                        | 🚫          | 🚫        | 🚫    |
| [IconBookmark](https://github.com/vtex-apps/store-icons/tree/master/react/IconBookmark.tsx)     | `bookmark`    | filled \| outline         | 🚫          | 🚫        | 🚫    |
| [IconPlay](https://github.com/vtex-apps/store-icons/tree/master/react/IconPlay.tsx)             | `play`        | filled \| outline         | 🚫          | 🚫        | 🚫    |
| [IconPause](https://github.com/vtex-apps/store-icons/tree/master/react/IconPause.tsx)           | `pause`       | filled \| outline         | 🚫          | 🚫        | 🚫    |

#### Navigation

| Component                                                                                  | id      | Type | Orientation                 | State | Shape |
| ------------------------------------------------------------------------------------------ | ------- | ---- | --------------------------- | ----- | ----- |
| [IconCaret](https://github.com/vtex-apps/store-icons/tree/master/react/IconCaret.tsx) | `caret` | 🚫   | up \| down \| left \| right | 🚫    | 🚫    | true \| false |

#### Status Indicators

| Component                                                                                          | id           | Type                      | Orientation | State | Shape |
| -------------------------------------------------------------------------------------------------- | ------------ | ------------------------- | ----------- | ----- | ----- |
| [IconClose](https://github.com/vtex-apps/store-icons/tree/master/react/IconClose.tsx)         | `close`      | filled \| outline         | 🚫          | 🚫    | 🚫    |
| [IconCheck](https://github.com/vtex-apps/store-icons/tree/master/react/IconCheck.tsx)         | `check`      | filled \| outline \| line | 🚫          | 🚫    | 🚫    |
| [IconVolumeOn](https://github.com/vtex-apps/store-icons/tree/master/react/IconVolumeOn.tsx)   | `volume-on`  | filled \| outline \| line | 🚫          | 🚫    | 🚫    |
| [IconVolumeOff](https://github.com/vtex-apps/store-icons/tree/master/react/IconVolumeOff.tsx) | `volume-off` | filled \| outline \| line | 🚫          | 🚫    | 🚫    |

## Customize

In the [usage](#usage) section, we discuss two ways of using icons. These ways extend to customization, so, prefer to change an existing Icon so that you can use the [dedicated](#dedicated-icon) version. You can check how to override and name icons below.

### Overwriting the default IconPack

As mentioned before, all icon IDs are stored at the [iconpack.svg](https://github.com/vtex-apps/store-icons/blob/master/docs/ICONPACK.md) file. You can overwrite the default one by:

1. On your [`store-theme`](https://github.com/vtex-apps/store-theme/tree/master/styles) create a new folder called `iconpacks`

2. Create a file called `iconpack.svg`

3. Declare your icon IDs (use the default `iconpack` as an example in how to do that properly).

### Nomenclature

The naming convention is: [`intention`](#icon-intention)-[`id`](#icon-list)--[`?modifiers`](#enhanced-props)

Where the `modifiers` follows the rule:
`?type`--`?orientation`--`?state`--`?shape`

**🤓 ? stands for optional inputs**

#### Icon Intention

`bnd` **Brand** - Display logos, brands or advertisements.

`hpa` **High priority actions** - Actions that are important to the global context.

`mpa` **Mild priority actions** - Actions that are important only to the current component context.

`inf` **Informational** - Represents information display or actions that, when triggered, reveal further details about the current context.

`nav` **Navigation** - Actions that triggers navigation.

`sti` **Status indicators** - Indicates the current item/component semantic status.

## CSS Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles          |
| -------------------- |
| 'arrowBackIcon'      |
| 'assistantSalesIcon' |
| 'caretIcon'          |
| 'cartIcon'           |
| 'checkIcon'          |
| 'closeIcon'          |
| 'deleteIcon'         |
| 'equalsIcon'         |
| 'eyeSightIcon'       |
| 'filterIcon'         |
| 'globeIcon'          |
| 'gridIcon'           |
| 'heartIcon'          |
| 'homeIcon'           |
| 'inlineGridIcon'     |
| 'locationInputIcon'  |
| 'locationMarkerIcon' |
| 'menuIcon'           |
| 'minusIcon'          |
| 'plusIcon'           |
| 'profileIcon'        |
| 'removeIcon'         |
| 'searchIcon'         |
| 'singleGridIcon'     |
| 'socialIcon'         |
| 'starIcon'           |
| 'swapIcon'           |
| 'playIcon'           |
| 'pauseIcon'          |
| 'fullscreenIcon'     |
| 'volumeOnIcon'       |
| 'volumeOffIcon'      |
