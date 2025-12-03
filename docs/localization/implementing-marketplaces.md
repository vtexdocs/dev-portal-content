---
title: "Implementing Marketplaces"
slug: "implementing-marketplaces"
hidden: false
excerpt: "Learn the initial steps for implementing a marketplace operation."
createdAt: ""
updatedAt: ""
---

A marketplace is a specialized ecommerce setup where a VTEX account operates as a platform that connects multiple sellers with customers, enabling third-party sellers to list and sell their products alongside the marketplace owner's products.

>ℹ️ Marketplace capabilities are available for all VTEX storefront technologies.

## Overview

VTEX offers different marketplace types to support various business models and integration scenarios. Understanding these types helps you choose the right approach for your operation.

### Marketplace IN (Receiving sellers)

When your VTEX store acts as a marketplace and receives products from sellers, you're operating a **Marketplace IN** model. This includes:

- **VTEX Seller** - Integrate sellers that are already VTEX stores. These sellers operate on the VTEX platform and can be connected natively without additional development.
- **External Seller** - Integrate sellers that operate outside the VTEX platform. These sellers require custom connector development to integrate with your marketplace.
- **Seller Portal** - Use the Seller Portal solution to onboard and manage sellers. The Seller Portal provides a streamlined interface for sellers to manage their products, orders, inventory, and performance metrics. This solution works for both VTEX and external sellers.

📖 **[Learn more about Marketplace IN →](./marketplace-in)**

### Marketplace OUT (Selling in other marketplaces)

When your VTEX store sells products in other marketplaces (external to your store), you're operating a **Marketplace OUT** model. This includes:

- **Native Connectors** - Sell your products in external marketplaces using VTEX's pre-built native connectors. These connectors are maintained by VTEX and support major marketplaces like Amazon, Mercado Libre, B2W, Via Varejo, Magazine Luiza, and others.
- **External Connectors** - Sell your products in external marketplaces that don't have native VTEX connectors. This requires developing a custom connector to integrate with the external marketplace's APIs.

📖 **[Learn more about Marketplace OUT →](./marketplace-out)**

### Franchises

Franchise accounts are a special type of marketplace architecture that integrates physical stores with online operations. Each franchise account operates as a white-label seller within the main account, inherits the catalog from the main account, and has its own logistics and order management settings.

This model is ideal for brands with multiple physical stores, franchises, or representatives that want to deliver products sold through the brand's ecommerce site from an omnichannel perspective.

📖 **[Learn more about Franchises →](./franchises)**

## Store architecture

To choose the most appropriate architecture that meets your business needs, address some initial questions that define the operation.

### Defining the operation

Before implementing your marketplace, make sure you have the following information ready:

- **Seller onboarding:** Define the process for adding new sellers to your marketplace, including approval workflows and seller verification requirements.

- **Product catalog management:** Decide how products will be managed—whether sellers manage their own catalogs or if there's a centralized catalog management system.

- **Inventory management:** Determine if inventory will be managed by sellers independently or if the marketplace will have visibility into seller inventory levels.

- **Order fulfillment:** Choose whether sellers fulfill orders directly or if the marketplace handles fulfillment through a centralized logistics system.

- **Payment processing:** Plan how payments will be processed—whether sellers receive payments directly or if the marketplace handles payment collection and distribution.

- **Commission structure:** Define the commission or fee structure for marketplace transactions, including how fees are calculated and when they're collected.

- **Seller ratings and reviews:** Plan how customer reviews and seller ratings will be managed and displayed.

- **Customer service:** Determine how customer service will be handled—whether sellers handle their own support or if the marketplace provides centralized support.

- **Tax compliance:** Ensure you have a system for handling tax collection and remittance, especially for multi-region operations.

- **Seller dashboard:** Plan the seller portal features, including order management, inventory updates, and performance analytics.

- **Integration requirements:** Identify what systems sellers need to integrate with (ERP, WMS, PIM) and what APIs or connectors are available.

- **Domains:** Define the primary domain for your marketplace and any subdomains for seller stores if applicable. Learn more in [Rules for main hosts](https://help.vtex.com/en/tutorial/configuring-the-store-domain--tutorials_2450#rules-for-main-host).

### Choosing the store architecture

After defining your operation based on the topics above, choose the architecture for your marketplace.

**Single account, multi-seller:**
- All sellers operate within one VTEX account
- Centralized catalog and order management
- Unified customer experience

**Multi-account, marketplace hub:**
- Main account acts as marketplace hub
- Seller accounts operate independently
- Orders flow through marketplace for coordination

**Hybrid model:**
- Combination of direct sellers and marketplace sellers
- Flexible seller onboarding options
- Mixed fulfillment models

See below the main differences between them:

| Feature | Single account, multi-seller | Multi-account, marketplace hub | Hybrid model |
|---------|----------------------------|-------------------------------|--------------|
| **VTEX accounts** | One account with multiple seller configurations | Main marketplace account plus separate seller accounts | Main account with mix of internal and external sellers |
| **Storefront** | Single website with seller filtering/branding | Marketplace website with links to seller stores | Unified storefront with seller sections |
| **Customer data** | Single Master Data instance for all customers | Customer data shared between marketplace and sellers | Centralized customer data with seller access |
| **Catalog ownership** | Centralized catalog with seller attribution | Sellers manage own catalogs; marketplace aggregates | Mixed: some centralized, some seller-managed |
| **Promotions** | Marketplace-wide and seller-specific promotions | Marketplace promotions limited by seller data access | Flexible promotion rules per seller type |
| **Checkout, OMS, Payments** | Unified checkout and order management | Marketplace coordinates orders across seller accounts | Unified checkout with seller-specific fulfillment |
| **Logistics** | Centralized logistics or seller-managed fulfillment | Each seller manages own logistics independently | Mixed fulfillment models |
| **Back-office systems (ERP/PIM/WMS)** | Single integration point for marketplace | Sellers integrate independently; marketplace has own systems | Marketplace systems plus seller integrations |
| **Seller management** | Seller configuration within account settings | Seller accounts managed separately | Combination of both approaches |

>ℹ️ Learn more about each approach in the section [Marketplace architecture](https://developers.vtex.com/docs/guides/store-architecture#marketplace-architecture) of the Store architecture guide.

## Getting started

To start implementing your marketplace operation, choose the marketplace type that best fits your business needs:

- **[Marketplace IN](./marketplace-in)** - If you want to receive products from sellers and operate as a marketplace platform
- **[Marketplace OUT](./marketplace-out)** - If you want to sell your products in external marketplaces
- **[Franchises](./franchises)** - If you want to integrate physical stores with online operations

Each guide includes detailed implementation steps, configuration requirements, and best practices specific to that marketplace type.

## Fundamental apps

The apps below are essential to enable the marketplace operation in your VTEX account:

**Seller Portal:** Provides sellers with a dedicated interface to manage their products, orders, inventory, and performance metrics. Sellers can access their dashboard, update product information, process orders, and view analytics.

**Marketplace Connector:** Enables integration between the marketplace and seller systems, allowing automated product synchronization, inventory updates, and order management. Learn more in [Marketplace Connector](https://developers.vtex.com/docs/guides/vtex-marketplace-connector).

**Seller Performance Dashboard:** Provides marketplace administrators with insights into seller performance, including sales metrics, order fulfillment rates, customer satisfaction scores, and commission tracking.

**Order Management for Marketplaces:** Handles order routing, split orders, and coordination of fulfillment across multiple sellers. Manages order status updates and ensures proper communication between marketplace, sellers, and customers.

**Catalog Management:** Enables marketplace administrators to review, approve, and manage seller product listings. Includes tools for catalog quality control, duplicate detection, and bulk operations.

**Commission Calculator:** Automatically calculates commissions and fees based on configured rules. Handles different commission structures per seller tier, product category, or transaction type.

>ℹ️ For advanced marketplace operations, you may also need custom apps for seller onboarding workflows, automated product approval, or specialized reporting. Consider working with VTEX partners or developing custom solutions using [VTEX IO](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-io).

## Next steps

<WhatsNextCard
title="Marketplace IN"
description="Learn how to implement a marketplace that receives products from sellers."
linkTo="./marketplace-in"
linkTitle="See more"
/>

<WhatsNextCard
title="Marketplace OUT"
description="Learn how to sell your products in external marketplaces."
linkTo="./marketplace-out"
linkTitle="See more"
/>

<WhatsNextCard
title="Franchises"
description="Learn how to implement franchise accounts for omnichannel operations."
linkTo="./franchises"
linkTitle="See more"
/>

<WhatsNextCard
title="Managing seller catalogs"
description="Understand how to manage product catalogs from multiple sellers in your marketplace."
linkTo="https://developers.vtex.com/docs/guides/managing-seller-catalogs"
linkTitle="See more"
/>

<WhatsNextCard
title="Marketplace order management"
description="Learn how to handle orders from multiple sellers and coordinate fulfillment."
linkTo="https://developers.vtex.com/docs/guides/marketplace-order-management"
linkTitle="See more"
/>

<WhatsNextCard
title="Configuring marketplace payments"
description="Discover how to set up payment processing and commission distribution for your marketplace."
linkTo="https://developers.vtex.com/docs/guides/configuring-marketplace-payments"
linkTitle="See more"
/>
