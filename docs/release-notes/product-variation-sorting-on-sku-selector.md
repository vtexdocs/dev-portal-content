---
slug: "product-variation-sorting-on-sku-selector"
title: "Product variation sorting on SKU Selector"
createdAt: 2020-07-07T18:04:00.000Z
hidden: false
type: "fixed"
---

![Store Framework](https://img.shields.io/badge/-Store%20Framework-red)

Previously, the SKU Selector rendered in a Product Summary Component ([product-summary-sku-selector block](https://vtex.io/docs/components/all/vtex.product-summary/product-summary-sku-selector/)) did not respect the Catalog data when displaying product variations.

As a result, the product variations didn't have a specific sorting when displayed to users, leading to a poor UX.

This unexpected behavior is now fixed and the SKU Selector now presents the variations according to their ordering in the Catalog module.
