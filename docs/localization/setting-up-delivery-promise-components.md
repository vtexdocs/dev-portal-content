---
title: "Setting up Delivery Promise components (Beta)"
slug: "setting-up-delivery-promise-components"
excerpt: ""
hidden: false
createdAt: "2025-05-23T22:18:24.684Z"
updatedAt: "2025-05-23T22:18:24.684Z"
---

>ℹ️ This feature is in closed beta, which means that only selected customers can access it. If you are interested in implementing it in the future, please contact our [Support](https://support.vtex.com/hc/en-us) team.

The [Delivery Promise (Beta)](https://help.vtex.com/en/tutorial/delivery-promise-beta--p9EJH9GgxL0JceA6dBswd) feature helps create a more accurate and reliable shopping experience by ensuring customers only see products that can be delivered to the provided address or picked up at available locations.

The availability is displayed following these rules:

* For pickup points selected in the header or a specific pickup point, the system displays all available pickup points within a 50 km pickup radius configured in Checkout. There is no limit to the number of pickup points displayed.
* For the nearby pickup filter, pickup points within a 10 km radius of the buyer's location are displayed, with a maximum of 40 pickup points.

![delivery-promise-components](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/delivery-promise-component.gif)

If you're building your storefront with Store Framework, you can enable this experience using two key apps:

* [Shipping Option Components](https://developers.vtex.com/docs/apps/vtex.shipping-option-components): Used to display a location selector.
* [Search Result](https://developers.vtex.com/docs/apps/vtex.search-result): Used to implement sidebar filters.

This guide walks you through the basic setup needed to implement these components in your store.

## Before you begin

To enable Delivery Promise (Beta) in your store, the following conditions must be met:

* The store must use [Intelligent Search](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/3qgT47zY08biLP3d5os3DG).
* Your storefront must be built with [Store Framework](https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/67SCtUreXxKYWhZh8n0zvZ#store-framework).
* The store can't act as a marketplace for [Seller Portal](https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/4yPqZQyj0t675QpcG7H6yl#vtex-account-types) accounts or external sellers.

## Instructions

### Step 1 - Requesting Delivery Promise activation

Contact our [Support](https://support.vtex.com/hc/en-us) team to request the activation of Delivery Promise.

### Step 2 - Displaying a location selector

To use Delivery Promise, customers must define a delivery address early in their shopping journey. The [`Shipping Option Components`](https://developers.vtex.com/docs/apps/vtex.shipping-option-components) app provides blocks that allow users to select a location and display delivery options accordingly.

1. Add the `shipping-option-components` app to your theme dependencies in the `manifest.json` as shown below:

   ```json
      "dependencies": {
        "vtex.shipping-option-components": "0.x"
      }
   ```

2. Declare the `shipping-option-location-selector` block as a child block of your [header](https://developers.vtex.com/docs/apps/vtex.store-header) block, exported by the `store-header` app. Example:

   ```json mark=15:17
        "header.full": {
           "blocks": ["header-layout.desktop", "header-layout.mobile"]
         },
        
         "header-layout.desktop": {
           "children": [
             "header-row#1-desktop",
           ]
         },
        
         "header-row#1-desktop": {
           "children": ["shipping-option-location-selector"],
         },
        
        "shipping-option-location-selector": {
          "props": {
            "compactMode": true,
          }
        },
   ```

3. Configure the behavior with props to customize how location selection is presented. Below, we highlight some of the key uses of the available props.
 
   * [Setting up a blocking modal](#setting-up-a-blocking-modal)
   * [Defining displayed delivery methods](#defining-displayed-delivery-methods)

   Learn more about all the available props in [Shipping Option Components](https://developers.vtex.com/docs/apps/vtex.shipping-option-components).

When the customer provides their address, an initial selection of products is made to display only products that can be delivered to that location or picked up at pickup points within a radius of up to 50 km from the provided address — a limit determined by the Checkout. This selection impacts all subsequent product listings and filters.

#### Setting up a blocking model

To ensure location input is provided before browsing, you can configure a blocking modal that displays when the page loads and can't be dismissed until a postal code is entered.

To do this, you must use both the `callToAction` and `dismissible` props:

* `callToAction`: Defines which UI is displayed on load:
 
  * `modal`: Displays a modal requiring postal code entry.
  * `popover-input` *(default)*: Opens a popover with a postal code input field.
  * `popover-button`: Displays a button that opens the popover when clicked.
* `dismissible`: When set to `false`, the modal can't be closed until a valid postal code is entered.

Configure the props as shown in the example below:

```json
"shipping-option-location-selector": {
  "props": {
    "dismissible": false,
    "callToAction": "modal"
  }
}
```

This configuration ensures the page is filtered for delivery availability from the first interaction, improving performance and relevance.

#### Defining displayed delivery methods

The `shippingSelection` prop controls which delivery methods are displayed:

* `delivery-and-pickup`: Enables both delivery and pickup location options.
* `only-pickup`: Displays only the pickup selector (for example, in stores focusing on in-store pickup).

Configure the prop as shown in the example below:

```json
"shipping-option-location-selector": {
  "props": {
    "shippingSelection": "delivery-and-pickup"
  }
}
```

### Step 3 - Implementing sidebar filters

To display available delivery filters in the search sidebar, follow the steps below using the [Search Result](https://developers.vtex.com/docs/apps/vtex.search-result) component. It automatically renders facets, including those related to delivery and pickup availability.

1. In your theme's `manifest.json`, add the `search-result` app as a dependency:

   ```json
    "dependencies": {
        "vtex.search-result": "3.x"
    }
   ```

2. Ensure your theme includes the `search-result-layout.desktop` or `search-result-layout.mobile` block, depending on the layout.

Within this layout, make sure the sidebar block includes `filter-navigator.v3`:

   ```json
    // store/search.json
    {
      "store.search#default": {
        "blocks": ["search-result-layout.desktop"]
      },
      "search-result-layout.desktop": {
        "children": ["filter-navigator.v3", "search-content"]
      }
    }
   ```

These blocks will display all applicable filters automatically. If a customer has selected a location using the Shipping Option component, delivery filters will reflect real-time availability based on that address.

>⚠️ The delivery promise filters are a beta feature and may be subject to breaking changes. If you customize this functionality, ensure your implementation can adapt to updates.
