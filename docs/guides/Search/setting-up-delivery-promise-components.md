---
title: "Setting up Delivery Promise components (Beta)"
slug: "setting-up-delivery-promise-components"
excerpt: ""
hidden: false
createdAt: "2025-05-23T22:18:24.684Z"
updatedAt: "2026-04-07T12:00:00.000Z"
seeAlso:
 - "/docs/apps/vtex.delivery-promise-components"
---

> ℹ️ This feature is in closed beta, which means that only selected customers can access it. If you are interested in implementing it in the future, please contact our [Support](https://support.vtex.com/hc/en-us) team.

The [Delivery Promise (Beta)](https://help.vtex.com/en/tutorial/delivery-promise-beta--p9EJH9GgxL0JceA6dBswd) feature helps create a more accurate and reliable shopping experience by ensuring customers only see products that can be delivered to the provided address or picked up at available locations.

The availability is displayed following these rules:

- For pickup points selected in the header or a specific pickup point, the system displays all available pickup points within a 50 km pickup radius configured in Checkout. There is no limit to the number of pickup points displayed.
- For the nearby pickup filter, pickup points within a 10 km radius of the buyer's location are displayed, with a maximum of 40 pickup points.

>ℹ️ Delivery Promise supports any seller architecture (franchise accounts, VTEX Sellers, [Seller Portal](https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/4yPqZQyj0t675QpcG7H6yl#vtex-account-types), and external sellers).

![delivery-promise-components](https://vtexhelp.vtexassets.com/assets/docs/src/shipping-option-components___c5a1d86b0ebf692a3eb9ca49f79b55f8.png)

If you're building your storefront with Store Framework, you can enable this experience using two key apps:

* [Delivery Promise Components](https://developers.vtex.com/docs/apps/vtex.delivery-promise-components): Used to display blocks for postal code, delivery versus pickup, and pickup point selection.
* [Search Result](https://developers.vtex.com/docs/apps/vtex.search-result): Used to implement sidebar filters.

This guide walks you through the basic setup needed to implement these components in your store.

>ℹ️ Explore the [Delivery Promise Figma library](https://www.figma.com/community/file/1545494767147168145/delivery-promise-by-vtex) to learn more about component specs, usage guidelines, reference use cases, and behavioral patterns.

## Before you begin

To enable Delivery Promise (Beta) in your store, the following conditions must be met:

* The store must use [Intelligent Search](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/3qgT47zY08biLP3d5os3DG).
* Check if you have installed the `0.5.0` or a later version of the [`search-session`](https://developers.vtex.com/docs/apps/vtex.search-session) app. To do this, run the `vtex list` command in your terminal and search for the app in the results. If you don’t have this app installed, run the command `vtex install vtex.search-session`.
* Your storefront must be built with [Store Framework](https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/67SCtUreXxKYWhZh8n0zvZ#store-framework) to enable the components in this guide. If you use FastStore, check the [FastStore Delivery Promise implementation guide](https://developers.vtex.com/docs/guides/faststore/delivery-promise-implementation). If your store is headless, check [Delivery Promise for headless stores](https://developers.vtex.com/docs/guides/delivery-promise-for-headless-stores).

## Instructions

### Step 1 - Requesting Delivery Promise activation

Contact our [Support](https://support.vtex.com/hc/en-us) team to request the activation of Delivery Promise.

### Step 2 - Displaying a location selector

To use Delivery Promise, customers must provide a delivery address early in their shopping journey. The [`delivery-promise-components`](https://developers.vtex.com/docs/apps/vtex.delivery-promise-components) app exposes Store Framework blocks that collect the location and, optionally, the fulfillment method (delivery vs. pickup or a specific pickup point).

1. Add the `delivery-promise-components` app to your theme dependencies in `manifest.json` as shown below:

   ```json
      "dependencies": {
        "vtex.delivery-promise-components": "1.x"
      }
   ```

2. Declare the blocks in your theme header (or another layout that should show the controls). The app exposes three header blocks.

| Block                      | Description                                                                                           |
| -------------------------- | ----------------------------------------------------------------------------------------------------- |
| `shopper-location-setter`  | **Required.** Collects the shopper’s location (postal code or equivalent). This value drives all Delivery Promise subsequent availability calculations and filters.|
| `shipping-method-selector` | Optional. A control for choosing between delivery and pickup after a location is set. |
| `pickup-point-selector`    | Optional. A control for choosing which pickup point to use after a location is set.  |

> The `shopper-location-setter` block is required and must always be included in the header. `shipping-method-selector` and `pickup-point-selector` are optional. They complement the location setter but do not replace it, since both depend on the location already set in the session. Add them only if you want to expose additional controls in the UI. Otherwise, keep the header simple: either `shopper-location-setter` alone, or `shopper-location-setter` paired with one of the selectors. Using all three together is possible but uncommon.

Choose the configuration that matches your use case:

#### Location only

Use the `shopper-location-setter` block when you only need the shopper to provide their location, without separate header controls for shipping method or store.

**Example** 

```json
    "header-row#1-desktop": {
      "children": ["shopper-location-setter"]
    },

    "shopper-location-setter": {
      "props": {
        "required": false,
        "mode": "default",
        "showLocationDetectorButton": false
      }
    }
```

#### Location + shipping method

Use `shopper-location-setter` and `shipping-method-selector` when you want the header to make the delivery or pickup choice explicit right after the shopper enters a location.

**Example** 

```json
    "header-row#1-desktop": {
      "children": [
        "shopper-location-setter",
        "shipping-method-selector"
      ]
    },

    "shopper-location-setter": {
      "props": {
        "required": false,
        "mode": "default",
        "showLocationDetectorButton": false
      }
    },

    "shipping-method-selector": {
      "props": {
        "required": false,
        "mode": "default"
      }
    }
```

#### Location + pickup point

Use `shopper-location-setter` and `pickup-point-selector` when pickup is a central part of your experience, and you want both "where am I?" and "which store?" visible in the header.

**Example** 

```json
    "header-row#1-desktop": {
      "children": [
        "shopper-location-setter",
        "pickup-point-selector"
      ]
    },

    "shopper-location-setter": {
      "props": {
        "required": false,
        "mode": "default",
        "showLocationDetectorButton": false
      }
    },

    "pickup-point-selector": {
      "props": {
        "mode": "default"
      }
    }
```

3. Configure the behavior with props to customize the blocks. Below are the available props.

#### `shopper-location-setter`

| Prop                         | Type      | Default     | Description                                                                                                            |
| ---------------------------- | --------- | ----------- | ---------------------------------------------------------------------------------------------------------------------- |
| `required`                   | `boolean` | `false`     | When `true`, opens a non-dismissible postal code modal until a valid code is set. When `false`, uses the popover flow. |
| `mode`                       | `string`  | `"default"` | Display mode: `default` or `icon`.                                                                                     |
| `showLocationDetectorButton` | `boolean` | `false`     | Shows the control that uses the browser geolocation API to suggest the postal code. Available only on this block.      |

#### `shipping-method-selector`

| Prop       | Type      | Default     | Description                                                                                                       |
| ---------- | --------- | ----------- | ----------------------------------------------------------------------------------------------------------------- |
| `required` | `boolean` | `false`     | When `true`, the shipping method modal cannot be dismissed until a method is selected (after a postal code is entered). |
| `mode`     | `string`  | `"default"` | Display mode: `default` or `icon`.                                                                                |

#### `pickup-point-selector`

| Prop   | Type     | Default     | Description                        |
| ------ | -------- | ----------- | ---------------------------------- |
| `mode` | `string` | `"default"` | Display mode: `default` or `icon`. |

### Step 3 - Implementing sidebar filters

To display Delivery Promise filters in the search sidebar, configure the [Search Result](https://developers.vtex.com/docs/apps/vtex.search-result) app as described below.

> ⚠️ Delivery Promise filters are a beta feature and may be subject to breaking changes. If you customize this functionality, ensure your implementation can handle future updates.

1. In your theme's `manifest.json`, add the `search-result` app as a dependency:

   ```json
    "dependencies": {
        "vtex.search-result": "3.x"
    }
   ```

2. Ensure your theme uses either the `search-result-layout.desktop` or `search-result-layout.mobile` blocks, depending on the layout. Inside these layouts, include the `filter-navigator.v3` block so the sidebar can render filters:

  ```json store/search.json
  {
    "store.search#default": {
      "blocks": ["search-result-layout"]
    },
    "search-result-layout": {
      "children": [
        "search-result-layout.desktop",
        "search-result-layout.mobile"
      ]
    },
    "search-result-layout.desktop": {
      "children": ["filter-navigator.v3", "search-content"],
      "props": {
        "showShippingMethodFacet": true
      }
    },
    "search-result-layout.mobile": {
      "children": ["filter-navigator.v3", "search-content"],
      "props": {
        "showShippingMethodFacet": true
      }
    }
  }
  ```

3. Enable the Delivery Promise filters by setting the `showShippingMethodFacet` to `true` in each flexible search layout where the facet should appear. This property is disabled by default, so the shipping method filter remains hidden unless explicitly enabled. The example above enables it on both desktop and mobile layouts.
4. Optionally, define which shipping options should be displayed using the `availableShippingValues` prop in the same layout blocks. When this prop is not defined, or when it is set to an empty array, the default options are used: `delivery`, `pickup-in-point`, and `pickup-nearby`. When you provide a non-empty array, it replaces the default entirely, and only the specified values are shown. Supported values correspond to the search API facet names and include: `delivery`, `pickup-in-point`, `pickup-nearby`, `pickup-all`.

   Example with an explicit list (same as the default) plus `pickup-all` on desktop and mobile:

   ```json
   "search-result-layout.desktop": {
     "children": ["filter-navigator.v3", "search-content"],
     "props": {
       "showShippingMethodFacet": true,
       "availableShippingValues": [
         "delivery",
         "pickup-in-point",
         "pickup-nearby",
         "pickup-all"
       ]
     }
   }
   ```

The shipping method facet appears only when `showShippingMethodFacet` is enabled. The options listed match `availableShippingValues` when you set it, or fall back to the default set when the prop is not provided. Other Delivery Promise-related facets continue to behave as usual.

