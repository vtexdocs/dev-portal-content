---
title: "FastStore: Fixed cart validation for assembly options hidden from search"
slug: "2026-10-30-faststore-cart-validation-hidden-assembly-skus"
type: fixed
createdAt: "2026-10-30T00:00:00.000Z"
updatedAt: "2026-10-30T00:00:00.000Z"
hidden: false
excerpt: "FastStore no longer fails cart validation, or empties the Checkout cart, when an assembly option SKU is hidden from Intelligent Search."
tags:
  - FastStore
---

FastStore now keeps the cart working when it contains an assembly option, such as installation or haul away, whose SKU is hidden from the storefront.

## What has changed?

Assembly option SKUs often have **Display on website** turned off, so Intelligent Search doesn't return them, even with `show-invisible-items=true`. In this scenario, the `validateCart` mutation failed with the error `Search API did not found the following skus`. On the following validation, the cart in the browser could replace the one in Checkout, removing both the product and the service.

FastStore now builds the assembly option line from the Order Form data when Search doesn't return its SKU. The product and the service remain in the minicart after a reload, and removing the product also removes its service. Any other missing SKU still fails validation, so Search outages aren't hidden.

## Why did we make this change?

Keeping service SKUs hidden from the storefront is a common practice, as it prevents them from appearing in search results or having their own product page. Cart validation shouldn't require those SKUs to be visible.

## What needs to be done?

Update your store to FastStore `v4.10.3` or later by following [Updating the CLI package version](https://developers.vtex.com/docs/guides/faststore/developer-tools-updating-the-cli-package-version). No additional configuration is required.
