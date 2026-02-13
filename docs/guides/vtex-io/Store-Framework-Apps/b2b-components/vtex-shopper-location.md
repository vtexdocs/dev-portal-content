---
title: "Shopper Location"
slug: "vtex-shopper-location"
hidden: false
createdAt: "2020-09-03T21:01:54.967Z"
updatedAt: "2026-02-13T15:52:23.906Z"
---

>⚠️ This app is no longer maintained by VTEX. This means support and maintenance are no longer provided.

This app attempts to determine the user's location if it is not already known, first by requesting permission to use their browser's geolocation feature, then by looking up their location using their IP address as a fallback. The location is stored in the `shippingData` section of the `orderForm` and can then be used by other apps, such as [Location Availability](https://developers.vtex.com/docs/guides/vtex-location-availability).

A block is also provided, which renders a form allowing the user to manually change their location.

Shopper Location also supports redirecting a user to a URL based on their location, determined by the app. See the [Client Redirect](#client-redirect) section.

This app also supports white label sellers' selection, allowing shoppers to select one or more sellers available in their location. Shoppers will then be able to search and view products from those select sellers. See the [Region Seller Selection](#region-seller-selection) section.

> ℹ️ The Google Geolocation API key in your **Inventory & Shipping** settings is required for the geolocation feature.

>⚠️ To use the IP lookup fallback, you must have an API key for https://ip-geolocation.whoisxmlapi.com.

## Configuration

1. Using [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference), install `vtex.shopper-location` in the desired account.

2. In your account's admin dashboard, go to **Apps > My Apps** and click the `Settings` button for Shopper Location.

3. Enter your API key for https://ip-geolocation.whoisxmlapi.com in the provided field and click `Save`. If you plan to use the `Client Redirect` feature, it's configured here as well.

4. Modify your `store-theme` as follows:

  - Add the following as dependencies in your theme's manifest.json file, if not already present:

```json
  "vtex.store-components": "3.x",
  "vtex.modal-layout": "0.x",
  "vtex.shopper-location": "1.x"
```

   - In one of the JSON files in your theme's `store` folder, define the `shopper-location` block and its children, adjusting the props as needed:

```json
"shopper-location": {
    "children": ["modal-trigger#address"],
    "props": {
      "autofill": ["city", "country", "neighborhood", "number", "postalCode", "state", "street"]
    }
  },
  "modal-trigger#address": {
    "children": ["user-address", "modal-layout#address"]
  },
  "user-address": {
    "props": {
      "variation": "bar",
      "showStreet": false,
      "showCityAndState": true,
      "showPostalCode": true,
      "showPrefix": false,
      "showIfEmpty": true
    }
  },
  "modal-layout#address": {
    "children": ["modal-header#address", "modal-content#address"]
  },
  "modal-header#address": {
    "children": ["flex-layout.col#address-header"]
  },
  "flex-layout.col#address-header": {
    "children": ["rich-text#address-header"],
    "props": {
      "paddingLeft": 5
    }
  },
  "rich-text#address-header": {
    "props": {
      "text": "### Change Location"
    }
  },
  "modal-content#address": {
    "children": ["change-location"]
  },
  "change-location": {
    "props":{
      "postalCode": "first",
      "autocomplete": true,
      "notRequired": ["street", "number", "city", "state"],
      "hideFields": ["complement", "neighborhood", "receiverName", "reference"]
    }
  },
```

   - Also, in one of the JSON files, place the `shopper-location` block in your layout. For example, to place the block in the header:

```json
"flex-layout.row#header-desktop": {
    "props": {
      "blockClass": "main-header",
      "horizontalAlign": "center",
      "verticalAlign": "center",
      "preventHorizontalStretch": true,
      "preventVerticalStretch": true,
      "fullWidth": true
    },
    "children": [
      "flex-layout.col#logo-desktop",
      "flex-layout.col#category-menu",
      "flex-layout.col#spacer",
      "shopper-location",
      "search-bar",
      "locale-switcher",
      "login",
      "minicart.v2"
    ]
  },
```

### Client Redirect

You can redirect the user to a country-specific URL based on their location. In the **App Settings**, enter the [alpha-3 country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3#Officially_assigned_code_elements) and URL for each supported country.

On their first visit, if a user is not on their country's website, a modal will display an option to redirect to their country's website. For users in a country without an entry in the App Settings, no option is displayed.

Additionally, there is an `Automatic Redirect` option that redirects the user without displaying the modal.

### Region Sellers Selection

Allow users to select one or more sellers serving their location from a list, and display only products carried by those sellers in search results.

> ℹ️️ For this feature to work properly, the item cannot have inventory in seller "1". If there's stock in seller "1", the item will always appear in the search results, regardless of the inventory in the sellers selected.

Add the `region-sellers` block as a child of the `shopper-location` block to get started:

```json
"shopper-location": {
    "children": ["modal-trigger#address", "region-sellers"],
    "props": {
      "autofill": ["city", "country", "neighborhood", "number", "postalCode", "state", "street"]
    }
  },
```

#### Props

`shopper-location`:

| Prop name  | Type    | Description                                  | Default value | Accepted values                                                                                                 |
| ---------- | ------- | -------------------------------------------- | ------------- | --------------------------------------------------------------------------------------------------------------- |
| `autofill` | `array` | Define which address fields should be filled | `undefined`   | Array with any of these values `["city", "country", "neighborhood", "number", "postalCode", "state", "street"]` |

`change-location`:

| Prop name      | Type      | Description                                                                                            | Default value | Accepted values                                                                                              |
| -------------- | --------- | ------------------------------------------------------------------------------------------------------ | ------------- | ------------------------------------------------------------------------------------------------------------ |
| `postalCode`   | `string`  | Define the postalCode position on the form                                                             | `last`        | `first`,`last`                                                                                               |
| `autocomplete` | `boolean` | Enables google autocomplete based on the postalCode (Only works when **postalCode** is set to `first`) | `false`       | `true`,`false`                                                                                               |
| `notRequired`  | `array`   | Turn visible fields not required                                                                       | `undefined`   | `["city", "country", "neighborhood", "number", "state", "street", "complement","receiverName", "reference"]` |
| `hideFields`   | `array`   | Hide fields and turn them not required                                                                 | `undefined`   | `["city", "country", "neighborhood", "number", "state", "street", "complement","receiverName", "reference"]` |

`region-sellers`:

| Prop name            | Type      | Description                                                                                                    | Default value | Accepted values     |
| -------------------- | --------- | -------------------------------------------------------------------------------------------------------------- | ------------- | ------------------- |
| `mode`               | `string`  | Specify if component will be used as a search filter (`filter`). Otherwise display as a dropdown (`default`).  | `default`     | `filter`, `default` |
| `initiallyCollapsed` | `boolean` | When using `filter` mode, set sellers list to display as collapsed (`true`) or open (`false`) initially.       | `false`       | `true`,`false`      |
| `displayStoreIcon`   | `boolean` | Display store icon.                                                                                            | `true`        | `true`,`false`      |
| `useApplyButton`     | `boolean` | Apply sellers selection using a button (`true`) or automatically apply changes after each selection (`false`). | `false`       | `true`,`false`      |

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-css-handles-for-store-customization).

| CSS Handles                       |
| --------------------------------- |
| `changeLocationAddressContainer`  |
| `changeLocationContainer`         |
| `changeLocationFormContainer`     |
| `changeLocationGeoContainer`      |
| `changeLocationMapContainer`      |
| `changeLocationGeoErrorContainer` |
| `changeLocationGeolocationButton` |
| `changeLocationSubmitContainer`   |
| `changeLocationSubmitButton`      |
| `changeLocationTitle`             |
| `changeLocationError`             |
| `sellersSelector`                 |
| `sellersSelectorContainer`        |
| `storeListWrapper`                |
| `storeIcon`                       |
| `storesCurrent`                   |
| `storesCurrentNames`              |
| `storeFilterTitle`                |
| `storeListIcon`                   |
| `storeListContainer`              |
| `storeListItems`                  |
| `storeListItem`                   |
