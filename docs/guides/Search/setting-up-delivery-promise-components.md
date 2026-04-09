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

To use Delivery Promise, customers must define a delivery address early in their shopping journey. The [`delivery-promise-components`](https://developers.vtex.com/docs/apps/vtex.delivery-promise-components) app exposes Store Framework blocks that collect that location and, optionally, how the order should be fulfilled (delivery vs pickup, or a specific pickup point).

1. Add the `delivery-promise-components` app to your theme dependencies in `manifest.json` as shown below:

   ```json
      "dependencies": {
        "vtex.delivery-promise-components": "1.x"
      }
   ```

2. Declare the blocks in your theme header (or another layout that should show the controls). Start from one of the combinations below; adjust block IDs and `children` to match your `header` structure.

#### Blocks you can add to the header

The app exposes three header blocks. **`shopper-location-setter` is the one you always include** when using Delivery Promise in the header: it is where the shopper informs a postal code (or equivalent location), and that value is what the rest of the feature uses for availability and filters.

**`shipping-method-selector`** and **`pickup-point-selector`** are optional. They do not replace the location setter. They assume a location already exists in the session (the same state the shopper-location-setter writes). Use them when you want an extra control in the header after the postal code is set; omit them if a single location field is enough for your UX.

You can place all three blocks in the same page, but most implementations keep the header lighter: **`shopper-location-setter` alone**, or **`shopper-location-setter` plus one** of the selectors.

| Block                      | In practice                                                                                           |
| -------------------------- | ----------------------------------------------------------------------------------------------------- |
| `shopper-location-setter`  | The postal-code / location entry point; establishes where Delivery Promise should calculate from.     |
| `shipping-method-selector` | A dedicated control for choosing **delivery** versus **pickup** after the shopper has set a location. |
| `pickup-point-selector`    | A dedicated control for choosing **which pickup point** to use after the shopper has set a location.  |

##### Example: location only

Use this when you only need the shopper to inform where they are, without separate header controls for method or store.

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

##### Example: location + shipping method

Use this when you want the header to make the delivery vs pickup choice explicit right after the location exists.

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

##### Example: location + pickup point

Use this when pickup-in-point is central and you want both “where am I?” and “which store?” visible in the header.

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

3. Configure the behavior with props to customize the blocks. Below, the available props.

**`shopper-location-setter`**

| Prop                         | Type      | Default     | Description                                                                                                            |
| ---------------------------- | --------- | ----------- | ---------------------------------------------------------------------------------------------------------------------- |
| `required`                   | `boolean` | `false`     | When `true`, opens a non-dismissible postal code modal until a valid code is set. When `false`, uses the popover flow. |
| `mode`                       | `string`  | `"default"` | Display mode: `default` or `icon`.                                                                                     |
| `showLocationDetectorButton` | `boolean` | `false`     | Shows the control that uses the browser geolocation API to suggest the postal code. Available only on this block.      |

**`shipping-method-selector`**

| Prop       | Type      | Default     | Description                                                                                                       |
| ---------- | --------- | ----------- | ----------------------------------------------------------------------------------------------------------------- |
| `required` | `boolean` | `false`     | When `true`, the shipping method modal cannot be dismissed until a method is chosen (after a postal code exists). |
| `mode`     | `string`  | `"default"` | Display mode: `default` or `icon`.                                                                                |

**`pickup-point-selector`**

| Prop   | Type     | Default     | Description                        |
| ------ | -------- | ----------- | ---------------------------------- |
| `mode` | `string` | `"default"` | Display mode: `default` or `icon`. |

### Step 3 - Implementing sidebar filters

To display filters in the search sidebar, follow the steps below using the [Search Result](https://developers.vtex.com/docs/apps/vtex.search-result) app.

1. In your theme's `manifest.json`, add the `search-result` app as a dependency:

   ```json
    "dependencies": {
        "vtex.search-result": "3.x"
    }
   ```

2. Ensure your theme includes the `search-result-layout.desktop` or `search-result-layout.mobile` block, depending on the layout.

Within each layout, make sure the sidebar includes `filter-navigator.v3`:

```json
// store/search.json
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

3. Set **`showShippingMethodFacet`** to **`true`** on each flexible search layout block where you want the **shipping method** facet. The default is `false`, so that filter group stays hidden until you opt in. The example above enables it on both **desktop** and **mobile** layouts.

4. Optionally set **`availableShippingValues`** on the same layout blocks to control **which** shipping options appear inside that facet. Omit the prop or use an empty array `[]` to keep the default set: **`delivery`**, **`pickup-in-point`**, and **`pickup-nearby`**. If you pass a **non-empty** array, it **replaces** that default entirely—only values you list are shown (for example add **`pickup-all`** when you want that option on the PLP). Allowed values match the search API shipping facet names: `delivery`, `pickup-in-point`, `pickup-nearby`, `pickup-all`.

   Example with an explicit list (same as the default) plus **`pickup-all`** on desktop and mobile:

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

The shipping method facet only appears when `showShippingMethodFacet` is enabled; which options are listed there follows `availableShippingValues` when you set it, or the default trio when you do not. Other facets related to delivery promise still render as usual.

>⚠️ The delivery promise filters are a beta feature and may be subject to breaking changes. If you customize this functionality, ensure your implementation can adapt to updates.
