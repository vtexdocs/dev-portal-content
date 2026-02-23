---
title: "Integrating VTEX stores"
hidden: false
excerpt: ""
createdAt: 2026-02-20T00:00:00.000Z
---

Integrating VTEX stores enables collaborative commerce, where stores can act as both marketplaces and sellers within the VTEX ecosystem. This guide shows you how to establish connections between VTEX stores, configure the necessary settings, and manage the integration to expand your sales channels or product assortment.

In this guide, you'll learn how to:

* Configure a VTEX marketplace to receive products from VTEX sellers.
* Set up a VTEX seller to sell products on VTEX marketplaces.
* Manage catalog mapping and product synchronization.
* Handle order fulfillment and payment processing.

## Before you begin

Before starting the integration between VTEX stores, ensure the following requirements are met:

**For marketplaces:**

* Ensure you have Admin access to manage sellers. Learn more in [Seller Manager](https://help.vtex.com/docs/tutorials/predefined-roles#seller-manager).

**For sellers:**

* Ensure you have Admin access to configure affiliates. For more information, see the release note [New permissions for accessing order configurations](https://help.vtex.com/announcements/2025-10-21-new-license-manager-resources-order-configurations).

**Shared requirements:**

* Define agreements on commissions, delivery policies, and return policies.
* Understand [marketplace strategies at VTEX](https://help.vtex.com/docs/tutorials/marketplace-strategies-at-vtex).
* Learn about the [information shared between marketplace and seller](https://help.vtex.com/docs/tutorials/shared-information-between-a-marketplace-and-a-seller-on-vtex).

> ℹ️ To discover new partners within the VTEX ecosystem, use the [Marketplaces and Integrations](https://help.vtex.com/docs/tutorials/marketplaces-and-integrations) feature, which streamlines identification and communication between marketplaces and sellers.

## [SELLER] Step 1 - Configuring the seller

This section guides sellers through the configurations necessary to sell products on VTEX marketplaces.

### Define sales channels

Determine the sales channel configuration for your marketplace integration:

1. Evaluate if you need specific configurations for the marketplace integration or if you can use your default sales channel.
2. If necessary, [configure a marketplace trade policy](https://help.vtex.com/docs/tutorials/configuring-a-marketplace-trade-policy) with the appropriate settings for product assortment, pricing, promotions, and logistics.

  > ℹ️ You can use the same sales channel to integrate with multiple marketplaces. [Requesting additional trade policies](/en/docs/tutorials/requesting-an-additional-trade-policy) to integrate with other VTEX stores is free of charge.

**Managing product assortment:**

* Use sales channels to control which products you want to send to the marketplace.
* Avoid using [collections](https://help.vtex.com/docs/tutorials/creating-a-product-collection) as the main control mechanism, as they were designed for storefront merchandising, not for core catalog logic.

**Configuring promotions:**

* You don't need a marketplace-specific sales channel just for promotions.
* Segment promotions using the [affiliate](https://help.vtex.com/docs/tutorials/what-is-an-affiliate).
* See [Configuring promotions for marketplaces](/en/docs/tutorials/configuring-promotions-for-marketplaces) for more information.

### Create an affiliate ID

The [affiliate](https://help.vtex.com/docs/tutorials/what-is-an-affiliate) is the code that identifies the marketplace where your products will be sold. Each marketplace must have a unique affiliate.

To create an affiliate:

1. In the VTEX Admin, go to **Store Settings > Orders > Settings**.
2. In the **Affiliates** tab, click `+ New Affiliate`.
3. Fill in the required fields. For detailed information about these fields, see [Configuring affiliates](https://help.vtex.com/docs/tutorials/configuring-affiliates).
4. Click `Save` to create the affiliate.

  > ℹ️ After creating the affiliate, provide the affiliate ID to the marketplace operator. The marketplace will use this ID when adding your store as a seller.

## [MARKETPLACE] Step 2 - Configuring the marketplace

This section guides marketplace operators through the necessary configurations to receive and sell products from VTEX sellers.

### Define sales channels

[Sales channels](https://help.vtex.com/docs/tutorials/how-trade-policies-work) determine the product assortment, prices, payments, promotions, customer segmentation, and shipping strategy for your marketplace.

To define sales channels for your marketplace:

1. Evaluate if you need different configurations for sellers in your marketplace. If all sellers use the same configurations, use your default sales channel.
2. If you need specific settings, [create a new trade policy](https://help.vtex.com/docs/tutorials/creating-a-trade-policy) for marketplace operations.
3. Configure the sales channel with the appropriate settings for catalog, pricing, promotions, and logistics.

> ℹ️ The same sales channel can be used to integrate with multiple sellers. [Requesting additional trade policies](https://help.vtex.com/docs/tutorials/requesting-an-additional-trade-policy) to integrate with other VTEX stores is free of charge.

### Add sellers to your marketplace

After defining sales channels, add VTEX sellers to your marketplace:

1. In the VTEX Admin, go to **Marketplace > Management**.
2. Click `Add Seller`.
3. Select **VTEX Seller** as the integration type.
4. Complete the required fields. For detailed information about these fields, see [Adding a seller](https://help.vtex.com/docs/tutorials/adding-a-seller).
5. Click `Save` to add the seller to your marketplace.

  > ℹ️ In a VTEX-VTEX integration, the seller is displayed in the marketplace storefront, allowing shoppers to choose from available sellers during their shopping experience.

### Configure the storefront

Configure your marketplace storefront to display seller information during the shopping experience.

**For Legacy CMS Portal stores:**

Add the following controls to your ecommerce templates:

* `<vtex.cmc:sellerDescription />`: Displays the seller's name and logo for the product.
* `<vtex.cmc:SellerOptions />`: Shows sellers offering the product, prices, and installment options.
* `<vtex.cmc:sellerInfo />`: Displays detailed seller information on the seller details page.

**For VTEX IO stores:**

Install the [Seller Selector](https://developers.vtex.com/docs/apps/vtex.seller-selector) app to:

* Display the number of sellers offering each product.
* Allow customers to compare prices from different sellers.
* Enable customers to add products from their preferred seller to the cart.

### Configure payments

Configure payment processing for your marketplace. There are different scenarios for payment processing in VTEX marketplaces:

* **Marketplace processes payments:** The marketplace receives payments and distributes the amounts to sellers according to commission agreements.
* **Seller processes payments:** Each seller receives payments directly for their orders.
* **Split payment:** Payment is divided between the marketplace and the seller according to predefined rules.

For detailed information on payment configurations, see [Payments in VTEX Marketplace](https://help.vtex.com/docs/tutorials/payments-in-vtex-marketplaces).

## [SELLER] Step 3 - Reindexing the database

After the marketplace adds the seller, it's time to send the seller's product catalog by reindexing the database. This process:

* Prepares SKU and product information.
* Sends catalog, price, and inventory data to the marketplace.
* Updates the marketplace with the current product assortment.

To reindex the database:

1. Open your browser and access the following URL, replacing `{storename}` with your store's account name:

`{storename}.vtexcommercestable.com.br/admin/Site/FullCleanUp.aspx`

2. Click the `Reindex database` button to start the process.
3. Monitor the reindexing progress in the VTEX Admin at **Catalog > Reports**.

  > ℹ️ Only the [sponsor user (owner)](https://help.vtex.com/docs/tracks/what-is-the-master-user) has permission to reindex the database. During reindexing, products remain available for sale on your store while being queued for information updates.

## [MARKETPLACE] Step 4 - Mapping catalog architecture

After the seller sends products to the marketplace, the marketplace must map the seller's catalog to match its own structure. This ensures products are properly categorized and displayed on the marketplace.

1. In the VTEX Admin, go to **Marketplace > Sellers > Catalog Mapping**.
2. Select the seller whose catalog you want to map.
3. For each unmapped category, brand, and specification, select the corresponding category, brand, or specification from your marketplace catalog.
4. Create a new category, brand, or specification in your catalog if necessary before mapping.
5. Click `Save` to confirm the mappings.

For detailed mapping instructions, see [Mapping categories, brands, and specifications for the marketplace](https://help.vtex.com/docs/tutorials/mapping-categories-and-brands-for-the-marketplace).

## [MARKETPLACE] Step 5 - Approving and cataloging seller products

After mapping the catalog architecture, the marketplace must approve and catalog the seller's products before they become available to customers.

### Review received SKUs

Review the SKUs sent by the seller:

1. In the VTEX Admin, go to **Marketplace > Sellers > Received SKUs**.
2. Filter by the seller to view their submitted SKUs.
3. Review product information, images, descriptions, and specifications.
4. Verify pricing and inventory information.

### Approve SKUs

Approve SKUs to make them available on your marketplace:

1. Select the SKUs you want to approve.
2. Click `Approve` to add them to your marketplace catalog.
3. The approved SKUs will be associated with the mapped categories, brands, and specifications.

  > ℹ️ You can set up automatic approval for trusted sellers to streamline cataloging. For more information, see [Cataloging received SKUs](https://help.vtex.com/docs/tutorials/manual-sku-cataloging).

### Verify product availability

After approval, verify that products appear correctly on your marketplace:

1. Check the marketplace storefront to confirm products are visible.
2. Verify that product information, images, and prices display correctly.
3. Test the purchase flow to ensure orders can be placed successfully.
4. Confirm that seller information appears correctly when configured to be visible.
