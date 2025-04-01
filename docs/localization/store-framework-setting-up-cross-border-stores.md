---
title: "Setting up cross-border stores"
slug: "store-framework-setting-up-cross-border-stores"
hidden: false
createdAt: "2024-09-06T14:53:36.032Z"
updatedAt: "2025-03-12T11:41:22.220Z"
excerpt: ""
---

Cross-border stores are a specialized type of [multistore](https://help.vtex.com/en/tutorial/creating-multi-store-multi-domain--tutorials_510?locale=en), where a single VTEX account manages multiple stores in different countries or regions.

This feature is ideal for stores with different brands and business models that require multiple operational environments. In a multistore, also known as a subaccount or multidomain, each store can be set up independently, which means that layouts, products, prices, and logistics can vary for each local store depending on its domain.

In a cross-border context, a multistore setup allows a single VTEX account to manage multiple stores, such as:
- `http://{storeName}.com/en` (English store)
- `http://{storeName}.com/pt` (Portuguese store)

>ℹ️ To become a cross-border store, open a [VTEX support ticket](https://help-tickets.vtex.com/smartlink/sso/login/zendesk) and request the setup of a multistore environment.
## Before you begin

<Steps>

### Define your operation

Before implementing your cross-border store, make sure you have the following information ready:

- **Target regions:** Identify the countries/regions where your store will operate.
- **Currencies and Languages:** Determine accepted payment currencies and supported site languages.
- **Inventory management:** Decide if inventory will be managed from Brazil or locally in each country/region.
- **Tax and Export partner:** If using fulfillment from Brazil, choose a partner for handling export taxes and fees. To find your partner, check out the [Partners](https://vtex.com/en-us/partners/) page on the VTEX website.
- **Catalog translation:** Check if your catalog is translated or needs localization for each country/region.
- **Promotions:** Plan the types of promotions for each store. Learn about the types available in [Promotions](https://help.vtex.com/subcategory/benefits--1yTYB5p4b6iwMsUg8uieyq) guides.
- **Operations:** Consider any existing physical stores, sellers, or other operations abroad. Learn more in [VTEX account types](https://help.vtex.com/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/4yPqZQyj0t675QpcG7H6yl#vtex-account-types) 
- **Teams:** Identify if different teams will manage each country/region’s ecommerce operations.
- **ERP Systems:** Confirm if each country/region has its own ERP or a centralized system.
- **Payment gateway:** Ensure you have a gateway that supports multiple currencies.
- **Domains:** Define the primary and secondary domains for your stores. Learn more in [Rules for main hosts](https://help.vtex.com/pt/tutorial/configuring-the-store-domain--tutorials_2450#rules-for-main-host) 

This information will help you to choose the most suitable architecture for your cross-border store.

### Choose your store architecture

After defining your operation based on the topics above, choose the architecture for your cross-border store following the section [Multi-language and multi-currency](https://developers.vtex.com/docs/guides/store-architecture#multi-language-and-multi-currency) within the Store Architecture guide.

</Steps>
## Essential concepts

To better understand how a VTEX cross-border multistore works, it's essential to comprehend the key concepts of bindings and trade policies.

### Binding

In VTEX, **binding** is the process of linking a website, a store name, and a trade policy to create a unique identifier for each store. This is essential for managing multiple stores within a single VTEX account.

Each store has a unique binding value, which is crucial for routing and configuring store-specific settings.

>ℹ️ To check the `binding` value of your stores, follow the [Checking your store's binding id](https://developers.vtex.com/docs/guides/checking-your-stores-binding-id) guide.

### Trade Policies

A **trade policy** is a set of configurations that define a store’s catalog, pricing, and logistics strategy. Each store can have its own trade policy, allowing for different setups depending on the market. For example, if the pricing structure differs between your stores in Spain and France, you'll need separate trade policies.

If two stores share the same logistics, catalog, and prices, they can use a common trade policy.

>ℹ️ To learn more, see the guide [How trade policies work](https://help.vtex.com/en/tutorial/how-trade-policies-work--6Xef8PZiFm40kg2STrMkMV).

## Guides in this section

<Flex>

<WhatsNextCard
title="Checking your store's binding id"
description="Understand how to identify the unique binding ID for each store in your cross-border setup."
linkTo="https://developers.vtex.com/docs/guides/checking-your-stores-binding-id"
linkTitle="See more"
/>

<WhatsNextCard
title="Creating robots files for cross-border stores"
description="Learn how to configure `robots.txt` files to manage search engine indexing for cross-border stores."
linkTo="https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-robots-files-for-cross-border-stores"
linkTitle="See more"
/>

<WhatsNextCard
title="Cross-border store content internationalization"
description="Discover how to customize URLs and manage content localization for cross-border stores."
linkTo="https://developers.vtex.com/docs/guides/cross-border-custom-urls-1"
linkTitle="See more"
/>

<WhatsNextCard
title="Managing landing pages in cross-border stores"
description="Learn how to manage landing pages tailored for different regions."
linkTo="https://developers.vtex.com/docs/guides/vtex-io-documentation-managing-landing-pages-in-cross-border-stores"
linkTitle="See more"
/>

<WhatsNextCard
title="Indicating alternate versions of localized pages in cross border stores"
description="Discover how to set up alternate page versions in cross-border stores."
linkTo="https://developers.vtex.com/docs/guides/vtex-io-documentation-indicating-alternate-pages-in-cross-border-stores"
linkTitle="See more"
/>

</Flex>
