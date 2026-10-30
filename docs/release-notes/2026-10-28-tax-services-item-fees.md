---
title: "Tax services: Item fees in the tax provider response"
slug: "2026-10-28-tax-services-item-fees"
type: "added"
createdAt: "2026-10-28T00:00:00.000Z"
updatedAt: "2026-10-28T00:00:00.000Z"
hidden: false
excerpt: "Tax providers can now return an optional fees array for each item, separating regulatory or commercial charges from taxes in the cart and order totals."
tags:
  - Checkout
---

[Tax service](https://developers.vtex.com/docs/guides/tax-services-overview) providers can now return an optional `fees` array for each item in the response to Checkout. Use it for charges that aren't taxes, such as regulatory or commercial fees, so they're kept apart from the taxes applied to the order.

## What has changed?

Until now, the tax provider response only accepted a `taxes` array. Any charge returned by the provider was handled as a tax, even when it wasn't a fiscal or government charge. For example, a deposit for returnable packaging that varies by state had to be returned as a tax, which added it to the tax total and resulted in incorrect fiscal values.

The tax provider can now also return a `fees` array for each item, at the same level as `taxes` and with the same fields. When the provider returns fees, Checkout:

- Adds each fee to the item's `priceTags` with the `FEE@{name}` prefix. Taxes keep the `TAXHUB@{name}` prefix.
- Adds the fee values to a new `Fee` totalizer in the cart and order, separate from the `CustomTax` totalizer that adds up the taxes.

## What needs to be done?

No action is required. The `fees` array is optional, and integrations that only return `taxes` work as before.

If your tax provider calculates charges that aren't taxes, you can return them in the `fees` array. For the full response format and examples, see [Item fees](https://developers.vtex.com/docs/guides/tax-services-specification#item-fees) in the Tax services specification.
