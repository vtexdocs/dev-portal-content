---
title: "Store Framework: Shipping Option Components deprecated in favor of Delivery Promise Components"
slug: "2026-04-13-store-framework-shipping-option-components-deprecated-in-favor-of-delivery-promise-components"
hidden: false
type: "deprecated"
createdAt: "2026-04-13T12:00:00.000Z"
excerpt: "The Shipping Option Components app is deprecated. Stores using Delivery Promise on Store Framework should migrate to Delivery Promise Components, which introduces a new block model and theme configuration."
---

The [Shipping Option Components](https://developers.vtex.com/docs/apps/vtex.shipping-option-components) app is **deprecated** in favor of [Delivery Promise Components](https://developers.vtex.com/docs/apps/vtex.delivery-promise-components). If your storefront uses [Delivery Promise](https://developers.vtex.com/docs/guides/delivery-promise) with Store Framework, plan a theme migration to the new app.

> ℹ️ Delivery Promise remains in **closed beta**, which means that only selected customers can access it. If you're interested in implementing it in the future, please contact our [Support](https://support.vtex.com/hc/en-us) team.

## What has changed?

Previously, the Delivery Promise experience relied on the Shipping Option Components app and a single header block (`shipping-option-location-selector`) to collect the shopper's location and drive product availability and filters.

Now, the header experience is powered by the Delivery Promise Components app, which exposes three separate Store Framework blocks:

- `shopper-location-setter` (required): Collects the shopper's location (postal code or equivalent) and drives Delivery Promise availability and filters.
- `shipping-method-selector` (optional): Lets shoppers choose between delivery and pickup after setting their location.
- `pickup-point-selector` (optional): Lets shoppers choose a specific pickup point after setting their location.

### Breaking changes for storefront themes

Migrating isn't a drop-in dependency rename. Expect the following when moving from Shipping Option Components to Delivery Promise Components:

| Area | Before (Shipping Option Components) | After (Delivery Promise Components) |
| --- | --- | --- |
| **Theme dependency** | `vtex.shipping-option-components` (for example `1.x`) | `vtex.delivery-promise-components` (see [app documentation](https://developers.vtex.com/docs/apps/vtex.delivery-promise-components) for the supported major line) |
| **Blocks** | Single block such as `shipping-option-location-selector`. | Separate blocks, including `shopper-location-setter`, `shipping-method-selector`, and `pickup-point-selector`. |
| **Block props** | Props such as `callToAction`, `compactMode`, and `dismissible` on one block. | Props split across blocks (for example, `required`, `mode`, `shippingSelection` per block). There is no one-to-one mapping for all legacy props. |
| **Session / layout** | Legacy single-header pattern. | Theme should follow the [app documentation](https://developers.vtex.com/docs/apps/vtex.delivery-promise-components) for `DeliveryPromiseProvider` (for example, via the `store` app's `StoreWrapper`) so blocks share the same session state. |
| **CSS handles** | Handles such as `buttonLabel`, `deliveryPopover`, and `shippingOptionButton`. | New handle set (for example `shopperLocationSetterContainer`, `shippingMethodSelector`). Existing CSS customizations must be rewritten against the new handles. |

Flexible PLP and shipping-method facet were not documented the same way | If you show Delivery Promise on the PLP via **`search-result`**, configure layout props such as **`showShippingMethodFacet`** and **`availableShippingValues`** as in the [setup guide](https://developers.vtex.com/docs/guides/setting-up-delivery-promise-components) 

Custom code that imported or extended the old app's React surface may also require changes; check the new app's documentation for supported exports (for example, presentational pickup UI where applicable).

## What needs to be done?

To adapt to this change and continue using Delivery Promise in your Store Framework storefront header, follow these steps:

1. Update your app dependency

In your theme's manifest.json file, remove the old app and add the new app:

```manifest.json
"dependencies": {
  "vtex.delivery-promise-components": "1.x"
}
```

2. Remove the legacy header block

Remove any usage of the `shipping-option-location-selector` block from your header layout configuration.

3. Add and configure the new blocks

- Add the `shopper-location-setter` block to your header (required).
- Depending on your needs, optionally add:
    - `shipping-method-selector` to let shoppers choose between delivery and pickup.
    - `pickup-point-selector` to let shoppers choose a specific pickup point.

4. Validate the storefront behavior

Confirm that:
- The header collects the shopper's location.
- Delivery Promise availability and filters respond correctly to the chosen location, shipping method, and pickup point.

To learn more about configuring Delivery Promise in Store Framework and see complete examples, see the [Setting up Delivery Promise components (Beta)](https://developers.vtex.com/docs/guides/setting-up-delivery-promise-components) guide and the [Delivery Promise Components](https://developers.vtex.com/docs/apps/vtex.delivery-promise-components) app documentation.
