---
title: "FastStore Release Notes — Version 4.9.0"
slug: "2026-09-30-faststore-release-notes-4-9-0"
type: improved
excerpt: "FastStore 4.9.0 improves cart and My Account for B2B Buyer Portal account reliability, Windows development, localized SEO, custom search sorting, and access to product cluster data"
createdAt: "2026-09-30T00:00:00.000Z"
updatedAt: "2026-09-30T00:00:00.000Z"
hidden: true
tags:
  - FastStore
---

FastStore `v4.9.0` keeps cart services and My Account for B2B Buyer Portal sessions consistent, gives merchants more control over localized account content, and corrects localized storefront URLs. Developers gain more reliable builds, especially on Windows, plus new APIs for custom sorting and product cluster data. See the fixes and features below for details.

> ⚠️ Follow the instructions in [Updating the CLI package version](https://developers.vtex.com/docs/guides/faststore/developer-tools-updating-the-cli-package-version) to upgrade to `v4.9.0` and keep your store up to date with the following improvements.

## Bug Fixes

### Prevent caching of GraphQL error responses (PR: [#3485](https://github.com/vtex/faststore/pull/3485))

FastStore now applies `cache-control: no-store` to GraphQL and unexpected-error responses unless headers have already been sent. Successful GraphQL response caching remains unchanged.

Shoppers are less likely to receive a previously cached 404, 410, or other GraphQL failure from a CDN or intermediary. Merchants gain more reliable recovery after temporary API errors without additional configuration.

### Normalize locale-aware storefront URLs (PR: [#3498](https://github.com/vtex/faststore/pull/3498))

FastStore now removes a trailing slash from locale-aware store URLs before appending landing-page, product, home-search, and search-page paths. Search SEO generation also receives the active router locale.

Shoppers and search engines receive valid canonical, Open Graph, breadcrumb, and search URLs without accidental double slashes. Localized stores get the correction automatically after upgrading.

### Resolve custom GraphQL definitions in repositories ending with `.faststore` (PR: [#3502](https://github.com/vtex/faststore/pull/3502))

The CLI now resolves the store root by folder name instead of treating any path ending in `.faststore` as the generated directory. Custom type definitions are consequently loaded from the correct `src/graphql` location, including when paths have trailing separators.

Developers whose repository names end with `.faststore` can build without custom GraphQL fields disappearing from the generated schema. No project rename or path workaround is required.

### Quote resolved Next.js executable paths (PR: [#3494](https://github.com/vtex/faststore/pull/3494))

Generated `.faststore/package.json` scripts now wrap resolved Next.js executable paths in double quotes. Paths containing unsafe quote, dollar, backtick, or percent characters fall back to the bare `next` command.

Developers can run generated `build`, `serve`, `dev`, and `dev-only` scripts when the Next.js binary resolves through directories containing spaces. The fallback also avoids generating malformed shell commands.

### Guard direct package script generation from unsafe paths (PR: [#3503](https://github.com/vtex/faststore/pull/3503))

The unsafe-character check for resolved Next.js paths now runs inside the package script builder. Direct callers that pass paths containing quote, dollar, backtick, or percent characters receive bare `next` scripts.

Developers are protected from malformed or shell-expanded generated commands even when code bypasses the normal path resolver. No action is required beyond upgrading.

### Preserve the search page on Yarn Classic for Windows (PR: [#3486](https://github.com/vtex/faststore/pull/3486))

The search page moves from `src/pages/s.tsx` to `src/pages/s/index.tsx`, preserving the `/s` route while avoiding a Yarn Classic tar-extraction collision on Windows. The search SSR generator now targets the nested path.

Windows developers using Yarn Classic no longer lose the search page during installation or encounter the resulting Next.js type-check failure. Store URLs and shopper navigation remain unchanged.

### Keep VTEX services attached to the correct cart line (PR: [#3504](https://github.com/vtex/faststore/pull/3504))

Cart validation now represents Checkout `bundleItems` as service properties and includes applied services in cart-line identity and relevant ETags. Serviced and unserviced units remain separate, and available offerings are not sent back to Checkout as selected services.

Shoppers keep services attached to the intended item through validation, quantity changes, reloads, and removals. Merchants avoid duplicated or dropped services and the resulting incorrect cart state.

---

## Features

### Support custom search sort values (PR: [#3496](https://github.com/vtex/faststore/pull/3496))

FastStore adds the optional `APIOptions.customSortMap` configuration and the SDK's `registerCustomSortKeys` export. Custom keys are resolved before built-in sort values, and unknown resolver values return a bad-request error.

Developers can connect custom Intelligent Search sorting to `StoreSort` and support matching deep-linked URLs without forking FastStore. Register the same keys in the API map and SDK URL parser when opting into custom sorting.

### Expose product clusters on product groups (PR: [#3499](https://github.com/vtex/faststore/pull/3499))

The GraphQL schema now includes the non-null `StoreProductCluster` type and a `productClusters` list on `StoreProductGroup`. The resolver returns Intelligent Search cluster IDs and names, or an empty list when none are available.

Developers can query a product's collections or clusters directly with its product-group data instead of adding a custom API extension or separate request. Storefronts can use this data for collection-aware merchandising and presentation after adding the field to their queries.

---

## My Account for B2B Buyer Portal (Closed beta)

### Localize My Account for B2B Buyer Portal order content (PR: [#3490](https://github.com/vtex/faststore/pull/3490))

My Account now exposes CMS fields for order filters, statuses, timelines, delivery details, totals, policy messages, and navigation labels. Dates follow the session locale, while delivery and total labels retain API or name fallbacks.

Merchants can replace hardcoded English and checkout-language strings with localized order content, giving shoppers a more consistent account experience. Regenerate and upload the My Account content schemas to make the new fields available in the CMS.

### Reset cart and session state when switching B2B contracts (PR: [#3479](https://github.com/vtex/faststore/pull/3479))

Contract switching now runs through `/api/fs/switch-contract`, sets the new authentication cookie, expires checkout ownership cookies, and clears persisted session and cart state. FastStore also identifies the default contract and keeps the account skeleton visible until session validation finishes.

B2B shoppers no longer carry a previous contract's cart into a new context or briefly see an incorrect sign-in state. Merchants gain clearer active and default contract information with no additional configuration required.

### Localize My Account quotes and the contract switcher (PR: [#3492](https://github.com/vtex/faststore/pull/3492))

FastStore replaces hardcoded Quotes and Contract Switcher text with CMS-resolvable labels, including quote statuses and filters. It also adds My Account Quotes to the CMS section and content-type pipeline.

Merchants can localize and customize quote management and contract selection, giving B2B shoppers consistent language throughout My Account. Regenerate and upload the My Account schemas to configure the new labels in the CMS.
