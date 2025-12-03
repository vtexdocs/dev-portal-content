---
title: "Implementing Marketplaces"
slug: "implementing-marketplaces"
hidden: false
excerpt: "Learn the initial steps for implementing a marketplace operation."
createdAt: ""
updatedAt: ""
---

A marketplace is a platform where multiple sellers offer their products, and the marketplace operator manages the platform and customer experience. VTEX enables businesses to operate as marketplaces, hosting products from various sellers—including those not on the VTEX platform—and manage everything through a unified system.

> ℹ️ Marketplace capabilities are available for all VTEX storefront technologies.

## Marketplace models

VTEX supports multiple marketplace models. Choose the one that best fits your operation:

### Acting as a marketplace

When your VTEX store receives products from sellers, you're **acting as a marketplace**. You can integrate with the following types of sellers:

- **VTEX sellers:** Sellers that already have VTEX stores. Connect them natively with no additional development.
- **External sellers:** Sellers that aren't integrated with VTEX but want to sell their products on a VTEX marketplace. Requires building a custom connector.

> ℹ️ Learn more in the guide [Acting as marketplace](./acting-as-marketplace)

### Acting as a seller

When your VTEX store sells products on other marketplaces, you're **acting as a seller**. You can integrate with the following types of marketplaces:

- **Native marketplace connectors:** Pre-built integrations maintained by VTEX that allow you to sell in external marketplaces without developing your own connector. These connectors are optimized for specific marketplaces and are fully integrated with VTEX Admin for catalog, inventory, and order flows.
- **External marketplace connectors:** Non‑native integrations, not built or maintained by VTEX, used to connect your VTEX store to marketplaces that don’t have a VTEX native connector or when you need custom behavior that native connectors don’t cover. These connectors can be partner apps (certified connectors) or custom integrations built on VTEX IO or other middleware.

> ℹ️ Learn more in the guide [Acting as seller](./acting-as-seller)

## Defining the operation

Before implementing your marketplace, answer these questions to determine which marketplace type fits your business needs:

- **VTEX accounts:** Determine if you'll use a single VTEX account or multiple accounts for your marketplace operation.

- **Storefronts:** Decide if you need separate storefronts for different sellers or a unified marketplace storefront.

- **Customer data:** Plan how customer data will be managed and shared between the marketplace and sellers.

- **Back-office systems:** Identify what back-office systems need integration (ERP, PIM, WMS) with your marketplace. Learn more in [VTEX integrations](https://developers.vtex.com/docs/guides/integrations).

- **Domains:** Define the primary domain for your marketplace and any subdomains for seller stores if applicable. Learn more in [Rules for main hosts](https://help.vtex.com/en/tutorial/configuring-the-store-domain--tutorials_2450#rules-for-main-host).

- **Sub-accounts:** Consider if you will use sub-accounts for different brands or regions. For multi-brand or multi-region operations, check out [Managing a multistore](https://help.vtex.com/en/tutorial/creating-multi-store-multi-domain--tutorials_510).

## Next steps

To start implementing your operation, follow the instructions of the marketplace type that best fits your business needs.

Each guide includes detailed implementation steps, configuration requirements, and best practices specific to that marketplace type.

<WhatsNextCard
title="Acting as marketplace"
description="Learn how to implement a marketplace that receives products from sellers."
linkTo="./marketplace-in"
linkTitle="See more"
/>

<WhatsNextCard
title="Acting as seller"
description="Learn how to sell your products in other marketplaces."
linkTo="./marketplace-out"
linkTitle="See more"
/>
