---
title: 'Integrating VTEX stores'
id: [to-be-assigned]
status: DRAFT
createdAt: 2026-02-20T00:00:00.000Z
updatedAt: 2026-02-20T00:00:00.000Z
contentType: guide
productTeam: Channels
locale: en
---

Integrating VTEX stores enables collaborative commerce where stores can act both as marketplaces and sellers within the VTEX ecosystem. This guide shows you how to establish connections between VTEX stores, configure the necessary settings, and manage the integration to expand your sales channels or product assortment.

In this guide, you will learn how to:

- Configure a VTEX marketplace to receive products from VTEX sellers
- Set up a VTEX seller to sell products on VTEX marketplaces
- Manage catalog mapping and product synchronization
- Handle order fulfillment and payment processing

## Before you begin

Before starting the integration between VTEX stores, ensure the following requirements are met:

**For marketplaces:**

- Defined trade policies for your sales channels.
- Admin access to configure seller management.
- Agreement with sellers on commissions, delivery policies, and return policies.

**For sellers:**

- Admin access to configure affiliates
- Defined trade policies for marketplace integrations.
- [Sponsor user (owner)](/en/docs/tracks/what-is-the-master-user) access for database reindexing.

**Shared requirements:**

- Understanding of [marketplace strategies at VTEX](/en/docs/tutorials/marketplace-strategies-at-vtex)
- Familiarity with [trade policies](/en/docs/tutorials/how-trade-policies-work)
- Knowledge of [information shared between marketplace and seller](/en/docs/tutorials/shared-information-between-a-marketplace-and-a-seller-on-vtex)

> ℹ️ To discover new partners within the VTEX ecosystem, use [Marketplaces and Integrations](/en/docs/tutorials/marketplaces-and-integrations), which facilitates identification and communication between marketplaces and sellers.

## Understanding the integration architecture

The VTEX architecture allows stores to operate both as marketplaces and sellers, creating a flexible collaborative commerce model. When integrating VTEX stores:

- **Marketplace:** The environment where products are displayed and sold to customers
- **Seller:** The store that owns the inventory and handles order fulfillment
- **Trade policy:** Groups configurations for catalog, pricing, promotions, logistics, customer segmentation, and payments

The integration between VTEX stores involves bidirectional communication:

1. The seller sends product information, pricing, and inventory to the marketplace
2. The marketplace receives orders and forwards them to the seller
3. The seller processes orders and updates order status
4. Both parties share information about shipping, invoicing, and delivery

## Step 1 - Configure the marketplace

This section guides marketplace operators through the necessary configurations to receive and sell products from VTEX sellers.

### Define trade policies

[Trade policies](/en/docs/tutorials/how-trade-policies-work) determine the product assortment, prices, payments, promotions, customer segmentation, and shipping strategy for your marketplace.

To define trade policies for your marketplace:

1. Evaluate if you need different configurations for sellers in your marketplace. If all sellers use the same configurations, use your default trade policy.
2. If you need specific settings, [create a new trade policy](/en/docs/tutorials/creating-a-trade-policy) for marketplace operations.
3. Configure the trade policy with the appropriate settings for catalog, pricing, promotions, and logistics.

> ℹ️ The same trade policy can be used to integrate with multiple sellers. [Requesting additional trade policies](/en/docs/tutorials/requesting-an-additional-trade-policy) to integrate with other VTEX stores is free of charge.

### Add sellers to your marketplace

After defining trade policies, add VTEX sellers to your marketplace:

1. In the VTEX Admin, go to **Marketplace > Management**.
2. Click `Add Seller`.
3. Select **VTEX Seller** as the integration type.
4. Complete the required fields:

**Integration section:**

- **VTEX seller's account:** Enter the [account name](/en/docs/tutorials/what-is-an-account-name) of the seller.
- **Affiliate ID:** Enter the three-consonant identification code created by the seller. This code must match the affiliate created in the seller's VTEX Admin.
- **Pause seller after creation:** Select this checkbox to create the seller in `Paused` status, allowing you to catalog offers and test before making the seller available on your storefront.

**Basic seller information:**

- **Seller name:** Name of the seller store that will appear in your marketplace.
- **Seller ID:** Internal identification code for the seller. Use lowercase letters without spaces or special characters, up to 50 characters.
- **Seller groups:** Keywords to organize sellers into groups for easier management and filtering.

**Trade agreements:**

- **Marketplace trade policies:** Select the trade policies that apply to the seller.
- **Product commissioning:** Define the commission percentage that applies to the seller's products.
- **Shipping commissioning:** Define the commission percentage for shipping costs.
- **Add commissioning by category:** Configure specific commission percentages for selected product categories.

**Additional information:**

- **Add logo:** Upload the seller's logo (PNG, JPG, or JPEG, up to 500kb).
- **CNPJ (Company registration number):** Seller's company registration number.
- **Email:** Email address of the responsible manager.
- **Description:** Commercial description of the seller that can appear in the marketplace storefront.
- **Delivery policy:** Delivery policy agreed upon between marketplace and seller.
- **Exchanges and returns:** Exchange and return policy details.
- **Privacy and security policy:** Security policy applicable to the seller's products.

5. Click `Save` to add the seller to your marketplace.

For detailed information on adding sellers, see [Adding a seller](/en/docs/tutorials/adding-a-seller).

### Step 1.3 - Configure seller visibility

Determine how sellers appear in the shopping experience:

**Identifiable sellers:**

- Visible on the marketplace storefront
- Customers can choose sellers in the buy box
- Suitable for third-party sellers or partners you want to showcase

**White label sellers:**

- Not visible during the shopping experience
- Automatically selected by the checkout system
- Typically used for franchise accounts or distribution centers

> ℹ️ To add white label sellers, this model must be included in your contract with VTEX. Submit a request to [add a franchise account](/en/docs/tutorials/what-is-a-franchise-account) through VTEX Support.

### Step 1.4 - Configure the storefront

Configure your marketplace storefront to display seller information during the shopping experience.

**For Legacy CMS Portal stores:**

Add the following controls to your ecommerce templates:

- `<vtex.cmc:sellerDescription />`: Displays the seller's name and logo for the product
- `<vtex.cmc:SellerOptions />`: Shows sellers offering the product, prices, and installment options
- `<vtex.cmc:sellerInfo />`: Displays detailed seller information on the seller details page

**For VTEX IO stores:**

Install the [Seller Selector](https://github.com/vtex-apps/seller-selector) app to:

- Display the number of sellers offering each product
- Allow customers to compare prices from different sellers
- Enable customers to add products from their preferred seller to the cart

For more information, see [Configuring a VTEX marketplace](/en/docs/tutorials/configuring-vtex-marketplace).

### Step 1.5 - Configure payments

Configure payment processing for your marketplace. There are different scenarios for payment processing in VTEX marketplaces:

- **Marketplace processes payments:** The marketplace receives payments and distributes the amounts to sellers according to commission agreements.
- **Seller processes payments:** Each seller receives payments directly for their orders.
- **Split payment:** Payment is divided between marketplace and seller according to predefined rules.

For detailed information on payment configurations, see [Payments in VTEX Marketplace](/en/docs/tutorials/payments-in-vtex-marketplaces).

## Step 2 - Configure the seller

This section guides sellers through the configurations necessary to sell products on VTEX marketplaces.

### Step 2.1 - Define trade policies

Determine the trade policy configuration for your marketplace integration:

1. Evaluate if you need specific configurations for the marketplace integration or if you can use your default trade policy.
2. If specific settings are required, [create a trade policy for the marketplace](/en/tutorial/configurando-a-politica-comercial-para-marketplace/).
3. Configure the trade policy with the appropriate settings for product assortment, pricing, promotions, and logistics.

> ℹ️ The same trade policy can be used to integrate with multiple marketplaces. [Requesting additional trade policies](/en/docs/tutorials/requesting-an-additional-trade-policy) to integrate with other VTEX stores is free of charge.

**Managing product assortment:**

- Use trade policies to control which products are sent to the marketplace
- Avoid using [collections](/en/docs/tutorials/creating-a-product-collection) for product management, as it adds complexity

**Configuring promotions:**

- You don't need a marketplace-specific trade policy just for promotions
- Segment promotions using the [affiliate](/en/docs/tutorials/what-is-an-affiliate)
- See [Configuring promotions for marketplaces](/en/docs/tutorials/configuring-promotions-for-marketplaces) for more information

### Step 2.2 - Create an affiliate ID

The [affiliate](/en/docs/tutorials/what-is-an-affiliate) is the code that identifies the marketplace where your products will be sold. Each marketplace must have a unique affiliate.

To create an affiliate:

1. In the VTEX Admin, go to **Orders > Orders management > Settings**.
2. In the **Affiliates** tab, click `+ New Affiliate`.
3. Fill in the following fields:

- **Name:** Descriptive name for the marketplace
- **ID:** Three-consonant identifier (repeated consonants are allowed, vowels are not). Example: MKT, FRN, or VTX
- **Trade Policy:** Select the trade policy you want to use for this marketplace
- **Email for notifications:** Email address to receive notifications about the integration
- **Search Endpoint:** URL where the marketplace will query product information (filled automatically for VTEX marketplaces)

4. Click `Save` to create the affiliate.

After creating the affiliate, provide the affiliate ID to the marketplace operator. The marketplace will use this ID when adding your store as a seller.

For detailed instructions, see [Configuring affiliates](/en/docs/tutorials/configuring-affiliates).

### Step 2.3 - Reindex the database

After the marketplace adds your store as a seller, send your product catalog by reindexing the database. This process:

- Prepares SKU and product information
- Sends catalog, price, and inventory data to the marketplace
- Updates the marketplace with your current product assortment

To reindex the database:

1. Open your browser and access the following URL, replacing `{storename}` with your store's account name:

`{storename}.vtexcommercestable.com.br/admin/Site/FullCleanUp.aspx`

2. Click the `Reindex database` button to start the process.
3. Monitor the reindexing progress in the VTEX Admin at **Catalog > Reports**.

> ℹ️ Only the [sponsor user (owner)](/en/docs/tracks/what-is-the-master-user) has permission to reindex the database. During reindexing, products remain available for sale on your store while being queued for information updates.

**Checking the index:**

Verify if a specific SKU was indexed correctly to the integration trade policy:

1. In the VTEX Admin, go to **Catalog > Products and SKUs**.
2. Click the down arrow next to the **CHANGE** button.
3. Select the `Indexed Info` option.
4. Verify that the trade policy number used in the marketplace integration appears in the SKU information.

## Step 3 - Map catalog architecture

After the seller sends products to the marketplace, the marketplace must map the seller's catalog to match its own structure. This ensures products are properly categorized and displayed on the marketplace.

### Step 3.1 - Map categories and brands

The marketplace must map the seller's categories and brands to equivalent items in its catalog:

1. In the VTEX Admin, go to **Marketplace > Sellers > Categories and Brands**.
2. Select the seller whose catalog you want to map.
3. For each unmapped category and brand, select the corresponding category or brand from your marketplace catalog.
4. Create new categories or brands in your catalog if necessary before mapping.
5. Click `Save` to confirm the mappings.

### Step 3.2 - Map product specifications

Map product specifications to ensure accurate product information:

1. In the mapping interface, review the seller's product specifications.
2. Match each specification to the equivalent specification in your catalog.
3. Create new specifications if required for the seller's products.
4. Verify that all mandatory specifications are properly mapped.

For detailed mapping instructions, see [Mapping categories and brands for the marketplace](/en/docs/tutorials/mapping-categories-and-brands-for-the-marketplace).

## Step 4 - Approve and catalog seller products

After mapping the catalog architecture, the marketplace must approve and catalog the seller's products before they become available to customers.

### Step 4.1 - Review received SKUs

Review the SKUs sent by the seller:

1. In the VTEX Admin, go to **Marketplace > Sellers > Received SKUs**.
2. Filter by the seller to view their submitted SKUs.
3. Review product information, images, descriptions, and specifications.
4. Verify pricing and inventory information.

### Step 4.2 - Approve SKUs

Approve SKUs to make them available on your marketplace:

1. Select the SKUs you want to approve.
2. Click `Approve` to add them to your marketplace catalog.
3. The approved SKUs will be associated with the mapped categories, brands, and specifications.

> ℹ️ You can set up automatic approval for trusted sellers to streamline the cataloging process. See [Manual SKU cataloging](/en/docs/tutorials/manual-sku-cataloging) for more information.

### Step 4.3 - Verify product availability

After approval, verify that products appear correctly on your marketplace:

1. Check the marketplace storefront to confirm products are visible.
2. Verify that product information, images, and prices display correctly.
3. Test the purchase flow to ensure orders can be placed successfully.
4. Confirm that seller information appears correctly when configured to be visible.

## Step 5 - Manage ongoing integration

After the initial integration setup, maintain and optimize the seller-marketplace relationship.

### Step 5.1 - Monitor product synchronization

Keep product information synchronized between seller and marketplace:

**Price updates:**

- The seller's price changes automatically update on the marketplace
- Monitor the [Prices](/en/docs/tutorials/prices-module-overview) module for synchronization status

**Inventory updates:**

- Inventory levels sync automatically from seller to marketplace
- Check the [Inventory management](/en/docs/tutorials/managing-stock-items) section for current stock levels

**Catalog changes:**

- New products require reindexing or manual updates
- Product modifications sync according to the affiliate configuration

### Step 5.2 - Manage orders

Handle orders placed on the marketplace for seller products:

**Order flow:**

1. Customer places an order on the marketplace
2. Marketplace receives the order and forwards it to the seller
3. Seller receives notification through the affiliate
4. Seller prepares and ships the order
5. Seller updates order status (invoiced, shipped, delivered)
6. Marketplace updates customer with order status

**Order management:**

- Sellers manage orders in **Orders > All Orders**
- Marketplaces monitor seller orders in **Marketplace > Sellers > Orders**
- Both parties can access order details and status updates

For more information, see [Order flow](/en/docs/tracks/order-flow).

### Step 5.3 - Monitor integration health

Regularly review integration performance:

**Key metrics to monitor:**

- Product synchronization rate and errors
- Order processing time and fulfillment rate
- Customer feedback and return rates
- Commission accuracy and payment reconciliation

**Troubleshooting common issues:**

- **Products not appearing:** Verify indexing, trade policy settings, and catalog mapping
- **Inventory discrepancies:** Check inventory synchronization and update frequency
- **Order processing delays:** Review notification settings and affiliate configuration
- **Pricing errors:** Confirm trade policy pricing rules and commission calculations

### Step 5.4 - Optimize seller performance

Work with sellers to improve marketplace performance:

- Review and optimize product information quality
- Enhance product images and descriptions
- Adjust pricing strategies based on competition
- Improve delivery times and fulfillment processes
- Analyze sales data to identify growth opportunities

## Managing multiple seller integrations

When integrating multiple VTEX sellers with your marketplace, consider the following strategies:

### Organizing sellers

Use seller groups to organize and manage multiple sellers:

- Group sellers by category, region, or business model
- Apply specific rules or promotions to seller groups
- Filter and monitor sellers by group in the management interface

### Scaling integration

Efficiently manage large numbers of seller integrations:

- Standardize trade policies across similar sellers
- Automate SKU approval for trusted sellers
- Use APIs for bulk operations and automated processes
- Implement monitoring tools for integration health

### Setting seller priorities

Configure seller selection rules to optimize fulfillment:

- Use the [White label sellers selection algorithm](/en/docs/tutorials/white-label-sellers-selection) to prioritize sellers
- Consider factors like delivery time, location, and inventory availability
- Configure comprehensive sellers for wide geographic coverage

For more information, see [Actions for VTEX marketplace operation](/en/docs/tutorials/actions-for-vtex-marketplace-operation).

## Integrating with Seller Portal

For sellers who don't have an existing VTEX account or ecommerce platform, consider using [Seller Portal](/en/docs/tutorials/how-to-set-up-your-store-on-seller-portal):

**Benefits of Seller Portal:**

- Quick onboarding for new sellers
- Simplified product management interface
- Integrated with marketplace operations
- Lower entry barriers for small sellers

**Inviting sellers to Seller Portal:**

1. Ensure Seller Portal is activated for your marketplace (contact your VTEX CSM)
2. Follow the instructions in [Marketplace invited sellers](/en/docs/tutorials/marketplace-invited-sellers)
3. Guide sellers through the onboarding process
4. Review and approve seller products

## Advanced integration scenarios

### Cross-border integration

When integrating VTEX stores across different countries:

- Configure appropriate trade policies for different regions
- Set up international shipping and logistics
- Handle currency conversion and international payments
- Comply with local tax and regulatory requirements

### White label seller integration

For franchise accounts or distribution centers:

- Ensure white label seller model is in your contract
- Request franchise account creation through VTEX Support
- Configure automatic seller selection algorithms
- Set up regional inventory distribution

### Hybrid marketplace models

Combine selling your own products with seller products:

- Configure your store as both seller and marketplace
- Use trade policies to separate own products from seller products
- Manage inventory and fulfillment for both channels
- Optimize the customer experience with unified product display

## Best practices

Follow these best practices for successful VTEX store integration:

**For marketplaces:**

- Establish clear policies and commission structures before integration
- Provide sellers with detailed onboarding documentation
- Monitor seller performance and provide feedback
- Maintain consistent product data quality standards
- Respond promptly to seller questions and issues

**For sellers:**

- Maintain accurate and up-to-date product information
- Keep inventory levels synchronized in real-time
- Process orders promptly and update order status
- Meet agreed delivery times and service levels
- Communicate proactively with marketplace operators

**For both parties:**

- Document integration processes and troubleshooting steps
- Schedule regular reviews to optimize performance
- Use analytics to identify improvement opportunities
- Stay informed about VTEX platform updates
- Maintain open communication channels

## Next steps

After completing the integration between VTEX stores:

1. **Test the integration:** Place test orders to verify the complete flow from product display to order fulfillment.
2. **Train teams:** Ensure both marketplace and seller teams understand their responsibilities and processes.
3. **Launch gradually:** Consider a soft launch with limited products to identify and resolve issues.
4. **Monitor performance:** Track key metrics and address any issues promptly.
5. **Optimize continuously:** Regularly review and improve integration processes based on performance data.

## Learn more

- [Marketplace strategies at VTEX](/en/docs/tutorials/marketplace-strategies-at-vtex)
- [Choosing between standard account, franchise account or Seller Portal](/en/docs/tutorials/choosing-between-standard-account-franchise-account-or-seller-portal)
- [Shared information between a marketplace and a seller on VTEX](/en/docs/tutorials/shared-information-between-a-marketplace-and-a-seller-on-vtex)
- [Configuring a VTEX marketplace](/en/docs/tutorials/configuring-vtex-marketplace)
- [Configuring a seller on VTEX marketplace](/en/docs/tutorials/configuring-a-seller-on-vtex-marketplace)
- [Actions for VTEX marketplace operation](/en/docs/tutorials/actions-for-vtex-marketplace-operation)
- [External Seller Integration Guide](https://developers.vtex.com/vtex-rest-api/docs/external-seller-integration-guide)
