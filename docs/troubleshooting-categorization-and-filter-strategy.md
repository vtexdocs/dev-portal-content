# Troubleshooting Categorization and Filtering Strategy

This document describes the recommended categorization and filtering structure for the Troubleshooting section in the VTEX Developer Portal.

## Overview

Based on the analysis of **28 articles** in `docs/troubleshooting`, this strategy proposes:

- **6 primary categories** (journey/topic navigation)
- **10 symptom filters** (problem-type navigation)
- **22 domain filters** (product/technology navigation)

---

## 1. Primary categories (6 options)

| Category                        | Description                                                                                     |
| ------------------------------- | ----------------------------------------------------------------------------------------------- |
| **API and Integrations**        | API usage, payload issues, resource updates, integration contracts, and external provider flows |
| **VTEX IO and App Development** | VTEX IO app lifecycle, CLI usage, dependencies, workspaces, installation, and publishing        |
| **Storefront and FastStore**    | Storefront behavior, rendering, FastStore implementation, routes, schema usage, and components  |
| **CMS and Content Delivery**    | Headless CMS access, releases, page publishing, overrides, and content delivery workflows       |
| **Checkout and Sessions**       | Checkout completion, cart/session propagation, and purchase-blocking storefront issues          |
| **Analytics and Tracking**      | Analytics behavior, GTM, GA, dataLayer, and tracking consistency                               |

---

## 2. Symptom filters (10 options)

| Symptom filter            | Description                                                                        |
| ------------------------- | ---------------------------------------------------------------------------------- |
| **Access restriction**    | Permission, authorization, authentication, or access-related failures              |
| **Misconfiguration**      | Incorrect setup, environment mismatch, dependency setup, or missing configuration  |
| **Installation failure**  | Installation, linking, plugin, or dependency installation failures                 |
| **Loading failure**       | Content, feature, or resource not loading or not becoming available                |
| **Performance degradation** | Slow behavior, delayed publishing, degraded performance, or timeouts             |
| **Publishing failure**    | Publish, release, deploy, or availability-after-publish failures                   |
| **Rendering mismatch**    | Wrong storefront output, missing visual behavior, display inconsistency            |
| **Runtime error**         | Explicit CLI, app, GraphQL, or runtime execution errors                            |
| **Tracking mismatch**     | Analytics, GTM, GA, UTM, or dataLayer inconsistency                                |
| **Validation error**      | Schema, API, dependency, version, or payload validation failures                   |

---

## 3. Domain filters (22 options)

| Domain filter            | Troubleshooting usage                                                            |
| ------------------------ | -------------------------------------------------------------------------------- |
| **Analytics**            | General analytics behavior, tracking setup, and event consistency                |
| **Apps**                 | App install, dependency, and publish issues                                      |
| **Catalog**              | Catalog data, SKU configuration, and product-related behavior                    |
| **Catalog API**          | API-based SKU and catalog operations                                             |
| **Checkout**             | Checkout flow, purchase completion, and cart behavior                            |
| **DNS**                  | DNS, hostname, SSL, and domain pointing issues                                   |
| **FastStore**            | FastStore storefront, performance, schema, and publishing topics                 |
| **Google Analytics**     | GA and GA4 tracking behavior                                                     |
| **Google Tag Manager**   | GTM setup, debugging, and event collection                                       |
| **GraphQL**              | GraphQL schema, queries, generated types, and extension issues                   |
| **Headless CMS**         | CMS access, plugins, pages, and content publishing                               |
| **License Manager**      | Roles, permissions, and CMS-related access control                               |
| **Pricing**              | Price rendering, price range, and price inconsistency topics                     |
| **Promotions**           | Promotion rendering and promotion-related storefront behavior                     |
| **Releases**             | Releases module, build status, and deployment delivery                           |
| **Routes/Rewriter**      | Routes, redirects, and rewrite behavior                                          |
| **Search**               | Search provider integration, result rendering, and search-driven storefront data |
| **Sessions**             | Session propagation, UTM forwarding, and checkout session behavior                |
| **Store Framework**      | VTEX IO Store Framework storefront implementation and behavior                    |
| **VTEX IO**              | VTEX IO platform, apps, workspaces, and account-level app behavior               |
| **VTEX IO CLI**          | CLI installation, execution, update, and command failures                        |
| **Workspace**            | Development workspace creation and behavior                                      |

---

## 4. Filter governance

1. Keep **Domain filters** as the primary discovery axis for troubleshooting articles.
2. Use **Symptom filters** as the secondary refinement axis to narrow the problem type.
3. Treat the **Primary category** as the broad navigation layer, not as the main retrieval mechanism.
4. Promote niche domain filters only when recurring article volume justifies them.
5. For hybrid articles, prioritize:
   1. the product or technical area the developer is most likely to associate with the issue as the main domain filter,
   2. the dominant symptom as the main troubleshooting refinement,
   3. additional domain filters only when they materially improve discovery.

---

## 5. Taxonomy governance for scale

To support the growth of troubleshooting content in the Developer Portal, follow the guidelines below when classifying articles.

### 5.1 Assignment guidelines

For each troubleshooting article, the following taxonomy structure is recommended:

- Primary category: typically **1** per article.
- Symptom filters: usually **1 to 2** per article.
- Domain filters: typically **1 to 3** per article.

Examples of recommended assignments:

1. `dev-portal-content/docs/troubleshooting/development/i-cant-install-vtex-io-cli.md`

   - Primary category: **VTEX IO and App Development**
   - Symptom filters: **Installation failure**, **Misconfiguration**
   - Domain filters: **VTEX IO CLI**, **VTEX IO**

2. `dev-portal-content/docs/troubleshooting/development/unable-to-access-headless-cms.md`

   - Primary category: **CMS and Content Delivery**
   - Symptom filters: **Access restriction**, **Misconfiguration**
   - Domain filters: **Headless CMS**, **License Manager**, **VTEX IO CLI**

3. `dev-portal-content/docs/troubleshooting/store-performance/i-cant-complete-a-purchase-on-a-faststore-website.md`

   - Primary category: **Checkout and Sessions**
   - Symptom filters: **Access restriction**, **Misconfiguration**
   - Domain filters: **Checkout**, **FastStore**, **DNS**

4. `dev-portal-content/docs/troubleshooting/store-performance/google-analytics-4-is-tracking-inconsistent-data-from-my-store.md`

   - Primary category: **Analytics and Tracking**
   - Symptom filters: **Tracking mismatch**, **Misconfiguration**
   - Domain filters: **Google Analytics**, **Google Tag Manager**, **Analytics**

### 5.2 Editorial decision guidelines

When classifying troubleshooting content, consider the following guidelines:

1. Prioritize the developer's likely entry point rather than internal team ownership.
2. For cross-product issues, use the dominant user-visible symptom as a tie-breaker.
3. Use domain filters to identify the product or technical area involved, and use symptom filters to describe the type of problem. Both should work together, since domain filters do not replace symptom filters.
4. Prefer symptom-first, user-language titles such as:
   - `I can't ...`
   - `My ... is not ...`
   - `... returns ... error`

### 5.3 When to add a new primary category

- Add a new primary category only when:
  - it would meaningfully group a recurring class of articles, and
  - existing categories are becoming too broad or ambiguous.
- As a working threshold, prefer adding a category only when it would cover at least **8 active articles** or when the current grouping is harming findability.

### 5.4 When to add or change filters

- Add a new domain filter only when a product or technical area recurs frequently enough to improve discovery.
- Add a new symptom filter only when the existing problem-type vocabulary no longer describes a recurring failure mode.
- Avoid one-off filters.

### 5.5 Review cadence

- Review the taxonomy **quarterly**.
- Check:
  - article distribution by primary category
  - overused or underused filters
  - duplicated troubleshooting topics
  - content gaps that should become new troubleshooting articles
