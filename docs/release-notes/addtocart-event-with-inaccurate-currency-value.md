---
slug: "addtocart-event-with-inaccurate-currency-value"
title: "addToCart event with inaccurate currency value"
createdAt: 2020-11-26T18:33:18.966Z
hidden: false
type: "fixed"
---

![Store Framework](https://img.shields.io/badge/-Store%20Framework-red)

The `addToCart` event was displaying misleading data on product prices, harming Facebook tracking tools. [The bug was quickly fixed](https://github.com/vtex-apps/facebook-pixel/pull/16) and the currency values are now fetched as they ought to be!
