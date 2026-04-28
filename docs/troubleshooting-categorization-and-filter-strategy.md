# Troubleshooting Categorization and Filtering Strategy

This document describes the recommended categorization and filtering structure for the Troubleshooting section in the VTEX Developer Portal.

## Overview

Based on the analysis of **28 articles** in `docs/troubleshooting`, this strategy proposes:

- **6 primary categories** (journey/topic navigation)
- **10 symptom filters** (problem-type navigation)
- **18 domain filters** (product/technology navigation)

---

## 1. Primary categories (navigation sidebar)

| Menu | Description |
| --- | --- |
| **API and integrations** | API usage, payload issues, resource updates, integration contracts, external provider flows, and related Admin configuration for integrations |
| **VTEX IO and app development** | VTEX IO app lifecycle, CLI usage, dependencies, workspaces, installation, publishing, and Admin settings related to app behavior and configuration |
| **Storefront** | Storefront behavior, rendering, customization of components and blocks, FastStore implementation, routes, overrides, schema usage, and Admin settings that affect storefront behavior |
| **Content Management (CMS)** | Issues related to accessing and using VTEX CMS tools, including CMS, Headless CMS (Legacy), Site Editor, and Layout, such as permissions and login, finding and editing content, publishing updates to the storefront, previewing changes where supported, and understanding how content changes propagate |
| **Checkout and shopping experience** | Checkout completion, cart behavior, purchase blockers, storefront issues that affect the shopping experience, and Admin settings related to checkout behavior |
| **Analytics and data collection** | Analytics behavior, GTM, GA, dataLayer, event collection, measurement consistency, and Admin settings related to analytics configuration |

---

## 2. Symptom filters (tags)

| Symptom filter | Description |
| --- | --- |
| **Access restriction** | Permission, authorization, authentication, or access-related failures |
| **Setup issue** | Incorrect setup, environment mismatch, dependency setup, or missing configuration |
| **Installation failure** | Installation, linking, plugin, or dependency installation failures |
| **Loading failure** | Content, feature, or resource not loading or not becoming available |
| **Performance degradation** | Slow behavior, delayed publishing, degraded performance, or timeouts |
| **Publishing failure** | Publish, release, deploy, or availability-after-publish failures |
| **Rendering mismatch** | Wrong storefront output, missing visual behavior, display inconsistency |
| **Runtime error** | Explicit CLI, app, GraphQL, or runtime execution errors |
| **Measurement inconsistency** | Analytics, GTM, GA, UTM, or dataLayer inconsistency |
| **Validation error** | Schema, API, dependency, version, or payload validation failures |

---

## 3. Domain filters (tags)

| Domain filter | Troubleshooting usage |
| --- | --- |
| **Analytics** | General analytics behavior, tracking setup, and event consistency |
| **Apps** | App install, dependency, and publish issues |
| **Catalog** | Catalog data, SKU configuration, and product-related behavior |
| **Checkout** | Checkout flow, cart behavior, purchase completion, and session-related storefront behavior |
| **CMS** | CMS access, plugins, pages, and content publishing |
| **DNS** | DNS, hostname, SSL, and domain pointing issues |
| **FastStore** | FastStore storefront, performance, schema, and publishing topics |
| **Google Analytics** | GA and GA4 tracking behavior |
| **Google Tag Manager** | GTM setup, debugging, and event collection |
| **Headless CMS (Legacy)** | Legacy Headless CMS access, content modeling, page publishing, plugin usage, and legacy content delivery behavior |
| **License Manager** | User roles, permissions, and resource access management |
| **Pricing and Promotions** | Price display, price configuration, discount behavior, promotional rules, and offer inconsistencies |
| **Releases** | Releases module, build status, and deployment delivery |
| **Routes/Rewriter** | Routes, redirects, and rewrite behavior |
| **Search** | Search provider integration, result rendering, and search-driven storefront data |
| **Site Editor** | Site Editor access, block-level content editing, storefront customization, preview, and publishing behavior |
| **Store Framework** | VTEX IO Store Framework storefront implementation and behavior |
| **VTEX IO** | VTEX IO platform, CLI usage, workspaces, app lifecycle, and account-level app behavior |

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

1. `dev-portal-content/docs/troubleshooting/vtex-io-and-app-development/i-cant-install-vtex-io-cli.md`
   - Primary category: **VTEX IO and app development**
   - Symptom filters: **Installation failure**, **Setup issue**
   - Domain filters: **VTEX IO**

2. `dev-portal-content/docs/troubleshooting/content-management-cms/unable-to-access-headless-cms.md`
   - Primary category: **Content Management (CMS)**
   - Symptom filters: **Access restriction**, **Setup issue**
   - Domain filters: **CMS**, **License Manager**, **VTEX IO**

3. `dev-portal-content/docs/troubleshooting/checkout-and-shopping-experience/i-cant-complete-a-purchase-on-a-faststore-website.md`
   - Primary category: **Checkout and shopping experience**
   - Symptom filters: **Access restriction**, **Setup issue**
   - Domain filters: **Checkout**, **FastStore**, **DNS**

4. `dev-portal-content/docs/troubleshooting/analytics-and-data-collection/google-analytics-4-is-tracking-inconsistent-data-from-my-store.md`
   - Primary category: **Analytics and data collection**
   - Symptom filters: **Measurement inconsistency**, **Setup issue**
   - Domain filters: **Google Analytics**, **Google Tag Manager**, **Analytics**

### 5.2 Editorial decision guidelines

When classifying troubleshooting content, consider the following guidelines:

1. Prioritize the user's mental model over internal team ownership or root-cause attribution.
2. Write and classify articles based on the context in which users are most likely to look for the issue.
3. Apply the filter governance rules defined in Section 4 for domain, symptom, and hybrid-article decisions.
