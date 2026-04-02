---
title: 'Integrating with non-VTEX marketplaces'
hidden: false
excerpt: ""
createdAt: 2026-03-18T00:00:00.000Z
---

Integrating your VTEX store with non-VTEX marketplaces enables you to expand your sales channels, reach new customers, and increase brand visibility. This guide shows you how to connect your VTEX store as a seller to marketplaces through connectors, APIs, or custom integrations.

> ℹ️ If you want to integrate your VTEX store as a seller of a VTEX marketplace, see the guide [Integrating VTEX stores](https://developers.vtex.com/docs/guides/integrating-vtex-stores).

## Understanding the integration architecture

Marketplace integration establishes a connection between your VTEX store (as a seller) and non-VTEX marketplaces. This architecture enables you to sell on multiple channels while managing everything from your VTEX Admin.

We have the following marketplace integration types:

**Native connectors:**

* Pre-built integrations developed by VTEX.
* Available for major marketplaces (Amazon, Mercado Libre, etc.).
* Maintained and updated by VTEX.

**Partner connectors:**

* Integrations developed by VTEX partners.
* Specialized solutions for specific marketplaces.
* Support provided by partner companies.
* May include additional features or customizations.

**External marketplace (custom connectors):**

* Developed specifically for unsupported marketplaces.
* Requires technical development resources.
* Uses VTEX APIs and marketplace APIs.
* Full control over integration logic.
* Ideal for unique or regional marketplaces.

## Instructions

### Choosing your integration method

Check whether VTEX provides a native connector or if there are certified partner solutions that meet your business needs:

1. In the VTEX Admin, go to **Marketplace > Connections > Marketplaces and Integrations**.
2. Browse available connectors or search for your target marketplace.
3. Check if the connector supports your business needs.

> ℹ️ For the list of available connectors and partner solutions, see [Marketplace strategies at VTEX](https://help.vtex.com/docs/tutorials/marketplace-strategies-at-vtex).

For unsupported marketplaces, consider developing a custom connector.

**When to develop custom connectors:**

* No native or certified connector exists.
* Marketplace has specific technical requirements.
* Integration requires unique business logic.
* Volume justifies development investment.

> ℹ️ To develop a custom marketplace integration, see the guides [External Marketplace Integration Guide](https://developers.vtex.com/vtex-developer-docs/docs/external-marketplace-integration-guide) and [Integration app template](https://developers.vtex.com/docs/guides/external-marketplace-integration-app-template).

### Defining sales channels

[Sales channels](https://help.vtex.com/docs/tutorials/how-trade-policies-work) control which products, prices, and conditions apply to each channel, including marketplaces.

To define sales channels for your marketplace:

1. Evaluate if you need different configurations for each marketplace. If all of them use the same configurations, use your default sales channel.

   The same sales channel can be used to integrate with multiple marketplaces. [Requesting additional trade policies](https://help.vtex.com/docs/tutorials/requesting-an-additional-trade-policy) for marketplace integrations may incur a monthly fee.
2. If you need specific settings, [create a new trade policy](https://help.vtex.com/docs/tutorials/creating-a-trade-policy) for your operations.
3. Configure the sales channel with the appropriate settings for catalog, pricing, promotions, and logistics. For detailed configuration instructions, see [Configuring a marketplace trade policy](https://help.vtex.com/docs/tutorials/configuring-a-marketplace-trade-policy).

### Creating an affiliate

> ℹ️ Ensure you have Admin access to configure affiliates. For more information, see the release note [New permissions for accessing order configurations](https://help.vtex.com/announcements/2025-10-21-new-license-manager-resources-order-configurations).

The [affiliate](https://help.vtex.com/docs/tutorials/what-is-an-affiliate) is the code that identifies the marketplace where your products will be sold. Each marketplace must have a unique affiliate.

To create an affiliate:

1. In the VTEX Admin, go to **Store Settings > Orders > Settings**.
2. In the **Affiliates** tab, click `+ New Affiliate`.
3. Fill in the required fields. For detailed information about these fields, see [Configuring affiliates](https://help.vtex.com/docs/tutorials/configuring-affiliates).
4. Click `Save` to create the affiliate.

> ℹ️ After creating the affiliate, provide the affiliate ID to the marketplace operator. The marketplace will use this ID when adding your store as a seller.

### Installing and configuring the connector

For VTEX native connectors or partner solutions:

1. In the VTEX Admin, go to **Marketplace > Connections > Marketplaces and Integrations**.
2. Find the marketplace connector.
3. Click `Connect`.
4. Follow the connector-specific setup wizard.
5. Provide required credentials and settings.
6. Authorize the connection with the marketplace.

> ℹ️ For detailed instructions on each available connector or partner solution, including how to map product categories and attributes when necessary, see the integration tutorial for each specific marketplace in the guide [Marketplace and Integrations](https://help.vtex.com/docs/tutorials/marketplaces-and-integrations#integration-tutorials).

### Sending products to the marketplace

For native connectors or partner solutions, products associated with the corresponding sales channel are sent automatically.

In custom integrations, you should:

* Implement product export using VTEX APIs.
* Handle Change Notification and SKU Suggestion flows.
* Process responses and retry failed products.

> ℹ️ For detailed information, see [Sending products to the marketplace](https://help.vtex.com/docs/tutorials/sending-products-to-the-marketplace).

### Configuring price divergence rules

Price divergence rules protect your store from processing orders with unexpected price differences between VTEX and the marketplace. Price differences can occur due to:

* Synchronization delays
* Promotional pricing mismatches
* Currency conversion variations
* Marketplace-applied promotions
* System errors or bugs

To configure acceptable price variance, follow these instructions:

1. In the VTEX Admin, go to **Store Settings > Orders > Order authorization**.
2. Click the **Price divergence** tab.
3. Click `Create rule`.
4. In the **Authorization Rules** panel, click `CREATE RULES` to set a new rule.
5. Set the interval and define what should happen in this interval: `Automatically authorize`, `Automatically deny`, or `Create a VTEX DO task for approval`.
6. Click `SAVE RULES` to save the rule.

> ℹ️ For detailed information, see [Price Divergence rule](https://help.vtex.com/en/docs/tutorials/price-divergence-rule).
