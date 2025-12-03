---
title: "Marketplace IN - Receiving Sellers"
slug: "marketplace-in"
hidden: false
excerpt: "Learn how to implement a marketplace that receives products from sellers."
createdAt: ""
updatedAt: ""
---

When your VTEX store acts as a marketplace and receives products from sellers, you're operating a **Marketplace IN** model. This guide covers the different approaches for integrating sellers into your marketplace.

## Types of Marketplace IN implementations

Marketplace IN supports three main approaches for integrating sellers:

### VTEX Seller

Integrate sellers that are already VTEX stores. These sellers operate on the VTEX platform and can be connected natively without additional development.

**Key characteristics:**
- Native integration with no custom connector development required
- Sellers already have VTEX accounts and infrastructure
- Seamless product synchronization and order management
- Direct access to VTEX APIs and features

**Best for:** Marketplaces that want to quickly onboard sellers who are already on the VTEX platform.

Learn more in [Marketplace overview](https://developers.vtex.com/docs/guides/marketplace-overview).

### External Seller

Integrate sellers that operate outside the VTEX platform. These sellers require custom connector development to integrate with your marketplace.

**Key characteristics:**
- Requires developing a custom connector
- Sellers operate on different platforms (e.g., Shopify, WooCommerce, custom systems)
- More complex integration process
- Full control over integration logic and data mapping

**Best for:** Marketplaces that need to integrate with sellers using non-VTEX platforms or custom ecommerce solutions.

Learn more in [External Seller Integration Guide](https://developers.vtex.com/docs/guides/external-seller-integration-guide).

### Seller Portal

Use the Seller Portal solution to onboard and manage sellers. The Seller Portal provides a streamlined interface for sellers to manage their products, orders, inventory, and performance metrics. This solution works for both VTEX and external sellers.

**Key characteristics:**
- Pre-built seller interface and management tools
- Works with both VTEX and external sellers
- Simplified onboarding process
- Built-in seller dashboard and analytics

**Best for:** Marketplaces that want a standardized, user-friendly solution for managing multiple sellers with minimal development effort.

Learn more in [Seller Portal](https://help.vtex.com/en/tutorial/seller-portal-primeiros-passos-para-o-marketplace--6ccErY3mCcfoW0qGXf167).

## Implementation steps

### Step 1 - Configure seller accounts

Seller accounts are essential for managing multiple sellers in your marketplace. Each seller needs to be configured with their own settings, including catalog permissions, payment terms, and fulfillment options.

To configure seller accounts, open a ticket with [VTEX Support](https://help.vtex.com/en/support), select the option Commercial and click Configure seller account. Learn more in [Managing sellers](https://help.vtex.com/en/tutorial/managing-sellers--tutorials_445).

When configuring seller accounts, ensure that:
- Seller information (name, contact, tax ID) is correctly entered
- Payment and commission settings are properly configured
- Catalog permissions and product approval workflows are set up
- Fulfillment options are defined

### Step 2 - Set up seller catalog integration

In a marketplace setup, sellers need to be able to add and manage their products. This can be done through:

- **Seller Portal:** Sellers can add products directly through the Seller Portal interface
- **Catalog API:** Sellers can integrate their systems using VTEX Catalog API
- **Product import:** Bulk product import via CSV or integration with seller's PIM/ERP

To enable seller catalog management, configure the appropriate permissions and workflows in the VTEX Admin under Marketplace > Sellers > Catalog Settings.

You can manage seller catalogs using the following API:

```bash
curl --location 'https://{accountName}.{environment}.com.br/api/catalog-seller/products' \
--header 'Content-Type: application/json' \
--header 'X-VTEX-API-AppKey: {appKey}' \
--header 'X-VTEX-API-AppToken: {appToken}'
```

Or following the instructions in the guide [Managing seller catalogs](https://developers.vtex.com/docs/guides/managing-seller-catalogs).

>⚠️ Ensure that product approval workflows are properly configured to maintain catalog quality. Products should be reviewed before being published to the marketplace.

### Step 3 - Configure order routing

Order routing determines how orders are distributed to sellers and how fulfillment is managed. Configure order routing rules based on:

- **Product ownership:** Orders automatically route to the seller who owns the product
- **Inventory availability:** Route to sellers with available inventory
- **Geographic location:** Route orders based on seller location and shipping capabilities
- **Seller capacity:** Consider seller order volume and fulfillment capacity

In the VTEX Admin, go to Marketplace > Settings > Order Routing.

Configure the routing rules that match your marketplace's fulfillment model.

>ℹ️ For multi-seller orders (products from different sellers), the marketplace can split orders or coordinate fulfillment across sellers.

### Step 4 - Set up payment and commission

Configure how payments are processed and how commissions are calculated and distributed:

1. In the VTEX Admin, go to Marketplace > Settings > Payments.
2. Configure payment gateway settings for marketplace transactions.
3. Set up commission rules based on product categories, seller tiers, or transaction value.
4. Define payment terms and settlement schedules for sellers.

Learn more in [Marketplace payments and commissions](https://help.vtex.com/en/tutorial/marketplace-payments--tutorials_446).

## Seller onboarding workflows

### For VTEX Sellers

1. **Invite the seller:** Use the Marketplace APIs to invite VTEX sellers to your marketplace
2. **Configure seller account:** Set up seller-specific settings, commissions, and permissions
3. **Product synchronization:** Sellers can start suggesting products from their catalog
4. **Catalog approval:** Review and approve seller products using VTEX Matcher or manual approval
5. **Go live:** Once approved, seller products become available in your marketplace

### For External Sellers

1. **Develop connector:** Build a custom connector to integrate with the external seller's platform
2. **Configure seller account:** Set up seller account in your VTEX marketplace
3. **Product mapping:** Map external seller's product data to your catalog structure
4. **Inventory synchronization:** Set up real-time or scheduled inventory updates
5. **Order management:** Configure order routing and fulfillment workflows
6. **Testing:** Thoroughly test the integration before going live

### For Seller Portal

1. **Invite seller lead:** Use the Seller Portal APIs to invite new sellers
2. **Seller acceptance:** Seller accepts the invitation and sets up their Seller Portal account
3. **Seller configuration:** Marketplace activates and configures the seller account
4. **Product onboarding:** Seller adds products through the Seller Portal interface
5. **Catalog approval:** Marketplace reviews and approves seller products
6. **Go live:** Seller products become available in the marketplace

## Catalog management

### Product suggestions and approval

Sellers send product suggestions to your marketplace. You can approve these suggestions manually or automatically:

- **Manual approval:** Review each product suggestion individually in the VTEX Admin
- **Automatic approval:** Use VTEX Matcher to automatically approve products based on matching scores
- **Hybrid approach:** Automatically approve high-confidence matches, manually review others

### Catalog quality control

Maintain catalog quality by:
- Setting up product approval workflows
- Defining minimum product information requirements
- Using VTEX Matcher to identify duplicate products
- Implementing catalog quality scoring
- Regular catalog audits and cleanup

## Order management

### Order routing

Configure how orders are distributed to sellers:
- Route orders to the seller who owns the product
- Consider inventory availability when routing
- Support multi-seller orders (products from different sellers)
- Handle order splitting when needed

### Fulfillment coordination

Coordinate fulfillment across multiple sellers:
- Track order status from each seller
- Manage split orders (products from different sellers)
- Handle returns and exchanges
- Coordinate shipping and delivery

## Commission and payment setup

### Commission structure

Define commission rules for your marketplace:
- Percentage-based commissions per category
- Fixed fee per transaction
- Tiered commission structures based on seller performance
- Commission rules per seller or seller group

### Payment processing

Configure payment collection and distribution:
- Marketplace collects payments from customers
- Payments are distributed to sellers based on commission rules
- Define payment settlement schedules
- Handle refunds and chargebacks

## Best practices

- **Seller onboarding:** Create clear documentation and processes for seller onboarding
- **Catalog quality:** Implement strict approval workflows to maintain catalog quality
- **Communication:** Establish clear communication channels with sellers
- **Performance monitoring:** Track seller performance metrics and provide feedback
- **Support:** Provide adequate support for sellers using your marketplace
- **Scalability:** Design your marketplace architecture to handle growth

## Next steps

<WhatsNextCard
title="Implementing Marketplaces"
description="Return to the main marketplace implementation guide."
linkTo="./implementing-marketplaces"
linkTitle="See more"
/>

<WhatsNextCard
title="External Seller Integration Guide"
description="Learn how to integrate external sellers into your marketplace."
linkTo="https://developers.vtex.com/docs/guides/external-seller-integration-guide"
linkTitle="See more"
/>

<WhatsNextCard
title="Managing seller catalogs"
description="Understand how to manage product catalogs from multiple sellers."
linkTo="https://developers.vtex.com/docs/guides/managing-seller-catalogs"
linkTitle="See more"
/>

<WhatsNextCard
title="Marketplace order management"
description="Learn how to handle orders from multiple sellers and coordinate fulfillment."
linkTo="https://developers.vtex.com/docs/guides/marketplace-order-management"
linkTitle="See more"
/>

