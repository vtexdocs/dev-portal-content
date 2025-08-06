---
title: "Using events to trigger side effects on store components"
slug: "vtex-io-documentation-using-events-to-trigger-side-effects-on-store-components"
hidden: false
createdAt: "2020-10-26T10:30:54.362Z"
updatedAt: "2025-07-31T20:13:24.802Z"
---

Events or Pixel Events are notifications broadcast by your storefront whenever a user performs a tracked action, such as:

- Adding an item to the cart (`addToCart` event).
- Removing an item from the cart (`removeItem` event).
- Accessing a loaded page (`pageView` event).
- Viewing a product (`productImpression` event).

Analytics tools commonly use these events to track users' shopping behavior and interactions across your store pages.

You can also use events to create dynamic interactions between your store components by using the `customPixelEventId` prop. These events can generate side effects on the UI, triggering automatic behaviors in your store components as needed.

The `customPixelEventId` prop can be used as either an event sender or receiver, depending on its implementation. When used in a sender component, it emits an event in response to user interaction. In a receiver component, it listens for that specific event and triggers a corresponding UI update.

The prop's value must be a unique ID, enabling blocks to identify which event is being sent or received during user interaction on the UI.

The following table lists the components that support the `customPixelEventId` prop:

| Block name | Behavior |
| -------------------- | --------------------------------------------------- |
| `add-to-cart-button` | Sends an event when clicked.           |
| `minicart.v2` | Receives an event and performs a UI action. |
| `drawer-trigger` | Sends an event when clicked.          |
| `drawer` | Receives an event and performs a UI action. |
| `modal-trigger` | Sends an event when clicked.           |
| `modal-layout` | Receives an event and performs a UI action. |

## Use case example

In this section, we describe how events and the `customPixelEventId` prop can trigger side effects in the interface. Follow the steps below to configure the [`Minicart`](https://developers.vtex.com/docs/apps/vtex.minicart) to automatically open once a new product is added using the [`Add To Cart Button`](https://developers.vtex.com/docs/apps/vtex.add-to-cart-button).

![open-minicart-demo](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-using-events-to-trigger-side-effects-on-store-components-0.gif)

### Instructions

#### Step 1 - Add dependencies

In your theme's `manifest.json` file, make sure the `minicart` and `add-to-cart-button` apps are listed as dependencies:

  ```json
  "dependencies": {
    "vtex.minicart": "2.x",
    "vtex.add-to-cart-button": "0.x"
  }
  ```

#### Step 2 - Configure the event sender

In your store theme code, declare the `customPixelEventId` prop in the block responsible for sending the desired event, passing a unique ID as its value. Example:

  ```json
  {
    "add-to-cart-button#example": {
      "props": {
        "customPixelEventId": "example-add-to-cart"
      }
    },
  }
  ```

#### Step 3 - Configure the event receiver

In the `minicart.v2` block, declare the `customPixelEventIdName` prop in the block responsible for listening for the desired event. Use the same unique ID that you declared in the sender block. Example:

  ```json
  {
    "minicart.v2": {
      "props": {
        "customPixelEventName": "example-add-to-cart"
      },
      "children": ["minicart-base-content"]
    }
  }
  ```

>ℹ The `customPixelEventIdName` prop triggers the `minicart.v2` to open automatically on the interface whenever it detects a pixel event with the specified name. If you also set a `customPixelEventId` prop on the sender, the `minicart.v2` opens only for events that match the name and the custom ID. Learn more in [Minicart](https://developers.vtex.com/docs/apps/vtex.minicart).

After saving your changes and [deploying your new Store Theme version](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-new-app-version-publicly-available), the Add To Cart Button component will send the `example-add-to-cart` event when clicked. At the same time, the Minicart will automatically open in response to any event with this ID.
