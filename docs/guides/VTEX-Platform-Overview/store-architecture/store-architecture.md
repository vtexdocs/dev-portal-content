---
title: "Store architecture"
slug: "store-architecture"
hidden: false
createdAt: "2024-05-23T13:08:55.338Z"
updatedAt: "2024-05-24T15:56:00.000Z"
excerpt: "Learn how our store architecture models are tailored to meet diverse business needs."
seeAlso:
 - "/docs/guides/understanding-vtex-reference-architectures"
---

Store architecture diagrams represent the fundamental structure for a particular project, providing a unified vision to all stakeholders and translating business needs into software components and project requirements. In this guide, we present an overview of basic store architecture models at VTEX.

There are different types and levels of architecture, but they generally work as a reference for technical and business teams. Moreover, store architectures define for all stakeholders the roles and responsibilities of each player, how different systems interoperate, and how data is transmitted between them.

To demonstrate how VTEX integrates with the ecosystem, we created VTEX reference architecture models based on common digital commerce strategies. These blueprints illustrate interactions between VTEX modules and the business, serving as a project starting point. Learn more about the structure of these models in [Understanding VTEX reference architectures](https://developers.vtex.com/docs/guides/understanding-vtex-reference-architectures).

The main use cases for common scenarios are the following:

- [Business-to-customer (B2C)](#business-to-customer-b2c)
- [Business-to-business (B2B)](#business-to-business-b2b)
- [Franchise accounts (Omnichannel)](#franchise-accounts-omnichannel)
- [Multi-language and Multi-currency](#multi-language-and-multi-currency)
  - [Single account, multi-bindings](#single-account-multi-bindings)
  - [Multi-account](#multi-account)
 
>ℹ️ The following diagrams represent one single VTEX account and assume that the customer is using the [Store Framework](https://developers.vtex.com/docs/guides/store-framework) as a storefront solution.

## Business-to-customer (B2C)

Business-to-customer (B2C) is the most common business model within VTEX customers. It serves as a foundation for other models.

The diagram below shows the main components of a B2C commerce implementation. Components highlighted in pink are offered out-of-the-box (OOTB) by VTEX, but the diagram also shows other parts that may come from customers' internal back office systems or third-party providers.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/store-architecture/basic-b2c.png)

Below is an integration flow diagram in a B2C architecture, where the asynchronous calls (not in real time) are represented by black arrows, and synchronous calls are represented by blue arrows (real time).

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/store-architecture/b2c-integration-flow.png)

An example of an asynchronous call is the stock update, which is represented by a black arrow pointing from the ERP to the Inventory module. A real-time update of rates in a payment is represented by a blue arrow, with information exchange in both blocks. This last scenario is synchronous because it is a sensitive stage of the customer’s purchase flow.

The architecture suggested here may go beyond B2C, as you can see in the following sections.

## Business-to-business (B2B) with B2B Suite

The main characteristic of a [business-to-business (B2B)](https://help.vtex.com/en/tutorial/b2b-overview--5vb9SNXhX2bZnkpAh7ADdC) model is that transactions occur between two or more legal entities.

The diagram below presents an example where the business model is a B2B using the [B2B Suite](https://developers.vtex.com/docs/apps/vtex.b2b-suite), which is represented within the **B2B Core Modules**. In this architecture, the main account acts as a marketplace for other VTEX sellers.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/store-architecture/basic-b2b.png)

The B2B Suite is a set of VTEX IO apps tailored to streamline B2B store management. This collection of apps empower the store to oversee organizations (the companies enabled to make purchases in the store), as well as other functions and permissions for storefront and checkout. For instance, the store can offer specific price tables, collections, and custom payments methods for organizations, customers can have different user roles within organizations, among other features.

The main account has more modules than the sellers, sharing just some, such as the [Order Management System (OMS)](https://developers.vtex.com/docs/guides/orders-overview) and [Catalog](https://developers.vtex.com/docs/guides/catalog-overview), as you can see in the diagram below.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/store-architecture/basic-b2b-suite.png)

Declaring these modules in the architecture not only makes the process clearer but also makes the visualization of player responsibilities easier to understand. In this case, for example, [Master Data](https://developers.vtex.com/docs/guides/master-data-introduction) remains with the sellers because customer approval is done at the seller level.

In B2B scenarios, real-time communication between the B2B Suite and sellers is common, as the information is always up-to-date, and also for any calculations of fees and taxes at checkout, since the end customer needs to have a smooth purchasing experience.

In the diagram above you can see the synchronous communication between the [Organizations](https://developers.vtex.com/docs/apps/vtex.b2b-organizations) component in the main account and the sellers.

### Why choose this architecture?

- **Streamlined Organization management**: Fosters efficient management of multiple [organizations](https://developers.vtex.com/docs/apps/vtex.b2b-organizations) from a centralized platform by grouping storefront users into organizations and dividing them into cost centers.
- **Customized user experience**: Tailor the user experience for each [organization](https://developers.vtex.com/docs/apps/vtex.b2b-organizations), providing personalized pricing, payment methods, and product catalogs to meet specific business needs.
- **Enhanced security and control**: Assign roles and permissions to B2B customers, ensuring appropriate access levels and maintaining control over sensitive information and transactions. Learn more in the [Storefront Permissions](https://developers.vtex.com/docs/apps/vtex.storefront-permissions) and [Storefront Permissions UI](https://developers.vtex.com/docs/apps/vtex.storefront-permissions-ui) apps documentation.
- **Optimized quoting system**: Facilitates [quote requests](https://developers.vtex.com/docs/guides/vtex-b2b-quotes) and its management, enhancing negotiation and ensuring accurate pricing by integrating the quote-to-order process.
- **Efficient Order Processing**: Simplifies the [checkout](https://developers.vtex.com/docs/apps/vtex.b2b-checkout-settings) process with shared shipping addresses for cost centers, reducing errors and streamlining order fulfillment.

### Learn more

- [B2B Suite - Overview](https://help.vtex.com/en/tutorial/b2b-suite-overview--5eG6UfveWrai7looK0kVG3)

## Franchise accounts (Omnichannel)

This is a very common architecture model that integrates physical stores with ecommerce as [franchise accounts](https://help.vtex.com/en/tutorial/what-is-a-franchise-account--kWQC6RkFSCUFGgY5gSjdl) in VTEX.

A franchise account is linked to a main account and has the following characteristics, which you can see in the reference architecture below:

- **No separate website**: Franchise accounts do not have their own dedicated website, as they operate within the main account's ecommerce, effectively acting as part of a larger [marketplace](https://help.vtex.com/en/tutorial/what-is-a-marketplace--680lLJTnmEAmekcC0MIea8).
- **Customer Data Storage**: Customer data is stored in the main account’s [Master Data](https://developers.vtex.com/docs/guides/master-data-introduction).
- **Seller Type**: Each franchise account automatically functions as a [white label seller](https://help.vtex.com/en/tutorial/seller-white-label--5orlGHyDHGAYciQ64oEgKa) within the main account.
- **Catalog**: Franchise accounts inherit their [catalog](https://developers.vtex.com/docs/guides/catalog-overview) from the main account.
- **Logistics and OMS**: Each franchise account has its own [Logistics](https://developers.vtex.com/docs/guides/fulfillment) settings and performs its own [Order Management](https://developers.vtex.com/docs/guides/orders-overview).
- **Prices and Payments**: Each franchise can have its own [price](https://developers.vtex.com/docs/guides/pricing-overview) and [payment](https://developers.vtex.com/docs/guides/payments-overview) methods, or they can inherit prices and payment methods from the main account.
- **Promotions**: It is possible to create [promotions](https://developers.vtex.com/docs/guides/promotions-overview) for each franchise account and for the main account.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/store-architecture/franchises-omni.png)

This architecture model works well for brands that have multiple physical stores, franchises, or representatives. In these cases, each physical store / franchise / representative can have a franchise account in VTEX integrated into the brand’s main account. This allows them to deliver the products sold through the brand’s ecommerce from an omnichannel perspective.

### Why choose this architecture?

- Potential to reduce the percentage of out-of-stock items.
- More shipping options, with the potential to reduce logistics costs.
- Physical stores can be configured as [pick-up points](https://help.vtex.com/en/tracks/unified-commerce-strategies--3WGDRRhc3vf1MJb9zGncnv/4hXfgqXxS1lwAfnxgja3xW).
- Physical stores can function as small warehouses, operating in the [ship from store](https://help.vtex.com/en/tracks/unified-commerce-strategies--3WGDRRhc3vf1MJb9zGncnv/50GAmxxFsJoLWqcnMysWdl) strategy.
- Possible gain from inventory reduction through the implementation of the [Endless Aisle](https://help.vtex.com/en/tracks/unified-commerce-strategies--3WGDRRhc3vf1MJb9zGncnv/40KMlmGI5tN0r0KPCDWgGn) strategy, which is done by using the [VTEX Sales App](https://help.vtex.com/en/tracks/instore-getting-started-and-setting-up--zav76TFEZlAjnyBVL5tRc/7fnnVlG3Kv1Tay9iagc5yf).

>ℹ️ The VTEX Sales App is available in Brazil and some LATAM countries. To know if it is available in your country, open a ticket to [VTEX Support](https://help.vtex.com/en/tutorial/abrir-chamados-para-o-suporte-vtex--16yOEqpO32UQYygSmMSSAM?locale=pt).

## Multi-language and Multi-currency

Some of our customers are present in multiple countries and want to have every local store running on VTEX. We provide a multi-language and multi-currency architecture for this scenario, explained in the following sections.

### Single account, multi-binding

In this architecture, a single VTEX account is configured to support multiple languages and currencies, using a [multidomain](https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/4yPqZQyj0t675QpcG7H6yl#multistore) approach.

The reference architecture below exemplifies its main characteristics:

- **Separated website**: One single account, but each store with its own domain, bound to different [trade policies](https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/4EPwTXx5oFdSG1dA3zIchz#trade-policy) by [bindings](https://help.vtex.com/en/tutorial/what-is-binding--4NcN3NJd0IeYccgWCI8O2W).
- **Search**: [Search Settings](https://developers.vtex.com/docs/guides/search-overview) are the same for all websites.
- **CMS**: Shared access to [Content Management System (CMS)](https://developers.vtex.com/docs/guides/vtex-io-documentation-cms) between websites.
- **Customer Data Storage**: One single [Master Data](https://developers.vtex.com/docs/guides/master-data-introduction) for all stores.
- **Catalog**: One single catalog, segmented by trade policies.
- **Logistics**: Each store has its logistics operation managed by different warehouses in the same Logistics panel.
- **Order Management System (OMS)**: One single Order Management System panel for all stores.
- **Payments**: Shared Payment settings between all stores.
- **Prices and Promotions**: It is possible to configure different prices and promotions for each store, as you can segment them by trade policy. Still, prices and promotions for all stores are managed in the same panel.
- **Message Center**: One single [Message Center](https://help.vtex.com/en/tutorial/understanding-the-message-center--tutorials_84) for all stores.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/store-architecture/multi-currency-language-single-account.png)

This model is easier to set up, integrate, and maintain compared to the [multi-account](#multi-account) approach, but it may not be efficient for large and complex operations. This architecture is recommended for operations present in more than one country, requiring the configuration of different languages and currencies, but without the need for data segregation, as all core services are shared. Therefore, it may work well for operations managed by a single, centralized team.

#### Why choose this architecture?

- Supports [multi-currency](https://developers.vtex.com/docs/guides/vtex-io-documentation-internationalizing-product-prices) natively.
- Supports multi-language with [Messages](https://developers.vtex.com/docs/guides/storefront-content-internationalization) and [Catalog Translation App](https://developers.vtex.com/docs/guides/catalog-internationalization).

>⚠ Product names are not translated on the [Checkout](https://help.vtex.com/en/tutorial/checkout-vtex-overview--7wcprkM7yZUflOqbzAN5SI) and [My Account](https://help.vtex.com/en/tutorial/how-my-account-works--2BQ3GiqhqGJTXsWVuio3Xh) pages. These modules directly call the Catalog API to get product data, so the information does not pass through the Messages API.

### Multi-account

In this architecture, one main account will act as a [seller](https://help.vtex.com/en/tutorial/what-is-a-seller--5FkLvhZ3Few4CWWIuYOK2w) in secondary accounts that act as [marketplaces](https://help.vtex.com/en/tutorial/configuring-the-marketplace-between-vtex-stores--tutorials_6520). 

The reference architecture below exemplifies its main characteristics:

- **Separated VTEX account**: Each store has its own VTEX account.
- **Separated website**: Each store has its own website and may customize its frontend with a different style per store.
- **Customer Data Storage**: Segregated by marketplace account. There is no customer information within the main account’s [Master Data](https://developers.vtex.com/docs/guides/master-data-introduction).
- **Promotions**: Promotions from the main account have limited capabilities, as every information that comes from the customer will not be accessible by the main account. For example, if you want to create promotions for a customer cluster in the main account, it will not work because it does not have access to the marketplace’s Master Data.
- **Checkout, Order Management System (OMS), Payments, and Message Center**: Each store manages these modules independently in its own Admin panel, without relying on the main account.
- **Catalog, Pricing, and Logistics**: The main account is the source of truth for these [VTEX Core services](https://developers.vtex.com/docs/guides/getting-started#vtex-core-services), but the management of them are independent, as each account has its own Admin panel. The product assortment can vary between accounts but is always based on the main account's catalog, as the main account is the owner of the it.

>⚠ [Assembly options](https://developers.vtex.com/docs/guides/assembly-options-app), [attachments](https://help.vtex.com/tutorial/what-is-an-attachment--aGICk0RVbqKg6GYmQcWUm), and [services](https://help.vtex.com/en/tutorial/what-is-a-service--46Ha8CEEQoC6Y40i6akG0y) are not supported.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/store-architecture/multi-currency-language-multi-account.png)

This architecture is recommended for operations in more than one country, requiring the configuration of different languages and currencies, where different teams manage each localized store.

#### Why choose this architecture?

- Supports both single fulfillment (all items shipped from one account) and multiple fulfillment (items shipped from different accounts within the same purchase), ensuring efficiency by optmizing logistics based on item availability and proximity to the customer.
- Having the seller (main account) act as catalog owner and the accounts for each country act as marketplaces enables a multi-language solution. This allows each store to manage its language and currency locally within its own store.
- Support better translations compared to the [single account, multi-binding](#single-account-multi-binding) model, as there is an **independent catalog translation**. Therefore, you do not need to rely on [Messages](https://developers.vtex.com/docs/guides/storefront-content-internationalization) or [Catalog translation app](https://developers.vtex.com/docs/guides/catalog-internationalization).

### Learn more

- [Accounts and architecture](https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/4yPqZQyj0t675QpcG7H6yl)
- [Choosing between a multi-store architecture or an additional environment](https://help.vtex.com/en/tutorial/choosing-between-a-multi-store-architecture-or-an-additional-environment--4HRNpa1OCKZ5YzP8yiilBL)
