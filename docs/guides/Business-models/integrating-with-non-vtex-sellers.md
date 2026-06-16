---
title: 'Integrating with non-VTEX sellers'
hidden: false
excerpt: "Learn how to act as a marketplace and onboard non-VTEX (external) sellers."
createdAt: "2026-06-16T00:00:00.000Z"
---

Integrating non-VTEX sellers into your VTEX store lets you expand your product assortment, reach new customers, and increase revenue through commissions, without holding the inventory yourself.

This guide shows how to onboard sellers that operate outside the VTEX platform (external sellers) and start receiving and selling their products, managing everything from your VTEX Admin.

ℹ️ If you want to integrate sellers that already have a VTEX store, see the guide [Integrating VTEX stores](https://developers.vtex.com/docs/guides/integrating-vtex-stores). To learn how to sell your own products on other marketplaces, see [Integrating with non-VTEX marketplaces](https://developers.vtex.com/docs/guides/integrating-with-non-vtex-marketplaces).

## Understanding the integration architecture

When your VTEX store receives and sells products from other stores, it's **acting as a marketplace**. VTEX's native multi-seller architecture decouples the marketplace subsystem from the seller subsystem, so you can onboard sellers and sell their offers in your storefront while each party keeps its own catalog and responsibilities.

A **non-VTEX seller** (external seller) is a store that isn't hosted on the VTEX platform that owns its products and is usually responsible for fulfilling its own orders. Unlike VTEX sellers, external sellers don't have a VTEX account, so they exchange catalog, price, inventory, and order data with your marketplace through endpoints and APIs.

Because non-VTEX sellers don't have a VTEX account, they're integrated through a **custom connector** that uses VTEX APIs to connect the seller's external platform to your marketplace:

* Developed specifically to connect a seller's external platform to your marketplace.
* Uses the VTEX Marketplace Protocol and APIs to exchange catalog, price, inventory, and order data.
* Requires technical development resources.
* Gives you full control over integration logic, suitable for high-volume or complex operations.

> ℹ️ The **Marketplace Protocol** is the set of API requests and definitions used to integrate external sellers into a VTEX marketplace. For the technical flow, see the [External Seller Integration Guide](https://developers.vtex.com/docs/guides/external-seller-integration-guide).

## Instructions

### Defining your operation

Before onboarding sellers, define the operation to choose the setup that best fits your business needs. Make sure you have the following information ready:

* **Seller types:** Define whether you'll integrate external sellers, VTEX sellers, or both. For details, see [Marketplace strategies at VTEX](https://help.vtex.com/docs/tutorials/marketplace-strategies-at-vtex#marketplace-types).
* **Integration strategy:** Plan how you'll build and maintain the custom connector that integrates each external seller's platform with your marketplace through VTEX APIs.
* **Seller hunting:** Identify and recruit sellers that cover your desired product variety, inventory availability, and logistics coverage. For details, see [Find sellers](https://help.vtex.com/docs/tutorials/find-sellers).
* **Catalog ownership:** Define who manages product catalogs (sellers, your marketplace team, or both), how offers are approved, and which product information is mandatory (for example, images, descriptions, and attributes).
* **Order fulfillment:** Choose how orders placed in your marketplace will be fulfilled (for example, fulfillment by each seller, centralized logistics, or a hybrid model).
* **Payment and settlement model:** Define how payments will be collected from shoppers and distributed to sellers, including settlement rules, commission structure, and responsibility for refunds and chargebacks.

### Developing the custom connector

Non-VTEX sellers are integrated through a custom connector that connects the seller's external platform to your marketplace using VTEX APIs. The connector is responsible for:

* Exposing the seller's catalog endpoint so your marketplace can fetch product data.
* Processing change notifications and price and inventory updates.
* Handling order placement and fulfillment communication through the Marketplace Protocol.

> ℹ️ For the full technical flow, see the [External Seller Integration Guide](https://developers.vtex.com/docs/guides/external-seller-integration-guide) and [Catalog management for the VTEX marketplace operation](https://developers.vtex.com/docs/guides/external-seller-integration-vtex-marketplace-operation).

### Defining sales channels

[Sales channels](https://help.vtex.com/docs/tutorials/how-trade-policies-work) determine the product assortment, prices, payments, promotions, customer segmentation, and shipping strategy applied to each channel, including the sellers in your marketplace.

To define sales channels for your sellers, follow the steps below:

1. Evaluate whether you need different configurations for the sellers in your marketplace. If all sellers share the same settings, use your default sales channel.
2. If you need specific settings, [create a new sales channel](https://help.vtex.com/docs/tutorials/creating-a-trade-policy) for your marketplace operation.
3. Use the **Sellers** configuration in the sales channel panel to specify which sellers can sell through each channel, controlling catalog, pricing, promotions, logistics, and payment settings per seller.

> ℹ️ The same sales channel can be used to integrate with multiple sellers. [Requesting additional sales channels](https://help.vtex.com/docs/tutorials/requesting-an-additional-trade-policy) for marketplace operations may incur a monthly fee.

### Adding and configuring the seller

> ℹ️ Make sure you have admin access to manage sellers. For more information, see [Seller Manager](https://help.vtex.com/docs/tutorials/predefined-roles#seller-manager).

To add a non-VTEX seller from the VTEX Admin, follow the steps below:

1. In the VTEX Admin, go to **Marketplace > Management** to access the [Seller Management](https://help.vtex.com/docs/tutorials/seller-management) panel.
2. Click `Add Seller`.
3. Choose **External seller** as the integration type.
4. Complete the required fields, including the connection information provided by the seller (such as the fulfillment and catalog endpoints). For detailed information about these fields, see [Adding a seller](https://help.vtex.com/docs/tutorials/adding-a-seller) and [Connecting a VTEX marketplace to an external seller](https://help.vtex.com/docs/tutorials/shared-information-between-a-marketplace-and-a-seller-on-vtex#connecting-a-vtex-marketplace-to-an-external-seller).
5. Click `Save` to add the seller to your marketplace.

> ℹ️ You can also add a seller using the API. In this case, use the call [Configure seller account](https://developers.vtex.com/docs/api-reference/marketplace-apis#post-/seller-register/pvt/sellers).

### Mapping the catalog

When a store operates as a marketplace, each seller's catalog keeps its own structure. To ensure compatibility between your marketplace catalog and the sellers' catalogs, map [Categories](https://help.vtex.com/docs/tracks/categories-concept-definition), [Brands](https://help.vtex.com/docs/tracks/brands-concept-definition), and [Products and SKU specifications](https://help.vtex.com/docs/tracks/specifications-concept-definition) whenever a seller sends products for the first time or sends products that contain new, previously unmapped data.

To map the catalog, follow the steps below:

1. In the VTEX Admin, go to **Marketplace > Sellers > Catalog Mapping**.
2. Select the seller whose catalog you want to map.
3. For each unmapped category, brand, and specification, select the corresponding value in your marketplace catalog.

> ℹ️ For detailed instructions, see [Mapping categories, brands, and specifications for the marketplace](https://help.vtex.com/docs/tutorials/mapping-categories-and-brands-for-the-marketplace).

### Approving and cataloging received SKUs

After the seller sends products and you map the catalog, review and approve the offers before they become available to customers. The **Received SKUs** panel lets you view, prioritize, and catalog items sent by sellers, including creating new products and linking received items to existing products or SKUs.

To approve received SKUs, follow the steps below:

1. In the VTEX Admin, go to **Marketplace > Sellers > Received SKUs**.
2. Review the SKUs received from each seller (content, images, price, and inventory).
3. `Approve`, link, or reject each item to control which products are listed on your marketplace.

> ℹ️ For detailed instructions, see [Cataloging received SKUs](https://help.vtex.com/docs/tutorials/manual-sku-cataloging). You can also automate approvals using offer quality rules.

### Configuring payments

Marketplaces support different payment scenarios, each with its own configuration:

* **Marketplace processes payments:** The marketplace receives payments and distributes the amounts to sellers according to commission agreements.
* **Seller processes payments:** Each seller receives payments directly for their orders.
* **Split payment:** The payment is divided between the marketplace and the seller according to predefined rules.

> ℹ️ For detailed information, see [Payments in VTEX Marketplace](https://help.vtex.com/docs/tutorials/payments-in-vtex-marketplaces).
