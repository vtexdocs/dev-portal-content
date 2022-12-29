---
slug: "unwanted-product-specifications-being-displayed"
title: "Unwanted product specifications being displayed"
createdAt: 2020-11-26T18:42:18.974Z
hidden: false
type: "fixed"
---

![Store Framework](https://img.shields.io/badge/-Store%20Framework-red)

Although we have a checkbox in the Catalog module to set whether a specification should be displayed on the product details page or not, this info was not properly handled in our Product Specifications component.

But not anymore: [unwanted specifications are now blocked from being displayed](https://github.com/vtex-apps/search-resolver/pull/115) when you select this option. This is what I call power of choice, my friends!
