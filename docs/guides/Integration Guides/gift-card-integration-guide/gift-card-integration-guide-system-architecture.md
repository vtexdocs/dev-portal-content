---
title: "Gift Card system architecture"
slug: "gift-card-integration-guide-system-architecture"
hidden: false
createdAt: "2020-07-01T02:20:23.146Z"
updatedAt: "2020-10-14T23:59:34.329Z"
---

Our Gift Card system provides stores with the flexibility to plug in multiple gift card providers and offer these different options to their customers. This is possible thanks to a layer of interaction between gift card providers and the store, which we call **Gift Card Hub**, and the communication standards defined in our **Gift Card Provider Protocol**.
![Gift Card Hub](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/gift-card-integration-guide-system-architecture-0.png)
[/block]
This article presents an overview of this architecture, so you understand its building blocks and how they interact with each other. We will also explain the purpose of the [Gift Card API](https://developers.vtex.com/reference/giftcard-api-overview) and the [Gift Card Hub API](https://developers.vtex.com/reference/giftcard-hub-api-overview) and how they should be used.
[block:callout]
{
  "type": "info",
  "title": "Our native gift card provider is available to all stores",
  "body": "If you do not need to integrate an external solution, remember you can [set up and manage gift cards](https://help.vtex.com/tutorial/gift-card--tutorials_995) natively in your admin panel or using our [Gift Card API](https://developers.vtex.com/reference/giftcard-api-overview)."
}
[/block]

## Gift Card Hub

This is the system that provides a layer of interaction between gift card providers and VTEX stores. It is used to manage multiple gift card providers connected to a store, both native and external, using a single interface - the [Gift Card Hub API](https://developers.vtex.com/reference/giftcard-hub-api-overview).

## Gift Card Provider Protocol

This is the protocol defining the communication standards gift card providers must follow in their integration with Gift Card Hub. The [Gift Card Provider Protocol](https://developers.vtex.com/reference/giftcard-provider-protocol-overview) section of our API Reference provides details on the eleven endpoints that should be exposed by the middleware connecting the external gift card provider to VTEX.

## VTEX Gift Card Provider

Our native gift card provider is bundled into your VTEX store, and [Gift Card API](https://developers.vtex.com/reference/giftcard-api-overview) is the implementation of the Gift Card Provider Protocol for it. It can be used to manage VTEX gift cards directly - although Gift Card Hub API provides the same functionality in a more generic abstraction layer.
[block:callout]
{
  "type": "warning",
  "body": "The `VtexGiftCard` provider was built from a legacy system, created before our Gift Card system architecture evolved to the Gift Card Hub model. As such, it should not be considered a reference implementation of the Gift Card Provider Protocol.",
  "title": "Our native gift card provider does not fully implement our protocol"
}
[/block]
