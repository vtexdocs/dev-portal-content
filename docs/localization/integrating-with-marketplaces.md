---
title: 'Integrating with marketplaces'
hidden: false
excerpt: ""
createdAt: 2026-02-20T00:00:00.000Z
---

Integrating your VTEX store with marketplaces enables you to expand your sales channels, reach new customers, and increase brand visibility. This guide shows you how to connect your VTEX store as a seller to marketplaces through connectors, APIs, or custom integrations.

In this guide, you will learn how to:

- Understand external marketplace integration architecture
- Configure your VTEX store as a seller for external marketplaces
- Implement product catalog synchronization
- Manage orders received from external marketplaces
- Handle pricing, inventory, and fulfillment operations

## Understanding the integration architecture

External marketplace integration establishes a connection between your VTEX store (as a seller) and marketplaces hosted on external platforms. This architecture enables you to sell on multiple channels while managing everything from your VTEX Admin.

### Integration types

**Native connectors:**

- Pre-built integrations developed by VTEX.
- Available for major marketplaces (Amazon, Mercado Libre, etc.).
- Maintained and updated by VTEX.
- Recommended for supported marketplaces.

**Certified partner connectors:**

- Integrations developed by certified VTEX partners.
- Specialized solutions for specific marketplaces.
- Support provided by partner companies.
- May include additional features or customizations.

**Custom connectors:**

- Developed specifically for unsupported marketplaces.
- Requires technical development resources.
- Uses VTEX APIs and marketplace APIs.
- Full control over integration logic.
- Ideal for unique or regional marketplaces.

## Instructions

### Step 1 - Choosing your integration method

Check whether VTEX provides a native connector or if there are certified partner solutions that meet your business needs:

1. In the VTEX Admin, go to **Marketplace > Connections > Marketplaces and Integrations**.
2. Browse available connectors or search for your target marketplace.
3. Check if the connector supports your business needs.

> ℹ️ For the list of available connectors and partner solutions, see [Marketplace strategies at VTEX](https://help.vtex.com/docs/tutorials/marketplace-strategies-at-vtex).

For unsupported marketplaces, consider developing a custom connector.

**When to develop custom connectors:**

- No native or certified connector exists.
- Marketplace has specific technical requirements.
- Integration requires unique business logic.
- Volume justifies development investment.

To develop a custom marketplace integration, see the guides [External Marketplace Integration Guide](https://developers.vtex.com/vtex-developer-docs/docs/external-marketplace-integration-guide) and [Integration app template](https://developers.vtex.com/docs/guides/external-marketplace-integration-app-template).

### Step 2 - Defining sales channels

[Sales channels](https://help.vtex.com/docs/tutorials/how-trade-policies-work) control which products, prices, and conditions apply to each channel, including marketplaces.

To define sales channels for your marketplace:

1. Evaluate if you need different configurations for each marketplace. If all of them use the same configurations, use your default sales channel.
   The same sales channel can be used to integrate with multiple marketplaces. [Requesting additional trade policies](https://help.vtex.com/docs/tutorials/requesting-an-additional-trade-policy) for marketplace integrations may incur a monthly fee.
3. If you need specific settings, [create a new trade policy](https://help.vtex.com/docs/tutorials/creating-a-trade-policy) for your operations.
4. Configure the sales channel with the appropriate settings for catalog, pricing, promotions, and logistics.

> ℹ️ After defining which sales channel you'll use in your integrations, configure specific settings. For detailed configuration instructions, see [Configuring a marketplace trade policy](https://help.vtex.com/docs/tutorials/configuring-a-marketplace-trade-policy).

### Step 3 - Creating an affiliate

> ℹ️ Ensure you have Admin access to configure affiliates. For more information, see the release note [New permissions for accessing order configurations](https://help.vtex.com/announcements/2025-10-21-new-license-manager-resources-order-configurations).

The [affiliate](https://help.vtex.com/docs/tutorials/what-is-an-affiliate) is the code that identifies the marketplace where your products will be sold. Each marketplace must have a unique affiliate.

To create an affiliate:

1. In the VTEX Admin, go to **Store Settings > Orders > Settings**.
2. In the **Affiliates** tab, click `+ New Affiliate`.
3. Fill in the required fields. For detailed information about these fields, see [Configuring affiliates](https://help.vtex.com/docs/tutorials/configuring-affiliates).
4. Click `Save` to create the affiliate.

> ℹ️ After creating the affiliate, provide the affiliate ID to the marketplace operator. The marketplace will use this ID when adding your store as a seller.

### Step 4 - Installing and configuring the connector

For VTEX native connectors or partner solutions:

1. In the VTEX Admin, go to **Marketplace > Connections > Marketplaces and Integrations**.
2. Find the marketplace connector.
3. Click `Connect`.
4. Follow the connector-specific setup wizard.
5. Provide required credentials and settings.
6. Authorize the connection with the marketplace.

> ℹ️ Check the integration tutorial for each specific marketplace to find the instructions for the available connector or partner solution.

### Step 5 - Mapping product categories and attributes

Each marketplace may use its own category structures and product attributes. Mapping ensures your products appear correctly on the marketplace.

#### Step 5.1 - Understand marketplace structure

Review the marketplace's catalog organization:

1. Access marketplace seller documentation.
2. Review available product categories.
3. Understand required and optional attributes.
4. Note any category-specific requirements.
5. Identify restricted or prohibited categories.

#### Step 5.2 - Map categories

Match your VTEX categories to marketplace categories:

1. In the connector settings, access category mapping.
2. Select each VTEX category to map.
3. Choose the corresponding marketplace category.
4. Review category requirements and restrictions.
5. Save category mappings.

**Mapping best practices:**

- Choose the most specific category available
- Verify category requirements (attributes, images, etc.)
- Check commission rates by category
- Understand marketplace category rules
- Map all categories before sending products

#### Step 5.3 - Map product attributes

Configure attribute mappings for product specifications:

1. Access attribute mapping in connector settings.
2. Review required attributes for each category.
3. Map VTEX specifications to marketplace attributes.
4. Configure attribute value transformations if needed.
5. Handle custom attributes specific to the marketplace.

**Common attributes to map:**

- Brand
- Model
- Color
- Size
- Material
- Dimensions (weight, height, width, depth)
- Warranty information
- Age range
- Gender
- Technical specifications

#### Step 5.4 - Configure product variations

Set up how product variations (SKUs) are represented:

1. Define variation attributes (color, size, etc.).
2. Configure variation grouping rules.
3. Set primary variation for product display.
4. Configure variation-specific images.
5. Map variation values to marketplace standards.

**Example variation mapping:**

- VTEX size "G" → Marketplace size "L"
- VTEX voltage "110V" → Marketplace voltage "110 Volts"

### Step 6 - Sending products to the marketplace

For native connectors or partner solutions, products associated with the corresponding sales channel are sent automatically.

In custom integrations, you should:
- Implement product export using VTEX APIs.
- Handle Change Notification and SKU Suggestion flows.
- Process responses and retry failed products.

**Common synchronization issues:**

- Missing required attributes
- Invalid category mapping
- Image format or size issues
- Price below marketplace minimum
- Stock unavailable
- EAN code conflicts

For detailed information, see [Sending products to the marketplace](https://help.vtex.com/docs/tutorials/sending-products-to-the-marketplace).

### Step 7 - Configuring price divergence rules

Price divergence rules protect your store from processing orders with unexpected price differences between VTEX and the marketplace.

#### Step 7.1 - Understand price divergence

Price differences can occur due to:

- Synchronization delays
- Promotional pricing mismatches
- Currency conversion variations
- Marketplace-applied promotions
- System errors or bugs

#### Step 7.2 - Create price divergence rule

Configure acceptable price variance:

1. In the VTEX Admin, go to **Orders > Order authorization**.
2. Click the **Price divergence** tab.
3. Click `Create rule`.
4. Fill in the fields:

- **Rule name:** Descriptive name for the marketplace
- **Sales channel:** Select the marketplace trade policy
- **Divergence rate:** Maximum acceptable percentage difference
- **Minimum price:** Lowest acceptable order value
- **Maximum price:** Highest acceptable order value

5. Click `Save`.

**Recommended settings:**

- Small divergence: 5-10% for tight price control
- Medium divergence: 10-20% for flexibility
- Large divergence: 20%+ for dynamic pricing scenarios
