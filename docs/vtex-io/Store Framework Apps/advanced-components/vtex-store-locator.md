---
title: "Store Locator"
slug: "vtex-store-locator"
excerpt: "vtex.store-locator@0.10.14"
hidden: false
createdAt: "2020-09-29T19:28:07.531Z"
updatedAt: "2022-10-07T13:56:32.252Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/vtex-io/Store Framework Apps/advanced-components/#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

The Store Locator app fetches the Pickup point data in order to display address location for retail stores.

![store-list](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-store-locator-0.png)
![store-detail](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-store-locator-1.png)

## Configuration

1. [Install](https://vtex.io/docs/recipes/development/installing-an-app/) the Store Locator app in your VTEX account by running `vtex install vtex.store-locator` in your terminal.
2. In your account's admin page, select **Inventory & Shipping** section and then access **Settings**.
3. Type in the Google Geolocation API key and save your changes.
4. Open your Store Theme app directory in your code editor.
5. Add the Store Locator app as a `peerDependency` in the `manifest.json` file:

```diff
 "peerDependencies": {
+  "vtex.store-locator": "0.x"
 }
```

Once installed, the app will generate a new route called `/stores` for your store, listing the retail stores registered in the **Pickup Points** section (under the **Inventory & Shipping** module).

The new page already contains a default template with all blocks exported by the Store Locator app, meaning the `/stores` page is ready to be rendered and no further actions are required. However, you can **customize the new page overwriting the template by creating a brand new one**. To do so, check the [**Advanced configuration**](./README.md#advanced-configuration) section below.

> ℹ️ _This app will also **add a new entry to your store's `/sitemap.xml` file so that all your pickup points are available to search engines** - make sure you already have the `vtex.store-sitemap@2.x` app installed in your VTEX account!_

### Advanced configuration

In order to define the Store Locator custom page UI, you must use the blocks exported by the `vtex.store-locator` app. Namely, they are:

|      Block name      |                                                                              Description                                                                              |
| :------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|     `store-list`     |                                              Renders a list of retail stores and a map with all their locations marked.                                               |
|    `store-group`     |                                  Provides the Pickup Point data to other blocks exported by the app, such as the ones listed below.                                   |
|     `store-name`     |                                                                        Renders the store name.                                                                        |
|  `store-back-link`   |                                                            Renders a link to return to the previous page.                                                             |
|     `store-map`      |                                                            Renders a map with the retail store's location.                                                            |
|   `store-address`    |                                                                     Renders the store's address.                                                                      |
|    `store-hours`     | Renders the store's opening hours. This information comes by default from the Pickup Points configuration, but you can also define manually through the Store's theme |
| `store-instructions` |                                                     Renders the desired instructions to access the retail store.                                                      |

1. Open your Store Theme app directory in your code editor.
2. In the `/store/blocks` folder of your Store Theme app, create a new file called `storelocator.json`.
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

|   Prop name   |   Type   |                                 Description                                  |    Default value     |
| :-----------: | :------: | :--------------------------------------------------------------------------: | :------------------: |
| `filterByTag` | `string` |                  Filter fetched Pickup Points by this tag.                   |      undefined       |
|    `icon`     | `string` | Icon used to display store location in map. Input icon URL (`svg` or `png`). |   Google's default   |
|  `iconWidth`  | `number` |                         Icon width in pixels (`px`).                         | Image default width  |
| `iconHeight`  | `number` |                        Icon height in pixels (`px`).                         | Image default height |
|    `zoom`     | `number` |                            Map zoom as a number.                             |         `10`         |
|     `lat`     | `number` |                             Latitude coordinate.                             |      undefined       |
|    `long`     | `number` |                            Longitude coordinate.                             |      undefined       |
|   `sortBy`    | `string` |        Property (`name` or `distance`) used to sort the stores list.         |      `distance`      |

> ℹ️ _Use the `lat` and `long` props to display Pickup Points configured in seller accounts. If these props are not configured and you do not have any pick up points set up in your main account, the app will display no stores._

> ℹ️ _The `filterByTag` prop cannot be used along with `lat` and `long`. If you set a value for `filterByTag`, the `lat` and `long` props will be ignored._

#### `store-group` props

|       Prop name       |   Type    |                                                                                                                     Description                                                                                                                      | Default value |
| :-------------------: | :-------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------: |
|        `title`        | `string`  |                                  Title used in the page's HTML `title` tag and Structured Data for SEO purposes. The `{storeName}`, `{storeCity}`, and / or `{storeState}` variables can be used in the title text.                                  | `{storeName}` |
|     `description`     | `string`  |                    Description text used in the page's HTML `description` meta tag and Structured Data for SEO purposes. The `{storeName}`, `{storeCity}`, and / or `{storeState}` variables can be used in the description text.                    | empty string  |
|    `imageSelector`    | `string`  |                                                                                      CSS Selector to select the images included in the page's Structured Data.                                                                                       | empty string  |
| `instructionsAsPhone` | `boolean` | To provide a unique phone number for each store, a phone number can be entered in the `Instructions` field in the Pickup Points section. The `store-instructions` will display a phone number and it will be included in the page's Structured Data. |    `false`    |

⚠️ _Both `imageSelector` and `instructionsAsPhone` must be declared with valid values in order to provide Structured Data for SEO purposes._

#### `store-name` props

| Prop name |   Type   |                                                               Description                                                                | Default value |
| :-------: | :------: | :--------------------------------------------------------------------------------------------------------------------------------------: | :-----------: |
|  `text`   | `string` | Text to be displayed as store name. `{storeName}`, `{storeCity}`, and / or `{storeState}` values can be used to generate the store name. |   undefined   |
|   `tag`   | `string` |                                   HTML element to wrap the `store-name` block when rendered on the UI.                                   |     `div`     |

#### `store-back-link` props

| Prop name |   Type   |                            Description                             |    Default value     |
| :-------: | :------: | :----------------------------------------------------------------: | :------------------: |
|  `label`  | `string` | Text displayed by `store-back-link` block when rendered on the UI. | `Back to all stores` |

#### `store-map` props

| Prop name |   Type    |                                 Description                                  | Default value |
| :-------: | :-------: | :--------------------------------------------------------------------------: | :-----------: |
|  `width`  | `string`  |                                  Map width.                                  |    `100%`     |
| `height`  | `string`  |                                 Map height.                                  |    `200px`    |
|  `zoom`   | `integer` |                            Map zoom as a `number`                            |     `14`      |
|  `icon`   | `string`  | Icon used to display store location in map. Input icon URL (`svg` or `png`). |   undefined   |

#### `store-address` props

| Prop name |   Type   |                         Description                          |  Default value  |
| :-------: | :------: | :----------------------------------------------------------: | :-------------: |
|  `label`  | `string` | Label for the `store-address` block when rendered on the UI. | `Store address` |

#### `store-hours` props

|    Prop name    |       Type        |                                    Description                                    | Default value. |
| :-------------: | :---------------: | :-------------------------------------------------------------------------------: | :------------: |
|     `label`     |     `string`      |            Label for the `store-hours` block when rendered on the UI.             | `Store hours`  |
|    `format`     |      `enum`       |                 Hour format. Possible values are `12h` and `24h`.                 |     `24h`      |
| `businessHours` | `array of object` | format `{"dayOfWeek": "Sunday","openingTime": "11:00am","closingTime": "5:00pm"}` |   undefined    |

#### `store-description` props

| Prop name |   Type   |                                                                     Description                                                                      | Default value |
| :-------: | :------: | :--------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------: |
|  `text`   | `string` | Text to be displayed on the store page. Use `{storeName}`, `{storeCity}`, or `{storeState}` within your text to display that store's specific value. |   undefined   |

#### `store-instructions` props

| Prop name |   Type   |                            Description                            | Default value |
| :-------: | :------: | :---------------------------------------------------------------: | :-----------: |
|  `label`  | `string` | Label for the `store-instructions` block when rendered on the UI. | `Information` |

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