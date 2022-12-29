---
title: "Store Icons"
slug: "vtex-store-icons"
excerpt: "vtex.store-icons@0.18.0"
hidden: false
createdAt: "2020-06-03T15:19:30.629Z"
updatedAt: "2020-10-05T18:52:00.018Z"
---
📢 Use this project, [contribute](https://github.com/vtex-apps/store-icons) to it or open issues to help evolve it using [Store Discussion](https://github.com/vtex-apps/store-discussion).

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/vtex-io/Store Framework Apps/functional-apps/#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->

# Store Icons

[![Build Status](https://travis-ci.org/vtex-apps/store-icons.svg?branch=master)](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-store-icons-0.png)

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

First of all, add into the dependencies of your `manifest.json` and use it as an npm module:

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
| [IconSocial](https://github.com/vtex-apps/store-icons/blob/feature/docs/react/IconSocial.js) | `social` | 🚫   | 🚫          | 🚫    | square \| rounded \| circle |

#### High Priority Actions

| Component                                                                                                    | id                | Type | Orientation | State | Shape |
| ------------------------------------------------------------------------------------------------------------ | ----------------- | ---- | ----------- | ----- | ----- |
| [IconArrowBack](https://github.com/vtex-apps/store-icons/blob/feature/docs/react/IconArrowBack.js)           | `arrow-back`      | 🚫   | 🚫          | 🚫    | 🚫    |
| [IconAssistantSales](https://github.com/vtex-apps/store-icons/blob/feature/docs/react/IconAssistantSales.js) | `assistant-sales` | 🚫   | 🚫          | 🚫    | 🚫    |
| [IconProfile](https://github.com/vtex-apps/store-icons/blob/feature/docs/react/IconProfile.js)               | `profile`         | 🚫   | 🚫          | 🚫    | 🚫    |
| [IconCart](https://github.com/vtex-apps/store-icons/blob/feature/docs/react/IconCart.js)                     | `cart`            | 🚫   | 🚫          | 🚫    | 🚫    |
| [IconSearch](https://github.com/vtex-apps/store-icons/blob/feature/docs/react/IconSearch.js)                 | `search`          | 🚫   | 🚫          | 🚫    | 🚫    |
| [IconDelete](https://github.com/vtex-apps/store-icons/blob/feature/docs/react/IconDelete.js)                 | `delete`          | 🚫   | 🚫          | 🚫    | 🚫    |
| [IconMenu](https://github.com/vtex-apps/store-icons/blob/feature/docs/react/IconMenu.js)                     | `menu`            | 🚫   | 🚫          | 🚫    | 🚫    |
| [IconLocationMarker](https://github.com/vtex-apps/store-icons/blob/feature/docs/react/IconLocationMarker.js) | `location-marker` | 🚫   | 🚫          | 🚫    | 🚫    |

#### Medium Priority Actions

| Component                                                                                            | id            | Type                      | Orientation | State     | Shape |
| ---------------------------------------------------------------------------------------------------- | ------------- | ------------------------- | ----------- | --------- | ----- |
| [IconEyesight](https://github.com/vtex-apps/store-icons/blob/feature/docs/react/IconEyesight.js)     | `eyesight`    | filled \| outline         | 🚫          | on \| off | 🚫    |
| [IconMinus](https://github.com/vtex-apps/store-icons/blob/feature/docs/react/IconMinus.js)           | `minus`       | filled \| outline \| line | 🚫          | 🚫 brands |
| [IconPlus](https://github.com/vtex-apps/store-icons/blobrandseact/IconPlus.js)                       | `plus`        | filled \| outline \| line | 🚫          | 🚫        | 🚫    | brands |
| [IconSingleItem](https://github.com/vtex-apps/store-icons/blob/feature/docs/react/IconSingleItem.js) | `single-item` | 🚫                        | 🚫          | 🚫        | 🚫    |
| [IconList](https://github.com/vtex-apps/store-icons/blob/feature/docs/react/IconList.js)             | `list`        | 🚫                        | 🚫          | 🚫        | 🚫    |
| [IconGallery](https://github.com/vtex-apps/store-icons/blob/feature/docs/react/IconGallery.js)       | `gallery`     | 🚫                        | 🚫          | 🚫        | 🚫    |
| [IconRemove](https://github.com/vtex-apps/store-icons/blob/feature/docs/react/IconRemove.js)         | `remove`      | 🚫                        | 🚫          | 🚫        | 🚫    |
| [IconSwap](https://github.com/vtex-apps/store-icons/blob/feature/docs/react/IconSwap.js)             | `swap`        | 🚫                        | 🚫          | 🚫        | 🚫    |
| [IconHeart](https://github.com/vtex-apps/store-icons/blob/feature/docs/react/IconHeart.js)           | `heart`       | 🚫                        | 🚫          | 🚫        | 🚫    |
| [IconGlobe](https://github.com/vtex-apps/store-icons/blob/feature/docs/react/IconGlobe.js)           | `globe`       | 🚫                        | 🚫          | 🚫        | 🚫    |
| [IconBookmark](https://github.com/vtex-apps/store-icons/blob/feature/docs/react/IconBookmark.js)     | `bookmark`    | filled \| outline         | 🚫          | 🚫        | 🚫    |
| [IconPlay](https://github.com/vtex-apps/store-icons/blob/feature/docs/react/IconPlay.js)             | `play`        | filled \| outline         | 🚫          | 🚫        | 🚫    |
| [IconPause](https://github.com/vtex-apps/store-icons/blob/feature/docs/react/IconPause.js)           | `pause`       | filled \| outline         | 🚫          | 🚫        | 🚫    |

#### Navigation

| Component                                                                                  | id      | Type | Orientation                 | State | Shape |
| ------------------------------------------------------------------------------------------ | ------- | ---- | --------------------------- | ----- | ----- |
| [IconCaret](https://github.com/vtex-apps/store-icons/blob/feature/docs/react/IconCaret.js) | `caret` | 🚫   | up \| down \| left \| right | 🚫    | 🚫    | true \| false |

#### Status Indicators

| Component                                                                                          | id           | Type                      | Orientation | State | Shape |
| -------------------------------------------------------------------------------------------------- | ------------ | ------------------------- | ----------- | ----- | ----- |
| [IconClose](https://github.com/vtex-apps/store-icons/blob/feature/docs/react/IconClose.js)         | `close`      | filled \| outline         | 🚫          | 🚫    | 🚫    |
| [IconCheck](https://github.com/vtex-apps/store-icons/blob/feature/docs/react/IconCheck.js)         | `check`      | filled \| outline \| line | 🚫          | 🚫    | 🚫    |
| [IconVolumeOn](https://github.com/vtex-apps/store-icons/blob/feature/docs/react/IconVolumeOn.js)   | `volume-on`  | filled \| outline \| line | 🚫          | 🚫    | 🚫    |
| [IconVolumeOff](https://github.com/vtex-apps/store-icons/blob/feature/docs/react/IconVolumeOff.js) | `volume-off` | filled \| outline \| line | 🚫          | 🚫    | 🚫    |

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

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!