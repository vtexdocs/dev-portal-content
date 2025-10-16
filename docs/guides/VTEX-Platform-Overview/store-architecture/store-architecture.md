---
title: "Store architecture"
slug: "store-architecture"
hidden: false
createdAt: "2024-05-23T13:08:55.338Z"
updatedAt: "2025-10-16T18:23:22.662Z"
excerpt: "Learn how our store architecture models are tailored to meet different business needs."
seeAlso:
 - "/docs/guides/understanding-vtex-reference-architectures"
---

Store architecture diagrams represent the fundamental structure of a particular project, providing a unified vision to all stakeholders and translating business needs into software components and project requirements. In this guide, we present an overview of basic store architecture models on VTEX.

There are different types and levels of architecture, but they generally work as a reference for technical and business teams. Additionally, store architectures define the roles and responsibilities of each player for all stakeholders while explaining how different systems interoperate and how data is transmitted between them.

To demonstrate how VTEX integrates with the ecosystem, we have created VTEX reference architecture models based on common digital commerce strategies. These blueprints illustrate interactions between VTEX modules and the business, serving as a starting point for projects. Learn more about the structure of these models in [Understanding VTEX reference architectures](https://developers.vtex.com/docs/guides/understanding-vtex-reference-architectures).

These are the main use cases for common scenarios:

- [Business-to-customer (B2C)](#business-to-customer-b2c)
- [Business-to-business (B2B)](#business-to-business-b2b)
- [Franchise accounts (Omnichannel)](#franchise-accounts-omnichannel)
- [Multi-language and multi-currency](#multi-language-and-multi-currency)
  - [Single account, multi-bindings](#single-account-multi-bindings)
  - [Multi-account](#multi-account)

>ℹ️ Except for the [Headless](#headless) architecture, the following diagrams consider the client is using [Store Framework](https://developers.vtex.com/docs/guides/store-framework) as a storefront solution.

## Business-to-customer (B2C)

Business-to-customer (B2C) is the most common business model among VTEX clients and serves as a foundation for other models.

The diagram below illustrates the main components of a B2C commerce implementation. Components highlighted in pink are offered out-of-the-box (OOTB) by VTEX. However, the diagram also includes other parts that may be integrated from the client's internal back-office systems or third-party providers.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/store-architecture/basic-b2c.png)

Below is an integration flow diagram in a B2C architecture, where asynchronous calls (not in real time) are represented by black arrows, and synchronous calls (in real time) are represented by blue arrows.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/store-architecture/b2c-integration-flow.png)

An example of an asynchronous call is the stock update, represented by a black arrow pointing from the ERP to the Inventory module. A real-time update of payment rates is represented by a blue arrow, with information exchanged between both blocks. This last scenario is synchronous because it occurs in a critical stage of the customer purchase flow.

The architecture suggested here extends beyond B2C, as you can see in the following sections.

## Business-to-business (B2B) with B2B Suite

The main characteristic of a [business-to-business (B2B)](https://help.vtex.com/en/tutorial/b2b-overview--5vb9SNXhX2bZnkpAh7ADdC) model is that transactions occur between two or more legal entities.

The diagram below presents an example of a B2B business model using [B2B Suite](https://developers.vtex.com/docs/apps/vtex.b2b-suite), represented within the **B2B Core Modules**. In this architecture, the main account acts as a marketplace for other VTEX sellers.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/store-architecture/basic-b2b.png)

B2B Suite is a set of VTEX IO apps tailored to streamline B2B store management. This collection of apps enables the store to manage organizations (the companies enabled to make purchases in the store) and other functions and permissions for storefront and checkout. For instance, the store can offer specific price tables, collections, and custom payment methods for organizations. Besides, clients can have different user roles within organizations, among other features.

The main account has access to more modules than the sellers, sharing only some of them, such as the [Order Management System (OMS)](https://developers.vtex.com/docs/guides/orders-overview) and [Catalog](https://developers.vtex.com/docs/guides/catalog-overview) modules, as you can see in the diagram below.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/store-architecture/basic-b2b-suite.png)

Declaring these modules in the architecture not only makes the process clearer but also makes it easier to understand the responsibilities of each player. In this case, for example, [Master Data](https://developers.vtex.com/docs/guides/master-data) remains with the sellers because customer approvals are handled at the seller level.

In B2B scenarios, real-time communication between the B2B Suite and sellers is common, as the information is always up-to-date. This is also crucial for fee and tax calculations at checkout to ensure a smooth purchasing experience for the end customer.

In the diagram above, you can see the synchronous communication between the [Organizations](https://developers.vtex.com/docs/apps/vtex.b2b-organizations) component in the main account and the sellers.

### Why choose this architecture?

- **Streamlined organization management**: Manage multiple [organizations](https://developers.vtex.com/docs/apps/vtex.b2b-organizations) from a centralized platform by grouping storefront users into organizations and dividing them into cost centers.
- **Customized user experience**: Tailor the user experience for each [organization](https://developers.vtex.com/docs/apps/vtex.b2b-organizations), providing personalized pricing, payment methods, and product catalogs to meet specific business needs.
- **Enhanced security and control**: Assign roles and permissions to B2B clients, ensuring appropriate access levels and maintaining control over sensitive information and transactions. Learn more in the [Storefront Permissions](https://developers.vtex.com/docs/apps/vtex.storefront-permissions) and [Storefront Permissions UI](https://developers.vtex.com/docs/apps/vtex.storefront-permissions-ui) app documentation.
- **Optimized quoting system**: Facilitate [quote requests](https://developers.vtex.com/docs/guides/vtex-b2b-quotes) and management, enhancing negotiations and ensuring accurate pricing by integrating the quote-to-order process.
- **Efficient order processing**: Simplify the [checkout](https://developers.vtex.com/docs/apps/vtex.b2b-checkout-settings) process with shared shipping addresses for cost centers, reducing errors and streamlining order fulfillment.

### Learn more

- [B2B Suite - Overview](https://help.vtex.com/en/tutorial/b2b-suite-overview--5eG6UfveWrai7looK0kVG3)

## Franchise accounts (omnichannel)

This is a very common architecture model that integrates physical stores with ecommerce as [franchise accounts](https://help.vtex.com/en/tutorial/what-is-a-franchise-account--kWQC6RkFSCUFGgY5gSjdl) on VTEX.

A franchise account is linked to a main account and has the following characteristics:

- **No separate website**: Franchise accounts have no dedicated website. Instead, they operate within the main account's ecommerce site as part of a larger [marketplace](https://help.vtex.com/en/tutorial/what-is-a-marketplace--680lLJTnmEAmekcC0MIea8).
- **Customer data storage**: Customer data is stored in the main account's [Master Data](https://developers.vtex.com/docs/guides/master-data).
- **Seller type**: Each franchise account automatically operates as a [white-label seller](https://help.vtex.com/en/tutorial/seller-white-label--5orlGHyDHGAYciQ64oEgKa) within the main account.
- **Catalog**: Franchise accounts inherit their [catalog](https://developers.vtex.com/docs/guides/catalog-overview) from the main account.
- **Logistics and OMS**: Each franchise account has its own [logistics](https://developers.vtex.com/docs/guides/fulfillment) settings and performs its own [order management](https://developers.vtex.com/docs/guides/orders-overview).
- **Prices and payments**: Each franchise can have its own [pricing](https://developers.vtex.com/docs/guides/pricing-overview) and [payment](https://developers.vtex.com/docs/guides/payments-overview) methods, or they can inherit these from the main account.
- **Promotions**: [Promotions](https://developers.vtex.com/docs/guides/promotions-overview) can be created for each franchise account and for the main account.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/store-architecture/franchises-omni.png)

This architecture model works well for brands with multiple physical stores, franchises, or representatives. In these cases, each physical store/franchise/representative can have a franchise account on VTEX integrated with the brand's main account. This allows them to deliver the products sold through the brand's ecommerce site from an omnichannel perspective.

### Why choose this architecture?

- Potential to reduce the percentage of out-of-stock items.
- More shipping options, potentially reducing logistics costs.
- Physical stores can be configured as [pickup points](https://help.vtex.com/en/tracks/unified-commerce-strategies--3WGDRRhc3vf1MJb9zGncnv/4hXfgqXxS1lwAfnxgja3xW).
- Physical stores can operate as small warehouses, using the [ship-from-store](https://help.vtex.com/en/tracks/unified-commerce-strategies--3WGDRRhc3vf1MJb9zGncnv/50GAmxxFsJoLWqcnMysWdl) strategy.
- Possible inventory reduction through the implementation of the [Endless Aisle](https://help.vtex.com/en/tracks/unified-commerce-strategies--3WGDRRhc3vf1MJb9zGncnv/40KMlmGI5tN0r0KPCDWgGn) strategy through [VTEX Sales App](https://help.vtex.com/en/tracks/instore-getting-started-and-setting-up--zav76TFEZlAjnyBVL5tRc/7fnnVlG3Kv1Tay9iagc5yf).

>ℹ️ VTEX Sales App is available in Brazil and some LATAM countries. To check if it's available in your country, open a ticket with [VTEX Support](https://help.vtex.com/en/tutorial/opening-tickets-to-vtex-support--16yOEqpO32UQYygSmMSSAM).

## Multi-language and multi-currency

Some of our clients operate in multiple countries and want to have each local store running on VTEX. We provide a multi-language and multi-currency architecture for this scenario, which is explained in the following sections.

### Single account, multi-binding

In this architecture, a single VTEX account is configured to support multiple languages and currencies using a [multi-domain](https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/4yPqZQyj0t675QpcG7H6yl#multistore) approach.

The reference architecture below exemplifies its main characteristics:

- **Separate website**: A single account, but each store with its own domain, bound to different [trade policies](https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/4EPwTXx5oFdSG1dA3zIchz#trade-policy) by [bindings](https://help.vtex.com/en/tutorial/what-is-binding--4NcN3NJd0IeYccgWCI8O2W).
- **Search**: Same [search settings](https://developers.vtex.com/docs/guides/search-overview) for all websites.
- **CMS**: Shared access to the [Content Management System (CMS)](https://developers.vtex.com/docs/guides/vtex-io-documentation-cms) between websites.
- **Customer data storage**: A single [Master Data](https://developers.vtex.com/docs/guides/master-data) for all stores.
- **Catalog**: A single catalog segmented by trade policies.
- **Logistics**: Each store manages its logistics through different warehouses in the same logistics panel.
- **Order Management System (OMS)**: A unified OMS panel for all stores.
- **Payments**: Shared payment settings across all stores.
- **Prices and promotions**: Different prices and promotions can be configured for each store, segmented by trade policy. Still, prices and promotions for all stores are managed in the same panel.
- **Message Center**: A single [Message Center](https://help.vtex.com/en/tutorial/understanding-the-message-center--tutorials_84) for all stores.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/store-architecture/multi-currency-language-single-account.png)

This model is easier to set up, integrate, and maintain compared to the [multi-account](#multi-account) approach, but it may not be efficient for large and complex operations. This architecture is recommended for operations across multiple countries that require configuring different languages and currencies but don't require data segregation, as all core services are shared. Therefore, it may work well for operations managed by a single, centralized team.

#### Why choose this architecture?

- Supports [multi-currency](https://developers.vtex.com/docs/guides/vtex-io-documentation-internationalizing-product-prices) natively.
- Supports multi-language with [Messages](https://developers.vtex.com/docs/guides/storefront-content-internationalization) and the [Catalog translation app](https://developers.vtex.com/docs/guides/catalog-internationalization).

>⚠ Product names aren't translated on the [Checkout](https://help.vtex.com/en/tutorial/checkout-vtex-overview--7wcprkM7yZUflOqbzAN5SI) and [My Account](https://help.vtex.com/en/tutorial/how-my-account-works--2BQ3GiqhqGJTXsWVuio3Xh) pages. These modules call the Catalog API directly to retrieve product data, so the information doesn't pass through the Messages API.

### Multi-account

In a multi-account architecture, a brand operates multiple VTEX accounts (typically one per country or market), allowing each to be independently localized and operated. It's recommended for operations across multiple countries that require configuring different languages and currencies, where different teams manage each localized store.

There are two variants, depending on how back-office systems like ERP, PIM, and WMS are integrated: 
* [Shared back-office systems](#multi-account-shared-back-office-systems)
* [Independent back-office systems](#multi-account-independent-back-office-systems)

#### Multi-account, shared back-office systems

In this model, a main account acts as a [seller](https://help.vtex.com/en/tutorial/what-is-a-seller--5FkLvhZ3Few4CWWIuYOK2w) in secondary accounts that act as [marketplaces](https://help.vtex.com/en/tutorial/configuring-the-marketplace-between-vtex-stores--tutorials_6520).

The reference architecture below exemplifies its main characteristics:

- **Separate VTEX account**: Each store operates with its own VTEX account.
- **Separate website**: Each store has its own website and can customize a different frontend style.
- **Customer data storage**: Customer data is segregated by marketplace account. No customer information is stored within the main account's [Master Data](https://developers.vtex.com/docs/guides/master-data).
- **Promotions**: Promotions from the main account have limited capabilities because the main account can't access customer data from the marketplace. For example, if you want to create promotions for a customer cluster in the main account, it will not work because the account doesn't have access to the marketplace Master Data. Additionally, promotions configured in the marketplace based on a seller's [payment methods](https://newhelp.vtex.com/en/docs/tutorials/difference-between-payment-methods-and-payment-conditions) don't work. Learn more in [Configuring promotions for marketplaces](https://newhelp.vtex.com/en/docs/tutorials/configuring-promotions-for-marketplaces).
- **Checkout, Order Management System (OMS), Payments, and Message Center**: Each store manages these modules independently in its own Admin, without relying on the main account.
- **Catalog, Pricing, and Logistics**: The main account is the source of truth for these [VTEX Core services](https://developers.vtex.com/docs/guides/getting-started#vtex-core-services), but management is independent, as each account has its own Admin. The product assortment can vary between accounts, but it's always based on the main account's catalog, as the main account is the owner.

>⚠ [Assembly options](https://developers.vtex.com/docs/guides/assembly-options-app) and [services](https://help.vtex.com/en/tutorial/what-is-a-service--46Ha8CEEQoC6Y40i6akG0y) are not supported. [Attachments](https://help.vtex.com/tutorial/what-is-an-attachment--aGICk0RVbqKg6GYmQcWUm) only work if configured in the seller account.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/store-architecture/multi-currency-language-multi-account.png)

##### Why choose this architecture?

- Supports both single fulfillment (all items shipped from one account) and multiple fulfillment (items shipped from different accounts within the same purchase), ensuring efficiency by optimizing logistics based on item availability and proximity to the customer.
- Having the seller (main account) act as catalog owner and the accounts for each country act as marketplaces enables a multi-language solution. This allows each store to manage its language and currency locally within its own environment.
- Supports better translations compared to the [single account, multi-binding](#single-account-multi-binding) model, as there is an **independent catalog translation**. Therefore, you don't need to rely on [Messages](https://developers.vtex.com/docs/guides/storefront-content-internationalization) or the [Catalog translation app](https://developers.vtex.com/docs/guides/catalog-internationalization).
- The catalog can be translated in the marketplace after the seller sends the item.

#### Multi-account, independent back-office systems

In this model, each country/region operates with its own back-office, resulting in greater operational and integration autonomy.

The reference architecture below exemplifies its main characteristics:

- **Separate VTEX account**: Each store operates with its own VTEX account.
- **Separate website**: Each store has its own website and can customize a different frontend style.
- **Customer data storage**: Customer data is segregated by account. No customer information is shared between accounts, as each has its own [Master Data](https://developers.vtex.com/docs/guides/master-data).
- **Promotions**: Different promotions can be configured for each store. If any individual account runs a [marketplace with external sellers](https://developers.vtex.com/docs/guides/external-seller-integration-architecture), the seller-marketplace limitations are applied within that specific relation, but that is separate from the cross-country independence model. Learn more about these restrictions in [Configuring promotions for marketplaces](https://newhelp.vtex.com/en/docs/tutorials/configuring-promotions-for-marketplaces).
- **Checkout, Order Management System (OMS), Payments, and Message Center**: Each store manages these modules independently in its own Admin.
- **Catalog, Pricing, and Logistics**: Each store manages these [VTEX Core services](https://developers.vtex.com/docs/guides/getting-started#vtex-core-services) independently. Integrations are not shared between accounts.

##### Why choose this architecture?

- Supports both single fulfillment (all items shipped from one account) and multiple fulfillment (items shipped from different accounts within the same purchase), ensuring efficiency by optimizing logistics based on item availability and proximity to the customer.
- Having the seller (main account) act as catalog owner and the accounts for each country act as marketplaces enables a multi-language solution. This allows each store to manage its language and currency locally within its own environment.
- Support better translations compared to the [single account, multi-binding](#single-account-multi-binding) model, as there is an **independent catalog translation**. Therefore, you don't need to rely on [Messages](https://developers.vtex.com/docs/guides/storefront-content-internationalization) or the [Catalog translation app](https://developers.vtex.com/docs/guides/catalog-internationalization).

#### Learn more

- [Accounts and architecture](https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/4yPqZQyj0t675QpcG7H6yl)
- [Choosing between a multi-store architecture or an additional environment](https://help.vtex.com/en/tutorial/choosing-between-a-multi-store-architecture-or-an-additional-environment--4HRNpa1OCKZ5YzP8yiilBL)

## Headless

In a headless architecture, the frontend (or "head") is decoupled from the backend. This allows the user interface to be built with any technology while the backend supplies the data and functionality, providing greater flexibility and scalability.

The frontend layer includes font type, colors, styles, images, buttons, etc. The backend manages the ecommerce functionality, pricing, infrastructure, security, checkout, and more. This architecture allows stores to fully control the user experience on the storefront while customizing backend to meet their specific needs.

![headless](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/store-architecture/headless.png)

The diagram above represents an account implemented with [FastStore](https://developers.vtex.com/docs/guides/faststore), the VTEX native solution that allows developers to build headless storefronts. It outlines the main components of a headless implementation, providing an overview that can be expanded to address specific business needs.

>ℹ️  If your store uses a third-party Content Management System (CMS) instead of VTEX storefront solutions, you can leverage VTEX APIs to build a headless shopping experience. Learn more in the [Headless Commerce](https://developers.vtex.com/docs/guides/headless-commerce) guide and the Pragmatic Composability section in the [Composability](https://developers.vtex.com/docs/guides/composability#pragmatic-composability) guide.

### Why choose this architecture?

- **Flexibility:** A headless approach allows complete ownership over the website architecture.
- **Faster websites:** A headless ecommerce platform houses content centrally and can deliver it anywhere via APIs, allowing faster delivery compared to traditional ecommerce architecture.
- **Personalized experiences:** Stores can create customizable experiences and adapt them to achieve the desired look and feel.
- **Low-risk experimentation:** Decoupling the backend from the frontend makes it simpler and less risky to make changes to the frontend, knowing that it won't impact the site's underlying backend architecture.
- **Seamless integration:** Stores can integrate their existing systems (ERP, PIM, OMS, etc.) to build a cohesive shopping experience using any programming language.

### Learn more

- [Headless CMS - Overview](https://help.vtex.com/en/tutorial/headless-cms-overview--3U5gvhHdQL0jczYH8gjX09)
