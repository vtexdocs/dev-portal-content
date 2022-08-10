---
title: "Pickup point selector"
slug: "vtexbr-pickup-selector"
excerpt: "vtexbr.pickup-selector@2.0.4"
hidden: false
createdAt: "2022-04-20T12:40:48.378Z"
updatedAt: "2022-06-30T19:59:43.817Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

The pickup point selector app adds a block to your store, which allows shoppers to add a product to cart and select a pickup point for it with a single action.

The app creates a list of available pickup points by running a simulation with the selected SKU and the zipcode provoded by the shopper.

> ⚠️ Warning: This app should only be used inside the product page, since one of its dependencies is the `product-context`.

## Configuration

Follow the steps below to configure the app on your store theme.

### 1. Install the app in your workspace and account.

To do this, you can go to the [Pickup point selector page](https://apps.vtex.com/vtexbr-pickup-selector/p) in the VTEX app store or run this command in your terminal:
```bash
vtex install vtexbr.pickup-selector
```

### 2. Add the app as a theme dependency in the `manifest.json` file.

See an example of how to do this:
```json
  "peerDependencies": {
    "vtexbr.pickup-selector": "2.x"
  }
```

Now, you are able to use all the [blocks](#blocks) exported by the **pickup-selector** app and its respective [props](#props).

### 3. Adding the main block

Declare the app's main block in a given theme template or inside another block from the theme. See the code example below.

```json
  "pickup-selector": {
    "children": [
      "pickup-selector-zipcode-input",
      "pickup-selector-search-sla-button",
      "pickup-selector-sla-list"
    ]
  }
```

> ℹ️ Note that the [blocks](#blocks) `pickup-selector-zipcode-input`, `pickup-selector-search-sla-button` and `pickup-selector-sla-list` are required inside the main block. But you can use them in any order you want. You can also use flex-layout if needed.

### 4. Configuring the `pickup-selector-sla-list`

The only [block](#blocks) that should be used inside this one is the `pickup-selector-option-card`. We do this so that you can be free to style the option card as you want, and we will use that as a template for all the options. Below you can see an example.

```json
  "pickup-selector-sla-list": {
    "children": [
      "pickup-selector-option-card"
    ]
  }
```

### 5. Configuring the `pickup-selector-option-card`

You are free to style this block as you wish.

The app provides [blocks](#blocks) that will help with the information about the pickup point. They are the following:

- `pickup-selector-option-card-pickup-point-name`
- `pickup-selector-option-card-pickup-point-address`
- `pickup-selector-option-card-pickup-point-distance`
- `pickup-selector-option-card-pickup-point-sla`

The only mandatory block inside this one is the `pickup-selector-option-card-add-product-button`.

Below you can see and example of this:

```json
  "pickup-selector-option-card": {
    "children": [
      "flex-layout.col#card-container"
    ]
  },

  "flex-layout.col#card-container": {
    "children": [
      "flex-layout.row#card-header",
      "product-separator",
      "flex-layout.row#card-body"
    ]
  },

  "flex-layout.row#card-header": {
    "props": {
      "colSizing": "auto"
    },
    "children": [
      "pickup-selector-option-card-pickup-point-distance",
      "pickup-selector-option-card-pickup-point-name"
    ]
  },

  "flex-layout.row#card-body": {
    "props": {
      "colSizing": "auto"
    },
    "children": [
      "flex-layout.col#card-body-address",
      "flex-layout.col#card-body-call-to-action"
    ]
  },

  "flex-layout.col#card-body-address": {
    "children": [
      "pickup-selector-option-card-pickup-point-address"
    ]
  },

  "flex-layout.col#card-body-call-to-action": {
    "children":[
      "pickup-selector-option-card-pickup-point-sla",
      "pickup-selector-option-card-add-product-button"
    ]
  }
```

Using the configuration above, the end result would look like this:

![image](https://user-images.githubusercontent.com/8519076/136956522-eb7fab05-66dd-4356-9fe2-62d857e32341.png)


## Blocks

Check out the full list of exported blocks below:

| Block name                                          | Description                                                                                    |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `pickup-selector`                                   | Main block.                                                                                     |
| `pickup-selector-zipcode-input`                     | Shows the zipcode input.                                                                        |
| `pickup-selector-search-sla-button`                 | Button used to search the pickup SLA options based on the provided postal code and the selected SKU. |
| `pickup-selector-sla-list`                          | List that shows the card with the avaiable pickup options.                                      |
| `pickup-selector-option-card`                       | Card with pickup option information.                                                        |
| `pickup-selector-option-card-pickup-point-name`     | Pickup point name.                                                                              |
| `pickup-selector-option-card-pickup-point-address`  | Pickup point address.                                                                           |
| `pickup-selector-option-card-pickup-point-distance` | Distance to pickup point (in Km).                                                                   |
| `pickup-selector-option-card-pickup-point-sla`      | Pickup point SLA.                                                                               |
| `pickup-selector-option-card-add-product-button`    | Button that adds the product to cart and selects the pickup point.                           |

### Props

Some of these blocks accept props as described below:

#### `pickup-selector-option-card-pickup-point-distance` props

| Prop name        | Type     | Description                                                                                                                                          | Default value |
| ---------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `distanceSystem` | `string` | This prop is used to calculate the distance displayed by the block, it accepts `metric` (shows distance in Km) and `imperial` (shows distance in Mi). | `metric`      |

#### `pickup-selector-option-card-add-product-button` props

| Prop name            | Type      | Description                                                                                                                                                                                                                                                                                       | Default value |
| -------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `customPixelEventId` | `string`  | This prop should only be used with [minicart.v2](https://github.com/vtex-apps/minicart). It defines the ID for the event that is sent by the button upon user interaction. Should be the same ID configured on **minicart.v2** so that the drawer opens on successfully adding the product to the cart. | `undefined`   |
| `showToastFeedback`  | `boolean` | This prop is a fallback in order to support `minicart.v1`. This will show a toast with feedback on successfully adding the product to the cart.                                                                                                                                                     | `false`       |

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles                        |
| ---------------------------------- |
| `pickupPointOptionCard`            |
| `pickupPointAddress`               |
| `pickupPointDistance`              |
| `pickupPointName`                  |
| `pickupPointSla`                   |
| `pickupSelectorContainer`          |
| `pickupSelectorSlaList`            |
| `searchSlaButtonContainer`         |
| `selectPickupPointButtonContainer` |
| `zipcodeInputContainer`            |

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