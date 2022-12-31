---
slug: "minicart-v2-automatic-display"
title: "Minicart v2 automatic display"
createdAt: 2020-08-26T16:28:00.000Z
hidden: false
type: "improved"
---

![Store Framework](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/minicart-v2-automatic-display-0.png) 

A trigger responsible for automatically opening the Minicart v2 on the interface can now be set by you using a store event and the block's new `customPixelEventId`  and `customPixelEventName` props!

A long-awaited scenario, in which this new release is extremely useful, is to automatically open the Minicart component whenever the `Add To Cart button` is clicked on by users. 

Brace yourselves because the wait has finally come to an end: to prettify this release, the `add-to-cart-button` block has also gained a new prop called `customPixelEventId` to broadcast an event of its own when it is clicked on.

In practice, this means that you can now set up both `add-to-cart-button` and `minicart.v2` blocks to configure this behavior in your store, displaying to your users the options to move to checkout or  just keep shopping.