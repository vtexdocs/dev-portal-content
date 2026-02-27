---
title: 'Integrating with external marketplaces'
hidden: false
excerpt: ""
createdAt: 2026-02-20T00:00:00.000Z
---

Integrating your VTEX store with external marketplaces enables you to expand your sales channels, reach new customers, and increase brand visibility. This guide shows you how to connect your VTEX store as a seller to external marketplaces—those not hosted on the VTEX platform—through connectors, APIs, or custom integrations.

In this guide, you will learn how to:

- Understand external marketplace integration architecture
- Configure your VTEX store as a seller for external marketplaces
- Implement product catalog synchronization
- Manage orders received from external marketplaces
- Handle pricing, inventory, and fulfillment operations

## Before you begin

Before integrating your VTEX store with external marketplaces, ensure the following requirements are met:

**For VTEX sellers:**

- Admin access to your VTEX store
- Products in your catalog ready to sell
- Understanding of [trade policies](/en/docs/tutorials/how-trade-policies-work)
- Familiarity with [marketplace strategies at VTEX](/en/docs/tutorials/marketplace-strategies-at-vtex)
- Configured logistics for order fulfillment
- Payment processing capabilities

**For external marketplaces:**

- Account created on the target marketplace
- Understanding of marketplace requirements and policies
- Access to marketplace seller portal or admin panel
- Knowledge of marketplace commission structure
- Approved seller status (if applicable)

**Integration requirements:**

- Defined [trade policy](/en/docs/tutorials/how-trade-policies-work) for the marketplace
- [Affiliate](/en/docs/tutorials/what-is-an-affiliate) configuration in VTEX
- Understanding of the marketplace's technical requirements
- Connector availability or custom integration capability

> ℹ️ VTEX offers native connectors for several major marketplaces. Check the [list of available integrations](/en/docs/tutorials/marketplace-strategies-at-vtex) to see if a connector exists for your target marketplace.

## Understanding the integration architecture

External marketplace integration establishes a connection between your VTEX store (as a seller) and marketplaces hosted on external platforms. This architecture enables you to sell on multiple channels while managing everything from your VTEX Admin.

### Integration types

**Native connectors:**

- Pre-built integrations developed by VTEX
- Available for major marketplaces (Amazon, Mercado Libre, etc.)
- Simplified configuration through VTEX Admin
- Maintained and updated by VTEX
- Recommended for supported marketplaces

**Certified partner connectors:**

- Integrations developed by certified VTEX partners
- Available through the VTEX App Store
- Specialized solutions for specific marketplaces
- Support provided by partner companies
- May include additional features or customizations

**Custom connectors:**

- Developed specifically for unsupported marketplaces
- Requires technical development resources
- Uses VTEX APIs and marketplace APIs
- Full control over integration logic
- Ideal for unique or regional marketplaces

### Communication flow

The integration involves bidirectional communication between your VTEX store and the external marketplace:

**From VTEX to marketplace:**

1. Product catalog synchronization
2. Price and inventory updates
3. Product availability changes
4. SKU modifications
5. Order status updates
6. Invoice and tracking information

**From marketplace to VTEX:**

1. Customer orders
2. Order cancellation requests
3. Return requests
4. Customer questions or messages
5. Integration status notifications

### Business considerations

Before technical integration, evaluate:

- **Commission structure:** Percentage rates charged by the marketplace
- **Product requirements:** Categories allowed, quality standards, restrictions
- **Delivery expectations:** Shipping times, methods, and geographic coverage
- **Return policies:** Who handles returns and associated costs
- **Brand positioning:** How your products will be displayed
- **Competition:** Other sellers offering similar products
- **Marketplace reputation:** Customer trust and traffic levels

## Step 1 - Choose your integration method

Select the most appropriate integration method based on the marketplace and your technical capabilities.

### Step 1.1 - Check for native connectors

Verify if VTEX offers a native connector for your target marketplace:

1. In the VTEX Admin, go to **Marketplace > Connections**.
2. Browse available connectors or search for your target marketplace.
3. Review connector features and requirements.
4. Check if the connector supports your business needs.

**Available native connectors include:**

- Amazon
- Mercado Libre
- Magazine Luiza (Brazil)
- Carrefour
- Netshoes
- Dafiti
- Google Shopping
- Facebook
- And others

> ℹ️ For the complete list of available connectors, see [Marketplace strategies at VTEX](/en/docs/tutorials/marketplace-strategies-at-vtex).

### Step 1.2 - Explore certified partner solutions

If no native connector exists, check for certified partner solutions:

1. Visit the [VTEX App Store](https://apps.vtex.com/).
2. Search for marketplace integration apps.
3. Review app documentation and features.
4. Check partner reviews and support availability.
5. Evaluate pricing and licensing terms.

### Step 1.3 - Consider custom development

For unsupported marketplaces, evaluate custom connector development:

**When to develop custom connectors:**

- No native or certified connector exists
- Marketplace has specific technical requirements
- Integration requires unique business logic
- Volume justifies development investment

**Development resources:**

- [External Marketplace Integration Guide](https://developers.vtex.com/vtex-developer-docs/docs/external-marketplace-integration-guide)
- [Integration app template](https://developers.vtex.com/docs/guides/external-marketplace-integration-app-template)
- VTEX REST API documentation
- Partner developer support

## Step 2 - Configure trade policies

Trade policies control which products, prices, and conditions apply to each sales channel, including external marketplaces.

### Step 2.1 - Evaluate trade policy needs

Determine if you need a dedicated trade policy for the marketplace:

**Create a new trade policy when:**

- Offering a different product assortment
- Setting specific prices for the marketplace
- Applying unique promotions
- Using different shipping strategies
- Configuring marketplace-specific payment methods

**Use existing trade policy when:**

- Selling the same products with identical conditions
- Maintaining consistent pricing across channels
- No need for marketplace-specific configurations

### Step 2.2 - Create a marketplace trade policy

If needed, create a dedicated trade policy:

1. In the VTEX Admin, go to **Store Settings > Channels > Trade Policies**.
2. Click `Create Trade Policy`.
3. Fill in the following fields:

- **Name:** Descriptive name (e.g., "Amazon US" or "Mercado Libre Brazil")
- **Currency:** Currency used for the marketplace
- **Locale:** Primary language and region
- **Time zone:** Marketplace operating time zone

4. Click `Save` to create the trade policy.

> ℹ️ [Requesting additional trade policies](/en/docs/tutorials/requesting-an-additional-trade-policy) for marketplace integrations may incur a monthly fee. A single trade policy can be used for multiple marketplaces if configurations are identical.

### Step 2.3 - Configure trade policy settings

After creating the trade policy, configure specific settings:

**Catalog settings:**

1. Go to **Catalog > Products and SKUs**.
2. Associate products with the marketplace trade policy.
3. Define product collections for targeted assortments.
4. Set product visibility and availability.

**Pricing settings:**

1. Go to **Prices > Price list**.
2. Configure base prices for the trade policy.
3. Set up price rules specific to the marketplace.
4. Configure fixed prices when necessary.

**Promotion settings:**

1. Go to **Promotions > Promotions**.
2. Create marketplace-specific promotions.
3. Configure promotion conditions and restrictions.
4. Set promotion validity periods.

**Logistics settings:**

1. Go to **Inventory & shipping > Shipping strategy**.
2. Associate loading docks with the trade policy.
3. Configure warehouses and inventory allocation.
4. Set up shipping policies for marketplace orders.

For detailed configuration instructions, see [Configuring a marketplace trade policy](/en/docs/tutorials/configuring-a-marketplace-trade-policy).

## Step 3 - Create an affiliate

The affiliate is the identifier that links your VTEX store to the external marketplace for order and inventory synchronization.

### Step 3.1 - Create affiliate in VTEX

Configure the affiliate in your VTEX Admin:

1. Go to **Orders > Orders management > Settings**.
2. Click the **Affiliates** tab.
3. Click `+ New Affiliate`.
4. Fill in the following fields:

- **Name:** Marketplace name for internal reference
- **ID:** Three-consonant identifier (e.g., MKT, AMZ, MLB). Use only consonants; vowels are not accepted
- **Trade Policy:** Select the trade policy created for the marketplace
- **Email for notifications:** Email to receive integration alerts
- **Search Endpoint:** Endpoint URL for marketplace notifications (provided by connector or marketplace)

5. Click `Save` to create the affiliate.

### Step 3.2 - Configure affiliate notifications

The affiliate enables the marketplace to receive notifications about product and inventory changes:

**Notification types:**

- Price changes
- Inventory updates
- Product catalog modifications
- SKU activations or deactivations
- Promotional updates

**Configuration notes:**

- The Search Endpoint URL determines where notifications are sent
- Native connectors configure this automatically
- Custom integrations must implement the notification endpoint
- Test notifications to ensure proper delivery

For detailed instructions, see [Configuring affiliates](/en/docs/tutorials/configuring-affiliates).

## Step 4 - Install and configure the connector

This step varies depending on your integration method (native connector, partner app, or custom solution).

### Step 4.1 - Install native connector

For VTEX native connectors:

1. In the VTEX Admin, go to **Marketplace > Connections**.
2. Find the marketplace connector.
3. Click `Connect` or `Install`.
4. Follow the connector-specific setup wizard.
5. Provide required credentials and settings.
6. Authorize the connection with the marketplace.

### Step 4.2 - Install partner app

For certified partner connectors:

1. Visit the [VTEX App Store](https://apps.vtex.com/).
2. Search for the marketplace integration app.
3. Click `Get App` or `Install`.
4. Review app permissions and requirements.
5. Complete the installation in your VTEX Admin.
6. Follow the app's configuration instructions.
7. Provide marketplace credentials and settings.

### Step 4.3 - Configure connector settings

After installation, configure integration parameters:

**Basic settings:**

- Affiliate ID
- Trade policy
- Default shipping configuration
- Order processing rules

**Product settings:**

- Product selection criteria
- Category mapping rules
- Attribute transformation rules
- Image requirements and formats

**Pricing settings:**

- Price calculation rules
- Currency conversion (if applicable)
- Tax handling
- Markup or discount rules

**Inventory settings:**

- Inventory synchronization frequency
- Safety stock levels
- Multi-warehouse allocation

**Order settings:**

- Order import rules
- Status mapping
- Cancellation policies
- Return handling

### Step 4.4 - Authenticate with the marketplace

Complete the authentication process:

1. Access the marketplace seller portal or admin panel.
2. Generate API credentials or authentication tokens.
3. Enter credentials in the VTEX connector configuration.
4. Authorize VTEX to access marketplace APIs.
5. Verify successful authentication.

> ℹ️ Authentication methods vary by marketplace. Follow the specific marketplace documentation for detailed instructions.

## Step 5 - Map product categories and attributes

External marketplaces use their own category structures and product attributes. Mapping ensures your products appear correctly on the marketplace.

### Step 5.1 - Understand marketplace structure

Review the marketplace's catalog organization:

1. Access marketplace seller documentation.
2. Review available product categories.
3. Understand required and optional attributes.
4. Note any category-specific requirements.
5. Identify restricted or prohibited categories.

### Step 5.2 - Map categories

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

### Step 5.3 - Map product attributes

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

### Step 5.4 - Configure product variations

Set up how product variations (SKUs) are represented:

1. Define variation attributes (color, size, etc.).
2. Configure variation grouping rules.
3. Set primary variation for product display.
4. Configure variation-specific images.
5. Map variation values to marketplace standards.

**Example variation mapping:**

- VTEX color "Vermelho" → Marketplace color "Red"
- VTEX size "G" → Marketplace size "L"
- VTEX voltage "110V" → Marketplace voltage "110 Volts"

## Step 6 - Configure pricing and inventory

Set up pricing and inventory synchronization between VTEX and the marketplace.

### Step 6.1 - Configure pricing rules

Determine how prices are calculated for the marketplace:

**Pricing strategies:**

- **Same prices:** Use identical prices from your VTEX store
- **Markup prices:** Add percentage markup to cover marketplace fees
- **Competitive prices:** Set prices based on marketplace competition
- **Fixed prices:** Define specific prices for marketplace products

**Implementation:**

1. Access pricing configuration in connector settings.
2. Select pricing strategy (base price, markup, or fixed).
3. Configure markup percentage if applicable.
4. Set minimum and maximum price limits.
5. Configure price rounding rules.
6. Enable or disable promotional pricing sync.

### Step 6.2 - Handle marketplace commissions

Factor marketplace commissions into your pricing:

1. Identify marketplace commission percentage.
2. Decide if you'll absorb or pass on the commission.
3. Configure markup to cover commission if needed.
4. Review pricing competitiveness.
5. Monitor profit margins regularly.

**Example calculation:**

- Base price: $100
- Marketplace commission: 15%
- Desired profit: 20%
- Markup needed: 35%
- Final price: $135

### Step 6.3 - Configure inventory synchronization

Set up inventory sync between VTEX and the marketplace:

**Synchronization settings:**

1. Access inventory configuration in connector settings.
2. Enable real-time or scheduled synchronization.
3. Set synchronization frequency (immediate, hourly, daily).
4. Configure safety stock levels.
5. Set minimum inventory thresholds.

**Inventory strategies:**

- **Full sync:** Send complete inventory levels to marketplace
- **Reserved allocation:** Allocate percentage of inventory to marketplace
- **Safety stock:** Keep buffer stock for your own store
- **Multi-channel allocation:** Distribute inventory across channels

### Step 6.4 - Handle stock allocation

Manage inventory across multiple sales channels:

1. Define inventory allocation per marketplace.
2. Set maximum quantities available per channel.
3. Configure inventory reservation rules.
4. Enable inventory prioritization if needed.
5. Monitor stock levels across channels.

**Best practices:**

- Reserve inventory for your primary channel
- Set minimum safety stock levels
- Monitor sell-through rates by channel
- Adjust allocations based on performance
- Implement low-stock alerts

## Step 7 - Send products to the marketplace

After configuration, send your product catalog to the marketplace.

### Step 7.1 - Prepare products for export

Ensure products meet marketplace requirements:

**Product information checklist:**

- [ ] Complete product titles and descriptions
- [ ] High-quality product images (multiple angles)
- [ ] All required specifications filled
- [ ] Correct category assignments
- [ ] Valid EAN/UPC codes
- [ ] Accurate dimensions and weight
- [ ] Active product status
- [ ] Available inventory
- [ ] Valid pricing

### Step 7.2 - Validate product data

Review products before sending:

1. Use connector validation tools to check product data.
2. Review error reports and warnings.
3. Fix missing required attributes.
4. Correct invalid attribute values.
5. Verify image quality and formats.
6. Check pricing and inventory levels.

### Step 7.3 - Send initial product catalog

Export products to the marketplace:

1. In the connector settings, access product export.
2. Select products to send (all or filtered selection).
3. Review product count and selection.
4. Click `Send products` or `Export catalog`.
5. Monitor export progress.
6. Review export results and errors.

**For native connectors:**

- Products associated with the trade policy are sent automatically
- Connector handles API calls and error handling
- Progress can be monitored in VTEX Admin

**For custom integrations:**

- Implement product export using VTEX APIs
- Handle Change Notification and SKU Suggestion flows
- Process responses and retry failed products

### Step 7.4 - Monitor product synchronization

Track synchronization status:

1. Review integration dashboard or logs.
2. Check for products pending approval.
3. Identify and resolve errors.
4. Monitor product activation on marketplace.
5. Verify products appear correctly on marketplace storefront.

**Common synchronization issues:**

- Missing required attributes
- Invalid category mapping
- Image format or size issues
- Price below marketplace minimum
- Stock unavailable
- EAN code conflicts

For detailed information, see [Sending products to the marketplace](/en/docs/tutorials/sending-products-to-the-marketplace).

## Step 8 - Configure price divergence rules

Price divergence rules protect your store from processing orders with unexpected price differences between VTEX and the marketplace.

### Step 8.1 - Understand price divergence

Price differences can occur due to:

- Synchronization delays
- Promotional pricing mismatches
- Currency conversion variations
- Marketplace-applied promotions
- System errors or bugs

### Step 8.2 - Create price divergence rule

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

### Step 8.3 - Handle divergent orders

Configure what happens when orders exceed the divergence threshold:

**Automatic actions:**

- Approve orders within threshold
- Hold orders above threshold for review
- Reject orders significantly over threshold

**Manual review process:**

1. Review held orders in **Orders > All Orders**.
2. Filter by marketplace and divergence status.
3. Investigate price difference cause.
4. Approve or cancel order as appropriate.
5. Adjust divergence rules if needed.

For detailed configuration, see marketplace-specific price divergence articles.

## Step 9 - Manage orders from the marketplace

Handle orders received from the external marketplace through your VTEX Admin.

### Step 9.1 - Understand order flow

Orders from external marketplaces follow a specific flow:

1. **Order placement:** Customer purchases on marketplace
2. **Order import:** Marketplace sends order to VTEX
3. **Order authorization:** VTEX validates order details
4. **Payment confirmation:** Payment is processed (by marketplace or seller)
5. **Fulfillment:** Seller prepares and ships order
6. **Status updates:** Seller updates order status
7. **Delivery:** Order reaches customer
8. **Completion:** Order marked as delivered

### Step 9.2 - Process marketplace orders

Manage orders in VTEX Admin:

1. Go to **Orders > All Orders**.
2. Filter orders by marketplace (using trade policy or affiliate).
3. Review order details and customer information.
4. Verify payment status.
5. Prepare order for shipment.
6. Generate invoice.
7. Update order status.

**Order information available:**

- Customer name and contact (subject to marketplace policies)
- Delivery address
- Products ordered with quantities
- Payment status
- Shipping method selected
- Marketplace order ID
- Special instructions or notes

### Step 9.3 - Invoice and ship orders

Complete order fulfillment:

1. In the order details, click `Invoice`.
2. Enter invoice information:

- Invoice number
- Invoice date
- Invoice value
- Invoice XML (if applicable)

3. Add tracking information:

- Carrier name
- Tracking number
- Tracking URL

4. Click `Save` to submit invoice.
5. Order status updates to "Invoiced" and "Shipped".

**Marketplace notification:**

- VTEX automatically notifies the marketplace
- Marketplace updates customer with tracking information
- Customer can track delivery through marketplace

### Step 9.4 - Handle order cancellations

Process cancellation requests:

**Before shipment:**

1. Review cancellation request in order details.
2. Verify cancellation is possible.
3. Click `Cancel order`.
4. Select cancellation reason.
5. Confirm cancellation.

**After shipment:**

- Contact marketplace support for guidance
- Follow marketplace return procedures
- Process return when product is received
- Issue refund per marketplace policy

**Cancellation initiated by seller:**

1. Go to order details.
2. Click `Cancel order`.
3. Provide cancellation reason.
4. Submit cancellation request.
5. Wait for marketplace approval.

## Step 10 - Monitor and optimize integration

Maintain and improve marketplace integration performance over time.

### Step 10.1 - Monitor integration health

Track key performance indicators:

**Product metrics:**

- Products successfully exported
- Products pending approval
- Products with errors
- Product synchronization rate
- Active products on marketplace

**Order metrics:**

- Orders received per period
- Average order value
- Order processing time
- Order cancellation rate
- Delivery performance

**Inventory metrics:**

- Synchronization success rate
- Out-of-stock incidents
- Oversold situations
- Safety stock performance

**Financial metrics:**

- Revenue by marketplace
- Commission costs
- Profit margins
- Return on investment
- Price divergence frequency

### Step 10.2 - Review integration logs

Regularly check integration logs for issues:

1. Access connector logs in VTEX Admin or app settings.
2. Filter logs by type (errors, warnings, info).
3. Identify recurring errors or patterns.
4. Investigate and resolve issues.
5. Document solutions for future reference.

### Step 10.3 - Optimize product performance

Improve product listings on the marketplace:

**Content optimization:**

- Enhance product titles with keywords
- Improve product descriptions
- Add more high-quality images
- Complete all optional attributes
- Use marketplace-recommended formats

**Pricing optimization:**

- Monitor competitor pricing
- Adjust prices based on market conditions
- Test different pricing strategies
- Balance competitiveness with profitability
- Use marketplace pricing tools

**Inventory optimization:**

- Maintain adequate stock levels
- Reduce out-of-stock situations
- Adjust safety stock based on sales velocity
- Optimize inventory allocation across channels
- Implement demand forecasting

### Step 10.4 - Leverage marketplace tools

Use marketplace features to increase sales:

**Advertising and promotion:**

- Marketplace sponsored ads
- Featured product placements
- Marketplace deals and promotions
- Seasonal campaigns
- Cross-selling opportunities

**Customer engagement:**

- Respond promptly to customer questions
- Maintain high seller ratings
- Provide excellent customer service
- Handle returns efficiently
- Build positive reviews

**Analytics and insights:**

- Review marketplace performance reports
- Analyze customer behavior data
- Identify top-performing products
- Understand seasonal trends
- Benchmark against competitors

## Advanced integration scenarios

### Multi-marketplace strategy

Selling on multiple marketplaces simultaneously:

**Benefits:**

- Diversified revenue streams
- Broader market reach
- Reduced dependency on single channel
- Geographic expansion opportunities

**Management considerations:**

- Create separate trade policies per marketplace
- Allocate inventory strategically
- Optimize pricing per marketplace
- Monitor performance across channels
- Centralize operations through VTEX

**Implementation approach:**

1. Start with one marketplace
2. Optimize operations and performance
3. Add additional marketplaces gradually
4. Scale inventory allocation as needed
5. Automate processes where possible

### International marketplace expansion

Selling in international marketplaces:

**Additional requirements:**

- Multi-currency pricing
- International shipping configuration
- Tax and customs compliance
- Localized product content
- Regional inventory allocation

**Implementation steps:**

1. Research target market requirements
2. Configure international logistics
3. Set up currency conversion
4. Translate product content
5. Comply with local regulations
6. Test order flow thoroughly

### Marketplace-specific customizations

Optimize for individual marketplace requirements:

**Amazon-specific:**

- Fulfillment by Amazon (FBA) integration
- Amazon Brand Registry
- Enhanced Brand Content
- Amazon Advertising
- Buy Box optimization

**Mercado Libre-specific:**

- Mercado Envios shipping
- Mercado Pago payments
- Premium listings
- Catalog quality requirements
- Regional variations

**Category-specific requirements:**

- Electronics: Warranty information, technical specs
- Fashion: Size charts, material details, care instructions
- Food: Expiration dates, nutritional information, certifications
- Health: Regulatory compliance, ingredient lists

## Troubleshooting common issues

### Products not appearing on marketplace

**Possible causes:**

- Products not associated with trade policy
- Missing required attributes
- Invalid category mapping
- Products pending marketplace approval
- Synchronization errors

**Solutions:**

1. Verify products are active and associated with correct trade policy
2. Check all required attributes are filled
3. Review category mapping configuration
4. Contact marketplace support for approval status
5. Review connector logs for specific errors
6. Resend products if synchronization failed

### Price or inventory not synchronizing

**Possible causes:**

- Affiliate misconfiguration
- Trade policy mismatch
- API connectivity issues
- Synchronization frequency settings
- Marketplace API limits

**Solutions:**

1. Verify affiliate is correctly configured
2. Check trade policy associations
3. Test API connectivity
4. Review synchronization settings
5. Implement retry logic for failed updates
6. Contact marketplace support if needed

### Orders not importing

**Possible causes:**

- Connector not properly configured
- Authentication failures
- Price divergence blocking orders
- Payment processing issues
- Marketplace API changes

**Solutions:**

1. Verify connector configuration and credentials
2. Check authentication status
3. Review price divergence rules
4. Confirm payment settings
5. Update connector to latest version
6. Review integration logs for errors

### Fulfillment issues

**Possible causes:**

- Invalid tracking information
- Shipping delays
- Incorrect status updates
- Missing invoice data
- Communication errors with marketplace

**Solutions:**

1. Validate tracking information format
2. Provide accurate delivery estimates
3. Update order status promptly
4. Include complete invoice data
5. Monitor marketplace notifications
6. Implement error handling for API failures

## Best practices

Follow these best practices for successful external marketplace integration:

**For product listings:**

- Use high-quality, professional product images
- Write detailed, keyword-rich descriptions
- Complete all optional attributes
- Keep product information accurate and current
- Use consistent naming conventions
- Optimize titles for marketplace search

**For pricing:**

- Monitor competitor pricing regularly
- Factor in all marketplace costs
- Maintain healthy profit margins
- Use dynamic pricing tools when available
- Test different pricing strategies
- Keep prices synchronized across channels

**For inventory:**

- Maintain adequate safety stock
- Synchronize inventory in real-time
- Prevent overselling with conservative allocation
- Monitor stock levels continuously
- Implement low-stock alerts
- Plan for seasonal demand variations

**For order fulfillment:**

- Process orders promptly (within 24 hours)
- Ship on time to meet marketplace standards
- Provide accurate tracking information
- Update order status regularly
- Communicate with customers proactively
- Handle returns efficiently

**For integration management:**

- Monitor integration health daily
- Review logs regularly for errors
- Keep connectors updated
- Test changes in sandbox environments
- Document processes and configurations
- Train team members on procedures
- Maintain backup and disaster recovery plans

## Security and compliance

Ensure secure and compliant marketplace operations:

### Data protection

- Protect customer information per marketplace policies
- Comply with data privacy regulations (GDPR, LGPD, CCPA)
- Secure API credentials and access tokens
- Implement access controls in VTEX Admin
- Monitor for unauthorized access
- Maintain data breach response procedures

### Marketplace policies

- Review and comply with marketplace terms of service
- Follow prohibited product guidelines
- Adhere to content policies
- Maintain required seller performance metrics
- Respond to policy violations promptly
- Stay informed about policy updates

### Tax compliance

- Calculate and collect appropriate taxes
- Comply with regional tax regulations
- Provide accurate tax documentation
- Handle cross-border tax requirements
- Maintain tax records as required
- Consult tax professionals when needed

## Next steps

After completing the external marketplace integration:

1. **Test thoroughly:** Place test orders to validate the complete flow
2. **Monitor closely:** Track integration health during the initial launch period
3. **Gather feedback:** Review customer feedback and marketplace performance reports
4. **Optimize continuously:** Refine product listings, pricing, and operations
5. **Scale gradually:** Expand product catalog and consider additional marketplaces
6. **Train team:** Ensure all team members understand processes and tools
7. **Plan for growth:** Develop strategies for scaling operations

## Learn more

- [Marketplace strategies at VTEX](/en/docs/tutorials/marketplace-strategies-at-vtex)
- [Configuring a marketplace trade policy](/en/docs/tutorials/configuring-a-marketplace-trade-policy)
- [Configuring affiliates](/en/docs/tutorials/configuring-affiliates)
- [Sending products to the marketplace](/en/docs/tutorials/sending-products-to-the-marketplace)
- [How trade policies work](/en/docs/tutorials/how-trade-policies-work)
- [External Marketplace Integration Guide](https://developers.vtex.com/vtex-developer-docs/docs/external-marketplace-integration-guide)
- [Integration app template](https://developers.vtex.com/docs/guides/external-marketplace-integration-app-template)
- [Fulfillment logistics at VTEX](/en/docs/tutorials/fulfillment-logistics-vtex)
