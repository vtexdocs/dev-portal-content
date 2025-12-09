---
title: "Acting as a Seller"
slug: "marketplace-out"
hidden: false
excerpt: "Learn how to sell your products on external marketplaces."
createdAt: ""
updatedAt: ""
---

When your VTEX store sells products on other marketplaces (external to your store), you're **acting as a seller**. This guide covers how to integrate your VTEX store with external marketplaces to expand your sales channels.

## Planning your seller operation

Before implementing, answer these questions to plan your marketplace operation:

**Target marketplaces:**
- Which external marketplaces do you want to sell on?
- Do these marketplaces have native VTEX connectors?
- If not, can you develop custom connectors?
- What are the marketplace requirements (catalog format, policies, fees)?

**Catalog and inventory:**
- How will you manage inventory across multiple channels?
- Do you need different product information per marketplace?
- How will you handle out-of-stock scenarios across channels?

**Pricing and operations:**
- How will you handle different pricing strategies per marketplace?
- How do marketplace fees and commissions affect your pricing?
- Can you fulfill orders from different marketplaces efficiently?
- How will you manage returns and refunds from external marketplaces?

## Types of marketplace integrations

You can sell on external marketplaces using two main approaches:

### Native Connectors

Sell your products in external marketplaces using VTEX's pre-built native connectors. These connectors are maintained by VTEX and support major marketplaces like Amazon, Mercado Libre, B2W, Via Varejo, Magazine Luiza, and others.

**Key characteristics:**
- Pre-built and maintained by VTEX
- No custom development required
- Regular updates and support from VTEX
- Optimized for specific marketplace requirements
- Quick setup and configuration

**Supported marketplaces:**
- Amazon
- Mercado Libre
- B2W
- Via Varejo
- Magazine Luiza
- And other major marketplaces

**Best for:** Sellers who want to quickly start selling on major marketplaces without development effort.

Learn more in [Marketplace overview](https://developers.vtex.com/docs/guides/marketplace-overview).

### External Connectors

Sell your products in external marketplaces that don't have native VTEX connectors. This requires developing a custom connector to integrate with the external marketplace's APIs.

**Key characteristics:**
- Custom development required
- Full control over integration logic
- Can integrate with any marketplace that provides APIs
- More flexible but requires maintenance
- Requires understanding of marketplace APIs

**Best for:** Sellers who need to integrate with marketplaces that don't have native VTEX connectors, or who need custom integration logic.

Learn more in [External Marketplace Integration Guide](https://developers.vtex.com/docs/guides/external-marketplace-integration-guide).

## Implementation steps

### Step 1 - Choose your marketplace connector

Determine which approach fits your needs:

- **Native Connector:** If the marketplace has a native VTEX connector, use it for the fastest setup
- **External Connector:** If no native connector exists, you'll need to develop a custom connector

### Step 2 - Configure marketplace connection

#### For Native Connectors

1. **Access the connector:** Navigate to the marketplace connector in VTEX Admin
2. **Authenticate:** Connect your marketplace account using OAuth or API credentials
3. **Configure settings:** Set up product mapping, pricing rules, and inventory sync settings
4. **Test connection:** Verify the connection and test product synchronization

#### For External Connectors

1. **Develop connector:** Build a custom connector using VTEX IO or external integration
2. **Implement APIs:** Connect to the marketplace's APIs for products, inventory, orders
3. **Map data:** Map your catalog structure to the marketplace's requirements
4. **Test integration:** Thoroughly test all integration points before going live

### Step 3 - Set up product synchronization

Configure how your products are synchronized with the external marketplace:

- **Product mapping:** Map your catalog structure to the marketplace's product format
- **Category mapping:** Align your categories with marketplace categories
- **Attribute mapping:** Map product attributes and specifications
- **Image synchronization:** Ensure product images are properly formatted and uploaded
- **Pricing rules:** Define pricing strategies (fixed markup, percentage, etc.)

### Step 4 - Configure inventory synchronization

Set up real-time or scheduled inventory updates:

- **Real-time sync:** Update inventory immediately when changes occur
- **Scheduled sync:** Sync inventory at regular intervals (hourly, daily, etc.)
- **Inventory rules:** Define how inventory is allocated across channels
- **Stock management:** Handle overselling and inventory reservations

### Step 5 - Configure order management

Set up order processing workflows:

- **Order import:** Configure how orders are imported from the marketplace
- **Order routing:** Route orders to appropriate fulfillment centers
- **Order status sync:** Keep order status synchronized between systems
- **Shipping updates:** Send tracking information back to the marketplace
- **Returns handling:** Process returns and refunds from marketplace orders

### Step 6 - Set up payment and fees

Configure payment processing and marketplace fees:

- **Marketplace fees:** Understand and account for marketplace commission fees
- **Payment processing:** Configure how payments are received from the marketplace
- **Settlement:** Set up payment settlement schedules
- **Fee tracking:** Track and report marketplace fees for accounting

## Product catalog management

### Offer Management

VTEX's Offer Management tool helps you monitor and manage your product listings (offers) across external marketplaces. This tool allows you to:

- **Track listing status:** Monitor which products are successfully listed on each marketplace
- **Identify errors:** Quickly spot and fix listing errors or rejections
- **Manage inventory:** View inventory levels across all channels
- **Update pricing:** Adjust prices for different marketplaces
- **Performance monitoring:** Track sales and performance metrics per marketplace

Access Offer Management in VTEX Admin under **Marketplace > Connections > Offer Management**.

Learn more in [Sent Offers Integration Guide](https://developers.vtex.com/docs/guides/sent-offers-integration-guide-connectors).

### Product listing

Ensure your products meet marketplace requirements:

- **Product information:** Complete product descriptions, specifications, and attributes
- **Images:** High-quality product images that meet marketplace standards
- **Categories:** Correct category assignment for better discoverability
- **SEO optimization:** Optimize product titles and descriptions for marketplace search

### Catalog synchronization

Keep your catalog synchronized with the marketplace:

- **New products:** Automatically or manually add new products to the marketplace
- **Product updates:** Sync price, inventory, and product information changes
- **Product removal:** Remove products that are no longer available
- **Bulk operations:** Use bulk import/export for large catalog updates

### Inventory management

Manage inventory across multiple channels:

- **Multi-channel inventory:** Track inventory across your store and marketplaces
- **Inventory allocation:** Allocate inventory to different channels
- **Stock synchronization:** Keep stock levels synchronized in real-time
- **Overselling prevention:** Prevent selling more than available inventory

## Order management

### Order processing workflow

1. **Order received:** Order is imported from the marketplace
2. **Order validation:** Validate order details and inventory availability
3. **Order routing:** Route order to appropriate fulfillment center
4. **Fulfillment:** Process and ship the order
5. **Tracking update:** Send tracking information to the marketplace
6. **Order completion:** Mark order as completed in both systems

### Order status synchronization

Keep order status synchronized:

- **Pending:** Order received but not yet processed
- **Processing:** Order is being prepared for shipment
- **Shipped:** Order has been shipped with tracking information
- **Delivered:** Order has been delivered to customer
- **Cancelled:** Order has been cancelled
- **Returned:** Order has been returned

### Returns and refunds

Handle returns and refunds:

- **Return requests:** Process return requests from the marketplace
- **Refund processing:** Process refunds according to marketplace policies
- **Return tracking:** Track returned items and update inventory
- **Dispute resolution:** Handle disputes and customer service issues

## Pricing strategies

### Pricing rules

Define pricing strategies for marketplace listings:

- **Fixed markup:** Add a fixed amount to your base price
- **Percentage markup:** Add a percentage to your base price
- **Marketplace-specific pricing:** Set different prices for different marketplaces
- **Dynamic pricing:** Adjust prices based on competition or demand

### Fee calculation

Account for marketplace fees in your pricing:

- **Commission fees:** Understand marketplace commission structures
- **Transaction fees:** Account for payment processing fees
- **Fulfillment fees:** Include shipping and fulfillment costs
- **Total cost calculation:** Calculate total costs to determine profitability

## Best practices

- **Catalog quality:** Maintain high-quality product listings with complete information
- **Inventory accuracy:** Keep inventory synchronized to avoid overselling
- **Order fulfillment:** Process orders quickly to maintain good seller ratings
- **Customer service:** Provide excellent customer service for marketplace orders
- **Performance monitoring:** Track sales performance and optimize listings
- **Compliance:** Ensure compliance with marketplace policies and regulations
- **Testing:** Thoroughly test integrations before going live
- **Documentation:** Maintain documentation of integration configurations

## Troubleshooting

### Common issues

- **Product sync failures:** Check API credentials and product data format
- **Inventory discrepancies:** Verify inventory sync settings and timing
- **Order import errors:** Check order format and validation rules
- **Payment issues:** Verify payment gateway configurations
- **API rate limits:** Implement proper rate limiting and retry logic

### Support resources

- [Marketplace overview](https://developers.vtex.com/docs/guides/marketplace-overview)
- [External Marketplace Integration Guide](https://developers.vtex.com/docs/guides/external-marketplace-integration-guide)
- [VTEX Support](https://help.vtex.com/en/support)

## Next steps

<WhatsNextCard
title="Implementing Marketplaces"
description="Return to the main marketplace implementation guide."
linkTo="./implementing-marketplaces"
linkTitle="See more"
/>

<WhatsNextCard
title="External Marketplace Integration Guide"
description="Learn how to develop custom connectors for external marketplaces."
linkTo="https://developers.vtex.com/docs/guides/external-marketplace-integration-guide"
linkTitle="See more"
/>

<WhatsNextCard
title="Offer Management"
description="Learn how to manage offers sent to external marketplaces."
linkTo="https://developers.vtex.com/docs/guides/sent-offers-integration-guide-connectors"
linkTitle="See more"
/>

<WhatsNextCard
title="Marketplace overview"
description="Learn more about marketplace architecture and integration options."
linkTo="https://developers.vtex.com/docs/guides/marketplace-overview"
linkTitle="See more"
/>

