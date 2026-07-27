---
title: "Implementing marketplaces"
slug: "implementing-marketplaces"
hidden: false
excerpt: "Learn about VTEX marketplace models to sell on other marketplaces or host multiple sellers."
createdAt: "2026-06-16T00:00:00.000Z"
---

A marketplace is an ecommerce platform where multiple sellers offer their products, while the marketplace operator manages the platform and the overall customer experience. With VTEX, you can operate as a marketplace, hosting products from various sellers, and sell your products on other marketplaces.

> ℹ️ Marketplace capabilities are available for all VTEX storefront technologies.

This section covers the main marketplace implementation scenarios supported by VTEX. You'll learn how to implement marketplace operations with VTEX, whether you want to connect VTEX stores, sell through non-VTEX marketplaces, or onboard external sellers into your marketplace.

## Choose your implementation scenario

### Integrate VTEX stores

Choose this path when both sides of the operation use VTEX and you want to connect stores inside the VTEX ecosystem. This scenario supports bidirectional operations, so one store can act as a seller and another can act as a marketplace.

Use this guide to learn how to:

* Define sales channels for marketplace operations.
* Create and share affiliate IDs.
* Add VTEX sellers to a marketplace.
* Configure storefront and payments.
* Reindex the seller catalog.
* Map catalog data and approve received SKUs.

For detailed instructions, see [Integrating VTEX stores](https://developers.vtex.com/docs/guides/integrating-vtex-stores).

### Integrate with non-VTEX marketplaces

Choose this path when your VTEX store acts as a seller, and you want to sell through marketplaces outside the VTEX platform. This scenario can use native connectors, partner connectors, or custom integrations, depending on marketplace support and business requirements.

Use this guide to learn how to:

* Evaluate the available integration method.
* Define sales channels for each marketplace.
* Create affiliates.
* Install and configure connectors.
* Send products to the marketplace.
* Configure price divergence rules.

For detailed instructions, see [Integrating with non-VTEX marketplaces](https://developers.vtex.com/docs/guides/integrating-with-non-vtex-marketplaces).

### Integrate with non-VTEX sellers

Choose this path when your VTEX store acts as a marketplace, and you want to onboard sellers who don't use VTEX. In this model, external sellers are integrated through a custom connector that exchanges catalog, price, inventory, and order data with your marketplace through VTEX APIs and the Marketplace Protocol.

Use this guide to learn how to:

* Define your marketplace operation.
* Develop a custom connector.
* Configure sales channels for sellers.
* Add and configure external sellers.
* Map catalog data.
* Approve received SKUs.
* Configure payments.

For detailed instructions, see [Integrating with non-VTEX sellers](https://developers.vtex.com/docs/guides/integrating-with-non-vtex-sellers).

## Guides in this section

<WhatsNextCard
title="Integrating VTEX stores"
description="Learn the initial steps to integrate VTEX stores to act as marketplaces and sellers."
linkTo="/docs/guides/integrating-vtex-stores"
linkTitle="See more"
/>

<WhatsNextCard
title="Integrating with non-VTEX marketplaces"
description="Learn how to act as a seller and connect your VTEX store to non-VTEX (external) marketplaces."
linkTo="/docs/guides/integrating-with-non-vtex-marketplaces"
linkTitle="See more"
/>

<WhatsNextCard
title="Integrating with non-VTEX sellers"
description="Learn how to act as a marketplace and onboard non-VTEX (external) sellers."
linkTo="/docs/guides/integrating-with-non-vtex-sellers"
linkTitle="See more"
/>
