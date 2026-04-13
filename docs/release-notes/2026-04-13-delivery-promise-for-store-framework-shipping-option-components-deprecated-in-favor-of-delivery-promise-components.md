---
title: "Delivery Promise for Store Framework: Shipping Option Components deprecated in favor of Delivery Promise Components"
slug: "2026-04-13-delivery-promise-for-store-framework-shipping-option-components-deprecated-in-favor-of-delivery-promise-components"
hidden: false
type: "deprecated"
createdAt: "2026-04-13T12:00:00.000Z"
excerpt: "The Shipping Option Components app is deprecated. Stores using Delivery Promise on Store Framework should migrate to Delivery Promise Components, which introduces a new block model and theme configuration."
---

The [`vtex.shipping-option-components`](https://developers.vtex.com/docs/apps/vtex.shipping-option-components) app is now **deprecated** and has been replaced by [`vtex.delivery-promise-components`](https://developers.vtex.com/docs/apps/vtex.delivery-promise-components). We made this change to provide a more flexible and modular way to configure the [Delivery Promise](https://developers.vtex.com/docs/guides/delivery-promise) experience in your Store Framework storefront.

## What has changed?

Previously, the Delivery Promise experience relied on the `vtex.shipping-option-components` app and a single header block, `shipping-option-location-selector`, to collect the shopper's location.

Now, the header experience is powered by the `vtex.delivery-promise-components` app, which provides three separate Store Framework blocks you can use:

- `shopper-location-setter` (required): Collects the shopper's location, such as postal code, to determine Delivery Promise availability and filters.
- `shipping-method-selector` (optional): Allows shoppers to choose between delivery and pickup after setting their location.
- `pickup-point-selector` (optional): Allows shoppers to choose a specific pickup point after setting their location.

### Breaking changes for storefront themes

Migrating from `vtex.shipping-option-components` to `vtex.delivery-promise-components` requires more than just a dependency name change. The following table highlights the main breaking changes:

| Area | Before (`vtex.shipping-option-components`) | Now (`vtex.delivery-promise-components`) |
| --- | --- | --- |
| **Theme dependency** | `vtex.shipping-option-components` | `vtex.delivery-promise-components` |
| **Blocks** | Single block: `shipping-option-location-selector`. | Separate blocks: `shopper-location-setter`, `shipping-method-selector`, and `pickup-point-selector`. |
| **Block props** | Props like `callToAction`, `compactMode`, and `dismissible` on one block. | Props are split across the new blocks, such as `required`, `mode`, and `shippingSelection`. |
| **CSS handles** | Handles such as `buttonLabel`, `deliveryPopover`, and `shippingOptionButton`. | New set of handles, including `shopperLocationSetterContainer` and `shippingMethodSelector`. |

## What needs to be done?

To adapt to this change and continue using Delivery Promise in your Store Framework storefront header, follow the instructions below:

1. In your theme's [`manifest.json`](https://developers.vtex.com/docs/guides/vtex-io-documentation-manifest) file, replace the dependency `vtex.shipping-option-components` with `vtex.delivery-promise-components`:

  ```manifest.json
  "dependencies": {
    "vtex.delivery-promise-components": "1.x"
  }
  ```

2. Remove any usage of the `shipping-option-location-selector` block from your header layout configuration.

3. Add and configure the new blocks:
- Add the `shopper-location-setter` block to your header (Required).
- Optionally, add the following blocks depending on your needs:
    - `shipping-method-selector` to allow shoppers to choose between delivery and pickup.
    - `pickup-point-selector` to allow shoppers to choose a specific pickup point.

4. Validate the storefront behavior by confirming that:
- The header collects the shopper's location.
- Delivery Promise availability and filters respond correctly to the chosen location, shipping method, and pickup point.

To learn more about configuring Delivery Promise in Store Framework, see the [Setting up Delivery Promise components (Beta)](https://developers.vtex.com/docs/guides/setting-up-delivery-promise-components) guide and the [Delivery Promise Components](https://developers.vtex.com/docs/apps/vtex.delivery-promise-components) app documentation.
