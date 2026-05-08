---
slug: "product-variation-sorting-on-sku-selector"
title: "Product variation sorting on SKU Selector"
createdAt: 2020-07-07T18:04:00.000Z
hidden: false
type: "fixed"
---

Previously, the SKU Selector rendered in a Product Summary Component ([product-summary-sku-selector block](https://developers.vtex.com/docs/apps/vtex.product-summary/ProductSummarySKUSelector/)) did not respect the Catalog data when displaying product variations.

As a result, the product variations didn't have a specific sorting when displayed to users, leading to a poor UX.

This unexpected behavior is now fixed and the SKU Selector now presents the variations according to their ordering in the Catalog module.
