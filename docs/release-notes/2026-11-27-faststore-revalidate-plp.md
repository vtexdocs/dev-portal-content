---
title: "FastStore: Keep PLP prices and stock up to date with `revalidatePLP`"
slug: "2026-11-27-faststore-revalidate-plp"
type: added
createdAt: "2026-11-27T00:00:00.000Z"
updatedAt: "2026-11-27T00:00:00.000Z"
hidden: true
excerpt: "FastStore now supports the opt-in `revalidatePLP` flag, so stores can set how often Product Listing Pages automatically refresh their prices, stock, and product order, keeping that data current for shoppers even between deploys."
tags:
  - FastStore
---

FastStore now supports the opt-in `experimental.revalidatePLP` flag, which keeps the price, stock, and product order shown on Product Listing Pages (PLP) up to date, without requiring a new deploy.

## What has changed?

Before this change, the first page of a PLP was generated once and then cached indefinitely: the price, stock, and product order shoppers saw stayed exactly as they were at that first render until the store's next deploy, no matter how much the catalog changed in the meantime. A price drop, a restock, or an Intelligent Search re-ranking could take hours or days to reach shoppers browsing that PLP.

With `experimental.revalidatePLP` set in `discovery.config.js`, you choose how often (in seconds) FastStore regenerates the PLP in the background. Shoppers keep getting the fast, cached page, but its catalog data now refreshes on the interval you define instead of only on deploy:

```js discovery.config.js
experimental: {
  revalidatePLP: 120, // window in seconds, a positive integer (minimum 60)
}
```

- The value is a number of seconds. The default is `false`, which keeps the current behavior unchanged for stores that don't set it.
- The minimum accepted value is `60`. A valid value below that is automatically raised to `60`, and FastStore logs a console warning the first time this happens.
- Invalid values, such as `0`, negative numbers, decimals, or strings, are treated the same as `false` (no revalidation) and also log a console warning naming the key, instead of breaking the page.
- This flag only affects catalog PLPs rendered by that route. CMS landing pages served by the same route aren't affected, since their content changes on a different cadence and for different reasons.

This is the same mechanism already used for Product Detail Pages (`experimental.revalidate`) and for `notFound` PDP, PLP, and slug pages (`experimental.revalidate404`).

## Why did we make this change?

A store reported that shoppers on high-traffic PLPs kept seeing outdated prices and stock levels for long stretches after Catalog or Search updates, since the only way to refresh that first-rendered page was a full redeploy. That mismatch between what shoppers see and the store's actual prices and inventory can lead to failed purchases and support tickets. `revalidatePLP` lets stores with frequently changing prices or stock close that gap on a schedule that fits their catalog, without the cost of redeploying or regenerating every PLP on every request.

## What needs to be done?

Update your store to the latest version by following [Updating the `@faststore/cli` package version](https://developers.vtex.com/docs/guides/faststore/developer-tools-updating-the-cli-package-version), and set `revalidatePLP` in the `experimental` object of your `discovery.config.js` file to the number of seconds you want between PLP regenerations (minimum `60`). For the full list of options, see [Configuration options for discovery.config.js](https://developers.vtex.com/docs/guides/faststore/developer-tools-config-options).
