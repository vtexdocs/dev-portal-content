---
title: "FastStore: Keep split cart lines with preserveCartLines"
slug: "2026-10-30-faststore-preserve-cart-lines"
type: added
createdAt: "2026-10-30T00:00:00.000Z"
updatedAt: "2026-10-30T00:00:00.000Z"
hidden: false
excerpt: "FastStore now supports the opt-in `preserveCartLines` flag, which keeps cart lines of the same SKU separate after they are split in Checkout."
tags:
  - FastStore
---

FastStore now supports the opt-in `api.preserveCartLines` flag, which keeps separate the cart lines of the same SKU that your store split in Checkout.

## What has changed?

By default, FastStore merges cart lines of the same SKU into one line. When a store splits a line in Checkout using the [split item endpoint](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/items/-itemUniqueId-/split), for example, `[refrigerator x1, refrigerator x1]`, FastStore merged them into `[refrigerator x2]` on the next cart validation, undoing the split in Checkout.

With `preserveCartLines: true`, FastStore respects the lines created in Checkout. Each line is shown separately in the minicart, and editing or removing a line affects only that line. FastStore doesn't split lines on its own, and stores that don't enable the flag keep the current behavior.

## Why did we make this change?

Some stores need each unit to be a separate line so shoppers can choose different assembly options for each unit, or so each unit can be integrated individually with an ERP.

## What needs to be done?

Update your store to FastStore `v4.10.3` or later, and set `preserveCartLines` to `true` in the `api` object of your `discovery.config.js` file. For step-by-step instructions, see [Keeping split cart lines](https://developers.vtex.com/docs/guides/faststore/developer-tools-preserve-cart-lines). For the full list of options, see [Configuration options for discovery.config.js](https://developers.vtex.com/docs/guides/faststore/developer-tools-config-options).
