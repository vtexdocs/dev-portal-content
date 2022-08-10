---
title: "Store Locator"
slug: "thefoschiniqa-store-locator"
excerpt: "thefoschiniqa.store-locator@0.0.6"
hidden: true
createdAt: "2022-07-06T09:17:24.193Z"
updatedAt: "2022-07-06T09:17:24.193Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

The Store Locator app fetches the Pickup point data in order to display address location for retail stores.

![store-list](https://user-images.githubusercontent.com/52087100/99975140-9f809500-2d80-11eb-87ce-2f9cfcf567d6.png)
![store-detail](https://user-images.githubusercontent.com/52087100/99975130-9abbe100-2d80-11eb-95ac-49ea37490c50.png)

## App customized to TFG

App customized to TFG adding:

- Filter by provinces.
- Filter by brands.
- New anchor in the list store named "Show on map".
- New anchor in store details named "Get directions".

![store-list-custom](./images/store-list-custom.png)
![store-detail-custom](./images/store-detail-custom.png)

### Filter configuration

1. Add tags with the name of the store to filter on `Pickup point` section
   ![pickup-tag](./images/pickup-tag.png)
2. Upload the images (SVG) of the stores to VTEX on admin. Go to admin > CMS > Layout > CMS > Files Manager > imagens.
   ![images-uploading](./images/images-uploading.png)
3. Go to Admin > Apps > My Apps. Search `Store Locator` app and go to settings.
   ![store-locator-settings](./images/store-locator-settings.png)
4. By default there are 19 stores to filter with their names and images. But you can add or delete more (By default there are 19 stores and is needed go to app configuration and save the default configuration to there can be showed on web).
   ![add-stores-to-filter](./images/add-stores-to-filter.png)

## Configuration

1. [Install](https://vtex.io/docs/recipes/development/installing-an-app/) the Store Locator app in your VTEX account by running `vtex install vtex.store-locator` in your terminal.
2. In your account's admin page, select **Inventory&Shipping** section and then acess **Settings**.
3. Type in the Google Geolocation API key and save your changes.
4. Open your Store Theme app directory in your code editor.
5. Add the Store Locator app as a `peerDependency` in the `manifest.json` file:

```diff
 "peerDependencies": {
+  "vtex.store-locator": "0.x"
 }
```

Once installed, the app will generate a new route called `/stores` for your store, listing the retail stores registered in the Pickup points section (under the Inventory & shipping module).

The new page already contains a default template with all blocks exported by the Store Locator app, meaning that the `/stores` page is ready to be rendered and no further actions are required. However, you can **customize the new page overwriting the template by creating a brand new one as you wish**. To do so, check the **Advanced configurations** section below.

> ℹ️ _This app will also **add a new entry to your store's `/sitemap.xml` file in order to have all the pickup points available to the search engines** - make sure you already have the `vtex.store-sitemap@2.x` app installed in your VTEX account!_

### Advanced configuration

In order to define the Store Locator custom page UI, you must use the blocks exported by the `vtex.store-locator` app. Namely, they are:

|      Block name      |                                                                              Description                                                                              |
| :------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|     `store-list`     |                                                Renders a list of retail stores and a map with all their localization.                                                 |
|    `store-group`     |                                  Provides the pickup point data to other blocks exported by the app, such as the ones listed below.                                   |
|     `store-name`     |                                                                        Renders the store name.                                                                        |
|  `store-back-link`   |                                                            Renders a link to return to the previous page.                                                             |
|     `store-map`      |                                                           Renders a map with the retail store localization.                                                           |
|   `store-address`    |                                                                     Renders the store's address.                                                                      |
|    `store-hours`     | Renders the store's opening hours. This information comes by default from the Pickup Points configuration, but you can also define manually through the Store's theme |
| `store-instructions` |                                                     Renders the desired instructions to access the retail store.                                                      |

1. Open your Store Theme app directory in your code editor.
2. In the `store/blocks` folder of your Store Theme app, create a new file called `storelocator.json`.
3. Create a new store template in it called `store.storelocator`. In its blocks array, paste the default implementation stated below:

```json
{
  "store.storelocator": {
    "blocks": ["flex-layout.row#title", "flex-layout.row#container"]
  },
  "flex-layout.row#title": {
    "children": ["flex-layout.col#title"]
  },
  "flex-layout.row#container": {
    "children": ["store-list"]
  },
  "flex-layout.col#title": {
    "children": ["rich-text#title"],
    "props": {
      "blockClass": "title",
      "preventVerticalStretch": true
    }
  },
  "rich-text#title": {
    "props": {
      "text": "## Store Locator"
    }
  },
  "store.storedetail": {
    "blocks": ["flex-layout.row#titleStore", "store-group"]
  },
  "store-group": {
    "children": ["flex-layout.row#containerStore"],
    "props": {
      "title": "{storeName} Store"
    }
  },
  "flex-layout.row#titleStore": {
    "children": ["flex-layout.col#titleStore"]
  },
  "flex-layout.row#containerStore": {
    "children": ["flex-layout.col#detail", "flex-layout.col#store"]
  },
  "flex-layout.col#titleStore": {
    "children": ["rich-text#titleStore"],
    "props": {
      "blockClass": "title",
      "preventVerticalStretch": true
    }
  },
  "rich-text#titleStore": {
    "props": {
      "text": "## Store Detail"
    }
  },
  "flex-layout.col#detail": {
    "children": [
      "store-back-link",
      "store-map",
      "store-address",
      "store-hours",
      "store-instructions"
    ],
    "props": {
      "width": "30%",
      "preventVerticalStretch": true
    }
  },
  "flex-layout.col#store": {
    "children": ["store-name"],
    "props": {
      "width": "70%"
    }
  },
  "store-hours": {
    "props": {
      "label": "Business hours:",
      "format": "12h",
      "businessHours": [
        {
          "dayOfWeek": "Sunday",
          "openingTime": "11:00am",
          "closingTime": "5:00pm"
        },
        {
          "dayOfWeek": "Monday",
          "openingTime": "11:00am",
          "closingTime": "6:00pm"
        },
        {
          "dayOfWeek": "Tuesday",
          "openingTime": "11:00am",
          "closingTime": "6:00pm"
        },
        {
          "dayOfWeek": "Wednesday",
          "openingTime": "11:00am",
          "closingTime": "6:00pm"
        },
        {
          "dayOfWeek": "Thursday",
          "openingTime": "11:00am",
          "closingTime": "6:00pm"
        },
        {
          "dayOfWeek": "Friday",
          "openingTime": "11:00am",
          "closingTime": "6:00pm"
        },
        {
          "dayOfWeek": "Saturday",
          "openingTime": "11:00am",
          "closingTime": "5:00pm"
        }
      ]
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
|    `zoom`     | `number` |                                Map zoom as number.                                |          10           |
|    `long`     | `number` |                       Longitude to be used as coordenates.                        |         null          |
|     `lat`     | `number` |                       Lattitude to be used as coordenates.                        |         null          |
|   `sortBy`    | `string` |        Property (`name` or `distance`) to be used to sort the stores list.        |       distance        |

ℹ️ _If you have all your pick up points as in seller accounts ** you should provide `long` and `lat` props to show all seller stores** - if you don't have this props and you neither have pick up points the app will not show nothing._

#### `store-group` props

|       Prop name       |   Type    |                                                                                                                     Description                                                                                                                      | Default value |
| :-------------------: | :-------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------: |
|        `title`        | `string`  |                                              Title text to be displayed on the store page. Use `{storeName}`, `{storeCity}`, or `{storeState}` as value to display the store's accurate data on the UI.                                              | `{storeName}` |
|     `description`     | `string`  |                                       Page description used in the page's Structured Data for SEO purposes. The `{storeName}`, `{storeCity}`, or `{storeState}` variables can be used in the description text.                                       |      ``       |
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

| Prop name |   Type    |                                   Description                                    |   Default value   |
| :-------: | :-------: | :------------------------------------------------------------------------------: | :---------------: |
|  `width`  | `string`  |                           Map width in pixels (`px`).                            |      `100%`       |
| `height`  | `string`  |                           Map height in pixels (`px`).                           |      `200px`      |
|  `zoom`   | `integer` |                               Map zoom as `number`                               |       `14`        |
|  `icon`   | `string`  | Icon URL (`svg` or `png`) to be displayed alongside with the `store-map` blocks. | Google's default. |

#### `store-address` props

| Prop name |   Type   |                         Description                         |  Default value  |
| :-------: | :------: | :---------------------------------------------------------: | :-------------: |
|  `label`  | `string` | Entitles the `store-address` block when rendered on the UI. | `Store address` |

#### `store-hours` props

|    Prop name    |       Type        |                                    Description                                    | Default value. |
| :-------------: | :---------------: | :-------------------------------------------------------------------------------: | :------------: |
|     `label`     |     `string`      |             Entitles the `store-hours` block when rendered on the UI.             | `Store hours`  |
|    `format`     |      `enum`       |                Hour format. Possible values are : `12h` and `24h`.                |     `24h`      |
| `businessHours` | `array of object` | format `{"dayOfWeek": "Sunday","openingTime": "11:00am","closingTime": "5:00pm"}` |  `undefined`   |

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

|         CSS Handles         |
| :-------------------------: |
|     `addressContainer`      |
|       `addressLabel`        |
|   `addressListFirstItem`    |
|      `addressListItem`      |
|      `addressListLink`      |
|        `addressList`        |
|    `addressStoreAddress`    |
|     `addressStoreName`      |
| `addressStoreAddressGroupA` |
| `addressStoreAddressNumber` |
| `addressStoreAddressStreet` |
|     `backlinkContainer`     |
|         `backlink`          |
|       `businessHours`       |
|         `container`         |
|   `descriptionContainer`    |
|      `descriptionText`      |
|         `dayOfWeek`         |
|          `divider`          |
|          `hourRow`          |
|      `hoursContainer`       |
|        `hoursLabel`         |
|   `instructionsContainer`   |
|     `instructionsLabel`     |
|     `instructionsText`      |
|    `listingMapContainer`    |
|          `loadAll`          |
|     `markerInfoAddress`     |
|      `markerInfoLink`       |
|    `markerInfoStoreName`    |
|        `markerInfo`         |
|         `noResults`         |
|         `storeName`         |
|       `storesListCol`       |
|        `storesList`         |
|       `storesMapCol`        |

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