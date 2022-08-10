---
title: "Store Locator"
slug: "canali-store-locator"
excerpt: "canali.store-locator@0.1.8"
hidden: true
createdAt: "2022-07-13T12:54:35.309Z"
updatedAt: "2022-08-09T17:38:22.050Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

The Store Locator app fetches the Pickup point data in order to display address location for retail stores.

![store-list](images/store-list.png)
![store-detail](images/store-detail.png)

## Configuration

1. [Install](https://vtex.io/docs/recipes/development/installing-an-app/) the Store Locator app in your VTEX account by running `vtex install codeby.store-locator` in your terminal.
2. In your account's admin page, select **Inventory&Shipping** section and then acess **Settings**.
3. Type in the Google Geolocation API key and save your changes.
4. Open your Store Theme app directory in your code editor.
5. Add the Store Locator app as a `peerDependency` in the `manifest.json` file:

```diff
 "peerDependencies": {
+  "codeby.store-locator": "1.x"
 }
```

Once installed, the app will generate a new route called `/stores` for your store, listing the retail stores registered in the Pickup points section (under the Inventory & shipping module).

The new page already contains a default template with all blocks exported by the Store Locator app, meaning that the `/stores` page is ready to be rendered and no further actions are required. However, you can **customize the new page overwriting the template by creating a brand new one as you wish**. To do so, check the **Advanced configurations** section below.

> ℹ️ _This app will also **add a new entry to your store's `/sitemap.xml` file in order to have all the pickup points available to the search engines** - make sure you already have the `vtex.store-sitemap@2.x` app installed in your VTEX account!_

### Advanced configuration

In order to define the Store Locator custom page UI, you must use the blocks exported by the `codeby.store-locator` app. Namely, they are:

|       Block name       |                                            Description                                             |
| :--------------------: | :------------------------------------------------------------------------------------------------: |
|      `store-list`      |               Renders a list of retail stores and a map with all their localization.               |
|     `store-group`      | Provides the pickup point data to other blocks exported by the app, such as the ones listed below. |
|      `store-name`      |                                      Renders the store name.                                       |
|   `store-back-link`    |                           Renders a link to return to the previous page.                           |
|      `store-map`       |                         Renders a map with the retail store localization.                          |
|    `store-address`     |                                    Renders the store's address.                                    |
|     `store-hours`      |                                 Renders the store's opening hours.                                 |
|  `store-instructions`  |                    Renders the desired instructions to access the retail store.                    |
| `store-default-styles` |                        Apply a default style for both list and details page                        |

1. Open your Store Theme app directory in your code editor.
2. In the `store` folder of your Store Theme app, create a new file called `storelocator.json`.
3. Create a new store template in it called `store.storelocator`. In its blocks array, paste the default implementation stated below:

```json
{
  "store.storelocator": {
    "blocks": ["store-default-styles", "store-list"]
  },
  "store-list": {
    "props": {
    }
  },
  "store.storedetail": {
    "blocks": ["store-group"]
  },
  "store-group": {
    "children": ["flex-layout.row#containerStore"],
    "props": {
      "title": "{storeName} Store"
    }
  },
  "flex-layout.row#containerStore": {
    "children": ["flex-layout.col#detail"],
    "props": {
      "blockClass": "detailsContainer"
    }
  },
  "flex-layout.col#detail": {
    "children": [
      "store-back-link",
      "store-name",
      "store-map",
      "store-address",
      "store-hours",
      "store-instructions"
    ],
    "props": {
      "preventVerticalStretch": true
    }
  },
  "store-hours": {
    "props": {
      "label": "Business hours:",
      "format": "12h"
    }
  },
  "store-back-link": {
    "props": {
      "label": "Back to all stores"
    }
  },
  "store-instructions": {
    "props": {
      "label": ""
    }
  }
}
```

4. Configure each one of the blocks previously declared as you wish using their props (check out the following tables).

#### `store-list`

|   Prop name   |   Type   |                                    Description                                    |     Default value     |
| :-----------: | :------: | :-------------------------------------------------------------------------------: | :-------------------: |
| `filterByTag` | `string` |      Desired tags to filter the Pickup Points fetched and displayed. You can      |      `undefined`      |
|    `icon`     | `string` | Icon URL (`svg` or `png`) to be displayed alongside with the `store-list` blocks. |   Google's default.   |
|  `iconWidth`  | `number` |                           Icon width in pixels (`px`).                            | Image default width.  |
| `iconHeight`  | `number` |                           Icon height in pixels (`px`).                           | Image default height. |

#### `store-group` props

|       Prop name       |   Type    |                                                                                                                     Description                                                                                                                      | Default value |
| :-------------------: | :-------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------: |
|        `title`        | `string`  |                                           Text to be displayed alongside with the store name. Use `{storeName}`, `{storeCity}`, or `{storeState}` as value to display the store's accurate data on the UI.                                           | `{storeName}` |
|    `imageSelector`    | `string`  |                                                                                           CSS Selector that will wrap all the images displayed on the UI.                                                                                            |  `undefined`  |
| `instructionsAsPhone` | `boolean` | To provide a unique phone number for each store, a phone number can be entered in the `Instructions` field in the Pickup Points section. The `store-instructions` will display a phone number and it will be included in the page's Structured Data. |    `false`    |

> ⚠️ _Both `imageSelector` and `instructionsAsPhone` must be declared with valid values in order to provide Structured Data for SEO purposes._

#### `store-name` props

| Prop name |   Type   |                                                                           Description                                                                            | Default value |
| :-------: | :------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------: |
|  `text`   | `string` | Text to be displayed alongside with the store name. Use `{storeName}`, `{storeCity}`, or `{storeState}` as value to display the store's accurate data on the UI. |               |
|   `tag`   | `string` |                                               HTML element to wrap the `store-name` block when rendered on the UI.                                               |     `div`     |

#### `store-back-link` props

| Prop name |   Type   |                          Description                          |    Default value     |
| :-------: | :------: | :-----------------------------------------------------------: | :------------------: |
|  `label`  | `string` | Entitles the `store-back-link` block when rendered on the UI. | `Back to all stores` |

#### `store-map` props

| Prop name |   Type   |         Description          | Default value |
| :-------: | :------: | :--------------------------: | :-----------: |
|  `width`  | `string` | Map width in pixels (`px`).  |    `100%`     |
| `height`  | `string` | Map height in pixels (`px`). |    `200px`    |

#### `store-address` props

| Prop name |   Type   |                         Description                         |  Default value  |
| :-------: | :------: | :---------------------------------------------------------: | :-------------: |
|  `label`  | `string` | Entitles the `store-address` block when rendered on the UI. | `Store address` |

#### `store-hours` props

| Prop name |   Type   |                        Description                        | Default value. |
| :-------: | :------: | :-------------------------------------------------------: | :------------: |
|  `label`  | `string` | Entitles the `store-hours` block when rendered on the UI. | `Store hours`  |
| `format`  |  `enum`  |    Hour format. Possible values are : `12h` and `24h`.    |     `24h`      |

#### `store-description` props

| Prop name |   Type   |                                                                     Description                                                                      | Default value |
| :-------: | :------: | :--------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------: |
|  `text`   | `string` | Text to be displayed on the store page. Use `{storeName}`, `{storeCity}`, or `{storeState}` within your text to display that store's specific value. |               |

#### `store-instructions` props

| Prop name |   Type   |                           Description                            | Default value |
| :-------: | :------: | :--------------------------------------------------------------: | :-----------: |
|  `label`  | `string` | Entitles the `store-instructions` block when rendered on the UI. | `Information` |

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

|       CSS Handles       |
| :---------------------: |
|   `addressContainer`    |
|     `addressLabel`      |
| `addressListFirstItem`  |
|    `addressListItem`    |
|    `addressListLink`    |
|      `addressList`      |
|  `addressStoreAddress`  |
|   `addressStoreName`    |
|   `backlinkContainer`   |
|       `backlink`        |
|     `businessHours`     |
|       `container`       |
| `descriptionContainer`  |
|    `descriptionText`    |
|       `dayOfWeek`       |
|        `divider`        |
|        `hourRow`        |
|    `hoursContainer`     |
|      `hoursLabel`       |
| `instructionsContainer` |
|   `instructionsLabel`   |
|   `instructionsText`    |
|  `listingMapContainer`  |
|        `loadAll`        |
|   `markerInfoAddress`   |
|    `markerInfoLink`     |
|  `markerInfoStoreName`  |
|      `markerInfo`       |
|       `noResults`       |
|       `storeName`       |
|     `storesListCol`     |
|      `storesList`       |
|     `storesMapCol`      |