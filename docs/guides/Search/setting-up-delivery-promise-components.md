---
title: "Setting up Delivery Promise components (Beta)"
slug: "setting-up-delivery-promise-components"
excerpt: ""
hidden: false
createdAt: "2025-05-23T22:18:24.684Z"
updatedAt: "2026-08-14T12:00:00.000Z"
seeAlso:
 - "/docs/apps/vtex.delivery-promise-components"
 - "/docs/guides/gathering-delivery-promise-information"
---

>⚠️ This feature is in open beta phase. If you're interested in testing it, contact our [Support team](https://support.vtex.com/hc/en-us).

The [Delivery Promise (Beta)](https://help.vtex.com/en/docs/tutorials/delivery-promise-beta) feature helps create a more accurate and reliable shopping experience by ensuring customers only see products the store can deliver to the provided address or pick up at available locations.

Availability is determined by the following rules:

- When a pickup point is selected — whether in the header or on its own page — the system displays all available pickup points within a 50 km radius configured in Checkout. There's no limit to the number of pickup points displayed.
- For the nearby pickup filter, pickup points within a 10 km radius of the shopper's location are displayed, with a maximum of 40 pickup points.

>ℹ️ Delivery Promise supports any seller architecture (franchise accounts, VTEX Sellers, [Seller Portal](https://help.vtex.com/en/docs/tracks/accounts-and-architecture#vtex-account-types), and external sellers).

![delivery-promise-components](https://vtexhelp.vtexassets.com/assets/docs/src/shipping-option-components___c5a1d86b0ebf692a3eb9ca49f79b55f8.png)

If you're building your storefront with Store Framework, you can enable this experience using two key apps:

- [Delivery Promise Components](https://developers.vtex.com/docs/apps/vtex.delivery-promise-components): Used to display blocks for postal code, delivery versus pickup, and pickup point selection.
- [Search Result](https://developers.vtex.com/docs/apps/vtex.search-result): Used to implement sidebar filters.

Additionally, you can leverage the [Delivery Promise Suggestions API](https://developers.vtex.com/docs/api-reference/delivery-promise-suggestions-api) to display delivery-related tags and badges directly on product cards in the Product Listing Page (PLP), such as "Same Day Delivery", "Express Delivery", and "Pickup Today". Showing these suggestions brings delivery context into the shopping journey earlier, improving product discoverability and conversion rates. For more details, see [Gathering delivery promise information](https://developers.vtex.com/docs/guides/gathering-delivery-promise-information).

This guide walks you through the basic setup needed to implement Delivery Promise in your store.

>ℹ️ Explore the [Delivery Promise Figma library](https://www.figma.com/community/file/1545494767147168145/delivery-promise-by-vtex) to learn more about component specs, usage guidelines, reference use cases, and behavioral patterns.

## Before you begin

To enable Delivery Promise in your store, you must meet the following conditions:

- The store must use [Intelligent Search](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/3qgT47zY08biLP3d5os3DG).
- Check whether you've got version `0.5.0` or later of the [`search-session`](https://developers.vtex.com/docs/apps/vtex.search-session) app installed. To do this, run the `vtex list` command in your terminal and search for the app in the results. If you don't have this app installed, run the command `vtex install vtex.search-session`.
- Your storefront must be built with [Store Framework](https://developers.vtex.com/en/docs/guides/store-framework) to enable the components in this guide. If you use FastStore, check the [FastStore Delivery Promise implementation guide](https://developers.vtex.com/docs/guides/faststore/delivery-promise-implementation). If your store is headless, see [Delivery Promise for headless stores](https://developers.vtex.com/docs/guides/delivery-promise-for-headless-stores).

## Instructions

### Step 1 - Request Delivery Promise activation

Contact our [Support](https://support.vtex.com/hc/en-us) team to request the activation of Delivery Promise.

Activation happens in two stages, so you can validate the experience before impacting production traffic:

- **`DpReady`:** The initial state Support applies to your account. In this state, Delivery Promise is available for testing, but production search requests aren't affected. This lets you validate Delivery Promise in a [development workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-workspace) before applying it to `master`.
- **`DpLive`:** The production state. After you finish testing, contact [Support](https://support.vtex.com/hc/en-us) again to request promotion from `DpReady` to `DpLive`. From that point on, search requests using Delivery Promise hashes or ZIP code use Delivery Promise in production.

### Step 2 - Create a development workspace

While your account is in the `DpReady` state, you can validate Delivery Promise without affecting production search traffic by using a development [workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-workspace). This lets you validate the full storefront experience (postal code modal, shipping method selector, pickup point selector, and sidebar filters) while `master` continues to serve production traffic without Delivery Promise.

[Create a development workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace) by running the following command in your terminal:

```bash
vtex use {wokspaceName}
```

> ⚠️ Replace values between curly braces according to your scenario.

Perform the configurations in the next steps in this workspace so you can validate them end-to-end before promoting the account to `DpLive`.

### Step 3 - Display a location selector

To use Delivery Promise, customers must provide a delivery address early in their shopping journey. The [`delivery-promise-components`](https://developers.vtex.com/docs/apps/vtex.delivery-promise-components) app exposes Store Framework blocks that collect the location and, optionally, the fulfillment method (delivery vs. pickup or a specific pickup point).

1. Add the `delivery-promise-components` app to your theme dependencies in `manifest.json` as shown below:

   ```json
      "dependencies": {
        "vtex.delivery-promise-components": "1.x"
      }
   ```

2. Declare the blocks in your theme header (or another layout that should show the controls). The app exposes three header blocks.

   | Block                      | Description                                                                                                                                                         |
   | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | `shopper-location-setter`  | **Required.** Collects the shopper's location (postal code or equivalent). This value drives all Delivery Promise subsequent availability calculations and filters. |
   | `shipping-method-selector` | Optional. A control for choosing between delivery and pickup after setting a location.                                                                              |
   | `pickup-point-selector`    | Optional. A control for choosing which pickup point to use after setting a location.                                                                                |

   >ℹ️ The `shopper-location-setter` block is required, and you must always include it in the header. `shipping-method-selector` and `pickup-point-selector` are optional. These blocks complement the location setter but don't replace it, since both depend on the location already set in the session. Add them only if you want to expose additional controls in the UI. Otherwise, keep the header simple: either `shopper-location-setter` alone, or `shopper-location-setter` paired with one of the selectors. Using all three together is possible but uncommon.

   Choose the configuration that matches your use case:

   #### Location only

   Use the `shopper-location-setter` block when you only need the shopper to provide their location, without separate header controls for shipping method or store.

   **Example:**

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

   **Example:**

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

   **Example:**

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

3. Use the props below to customize each block's behavior.

   #### `shopper-location-setter`

   | Prop                         | Type      | Default     | Description                                                                                                             |
   | ---------------------------- | --------- | ----------- | ----------------------------------------------------------------------------------------------------------------------- |
   | `required`                   | `boolean` | `false`     | When `true`, opens a non-dismissible postal code modal until the shopper sets a valid code. When `false`, uses the popover flow. |
   | `mode`                       | `string`  | `"default"` | Display mode: `default` or `icon`.                                                                                      |
   | `showLocationDetectorButton` | `boolean` | `false`     | Shows the control that uses the browser geolocation API to suggest the postal code. Available only on this block.       |

   #### `shipping-method-selector`

   | Prop       | Type      | Default     | Description                                                                                                      |
   | ---------- | --------- | ----------- | ---------------------------------------------------------------------------------------------------------------- |
   | `required` | `boolean` | `false`     | When `true`, the shipping method modal can't be dismissed until a method is selected (after entering a postal code). |
   | `mode`     | `string`  | `"default"` | Display mode: `default` or `icon`.                                                                               |

   #### `pickup-point-selector`

   | Prop   | Type     | Default     | Description                        |
   | ------ | -------- | ----------- | ---------------------------------- |
   | `mode` | `string` | `"default"` | Display mode: `default` or `icon`. |

### Step 4 - Implement sidebar filters

To display Delivery Promise filters in the search sidebar, configure the [Search Result](https://developers.vtex.com/docs/apps/vtex.search-result) app as described below.

> ⚠️ Delivery Promise filters are a beta feature and may be subject to breaking changes. If you customize this functionality, ensure your implementation can handle future updates.

1. In your theme's `manifest.json`, add the `search-result` app as a dependency:

   ```json
    "dependencies": {
        "vtex.search-result": "3.x"
    }
   ```

2. Make sure your theme uses either the `search-result-layout.desktop` or the `search-result-layout.mobile` block, depending on the layout. Inside these layouts, include the `filter-navigator.v3` block so the sidebar can render filters:

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

3. Set `showShippingMethodFacet` to `true` in each flexible search layout where you want the Delivery Promise filters to appear. By default, this property is disabled, so the shipping method filter remains hidden unless you explicitly enable it. The example above enables it on both desktop and mobile layouts.
4. Optionally, use the `availableShippingValues` prop in the same layout blocks to define which shipping options to display. If you don't define this prop or set it to an empty array, the system uses the default options: `delivery`, `pickup-in-point`, and `pickup-nearby`. When you provide a non-empty array, it replaces the default entirely and shows only the specified values. Supported values correspond to the search API facet names: `delivery`, `pickup-in-point`, `pickup-nearby`, `pickup-all`.

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

The shipping method facet appears only when `showShippingMethodFacet` is enabled. If you set `availableShippingValues`, the component lists those options; otherwise, it falls back to the default. Other Delivery Promise-related facets behave as usual.

### Step 5 - Validate the experience in the development workspace

[Link](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app) your theme in the development workspace created in [Step 2 - Create a development workspace](#step-2---create-a-development-workspace) and open the workspace URL (for example, `https://{workspaceName}--{accountName}.myvtex.com`) to validate the Delivery Promise experience end-to-end, including the postal code modal, shipping method selector, pickup point selector, and sidebar filters.

> ⚠️ Replace values between curly braces according to your scenario.

### Step 6 - Make Delivery Promise live

Once you finish testing, contact [Support](https://support.vtex.com/hc/en-us) to promote the account from `DpReady` to `DpLive`, and follow the standard release flow to make your theme changes public. For detailed instructions, see [Making your theme content public](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-theme-content-public).

From that point on, Delivery Promise applies to production traffic, and search responses return `deliveryPromiseEnabled: true`.
