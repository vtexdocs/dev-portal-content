---
slug: "addtocart-event-with-inaccurate-currency-value"
title: "addToCart event with inaccurate currency value"
createdAt: 2020-11-26T18:33:18.966Z
hidden: false
type: "fixed"
---

![Store Framework](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/addtocart-event-with-inaccurate-currency-value-0.png)

The `addToCart` event was displaying misleading data on product prices, harming Facebook tracking tools. [The bug was quickly fixed](https://github.com/vtex-apps/facebook-pixel/pull/16) and the currency values are now fetched as they ought to be!
