---
title: "Cart simulation: New allowedOutdatedData parameter"
slug: "2026-03-11-cart-simulation-new-allowedoutdateddata-parameter"
type: "added"
createdAt: "2026-03-11T17:08:52.219Z"
updatedAt: "2026-03-11T17:08:52.219Z"
excerpt: "The Cart simulation endpoint now supports the allowedOutdatedData parameter for improved performance with cached data."
---

The [Cart simulation](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/simulation) endpoint now includes a new optional parameter `allowedOutdatedData` to give you more control over data freshness and performance trade-offs.

## What has changed?

The Cart simulation endpoint now accepts an optional `allowedOutdatedData` parameter. This parameter allows you to specify which data types can use cached or slightly outdated information during cart simulation, potentially improving response times for cart operations.

## Why did we make this change?

In order to provide more flexibility and improve performance for cart simulations, we added the `allowedOutdatedData` parameter. This enhancement allows developers to optimize their checkout experience by choosing when to prioritize speed over real-time data accuracy, particularly useful for high-traffic scenarios where cart simulation performance is critical.

## What needs to be done?

This is an optional parameter, so no action is required. Existing implementations will continue to work without any changes.

To use this new parameter in your cart simulations, include `allowedOutdatedData` in your request body when calling the Cart Simulation endpoint. Refer to the [Cart simulation API reference](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/simulation) for detailed information about the parameter's accepted values and behavior.
