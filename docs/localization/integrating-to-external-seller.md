---
title: 'Integrating to an external seller'
id: [to-be-assigned]
status: DRAFT
createdAt: 2026-02-20T00:00:00.000Z
updatedAt: 2026-02-20T00:00:00.000Z
contentType: guide
productTeam: Channels
locale: en
---

Integrating external sellers into your VTEX marketplace allows you to expand your product catalog and offer customers a wider variety of products without managing additional inventory. This guide shows you how to connect external sellers—those not hosted on the VTEX platform—to your VTEX marketplace through API integration or custom connectors.

In this guide, you will learn how to:

- Understand the external seller integration architecture
- Configure your VTEX marketplace to receive external sellers
- Implement the required API endpoints for external sellers
- Manage catalog synchronization and order fulfillment
- Handle order processing and payment flows

## Before you begin

Before integrating external sellers with your VTEX marketplace, ensure the following requirements are met:

**For VTEX marketplaces:**

- Admin access to your VTEX marketplace
- Defined [trade policies](/en/docs/tutorials/how-trade-policies-work) for seller integrations
- Understanding of [marketplace strategies at VTEX](/en/docs/tutorials/marketplace-strategies-at-vtex)
- Agreement with external sellers on commissions, delivery policies, and return policies
- Knowledge of [shared information between marketplace and seller](/en/docs/tutorials/shared-information-between-a-marketplace-and-a-seller-on-vtex)

**For external sellers:**

- Technical capability to implement REST API endpoints
- Product catalog with standardized data format
- Order management system capable of processing marketplace orders
- Logistics infrastructure for order fulfillment
- Admin email for marketplace communications

**Technical requirements:**

- Understanding of RESTful API principles
- Ability to handle JSON data formats
- Authentication credentials (API keys and tokens)
- HTTPS-enabled endpoints for secure communication
- Knowledge of webhook implementations for real-time notifications

> ℹ️ For detailed technical specifications, refer to the [External Seller Integration Guide](https://developers.vtex.com/vtex-rest-api/docs/external-seller-integration-guide) in the VTEX Developer Portal.

## Understanding the integration architecture

The external seller integration establishes a connection between your VTEX marketplace and sellers hosted on external platforms. This architecture enables collaborative commerce while maintaining clear separation of responsibilities.

### Integration model

**Marketplace responsibilities:**

- Display products on the storefront
- Handle customer checkout process
- Manage seller offers and catalog binding
- Process customer orders and forward to sellers
- Provide customer support for marketplace experience

**External seller responsibilities:**

- Own and manage product inventory
- Send product offers with complete information
- Provide pricing and inventory updates
- Fulfill orders and handle shipping
- Update order status and tracking information
- Handle product-specific customer support

### Communication flow

The integration involves bidirectional API communication:

**From seller to marketplace:**

1. Catalog notification and SKU suggestions
2. Price and inventory updates
3. Order invoicing notifications
4. Cancellation and return processing

**From marketplace to seller:**

1. Fulfillment simulation requests
2. Order placement
3. Order authorization
4. Cancellation requests

This architecture requires 12 API requests across multiple steps, with 4 requests from seller to marketplace, 7 requests from marketplace to seller, and 1 bidirectional request.

### Business agreements

Before technical integration, establish clear agreements covering:

- **Delivery requirements:** Expected delivery times, shipping methods, and geographic coverage
- **Customer support:** Responsibilities for pre-sale and post-sale support
- **Product selection:** Criteria for product approval and quality standards
- **Commission structure:** Percentage rates for product and shipping commissions
- **Returns and exchanges:** Policies and procedures for product returns
- **Privacy and security:** Data handling and customer information policies

## Step 1 - Configure the marketplace

This section guides marketplace operators through the configurations necessary to receive and manage external sellers.

### Step 1.1 - Define trade policies

[Trade policies](/en/docs/tutorials/how-trade-policies-work) control the product assortment, pricing, promotions, customer segmentation, and shipping strategy for external sellers.

To define trade policies:

1. Evaluate if external sellers require different configurations from your existing sellers.
2. If specific settings are needed, [create a new trade policy](/en/docs/tutorials/creating-a-trade-policy) for external seller integrations.
3. Configure the trade policy with appropriate settings for catalog, pricing, promotions, and logistics.

> ℹ️ The same trade policy can be used for multiple external sellers. [Requesting additional trade policies](/en/docs/tutorials/requesting-an-additional-trade-policy) for external seller integrations may incur a monthly fee.

### Step 1.2 - Add external sellers

Add external sellers to your marketplace using the VTEX Admin:

1. In the VTEX Admin, go to **Marketplace > Management**.
2. Click `Add Seller`.
3. Select **External Seller** as the integration type.
4. Complete the required fields:

**Integration section:**

- **Fulfillment URL:** Enter the endpoint URL for the seller's order fulfillment API. The seller must provide this URL, which the marketplace uses for all order-related communication.
- **User:** Enter the username if using a hub or middleware to integrate with the external seller.
- **Password:** Enter the password if using a hub or middleware to integrate with the external seller.
- **Pause seller after creation:** Select this checkbox to create the seller in `Paused` status, allowing you to test the integration before going live.

**Basic seller information:**

- **Seller name:** Name of the external seller as it appears in your marketplace.
- **Seller ID:** Internal identification code for the seller. Use lowercase letters without spaces or special characters, up to 50 characters. This ID cannot be edited after creation.
- **Seller groups:** Keywords to organize sellers into groups for management and filtering purposes.

**Trade agreements:**

- **Marketplace trade policies:** Select the trade policies that apply to this external seller.
- **Product commissioning:** Define the commission percentage for the seller's products.
- **Shipping commissioning:** Define the commission percentage for shipping costs.
- **Add commissioning by category:** Configure specific commission percentages for selected product categories if different rates apply.
- **Enable seller share in purchases with shopping vouchers:** Allow marketplace gift cards on seller products when sellers process payments.

**Additional information:**

- **Add logo:** Upload the seller's logo (PNG, JPG, or JPEG, up to 500kb).
- **CNPJ (Company registration number):** Seller's company registration number or equivalent tax identification.
- **Email:** Email address of the manager responsible for the seller account.
- **Description:** Commercial description of the seller that can appear in the marketplace storefront when customizing the CMS.
- **Delivery policy:** Text describing the delivery policy agreed upon between marketplace and seller.
- **Exchanges and returns:** Text describing the exchange and return policy.
- **Privacy and security policy:** Text describing the security policy applicable to the seller's products.

5. Click `Save` to add the external seller to your marketplace.

For detailed information, see [Adding a seller](/en/docs/tutorials/adding-a-seller).

### Step 1.3 - Configure seller visibility

External sellers are typically configured as identifiable sellers, meaning they're visible in the marketplace storefront. Customers can see which seller offers each product and choose their preferred seller.

To configure visibility settings:

1. Ensure the seller information (name, logo, description) is complete and accurate.
2. Configure your storefront to display seller information using CMS controls or VTEX IO apps.
3. Test the seller display on product pages and in the checkout process.

> ℹ️ White label seller configuration is not typically used for external sellers, as it requires franchise account setup which is designed for VTEX-based sellers.

### Step 1.4 - Configure payment processing

Determine the payment processing model for external sellers:

**Marketplace processes payments:**

- The marketplace receives all payments
- The marketplace distributes payments to sellers after deducting commissions
- Requires payment split configuration in the Gateway module
- Marketplace assumes payment processing responsibility

**Seller processes payments:**

- Each seller receives payments directly
- The seller pays commissions to the marketplace separately
- Requires coordination between marketplace and seller systems
- Seller assumes payment processing responsibility

For detailed payment configurations, see [Payments in VTEX Marketplace](/en/docs/tutorials/payments-in-vtex-marketplaces).

## Step 2 - Implement seller API endpoints

External sellers must implement specific API endpoints to communicate with the VTEX marketplace. This section outlines the required endpoints and their functions.

### Step 2.1 - Fulfillment simulation endpoint

The fulfillment simulation endpoint receives requests from the marketplace to simulate delivery options and calculate shipping costs for a given cart.

**Endpoint requirements:**

- **Method:** POST
- **URL:** The fulfillment URL configured when adding the seller
- **Authentication:** Implement authentication using the user/password credentials provided
- **Request format:** JSON with cart items, shipping address, and customer information
- **Response format:** JSON with available shipping options, costs, and estimated delivery dates

**Implementation considerations:**

- Calculate shipping costs based on products, quantities, and destination
- Return multiple shipping options when available (standard, express, etc.)
- Include accurate delivery time estimates
- Handle inventory availability checks
- Respond within 3 seconds to avoid timeout errors

### Step 2.2 - Order placement endpoint

The order placement endpoint receives order details when a customer completes a purchase.

**Endpoint requirements:**

- **Method:** POST
- **URL:** The fulfillment URL with order placement path
- **Request format:** JSON with complete order details, including customer information, items, shipping address, and payment status
- **Response format:** JSON with order acceptance confirmation and seller order ID

**Implementation considerations:**

- Validate order information before accepting
- Reserve inventory for confirmed orders
- Generate internal order ID for tracking
- Store order details in the seller's order management system
- Respond with confirmation or rejection

### Step 2.3 - Order authorization endpoint

The order authorization endpoint confirms that the seller can fulfill the order after payment confirmation.

**Endpoint requirements:**

- **Method:** POST
- **URL:** The fulfillment URL with authorization path
- **Request format:** JSON with order ID and authorization request
- **Response format:** JSON with authorization confirmation

**Implementation considerations:**

- Verify inventory availability
- Confirm the ability to fulfill the order
- Begin order processing after authorization
- Handle authorization failures with appropriate error messages

### Step 2.4 - Order cancellation endpoint

The order cancellation endpoint handles cancellation requests from the marketplace.

**Endpoint requirements:**

- **Method:** POST
- **URL:** The fulfillment URL with cancellation path
- **Request format:** JSON with order ID and cancellation reason
- **Response format:** JSON with cancellation confirmation

**Implementation considerations:**

- Process cancellations before shipment
- Handle partial cancellations for multi-item orders
- Update inventory when cancellations occur
- Notify internal systems of cancellation

For complete API specifications, see the [External Seller Integration Guide](https://developers.vtex.com/vtex-rest-api/docs/external-seller-integration-guide) in the VTEX Developer Portal.

## Step 3 - Implement marketplace API calls

External sellers must also call specific VTEX marketplace APIs to send product information and order updates.

### Step 3.1 - Send catalog notifications

Notify the marketplace about new or updated products using the Change Notification API.

**Implementation steps:**

1. Obtain API credentials (App Key and App Token) from the marketplace.
2. Implement the Change Notification API call with product SKU information.
3. Send notifications when products are created or updated.
4. Handle API responses and error conditions.

**Best practices:**

- Batch notifications when updating multiple products
- Implement retry logic for failed requests
- Monitor notification success rates
- Keep track of which products have been sent

### Step 3.2 - Send SKU suggestions

After sending catalog notifications, submit complete SKU information to the marketplace.

**Implementation steps:**

1. Use the SKU Suggestion API to send detailed product information.
2. Include all required fields: product name, description, images, specifications, pricing, and inventory.
3. Map your product categories to marketplace categories.
4. Handle suggestion approval workflow.

**Required product information:**

- Product name and description
- Product images (URLs to image files)
- Product specifications and attributes
- EAN or product identifiers
- Pricing information
- Inventory levels
- Shipping dimensions and weight

### Step 3.3 - Update pricing and inventory

Keep pricing and inventory information synchronized with the marketplace.

**Implementation strategies:**

- **Real-time updates:** Send updates immediately when prices or inventory change
- **Scheduled updates:** Batch updates at regular intervals (hourly or daily)
- **Hybrid approach:** Real-time for critical changes, scheduled for routine updates

**API calls required:**

- Price update API for pricing changes
- Inventory update API for stock level changes

### Step 3.4 - Send order status updates

Keep the marketplace informed of order status changes throughout the fulfillment process.

**Required updates:**

1. **Order accepted:** Confirm order receipt and acceptance
2. **Order invoiced:** Send invoice information when preparing shipment
3. **Order shipped:** Provide tracking information when shipped
4. **Order delivered:** Confirm successful delivery
5. **Order cancelled:** Notify of cancellations with reason codes

**Implementation requirements:**

- Send invoice notifications via the Order Invoice API
- Include invoice number, date, and tracking codes
- Update order status in real-time
- Handle partial shipments for multi-item orders

For detailed API specifications, refer to the [VTEX REST API documentation](https://developers.vtex.com/docs/guides/getting-started-list-of-rest-apis).

## Step 4 - Map catalog architecture

After the external seller sends product information, the marketplace must map the seller's catalog to its own structure.

### Step 4.1 - Review received SKUs

Check the SKUs submitted by the external seller:

1. In the VTEX Admin, go to **Marketplace > Sellers > Received SKUs**.
2. Filter by the external seller to view submitted SKUs.
3. Review product information for completeness and accuracy.
4. Verify images, descriptions, and specifications.

### Step 4.2 - Map categories and brands

Match the seller's categories and brands to your marketplace catalog:

1. In the VTEX Admin, go to **Marketplace > Sellers > Categories and Brands**.
2. Select the external seller.
3. Map each seller category to the equivalent marketplace category.
4. Map seller brands to marketplace brands.
5. Create new categories or brands if necessary.
6. Click `Save` to confirm mappings.

### Step 4.3 - Map product specifications

Ensure product specifications are properly mapped:

1. Review specification mappings in the catalog interface.
2. Match seller specifications to marketplace specifications.
3. Create new specifications if required for seller products.
4. Verify all mandatory specifications are mapped correctly.

For detailed instructions, see [Mapping categories and brands for the marketplace](/en/docs/tutorials/mapping-categories-and-brands-for-the-marketplace).

## Step 5 - Approve and catalog products

After mapping the catalog, approve and catalog the external seller's products.

### Step 5.1 - Approve SKUs

Review and approve SKUs to make them available on your marketplace:

1. In the VTEX Admin, go to **Marketplace > Sellers > Received SKUs**.
2. Select the SKUs to approve.
3. Verify all product information is complete and accurate.
4. Click `Approve` to add products to your marketplace catalog.

### Step 5.2 - Verify product display

After approval, verify products appear correctly:

1. Check the marketplace storefront to confirm product visibility.
2. Verify product information, images, and pricing display correctly.
3. Test the purchase flow to ensure checkout works properly.
4. Confirm seller information displays when configured to be visible.

### Step 5.3 - Set up automatic approval (optional)

For trusted external sellers, configure automatic approval to streamline operations:

1. Verify the seller consistently provides high-quality product data.
2. Configure automatic approval rules in the seller settings.
3. Monitor automatically approved products for quality.
4. Adjust rules based on approval success rates.

For more information, see [Manual SKU cataloging](/en/docs/tutorials/manual-sku-cataloging).

## Step 6 - Test the integration

Before launching the external seller integration in production, conduct thorough testing.

### Step 6.1 - Test fulfillment simulation

Verify that the seller's fulfillment endpoint returns accurate information:

1. Add products to cart on a test environment.
2. Proceed to checkout to trigger fulfillment simulation.
3. Verify shipping options and costs are accurate.
4. Test multiple shipping addresses in different regions.
5. Confirm delivery time estimates are realistic.

### Step 6.2 - Test order placement

Ensure orders are correctly transmitted to the external seller:

1. Place test orders with various product combinations.
2. Verify the seller receives complete order information.
3. Check that customer data is transmitted correctly.
4. Confirm order IDs are properly linked between systems.
5. Test order placement error handling.

### Step 6.3 - Test order flow

Validate the complete order lifecycle:

1. Place a test order from the marketplace.
2. Verify the seller receives the order notification.
3. Process the order through the seller's system.
4. Send invoice and tracking information to the marketplace.
5. Update order status through delivery and completion.
6. Verify marketplace displays accurate order status to customers.

### Step 6.4 - Test cancellations and returns

Verify cancellation and return processes work correctly:

1. Test order cancellation before shipment.
2. Verify cancellation notifications are sent correctly.
3. Test return request processing.
4. Confirm inventory updates after cancellations.
5. Verify refund processing when applicable.

## Step 7 - Monitor and maintain the integration

After launching the external seller integration, maintain ongoing monitoring and optimization.

### Step 7.1 - Monitor integration health

Track key metrics to ensure integration performance:

**Critical metrics:**

- API response times and timeout rates
- Product synchronization success rates
- Order placement success rates
- Inventory accuracy between systems
- Order fulfillment times
- Customer feedback and return rates

**Monitoring tools:**

- Use VTEX Admin reports to track seller performance
- Implement logging in seller systems for troubleshooting
- Set up alerts for integration failures
- Monitor API call volumes and patterns

### Step 7.2 - Handle integration issues

Address common integration problems:

**Product sync issues:**

- Verify API credentials are valid
- Check product data format and required fields
- Review error logs for specific failure reasons
- Ensure catalog notification and SKU suggestion sequence is correct

**Order processing issues:**

- Verify fulfillment endpoint availability
- Check order data format and required fields
- Review timeout settings and response times
- Ensure order status updates are sent correctly

**Inventory discrepancies:**

- Verify inventory update frequency
- Check for failed inventory update API calls
- Review inventory calculation logic
- Ensure real-time updates are working

### Step 7.3 - Optimize performance

Continuously improve integration performance:

**For marketplaces:**

- Review and refine catalog mapping processes
- Optimize approval workflows
- Improve seller onboarding documentation
- Analyze sales data to identify growth opportunities

**For external sellers:**

- Optimize API response times
- Improve product data quality
- Enhance inventory accuracy
- Streamline order fulfillment processes
- Reduce order processing times

### Step 7.4 - Scale the integration

As the partnership grows, consider scaling strategies:

- Implement caching for frequently accessed data
- Optimize database queries for better performance
- Use asynchronous processing for non-critical operations
- Implement rate limiting to prevent API overload
- Consider using webhooks for real-time notifications
- Evaluate middleware solutions for complex integrations

## Advanced integration scenarios

### Using integration hubs

Integration hubs or middleware platforms can simplify external seller integration:

**Benefits:**

- Pre-built connectors for common ecommerce platforms
- Simplified data transformation and mapping
- Centralized integration management
- Reduced development effort
- Built-in error handling and monitoring

**Popular integration hubs:**

- VTEX-certified integration partners
- iPaaS (Integration Platform as a Service) solutions
- Custom middleware solutions

**Implementation considerations:**

- Evaluate hub capabilities and costs
- Ensure hub supports required VTEX APIs
- Verify data security and compliance
- Test thoroughly before production deployment

### Building custom connectors

For unique requirements, develop custom connectors:

**Development approach:**

1. Review the [External Seller Integration Guide](https://developers.vtex.com/vtex-rest-api/docs/external-seller-integration-guide)
2. Use VTEX's integration template app for faster development
3. Implement required API endpoints and calls
4. Add error handling and logging
5. Conduct comprehensive testing
6. Deploy and monitor in production

**Best practices:**

- Follow RESTful API design principles
- Implement comprehensive error handling
- Use asynchronous processing where appropriate
- Implement retry logic with exponential backoff
- Log all API interactions for troubleshooting
- Secure API credentials properly
- Document the integration thoroughly

### Multi-marketplace scenarios

External sellers may want to sell on multiple VTEX marketplaces:

**Considerations:**

- Use separate API credentials for each marketplace
- Implement marketplace-specific configurations
- Handle different commission structures
- Manage multiple inventory allocations
- Coordinate order routing to appropriate fulfillment locations

## Security best practices

Ensure secure communication between external sellers and the marketplace:

### Authentication and authorization

- Use HTTPS for all API communications
- Protect API keys and tokens securely
- Implement rate limiting to prevent abuse
- Use IP whitelisting when possible
- Rotate credentials periodically

### Data protection

- Encrypt sensitive customer information
- Comply with data privacy regulations (GDPR, LGPD, etc.)
- Limit data access to necessary personnel
- Implement audit logging for data access
- Follow PCI DSS standards for payment data

### API security

- Validate all API inputs
- Implement request signing for additional security
- Use appropriate HTTP status codes
- Handle errors securely without exposing system details
- Monitor for suspicious API activity

For more information on security, see [Mutual Transport Layer Security (mTLS)](/en/docs/tutorials/mutual-transport-layer-security-mtls).

## Best practices

Follow these best practices for successful external seller integration:

**For marketplaces:**

- Provide comprehensive integration documentation to sellers
- Offer sandbox environments for testing
- Respond promptly to seller technical questions
- Monitor seller performance metrics
- Provide feedback and support for improvement
- Establish clear SLAs for integration availability

**For external sellers:**

- Implement robust error handling and logging
- Maintain high API availability (99.9% uptime)
- Respond to API requests within recommended timeframes
- Keep product information accurate and up-to-date
- Process orders promptly and update status regularly
- Maintain sufficient inventory to avoid stockouts
- Provide accurate shipping estimates

**For both parties:**

- Establish clear communication channels
- Document integration processes and troubleshooting
- Conduct regular integration health reviews
- Stay informed about platform updates
- Test changes thoroughly before production deployment
- Maintain disaster recovery and backup procedures

## Troubleshooting common issues

### Products not appearing on marketplace

**Possible causes:**

- SKU suggestion not sent or incomplete
- Catalog mapping not completed
- Products not approved by marketplace
- Trade policy not configured correctly

**Solutions:**

- Verify catalog notification and SKU suggestion were sent
- Check received SKUs in marketplace admin
- Complete catalog mapping for categories and brands
- Approve SKUs through marketplace admin interface

### Order placement failures

**Possible causes:**

- Fulfillment endpoint unavailable or responding slowly
- Invalid order data format
- Authentication failures
- Network connectivity issues

**Solutions:**

- Verify fulfillment endpoint is accessible and responding
- Check API logs for specific error messages
- Validate API credentials
- Ensure proper error handling in seller system

### Inventory synchronization issues

**Possible causes:**

- Inventory update API calls failing
- Incorrect inventory calculation
- Delayed batch updates
- Network or system outages

**Solutions:**

- Verify inventory update API calls are succeeding
- Implement real-time inventory updates
- Check for failed API calls in logs
- Ensure inventory levels are calculated correctly

## Next steps

After completing the external seller integration:

1. **Launch gradually:** Start with limited products to identify and resolve issues
2. **Monitor closely:** Track integration health metrics during initial launch period
3. **Gather feedback:** Collect input from customers and seller teams
4. **Optimize continuously:** Refine processes based on performance data
5. **Scale thoughtfully:** Expand product catalog and seller participation gradually
6. **Document learnings:** Create runbooks for common scenarios and issues

## Learn more

- [Marketplace strategies at VTEX](/en/docs/tutorials/marketplace-strategies-at-vtex)
- [External Seller Integration Guide](https://developers.vtex.com/vtex-rest-api/docs/external-seller-integration-guide)
- [Configuring a VTEX marketplace](/en/docs/tutorials/configuring-vtex-marketplace)
- [Adding a seller](/en/docs/tutorials/adding-a-seller)
- [Shared information between a marketplace and a seller on VTEX](/en/docs/tutorials/shared-information-between-a-marketplace-and-a-seller-on-vtex)
- [Payments in VTEX Marketplace](/en/docs/tutorials/payments-in-vtex-marketplaces)
- [Actions for VTEX marketplace operation](/en/docs/tutorials/actions-for-vtex-marketplace-operation)
- [List of REST APIs](https://developers.vtex.com/docs/guides/getting-started-list-of-rest-apis)
