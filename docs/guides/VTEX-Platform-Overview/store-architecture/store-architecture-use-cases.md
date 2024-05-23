---
title: "Store architecture use cases"
slug: "store-architecture-use-cases"
hidden: false
createdAt: "2024-05-23T13:08:55.338Z"
updatedAt: "2024-05-23T13:08:55.338Z"
excerpt: "Learn how our store architecture models are tailored to meet diverse business needs."
seeAlso:
 - "/docs/guides/understanding-vtex-reference-architectures"
 - "/docs/guides/store-architecture"
---

Store architecture communicates project vision, translating business needs into software requirements, and offering references for technical and business teams. This guide will explore the main VTEX reference architectures to learn how the VTEX platform integrates with different digital commerce strategies.

>ℹ️ The diagrams were conceived according to the [Understanding VTEX reference architectures](https://developers.vtex.com/docs/guides/understanding-vtex-reference-architectures) guide.

## Business-to-customer (B2C)

The business-to-customer (B2C) is the most common business model in VTEX and the base for the other business models.

The diagram below shows the main components of a B2C commerce implementation, highlighting in pink the ones offered out-of-the-box (OOTB) by VTEX, also showing the other parts that may come from customers’ internal systems or third-party providers.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/store-architecture/basic-b2c.png)

>ℹ️ This diagram represents one single VTEX account and assumes that the customer is using the VTEX storefront solution.

Below is an integration flow diagram in a B2C architecture, where the asynchronous calls (not in real time) are represented by the black arrows, and synchronous calls represented by the blue arrows (real time).

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/store-architecture/b2c-integration-flow.png)

An example of an asynchronous call is the stock update, which is represented by a black arrow pointing from the ERP to the Inventory module. A real-time update of rates in a payment is represented by a blue arrow, with information exchange in both blocks. This last scenario is synchronous because it is a sensitive stage of the customer’s purchase flow.

The architecture suggested here may go further than just B2C, as you can see in the following diagrams.

## Business-to-business (B2B) with B2B Suite

The main characteristic of a [business-to-business (B2B)](https://help.vtex.com/en/tutorial/b2b-overview--5vb9SNXhX2bZnkpAh7ADdC) model is that transactions occur between two or more legal entities. 

The diagram below presents an example where the business model is a B2B using the [B2B Suite](https://developers.vtex.com/docs/apps/vtex.b2b-suite), which is represented within the **B2B Core Modules**. In this architecture, the main account acts as a marketplace for other VTEX sellers.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/store-architecture/basic-b2b.png)

The B2B Suite is a set of VTEX IO apps tailored to streamline B2B store management. This collection of apps empower the store to oversee organizations (the companies enable to make purchases in the store), as well as other functions and permissions for storefront and checkout. For instance, it prevents an organization from changing its address, offers special price tables, custom payments methods, user roles, among others settings.

The main account has more modules than the sellers, sharing just some, such as the [Order Management System (OMS)](https://developers.vtex.com/docs/guides/orders-overview) and [Catalog](https://developers.vtex.com/docs/guides/catalog-overview), as you can see in the diagram below.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/store-architecture/basic-b2b-suite.png)

Declaring these modules in the architecture not only makes the process clearer but also makes the visualization of player responsibilities easier to understand. In this case, for example, [Master Data](https://developers.vtex.com/docs/guides/master-data-introduction) remains with the sellers because customer approval is done at the seller level.

In B2B scenarios, real-time communication between the B2B Suite and sellers is common, as the information is always up-to-date, and also for any calculations of fees and taxes at checkout, since the end customer needs to have a smooth purchasing experience.

In the diagram above you can see the synchronous communication between [Organizations](https://developers.vtex.com/docs/apps/vtex.b2b-organizations) component in the main account and the sellers.

### Why choose this architecture?

- **Streamlined Organization management**: Fosters efficient management of multiple organizations from a centralized platform by grouping storefront users into organizations and dividing them into cost centers. Shared order history, payment terms, and price lists enhance efficiency and promote cohesive collaboration across the organization.
- **Customized user experience**: Tailor the user experience for each organization or user group, providing personalized pricing, payment methods, and product catalogs to meet specific business needs.
- **Enhanced security and control**: Assign roles and permissions to users, ensuring appropriate access levels and maintaining control over sensitive information and transactions.
- **Efficient Order Processing**: Simplify the checkout process with shared shipping addresses for cost centers, reducing eros and streamlining order fulfillment.
- **Improved communication and collaboration**: Facilitate communication between users within an organization and streamline the creation of new organizations through request forms and approval queues.

### Learn more

- [B2B Suite - Overview](https://help.vtex.com/pt/tutorial/b2b-suite-overview--5eG6UfveWrai7looK0kVG3)

## Franchise accounts (Omnichannel)

This is a very common architecture model that integrates physical stores with ecommerce as [franchise accounts](https://help.vtex.com/en/tutorial/what-is-a-franchise-account--kWQC6RkFSCUFGgY5gSjdl) in VTEX. 

A franchise account is linked to a main account and has the following characteristics, which you can see in the reference architecture below:

- **No separate website**: Franchise accounts do not have their own dedicated website, as they operate within the main account’s one, effectively acting as part of a larger [marketplace](https://help.vtex.com/pt/tutorial/o-que-e-um-marketplace--680lLJTnmEAmekcC0MIea8).
- **Customer Data Storage**: Customer data is stored in the main account’s [Master Data](https://developers.vtex.com/docs/guides/master-data-introduction).
- **Seller Type**: Each franchise account automatically functions as a [white label seller](https://help.vtex.com/en/tutorial/seller-white-label--5orlGHyDHGAYciQ64oEgKa) within the main account.
- **Catalog**: Franchise accounts inherit their [catalog](https://developers.vtex.com/docs/guides/catalog-overview) from the main account.
- **Logistics and OMS**: Each franchise account has its own [Logistics](https://developers.vtex.com/docs/guides/fulfillment) and performs its own [Order Management](https://developers.vtex.com/docs/guides/orders-overview).
- **Prices and Payments**: Each franchise can have its own [price](https://developers.vtex.com/docs/guides/pricing-overview) and [payment](https://developers.vtex.com/docs/guides/payments-overview) methods, or you can choose to inherit them from the main account.
- **Promotions**: It is possible to create [promotions](https://developers.vtex.com/docs/guides/promotions-overview) for each franchise account and for the main one.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/store-architecture/franchises-omni.png)

This architecture model works well for brands that have multiple physical stores, franchisees, or representatives. In these cases, each of them can have a franchise account in VTEX integrated into the brand’s main account. This allows them to deliver the products sold through the brand’s ecommerce from an Omnichannel perspective.

### Why choose this architecture?

- Potential to reduce the percentage of out-of-stock items.
- Possible gain from inventory reduction through the use of the [Endless Aisle](https://help.vtex.com/en/tracks/estrategias-de-comercio-unificado--3WGDRRhc3vf1MJb9zGncnv/40KMlmGI5tN0r0KPCDWgGn?&utm_source=autocomplete) feature.
- More shipping options, with the potential to reduce logistics costs.
- The physical stores can be configured as [pick-up points](https://help.vtex.com/en/tracks/unified-commerce-strategies--3WGDRRhc3vf1MJb9zGncnv/4hXfgqXxS1lwAfnxgja3xW).
- The physical stores can function as small warehouses, operating in the [ship from store](https://help.vtex.com/en/tracks/unified-commerce-strategies--3WGDRRhc3vf1MJb9zGncnv/50GAmxxFsJoLWqcnMysWdl?&utm_source=autocomplete) strategy.

### Learn more

- [Unified Commerce Strategies](https://help.vtex.com/en/tracks/estrategias-de-comercio-unificado--3WGDRRhc3vf1MJb9zGncnv/2LGAiUnHES1enjHsfi8fI3) 

## Multi-language and Multi-currency

Some of our customers are present in multiple countries and want to have every local store running on VTEX. We provide a multi-language and multi-currency architecture to serve this customer, as you can see below.

### Single account, multi-binding

In this architecture, a single VTEX account is configured to support multiple languages and currencies, using a [multidomain](https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/4yPqZQyj0t675QpcG7H6yl#multistore) approach.

The reference architecture below exemplifies its main characteristics:

- **Separated website**: One single account, but each store with its own domain, bound to different [sales channels](https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/4EPwTXx5oFdSG1dA3zIchz#trade-policy) by [bindings](https://help.vtex.com/en/tutorial/what-is-binding--4NcN3NJd0IeYccgWCI8O2W?&utm_source=autocomplete).  
- **Search**: [Settings](https://developers.vtex.com/docs/guides/search-overview) are the same for all websites. 
- **CMS**: Shared access to [Content Management System (CMS)](https://developers.vtex.com/docs/guides/vtex-io-documentation-cms) between websites.
- **Customer Data Storage**: One single [Master Data](https://developers.vtex.com/docs/guides/master-data-introduction) for all stores.
- **Catalog**: One single catalog, segmented by sales channels.
- **Logistics**: Each store has its logistics operation managed by different warehouses in the same Logistics panel.
- **Order Management System (OMS)**: One single Logistics and OMS for all stores.
- **Payments**: One Payments panel for all stores.
- **Prices and Promotions**: It is possible to configure different prices and promotions for each store, as you can segment by the sales channel. But prices and promotions for all stores are managed in the same panel.
- **Message Center**: One single [Message Center](https://help.vtex.com/en/tutorial/conhecendo-o-message-center--tutorials_84) for all stores.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/store-architecture/multi-currency-language-single-account.png)

#### Why choose this architecture?

- Supports [multi-currency](https://developers.vtex.com/docs/guides/vtex-io-documentation-internationalizing-product-prices) natively.
- Supports multi-language with [Messages](https://developers.vtex.com/docs/guides/storefront-content-internationalization) and [Catalog Translation App](https://developers.vtex.com/docs/guides/catalog-internationalization). 

>⚠ Product names are not translated on the [Checkout](https://help.vtex.com/en/tutorial/checkout-vtex-overview--7wcprkM7yZUflOqbzAN5SI) and [My Account pages](https://help.vtex.com/en/tutorial/how-my-account-works--2BQ3GiqhqGJTXsWVuio3Xh?&utm_source=autocomplete), as these modules call directly the catalog API to get product data, so the information does not pass through the Messages API. 

This model is easier to set up, integrate, and maintain compared to the [multi-account](#multi-account) approach, but it may not be efficient for large and complex operations. This architecture is recommended for operations present in more than one country, requiring the configuration of different languages and currencies, but without the need for data segregation, as all core services are shared. Therefore, it may work well for operations managed by a single, centralized team.

### Multi-account

In this architecture, there is a main VTEX account that will act as a [seller](https://help.vtex.com/en/tutorial/o-que-e-um-seller--5FkLvhZ3Few4CWWIuYOK2w) in all secondary VTEX accounts, acting as [marketplaces](https://help.vtex.com/en/tutorial/configurando-marketplace-entre-lojas-vtex). The main account - the seller - will be the source of truth for the [VTEX Core services](https://developers.vtex.com/docs/guides/getting-started#vtex-core-services), such as catalog, pricing, logistics, etc.

The reference architecture below exemplifies its main characteristics:

- **Separated VTEX account**: Each store has its own VTEX account.
- **Separated website**: Each store has its own website and may customize its frontend with a different look and feel per store.
- **Customer Data Storage**: Segregated by marketplaces' account. There is no customer information within the main account’s [Master Data](https://developers.vtex.com/docs/guides/master-data-introduction).
- **Catalog**: Separated catalog management, providing a unique assortment per store, defined based on the main account’s catalog.
- **Logistics and Order Management System (OMS)**: Independent Logistics and OMS per store.
- **Fulfillment**: Supports single or multiple fulfillment.
- **Payments**: Independent Payments management per store.
- **Pricing**: Independent Pricing management per store.
- **Promotions**: Independent Promotions system per store.
- **Message Center**: Independent Message Center per store

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/store-architecture/multi-currency-language-multi-account.png)

#### Why choose this architecture?

- The seller (main account) as catalog owner and marketplaces per country allows a way to make a multi-language solution, as each store can manage the language and currency locally, in its own store.
- Each account maintains its own catalog information since the information coming from the main account is always in the standard language set there.
- Support better translations compared to the [single account, multi-binding](#single-account-multi-binding) model, as there is an **independent catalog translation**. Therefore, you do not need to rely on Messages or Catalog translation app.

>⚠ [Assembly options](https://developers.vtex.com/docs/guides/assembly-options-app), [attachments](https://developers.vtex.com/docs/guides/cart-attachments-section-api-quick-start-guides), and [services](https://developers.vtex.com/docs/guides/vtex-io-documentation-service) are not supported.

Promotions from the main account have limited capabilities, as every information that comes from the customer will not be accessible by the main account. For example, if you want to create promotions for a customer cluster in the main account, it will not work because it does not have access to the marketplace’s Master Data.

This architecture is recommended for operations in more than one country, requiring the configuration of different languages and currencies, where different teams manage each localized store.

### Learn more

- [Accounts and architecture](https://help.vtex.com/en/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/4yPqZQyj0t675QpcG7H6yl) 
- [Choosing between a multi-store architecture or an additional environment](https://help.vtex.com/en/tutorial/escolhendo-entre-arquitetura-multi-loja-ou-ambiente-adicional--4HRNpa1OCKZ5YzP8yiilBL)
