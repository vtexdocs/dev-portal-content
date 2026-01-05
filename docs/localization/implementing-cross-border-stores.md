---
title: "Implementing cross-border stores"
slug: "implementing-cross-border-stores"
hidden: false
excerpt: "Learn the initial steps for implementing a cross-border store."
createdAt: "2026-01-05T14:48:34.630Z"
---

A cross-border store is a specialized [multistore](https://help.vtex.com/en/tutorial/managing-a-multistore--4S0lFVBPylRS5KpVgdyDhJ) setup where a VTEX account operates multiple localized stores for different countries or regions, each with its own catalog, prices, logistics, and language.

In this guide, you'll learn how to start implementing your cross-border operation, including:

* **[Store architecture](#store-architecture):** Define your operation to choose the architecture that best fits your business needs.
* **[Quickstart](#quickstart):** Discover the initial steps to implement your cross-border store.
* **[Fundamental apps](#fundamental-apps):** Set up the apps you must have for your cross-border operation to work correctly.

>ℹ️ The cross-border implementation is available only for stores developed using [Store Framework](https://developers.vtex.com/docs/guides/store-framework).

## Store architecture

To choose the most appropriate architecture that meets your business needs, address some initial questions that define the operation.

### Defining the operation

Before implementing your cross-border store, make sure you have the following information ready:

* **Target regions:** Identify the countries/regions where your store will operate.
* **Currencies and Languages:** Determine accepted payment currencies and supported site languages.
* **Inventory management:** Decide if inventory will be managed from Brazil or locally in each country/region.
* **Tax and Export partner:** If using fulfillment from Brazil, choose a partner for handling export taxes and fees. To find your partner, check out the [Partners](https://vtex.com/en-us/partners/) page on the VTEX website.
* **Catalog translation:** Check if your catalog is translated or needs localization for each country/region.
* **Promotions:** Plan the types of promotions for each store. Learn about the types available in [Promotions](https://help.vtex.com/subcategory/benefits--1yTYB5p4b6iwMsUg8uieyq) guides.
* **Operations:** Consider any existing physical stores, sellers, or other operations abroad. Learn more in [VTEX account types](https://help.vtex.com/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/4yPqZQyj0t675QpcG7H6yl#vtex-account-types)
* **Teams:** Identify if different teams will manage each country/region’s ecommerce operations.
* **ERP Systems:** Confirm if each country/region has its own ERP or a centralized system.
* **Payment gateway:** Ensure you have a gateway that supports multiple currencies.
* **Domains:** Define the primary and secondary domains for your stores. Learn more in [Rules for main hosts](https://help.vtex.com/pt/tutorial/configuring-the-store-domain--tutorials_2450#rules-for-main-host).

### Choosing the store architecture

After defining your operation based on the topics above, choose the architecture for your cross-border store.

* Single account, multi-binding
* Multi-account, shared back office systems
* Multi-account, independent back office systems

See below the main differences between them:

|                       | Single account, multi-binding | Multi-account, shared back-office systems | Multi-account, independent back-office systems |
| --------------------- | ----------------------------- | ----------------------------------------- | ---------------------------------------------- |
| **VTEX accounts** | One account serves multiple countries via bindings/trade policies. | Multiple accounts (usually one per country or region). A main account acts as the seller, and the others act as marketplaces. | Fully separate accounts, each operating independently. |
| **Storefront / Websites** | Separate websites or domains bound to different trade policies within the same account. | Separate websites per account. | Separate websites per account. |
| **Catalog** | One shared catalog segmented by trade policies. | The main account is the source of truth for the catalog. | Each account manages its own catalog. |
| **Multi-language** | Supported via bindings and locales, enabling translated content from a shared catalog. | Each marketplace account localizes the catalog received from the main seller. | Multi-language support is independent per account. |
| **Customer data** | All customer data stored in a single Master Data instance. | Customer data stored by marketplace account. The seller (main account) doesn't store marketplace customer data in its Master Data. | Customer data separated by account. Each account has its own Master Data with no sharing between accounts. |
| **Promotions** | Configured per store using trade policy segmentation and managed in the same panel. | The main account has few options for promotions because it cannot access the marketplace Master Data. Promotions that rely on seller payment methods may not work. | Each account sets up its own promotions. If an account operates a marketplace with external sellers, promotion limitations apply only to that seller–marketplace relationship. |
| **Checkout, OMS, Payments, Message Center** | All stores share these modules and panels. | Each store manages these modules in its own Admin, independent from the main account. | Each store manages these modules in its Admin. |
| **Logistics** | All stores share the same logistics panel and use different warehouses for each store. | The main account is the source of truth for logistics, but each account manages its own logistics settings in its Admin. | Each account manages its own logistics. |
| **Back-office systems (ERP/PIM/WMS)** | A single set of integrations connects the account to the back-office systems. | Shared back-office across accounts. The main account acts as the central connection for core services, while operations are specific to each account. | Independent back-office per account. |

All architectures support multi-currency through trade policies. The main differences lie in how prices are managed and where pricing logic is centralized.

>ℹ️ Learn more about each approach in the section [Multi-language and multi-currency](https://developers.vtex.com/docs/guides/store-architecture#multi-language-and-multi-currency) of the Store architecture guide.

## Quickstart

To start implementing your cross-border operation, follow the steps below:

### Step 1 - Configure a trade policy

A trade policy is the key that differentiates each country or region storefront within a single VTEX account that uses a multi-binding architecture. Each website is linked to a specific trade policy, allowing separate sites for different markets. Learn more in [How trade policies work](https://newhelp.vtex.com/en/docs/tutorials/how-trade-policies-work).

To request a new trade policy, open a ticket with [VTEX Support](https://help.vtex.com/en/support), select the option Commercial, and click Create a trade policy. Learn more in [Creating a trade policy](https://help.vtex.com/en/tutorial/creating-a-trade-policy--563tbcL0TYKEKeOY4IAgAE).

When configuring trade policies, ensure that the currency code and symbol, as well as the country code and cultural information, are adjusted correctly.

![trade-policies]()

### Step 2 - Create a new binding

In VTEX, binding is the process of linking a website, store name, and trade policy to create a unique identifier for each store. This is essential for managing multiple stores in a single VTEX account.

In a cross‑border setup, you create multiple bindings to connect each market’s domain to its corresponding trade policy and locale, so each site runs with the right catalog, currency, and language.

To create a new binding, open a ticket to [VTEX Support](https://help-tickets.vtex.com/smartlink/sso/login/zendesk).

You can get your store's binding id by using the following API:

```bash
curl --location '*http://portal.vtexcommercestable.com.br/api/license-manager/binding/site/haight*' \
--header 'Content-Type: application/json'
```

Or following the instructions in the guide [Checking your store's binding id](https://developers.vtex.com/docs/guides/checking-your-stores-binding-id).

>⚠️ When multiple language versions of URLs are required, create one binding for each language. Using a single binding for multiple languages isn't the proper approach. Even if you manually create additional URLs using GraphQL calls, it will lead to duplicate content. This is because the page will always default to displaying in the primary language, regardless of the new URLs.

### Step 3 - Enable the use of a custom currency symbol

1. In the VTEX Admin, go to **Store Settings > Storefront > Store**.
2. Click the `Advanced` tab.
3. Enable the option `Enable custom currency symbol`.

  >ℹ️ Use the currency symbol field defined in the trade policy.

  ![currency-symbol]()

## Fundamental apps

The apps below are essential to enable the cross-border operation in your VTEX account:

* **[Binding selector](https://developers.vtex.com/docs/apps/vtex.binding-selector):** Allows changing store bindings from the UI via a dropdown.
* **[Locale Switcher](https://developers.vtex.com/docs/guides/vtex-locale-switcher):** Allows switching languages on the site.
* **[Messages](https://developers.vtex.com/docs/apps/vtex.messages):** In VTEX IO, translations for store components are stored in a "/messages" folder located within the app's root directory. Thus, the translation of the content involves declaring the translated content for each language (binding) and for each element to be rendered via GraphQL. In this case, especially for specifications, breadcrumbs, and filters, the translation must be done using the Messages app. Learn more in the guides [Translating storefront content](https://developers.vtex.com/docs/guides/storefront-content-internationalization) and [Overwriting the Messages app](https://developers.vtex.com/docs/guides/vtex-io-documentation-overwriting-the-messages-app).
* **[Admin Catalog Translation](https://developers.vtex.com/docs/apps/vtex.admin-catalog-translation):** Enables the admin UI to translate catalog information (category, product, SKU, brand, specifications, and collections), overriding the automatic translation.

  You can also override the automatic translation using the GraphQL APIs described in [Translating Catalog content](https://developers.vtex.com/docs/guides/catalog-internationalization). Additionally, you can translate using the [Catalog API](https://developers.vtex.com/docs/api-reference/catalog-api#overview) but adding the "Accept-Language" header with the language into which you want to translate the information. This is especially relevant for headless stores.

  >ℹ️ Product information on the **Order Placed** pages and in transactional emails is automatically translated. However, on the **My Account** page, product information is not translated automatically. You need to implement customizations that make the above-mentioned GraphQL calls to perform these translations.

## Next steps

<WhatsNextCard
title="Setting up cross-border stores"
description="Learn how to set up a cross-border store."
linkTo="https://developers.vtex.com/docs/guides/store-framework-setting-up-cross-border-stores"
linkTitle="See more"
/>

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
