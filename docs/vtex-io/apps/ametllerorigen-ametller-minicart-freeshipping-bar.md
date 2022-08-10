---
title: "Yext Store Locator"
slug: "ametllerorigen-ametller-minicart-freeshipping-bar"
excerpt: "ametllerorigen.ametller-minicart-freeshipping-bar@1.0.0"
hidden: true
createdAt: "2022-08-02T13:49:51.112Z"
updatedAt: "2022-08-02T13:49:51.112Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

The Yext Store Locator app provides a way to bring in location data from the Yext Live API and create a store locator map, as well as, individual store pages for each location.

## Configuration

### Step 1 - Installing the Yext Store Locator

Using your terminal and [VTEX IO Toolbelt](https://vtex.io/docs/recipes/development/vtex-io-cli-installation-and-command-reference/#command-reference), log in to the VTEX account you are working on and [install](https://vtex.io/docs/recipes/store/installing-an-app) the `vtex.localoo-store-locator@0.x` app.

### Step 2 - Defining the app settings

In your VTEX account's admin, perform the following actions:

1. Access the **Apps** section and then **My Apps**.
2. Select the **Yext Store Locator** app box.
3. In the Settings section, enter your **Yext API key**.
4. Save your changes.

### Step 3 - Adding the locations map and store pages

Before performing the following actions, make sure you are already logged into the desired VTEX account and working on a [Developer workspace](https://vtex.io/docs/recipes/development/creating-a-development-workspace/).

1. Open your Store Theme app in your code editor.
2. Add the `localoo-store-locator` app as a `peerDependency` in your theme's `manifest.json` file:

```diff
 "peerDependencies": {
+  "vtex.localoo-store-locator": "0.x"
 }
```

3. In the `store/routes.json` file, create paths for the store locator pages as shown below:

```json
"store.storelocator": {
	"path": "/stores"
},
"store.storedetail": {
	"path": "/store/:slug/:store_id"
}
```

| Store page           | Description                                                                                         |
| -------------------- | --------------------------------------------------------------------------------------------------- |
| `store.storelocator` | Provides a listing of your store locations along with a map and markers for the each store location |
| `store.storedetail`  | A detail view of a single store location.                                                           |

### Step 4 - Declaring the pages' blocks

The Yext Store Locator app provides the following blocks for your use:

| Block name               | Description                                                                                                                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `store-address`          | Show the store address.                                                                                                                                                                                       |
| `store-back-link`        | Display a link to navigate back to the store locator map.                                                                                                                                                     |
| `store-brands`           | Show a list of brands available at the store.                                                                                                                                                                 |
| `store-conditional`      | A wrapper component that will only render its child blocks if the passed in custom data field returns content. Should be used in cases where custom data may be used in some locations, but absent in others. |
| `store-contact`          | Show store contact information.                                                                                                                                                                               |
| `store-custom-data`      | Show a custom data field from your Yext location.                                                                                                                                                             |
| `store-description`      | Show the store description.                                                                                                                                                                                   |
| `store-group`            | A context component that provides data for the store page's child blocks.                                                                                                                                     |
| `store-hours`            | Show the store hours.                                                                                                                                                                                         |
| `store-list`             | List of stores that are displayed on the map.                                                                                                                                                                 |
| `store-logo`             | Show the store logo.                                                                                                                                                                                          |
| `store-map`              | Map component to be used on the store detail page. Shows the viewed store's location.                                                                                                                         |
| `store-nearby-locations` | Used on the store page to display nearby stores.                                                                                                                                                              |
| `store-open-banner`      | Banner to display the open until time for the current day.                                                                                                                                                    |
| `store-page-banner`      | Banner component that can be customized with store data. Including the placeholders `{storeName}` or `{storeCity}` in the banner text, will be resolved to the locations values.                              |
| `store-payment-options`  | Show the payment options available at the store.                                                                                                                                                              |
| `store-social-links`     | Show the stores social media links.                                                                                                                                                                           |
| `store-title`            | Title block that contains the stores name and location.                                                                                                                                                       |

### `store-list` props

| Prop name    | Type     | Description                                                                                                   | Default value |
| ------------ | -------- | ------------------------------------------------------------------------------------------------------------- | ------------- |
| `icon`       | `string` | Image url (svg or png) to be used as the map location marker icon instead of the default red Google pin icon. | `undefined`   |
| `iconWidth`  | `number` | If a custom icon is used, a fixed width number in pixels can be set                                           | `undefined`   |
| `iconHeight` | `number` | If a custom icon is used, a fixed height number in pixels can be set                                          | `undefined`   |

### `store-address` props

| Prop name | Type     | Description                            | Default value |
| --------- | -------- | -------------------------------------- | ------------- |
| `label`   | `string` | Title to be displayed above the block. | `undefined`   |

### `store-back-link` props

| Prop name | Type     | Description                | Default value          |
| --------- | -------- | -------------------------- | ---------------------- |
| `label`   | `string` | Link text to be displayed. | `"Back to all stores"` |

### `store-brands` props

| Prop name | Type     | Description                            | Default value |
| --------- | -------- | -------------------------------------- | ------------- |
| `label`   | `string` | Title to be displayed above the block. | `undefined`   |

### `store-conditional` props

| Prop name | Type                                                 | Description                                                                                                                                | Default value |
| --------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------- |
| `id`      | `string`                                             | `The name of the custom data field to be used in the conditional block, include the`c\_`prefix Yext adds to your custom data field names.` | `undefined`   |
| `type`    | `text`&#124;`textList`&#124;`image`&#124;`imageList` | Custom field data type                                                                                                                     | `undefined`   |

### `store-contact` props

| Prop name | Type                                | Description                                                                                                                                                | Default value |
| --------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `label`   | `string`                            | Label to be displayed below the contact.                                                                                                                   | `undefined`   |
| `type`    | `mainPhone`&#124;`fax`&#124;`email` | Contact type as defined in your Yext data.                                                                                                                 | `undefined`   |
| `index`   | `number`                            | If type `email` and there are multiple emails associated in your Yext location, an index must be specified. The first email is used by default, index `0`. | `0`           |

### `store-custom-data` props

| Prop name | Type                                                 | Description                                                                                                                                                             | Default value |
| --------- | ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `label`   | `string`                                             | Title to be displayed above the block.                                                                                                                                  | `undefined`   |
| `id`      | `string`                                             | The name of your Yext custom field. Include the`c\_`prefix Yext adds to your custom data field names.                                                                   | `undefined`   |
| `type`    | `text`&#124;`textList`&#124;`image`&#124;`imageList` | The custom field data type. `text` or `image` when the data field is a single string or image. `textList` or `imageList` when the custom data contains a list of items. | `undefined`   |
| `altText` | `string`                                             | If type `image` or `imageList`, this is the alt text that will display                                                                                                  | `undefined`   |

### `store-description` props

| Prop name | Type     | Description                            | Default value |
| --------- | -------- | -------------------------------------- | ------------- |
| `label`   | `string` | Title to be displayed above the block. | `undefined`   |

### `store-hours` props

| Prop name | Type     | Description                            | Default value |
| --------- | -------- | -------------------------------------- | ------------- |
| `label`   | `string` | Title to be displayed above the block. | `undefined`   |

### `store-logo` props

| Prop name | Type     | Description           | Default value |
| --------- | -------- | --------------------- | ------------- |
| `width`   | `string` | Logo container width  | `300px`       |
| `height`  | `string` | Logo container height | `300px`       |

### `store-map` props

| Prop name    | Type     | Description                                                                                                   | Default value |
| ------------ | -------- | ------------------------------------------------------------------------------------------------------------- | ------------- |
| `width`      | `string` | Map container width                                                                                           | `undefined`   |
| `height`     | `string` | Map container height                                                                                          | `undefined`   |
| `icon`       | `string` | Image url (svg or png) to be used as the map location marker icon instead of the default red Google pin icon. | `undefined`   |
| `iconWidth`  | `number` | If a custom icon is used, a fixed width number in pixels can be set                                           | `undefined`   |
| `iconHeight` | `number` | If a custom icon is used, a fixed height number in pixels can be set                                          | `undefined`   |

### `store-page-banner` props

| Prop name   | Type     | Description           | Default value |
| ----------- | -------- | --------------------- | ------------- |
| `header`    | `string` | Header banner text    | `undefined`   |
| `subheader` | `string` | Subheader banner text | `undefined`   |

### `store-payment-options` props

| Prop name | Type     | Description                            | Default value |
| --------- | -------- | -------------------------------------- | ------------- |
| `label`   | `string` | Title to be displayed above the block. | `undefined`   |

### `store-social-links` props

| Prop name        | Type     | Description                                                 | Default value |
| ---------------- | -------- | ----------------------------------------------------------- | ------------- |
| `title`          | `string` | Title to be displayed above the block.                      | `undefined`   |
| `subtitle`       | `string` | Subtitle to be displayed below of the block title.          | `undefined`   |
| `facebookLabel`  | `string` | Facebook link text                                          | `undefined`   |
| `twitterLabel`   | `string` | Twitter link text                                           | `undefined`   |
| `instagramLabel` | `string` | Instagram link text                                         | `undefined`   |
| `youTubeHandle`  | `string` | YouTube handle. Gives the option to include a YouTube link. | `undefined`   |
| `youTubeLabel`   | `string` | YouTube link text                                           | `undefined`   |

## Customization

`In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).`

| CSS Handles                     |
| ------------------------------- |
| `addressContainer`              |
| `addressBlock`                  |
| `addressLabel`                  |
| `addressDirectionsContainer`    |
| `addressDirectionsLink`         |
| `storeListAddressList`          |
| `storeListAddressListFirstItem` |
| `storeListAddressListItem`      |
| `storeListStoreLinkContainer`   |
| `storeListStoreLink`            |
| `storeListAddressContainer`     |
| `storeListStoreName`            |
| `storeListAddress`              |
| `storeListLinks`                |
| `storeListLinkContainer`        |
| `storeListPhoneLink`            |
| `storeListDirectionsLink`       |
| `backLinkContainer`             |
| `backLink`                      |
| `brandsContainer`               |
| `brandsLabel`                   |
| `brandsList`                    |
| `brandsItem`                    |
| `contactsContainer`             |
| `contactsContact`               |
| `contactsLabel`                 |
| `customDataTextContainer`       |
| `customDataTextListContainer`   |
| `customDataTextListLabel`       |
| `customDataTextList`            |
| `customDataTextListItem`        |
| `customDataImageContainer`      |
| `customDataImageListContainer`  |
| `customDataImageListItem`       |
| `hoursContainer`                |
| `normalHours`                   |
| `holidayHours`                  |
| `hoursLabel`                    |
| `holidayHoursLabel`             |
| `hoursRow`                      |
| `hoursDayOfWeek`                |
| `hoursText`                     |
| `logoContainer`                 |
| `mapContainer`                  |
| `markerInfo`                    |
| `markerInfoLinkContainer`       |
| `markerInfoLink`                |
| `markerInfoAddressStreet`       |
| `markerInfoAddress`             |
| `markerInfoHours`               |
| `markerInfoDirectionsLink`      |
| `markerInfoStoreName`           |
| `markerInfoAddress`             |
| `nearbyLocationsBlock`          |
| `nearbyLocationsTitle`          |
| `nearbyLocationsContainer`      |
| `nearbyLocationsItem`           |
| `nearbyLocationsAddress`        |
| `nearbyLocationsLinkContainer`  |
| `nearbyLocationsPhoneLink`      |
| `nearbyLocationsDirectionsLink` |
| `openBanner`                    |
| `bannerContainer`               |
| `bannerHeader`                  |
| `bannerSubheader`               |
| `paymentOptionsContainer`       |
| `paymentOptionsLabel`           |
| `paymentOptionsText`            |
| `socialLinksBlock`              |
| `socialLinksHeader`             |
| `socialLinksTitle`              |
| `socialLinksSubtitle`           |
| `socialLinksContainer`          |
| `socialLinkTag`                 |
| `storeTitle`                    |
| `storeLink`                     |
| `storeLocatorBlock`             |
| `storeLocatorsearchContainer`   |
| `storeLocatorsearchInput`       |
| `storeLocatorsearchSpinner`     |
| `storeLocatorContainer`         |
| `storeLocatorMapContainer`      |
| `storeLocatorMap`               |

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

---

Check out some documentation models that are already live:

- [Breadcrumb](https://github.com/vtex-apps/breadcrumb)
- [Image](https://vtex.io/docs/components/general/vtex.store-components/image)
- [Condition Layout](https://vtex.io/docs/components/all/vtex.condition-layout@1.1.6/)
- [Add To Cart Button](https://vtex.io/docs/components/content-blocks/vtex.add-to-cart-button@0.9.0/)
- [Store Form](https://vtex.io/docs/components/all/vtex.store-form@0.3.4/)