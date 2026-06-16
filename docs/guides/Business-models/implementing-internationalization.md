---
title: "Implementing internationalization"
slug: "implementing-internationalization"
hidden: false
createdAt: "2026-06-16T00:00:00.000Z"
excerpt: "Learn how to prepare your store to operate in multiple languages by translating storefront and catalog content."
---

**Internationalization** prepares your store to operate in multiple languages by translating storefront content and catalog data and applying regional formatting. When your business requires multiple currencies, prices, or logistics per market, pair internationalization with a [cross-border setup](https://developers.vtex.com/docs/guides/implementing-cross-border-stores) that uses different trade policies.

In this guide, you'll learn how to start implementing internationalization in your store, including:

- **[Store architecture](#store-architecture):** Define your operation and the architecture that best fits your business needs.
- **[Quickstart](#quickstart):** Discover the initial steps to internationalize your store.
- **[Translation setup](#translation-setup):** Set up the tools you must have for your internationalized operation to work correctly.

>ℹ️ This guide covers the internationalization approach for stores developed using [Store Framework](https://developers.vtex.com/docs/guides/store-framework). FastStore projects handle internationalization through a separate Localization feature, which follows a different setup flow.

## Store architecture

### Defining the operation

Before implementing internationalization in your store, make sure you have the following information ready:

- **Target languages/locales:** List languages with curated translations and those relying on automatic translation, considering audience and SEO.
- **Translation scope:** Distinguish **storefront** content (messages from React apps) from **Catalog** content (names, descriptions, meta fields), as each layer has different tools and flows.
- **Currencies and regional formatting:** Confirm whether you only need language changes or also require the display of prices and regional formats (dates, numbers) per locale.
- **URLs and SEO:** Determine whether you'll have localized paths/hosts per language (for example, `/en`, `/pt`) and whether you need to declare `alternate` or `hreflang` tags between versions for search engines.

### Choosing the store architecture

If you only need to offer the same product in multiple languages, you can implement internationalization in any architecture as long as the store has been developed using Store Framework. You don't need to change your current architecture to set up a multi-language store.

However, if your operation involves different currencies, prices, payments, or logistics across countries or regions, integrate internationalization with a cross-border strategy. Learn more in the guide [Implementing cross-border stores](https://developers.vtex.com/docs/guides/implementing-cross-border-stores).

## Quickstart

To start implementing internationalization, configure the binding.

A **binding** represents a storefront surface that combines a domain (canonical base address), one or more locales, currency, and the sales channels (trade policies) it serves. This configuration is key for operating multiple languages within a single VTEX account.

To internationalize your store, configure the binding to use your final public domain as the **canonical base address**. In multi‑locale setups, use consistent paths per locale when sharing the same host (for example, `/en`, `/pt`). See the instructions below:

1. Access `{accountName}.myvtex.com/admin/binding`. Replace `{accountName}` based on your scenario.
2. Click the vertical ellipsis menu (`⋮`) alongside the canonical address you want to configure, then click `Edit`.
3. Set the canonical base address to your public domain (and the locale path, if applicable).
4. Go to **Locales** and click `+ Add` to add a new locale.
5. Click `Save` to save the changes.

#### Best practices on binding configuration

In a multi-locale setup on the same host, make each locale's **canonical base address** follow the same structure, typically with a path prefix for all locales (for example, `store.com/en`, `store.com/pt`), instead of mixing root for one locale and paths for others. This avoids conflicts in session cookies and redirects between locales.

When one locale is at the root (`store.com`), and another is under a path (`store.com/pt`), users can end up with two segment cookies: One scoped to `/` and another to `/pt`, which leads to conflicting session information and erratic behaviour during language switches. Using paths in both locales avoids this duplication.

✅ Do

Use a path prefix for every locale on the same host or use separate domains for each locale:

- Example with paths for all locales on the same host:
    
  **en-US:** `https://store.com/en`
  **pt-BR:** `https://store.com/pt`
    
- Example with different domains per locale:
    
  **en-US:** `https://en.store.com`
  **pt-BR:** `https://pt.store.com`

❌ Don't

Avoid mixing a root URL for one locale with a path prefix for another:

  **en-US:** `https://store.com/`
  **pt-BR:** `https://store.com/pt`

## Translation setup

The following tools are essential for enabling multi-language operation in your VTEX account.

- **[Messages](https://developers.vtex.com/docs/apps/vtex.messages):** In Store Framework projects, translations for store components are stored in a "/messages" folder located within the app's root directory. Thus, the translation of the content involves declaring the translated content for each language (binding) and for each element to be rendered via GraphQL. In this case, especially for specifications, breadcrumbs, and filters, the translation must be done using the Messages app. Learn more in the guides [Translating storefront content](https://developers.vtex.com/docs/guides/storefront-content-internationalization) and [Overwriting the Messages app](https://developers.vtex.com/docs/guides/vtex-io-documentation-overwriting-the-messages-app).
- **[Locale Switcher](https://developers.vtex.com/docs/guides/vtex-locale-switcher):** Allows switching languages on the site.
- **Catalog translation:** To translate catalog information (categories, products, SKUs, brands, specifications, and collections) and override the automatic translation, we recommend using the [Catalog Multi-Language API](https://developers.vtex.com/docs/guides/catalog-multi-language-integration-guide). It provides granular control over translations for products, SKUs, categories, brands, and other entities, while integrating natively with Intelligent Search and supporting Translation Management Systems (TMS). To learn how to implement it, see the [Catalog multi-language integration guide](https://developers.vtex.com/docs/guides/catalog-multi-language-integration-guide).

  >⚠️ The simultaneous use of both the Catalog Multi-Language API and the GraphQL (Messages) approach is not supported for catalog entities. Once the Catalog Multi-Language feature is activated for your account, you will no longer be able to manage translations using GraphQL.

  Alternatively, you can override the automatic translation using the legacy GraphQL approach: through the [Admin Catalog Translation](https://developers.vtex.com/docs/apps/vtex.admin-catalog-translation) app UI or the GraphQL APIs described in [Translating Catalog content](https://developers.vtex.com/docs/guides/catalog-internationalization). You can also translate using the [Catalog API](https://developers.vtex.com/docs/api-reference/catalog-api#overview) by adding the "**Accept-Language**" header with the desired target language. This is especially relevant for Headless stores.

  >ℹ️ Product information on the **Order Placed** pages and in transactional emails is automatically translated. However, on the **My Account** page, product information is not translated automatically. You need to implement customizations that make the above-mentioned GraphQL calls to perform these translations.

## Next steps

<Flex>

<WhatsNextCard
title="Handling internationalization"
description="Learn how to create a multi-language store using Store Framework."
linkTo="https://developers.vtex.com/docs/guides/vtex-io-multi-language-stores"
linkTitle="See more"
/>

<WhatsNextCard
title="Catalog multi-language integration guide"
description="Learn how to manage catalog translations using the recommended Catalog Multi-Language API."
linkTo="https://developers.vtex.com/docs/guides/catalog-multi-language-integration-guide"
linkTitle="See more"
/>

<WhatsNextCard
title="Internationalizing product prices"
description="Learn how to set up prices according to the ISO standard currency codes."
linkTo="https://developers.vtex.com/docs/guides/vtex-io-documentation-internationalizing-product-prices"
linkTitle="See more"
/>

<WhatsNextCard
title="Disabling automatic translation"
description="Learn how to disable automatic translations."
linkTo="https://developers.vtex.com/docs/guides/vtex-io-documentation-disabling-automatic-translation"
linkTitle="See more"
/>

<WhatsNextCard
title="Translating storefront content"
description="Learn how to translate text messages from a frontend app."
linkTo="https://developers.vtex.com/docs/guides/storefront-content-internationalization"
linkTitle="See more"
/>

<WhatsNextCard
title="Translating catalog content"
description="Learn how to overwrite automatic translation from the catalog."
linkTo="https://developers.vtex.com/docs/guides/catalog-internationalization"
linkTitle="See more"
/>

<WhatsNextCard
title="Overwriting the Messages app"
description="Learn how to overwrite automatic translations."
linkTo="https://developers.vtex.com/docs/guides/vtex-io-documentation-overwriting-the-messages-app"
linkTitle="See more"
/>

</Flex>
