---
title: "Implementing internationalization"
slug: "implementing-internationalization"
hidden: false
createdAt: "2026-06-16T00:00:00.000Z"
updatedAt: "2026-08-11T00:00:00.000Z"
excerpt: "Learn how to prepare your store to operate in multiple languages by translating storefront and catalog content."
---

**Internationalization** prepares your store to operate in multiple languages by translating storefront content and catalog data and applying regional formatting. When your business requires multiple currencies, prices, or logistics per market, pair internationalization with a [cross-border setup](https://developers.vtex.com/docs/guides/implementing-cross-border-stores) that uses different trade policies.

In this guide, you'll learn how to start implementing internationalization in your store, including:

- **[Store architecture](#store-architecture):** Define your operation and the architecture that best fits your business needs.
- **[Quickstart](#quickstart):** Discover the initial steps to internationalize your store.
- **[Fundamental tools](#fundamental-tools):** Set up the tools you must have for your internationalized operation to work correctly.

>ℹ️ Internationalization is available for [Store Framework](https://developers.vtex.com/docs/guides/store-framework) and for [FastStore](https://developers.vtex.com/docs/guides/faststore) through the [Localization feature](https://developers.vtex.com/docs/guides/faststore/storefront-features-handling-internationalization-with-the-localization-feature) in [FastStore v4](https://developers.vtex.com/docs/guides/faststore/getting-started-upgrading-faststore-to-v4). FastStore Localization is in **Closed Beta**. To request Localization access or set up a multistore environment, open a [VTEX support ticket](https://help.vtex.com/en/support).

## Store architecture

### Defining the operation

Before implementing internationalization in your store, make sure you have the following information ready:

- **Target languages/locales:** List languages with curated translations and those relying on automatic translation, considering audience and SEO.
- **Translation scope:** Distinguish **storefront** content (messages from React apps or CMS content) from **Catalog** content (names, descriptions, meta fields), as each layer has different tools and flows depending on your storefront.
- **Currencies and regional formatting:** Confirm whether you only need language changes or also require the display of prices and regional formats (dates, numbers) per locale.
- **URLs and SEO:** Determine whether you'll have localized paths/hosts per language (for example, `/en`, `/pt`) and whether you need to declare `alternate` or `hreflang` tags between versions for search engines.

### Choosing the store architecture

If you only need to offer the same product in multiple languages, you can implement internationalization without changing your current architecture. Multi-language support is available for [Store Framework](https://developers.vtex.com/docs/guides/store-framework) and for [FastStore](https://developers.vtex.com/docs/guides/faststore) via the Localization feature.

However, if your operation involves different currencies, prices, payments, or logistics across countries or regions, integrate internationalization with a cross-border strategy. Learn more in the guide [Implementing cross-border stores](https://developers.vtex.com/docs/guides/implementing-cross-border-stores).

## Quickstart

To start implementing internationalization, configure the binding. The steps differ by storefront technology.

A **binding** represents a storefront surface that combines a domain (canonical base address), locale, currency, and the sales channels (trade policies) it serves. This configuration is key for operating multiple languages within a single VTEX account.

### Store Framework

To internationalize your Store Framework store, configure the binding to use your final public domain as the **canonical base address**. In multi‑locale setups, use consistent paths per locale when sharing the same host (for example, `/en`, `/pt`). See the instructions below:

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

### FastStore

In FastStore, bindings are configured through [VTEX Support](https://help.vtex.com/en/support). Each domain is associated with a sales channel (currency, catalog, and pricing) and a locale. Even if a binding is configured with multiple locales, FastStore only considers the default locale.

After bindings are set up, enable Localization in your project by:

1. Configuring WebOps secrets so the platform can access your store's bindings.
2. Enabling the `localization` flag in `discovery.config.js`.
3. Activating the localization button in the CMS Navbar.

For the full implementation, including prerequisites such as FastStore v4 and the CMS, see [Handling internationalization with the Localization feature](https://developers.vtex.com/docs/guides/faststore/storefront-features-handling-internationalization-with-the-localization-feature).

## Fundamental tools

The tools you need depend on your storefront technology. Catalog translation applies to both Store Framework and FastStore.

### Shared tools

- **Catalog translation:** To translate catalog information (categories, products, SKUs, brands, specifications, and collections) and override the automatic translation, we recommend using the [Catalog Multi-Language API](https://developers.vtex.com/docs/guides/catalog-multi-language-integration-guide). It provides granular control over translations for products, SKUs, categories, brands, and other entities, while integrating natively with Intelligent Search and supporting Translation Management Systems (TMS). To learn how to implement it, see the [Catalog multi-language integration guide](https://developers.vtex.com/docs/guides/catalog-multi-language-integration-guide), including the [implementation by storefront type](https://developers.vtex.com/docs/guides/catalog-multi-language-integration-guide#implementation-by-storefront-type).

  >⚠️ The simultaneous use of both the Catalog Multi-Language API and the GraphQL (Messages) approach is not supported for catalog entities. Once the Catalog Multi-Language feature is activated for your account, you will no longer be able to manage translations using GraphQL.

  Alternatively, you can override the automatic translation using the legacy GraphQL approach: through the [Admin Catalog Translation](https://developers.vtex.com/docs/apps/vtex.admin-catalog-translation) app UI or the GraphQL APIs described in [Translating Catalog content](https://developers.vtex.com/docs/guides/catalog-internationalization). You can also translate using the [Catalog API](https://developers.vtex.com/docs/api-reference/catalog-api#overview) by adding the "**Accept-Language**" header with the desired target language. This is especially relevant for Headless stores.

  >ℹ️ Product information on the **Order Placed** pages and in transactional emails is automatically translated. However, on the **My Account** page, product information is not translated automatically. You need to implement customizations that make the above-mentioned GraphQL calls to perform these translations.

### Store Framework

- **[Messages](https://developers.vtex.com/docs/apps/vtex.messages):** In Store Framework projects, translations for store components are stored in a "/messages" folder located within the app's root directory. Thus, the translation of the content involves declaring the translated content for each language (binding) and for each element to be rendered via GraphQL. In this case, especially for specifications, breadcrumbs, and filters, the translation must be done using the Messages app. Learn more in the guides [Translating storefront content](https://developers.vtex.com/docs/guides/storefront-content-internationalization) and [Overwriting the Messages app](https://developers.vtex.com/docs/guides/vtex-io-documentation-overwriting-the-messages-app).
- **[Locale Switcher](https://developers.vtex.com/docs/guides/vtex-locale-switcher):** Allows switching languages on the site.

### FastStore

FastStore supports multi-language stores through the [Localization feature](https://developers.vtex.com/docs/guides/faststore/storefront-features-handling-internationalization-with-the-localization-feature) (**Closed Beta**). Requirements and setup include:

- **[FastStore v4](https://developers.vtex.com/docs/guides/faststore/getting-started-upgrading-faststore-to-v4):** Required for Localization.
- **[CMS](https://developers.vtex.com/docs/guides/cms-for-faststore-storefronts):** Localization works with the CMS and isn't available for [Headless CMS (legacy)](https://developers.vtex.com/docs/guides/faststore/headless-cms-overview). Storefront content is managed per locale in the CMS.
- **Bindings and sales channels:** Each domain is associated with a sales channel and a locale. Configure bindings with [VTEX Support](https://help.vtex.com/en/support), then enable the `localization` flag in `discovery.config.js` and the localization button in the CMS Navbar.
- **Catalog Multi-Language API:** FastStore retrieves translated catalog data through Intelligent Search. Use the Catalog Multi-Language API for a complete catalog translation solution.

For the full implementation, see [Handling internationalization with the Localization feature](https://developers.vtex.com/docs/guides/faststore/storefront-features-handling-internationalization-with-the-localization-feature).

## Next steps

<Flex>

<WhatsNextCard
title="Handling internationalization with the Localization feature"
description="Implement multi-language stores on FastStore v4 (Closed Beta)."
linkTo="https://developers.vtex.com/docs/guides/faststore/storefront-features-handling-internationalization-with-the-localization-feature"
linkTitle="See more"
/>

<WhatsNextCard
title="Handling internationalization"
description="Learn how to create a multi-language store using Store Framework."
linkTo="https://developers.vtex.com/docs/guides/vtex-io-multi-language-stores"
linkTitle="See more"
/>

</Flex>
