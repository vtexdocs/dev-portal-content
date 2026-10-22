---
title: "New Split cart item endpoint in the Checkout API"
slug: "2026-07-28-new-split-cart-item-endpoint-in-the-checkout-api"
type: "added"
createdAt: "2026-07-28T00:00:00.000Z"
updatedAt: "2026-07-28T00:00:00.000Z"
excerpt: "A new Checkout API endpoint lets you split a single cart item into multiple items, distributing its current quantity among them."
---

The [Checkout API](https://developers.vtex.com/docs/api-reference/checkout-api) now includes a new [Split a cart item](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/items/-itemUniqueId-/split) endpoint, which splits a single item in a cart into multiple items, distributing its current quantity among them. For example, this allows different shipping or fulfillment rules to be applied to portions of the same SKU.

## What changed?

To split a cart item, send a `POST` request to the [Split a cart item](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/items/-itemUniqueId-/split) endpoint, specifying the cart's `orderFormId` and the item's `uniqueId` as the `itemUniqueId` path parameter. In the request body, provide an array of objects, each with a `quantity` value. The endpoint will then split the original item into the same number of new items as objects in the array, assigning each new item the specified `quantity` and a new `uniqueId`. The total sum of `quantity` values in the request must exactly match the current quantity of the item being split.

> ⚠️ This request fails if the item's `noSplitItem` field is set to `true`. To check or change this configuration, use the [Handle cart items](https://developers.vtex.com/docs/api-reference/checkout-api#patch-/api/checkout/pub/orderForm/-orderFormId-/items) request.

## What needs to be done?

No action is required. This is a new, optional endpoint available for merchants and partners who need to programmatically split cart items.
