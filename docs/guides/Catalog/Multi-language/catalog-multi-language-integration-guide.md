---
title: "Catalog multi-language integration guide"
slug: "catalog-multi-language-integration-guide"
hidden: false
excerpt: "Manage multiple languages for catalog entities."
createdAt: "2026-01-13T00:00:00.000Z"
updatedAt: "2026-01-13T00:00:00.000Z"
---

> ℹ️ This feature is in beta, which means that we are working to improve it. If you have any questions, please contact our [Support](https://support.vtex.com/hc/en-us/requests).

Learn how to create translations and integrate localized content for catalog entities with the multi-language endpoints.

## Overview

The [multi-language feature](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/product/-productId-/language) enables the following capabilities:

- **Granular content management:** Retrieve and store translations for products, SKUs, categories, brands, specifications, collections, and services.
- **Automated translation workflows:** Integrate with Translation Management Systems (TMS) for automated translation.
- **Multiple storefront technologies:** Consume translations across different storefront implementations, such as Store Framework, FastStore, and headless implementations.
- **Localized experience:** Provide to customers localized shopping experiences across multiple markets.

## Use cases

The multi-language feature supports various integration scenarios:

| Use case | Description |
| :--- | :--- |
| Multilingual storefront | Displays translated product names, descriptions, and specifications based on the customer's locale identified by the storefront. |
| TMS integration | Connects your Translation Management System (TMS) to automatically push and pull translations via the [Catalog API](https://developers.vtex.com/docs/api-reference/catalog-api#overview). |
| Business expansion | Seamlessly adapts your catalog for new geographic markets without duplicating products. |
| SEO optimization | Provides localized meta descriptions, keywords, and URL slugs for better search engine rankings in each market. |
| Headless commerce | Fetches translated catalog data for headless storefront applications. |

## How the multi-language feature works

When you send translated content using the multi-language feature, the workflow is as follows:

```mermaid
┌────────────────────────────┐      ┌─────────────────────┐     ┌─────────────────────┐
│  1. Translation ingestion  │────▶│  2. Intelligent     │────▶│  3. Storefront      │
│                            │      │  Search indexing    │     │      display        │
│                            │      │                     │     │                     │
└────────────────────────────┘      └─────────────────────┘     └─────────────────────┘
```

### Step 1: Translation ingestion

The merchant or an integrated TMS makes a request to create or update the translation of a catalog entity, such as [product](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/product/-productId-/language) or [category](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/category/-categoryId-/language). The Catalog system validates and stores the translated fields per [locale](#locale-format), then triggers an update event to Intelligent Search.

### Step 2: Intelligent Search indexing

Intelligent Search indexes or reindexes the entity translated content to make it searchable and filterable in the storefront by the selected locale. This process runs asynchronously and usually completes within a few minutes. Larger amounts of data may take longer.

### Step 3: Storefront display

The storefront queries Intelligent Search and Catalog system at render time, so it automatically retrieves and displays the translations according to the customer's selected locale. No manual configuration or synchronization is needed.

>ℹ️ Valid for all storefront solutions, including Store Framework, FastStore, and headless implementations.

### Locale format

All locale codes follow the IETF BCP 47 standard, for example:

- `en-US`: English (United States)
- `es-ES`: Spanish (Spain)
- `pt-BR`: Portuguese (Brazil)
- `fr-FR`: French (France)
- `de-DE`: German (Germany)

## Activation

Open a [support ticket](https://help.vtex.com/en/support) requesting the activation of the Catalog multi-language feature for your account. Once the VTEX team activates it, they will contact you to inform that you can start using the feature.

>❗ The simultaneous use of both the multi-Language APIs and Messages APIs (GraphQL) is not supported for catalog entities. Therefore, once the new feature is activated, you will no longer be able to manage translations using GraphQL.

## Permissions

To successfully use the multi-language feature, the user or [API key](https://developers.vtex.com/docs/guides/authentication-overview#api-keys) must have the [License Manager resource](https://help.vtex.com/en/tutorial/license-manager-resources--3q6ztrC8YynQf6rdc6euk3) below, otherwise they will receive a 403 error:

| Product | Category | Resource |
| :--- | :--- | :--- |
| Catalog | Content | Categories Management |

## Recommendations

Some best practices to follow when using the multi-language feature are:

- **Start with high-impact entities:** Prioritize translating products, categories, and brands before moving to specifications and attachments.
- **Batch translations:** When integrating with a TMS, batch multiple translation updates to reduce API calls.
- **Validate before publishing:** Use the `GET` endpoints to verify translations before they go live.

## Troubleshooting

See below the most common issues and their respective solutions when using the multi-language feature:

| Issue | Solution |
| :--- | :--- |
| Translations not appearing on storefront | Wait a few minutes for Intelligent Search to reindex. Check that the locale matches your store binding configuration. |
| `403 Forbidden` error | Verify that your user or application key has the `Categories Management` resource enabled. |
| `404 Not Found` error | Confirm that the entity ID (product, SKU, category, etc.) exists in the Catalog. |
| `409 Conflict` error | The translation may already exist. Use `GET` to retrieve current translations before updating. |

> ℹ️ If the issue persists, contact our [Support](https://support.vtex.com/hc/en-us/requests).
