---  
title: "Implementing internationalization"
slug: "implementing-internationalization"
hidden: false
createdAt: ""
excerpt: "Learn how "
---

**Internationalization** prepares your store to operate in multiple languages by translating storefront content and catalog data and applying regional formatting. When your business requires multiple currencies, prices, or logistics per market, pair internationalization with a [cross-border setup](https://developers.vtex.com/docs/guides/implementing-cross-border-stores) that uses different trade policies.

In this guide, you'll learn how to start implementing internationalization in your store, including:

- **[Store architecture](#store-architecture):** Define your operation and the architecture that best fits your business needs.
- **[Quickstart](#quickstart):** Discover the initial steps to internationalize your store.
- **[Fundamental apps](#fundamental-apps):** Set up the apps you must have for your internationalized operation to work correctly.

>ℹ️ Internationalization is available only for stores developed using [Store Framework](https://developers.vtex.com/docs/guides/store-framework).

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

## Fundamental apps

The apps listed below are essential for enabling multi-language operation in your VTEX account.

- [Messages](https://developers.vtex.com/docs/apps/vtex.messages): In VTEX IO, translations for store components are stored in a "/messages" folder located within the app's root directory. Thus, the translation of the content involves declaring the translated content for each language (binding) and for each element to be rendered via GraphQL. In this case, especially for specifications, breadcrumbs, and filters, the translation must be done using the Messages app. Learn more in the guides [Translating storefront content](https://developers.vtex.com/docs/guides/storefront-content-internationalization) and [Overwriting the Messages app](https://developers.vtex.com/docs/guides/vtex-io-documentation-overwriting-the-messages-app).
- [Locale Switcher](https://developers.vtex.com/docs/guides/vtex-locale-switcher): Allows switching languages on the site.
- [Admin Catalog Translation](https://developers.vtex.com/docs/apps/vtex.admin-catalog-translation): Enables the admin UI to translate catalog information (category, product, SKU, brand, specifications, and collections), overriding the automatic translation.

  You can also override the automatic translation using the GraphQL APIs described in [Translating Catalog content](https://developers.vtex.com/docs/guides/catalog-internationalization). Additionally, you can translate using the [Catalog API](https://developers.vtex.com/docs/api-reference/catalog-api#overview) by adding the "**Accept-Language**" header with the desired target language. This is especially relevant for Headless stores.

  >ℹ️ Product information on the **Order Placed** pages and in transactional emails is automatically translated. However, on the **My Account** page, product information is not translated automatically. You need to implement customizations that make the above-mentioned GraphQL calls to perform these translations.

## Next steps

<WhatsNextCard
title="Handling internationalization"
description="Learn how to create a multi-language store using Store Framework."
linkTo="https://developers.vtex.com/docs/guides/vtex-io-multi-language-stores"
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
