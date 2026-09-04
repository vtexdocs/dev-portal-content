---
title: "FastStore Release Notes — Version 4.7.0"
slug: "2026-09-01-faststore-release-notes-4-7-0"
type: improved
excerpt: "FastStore version 4.7.0 adds My Account Cards with Personal and Shared listings, gates recommendation sessions through discovery config, and fixes redirects, localization hreflang, Order Details layout, and PDP JSON-LD markup"
createdAt: "2026-09-01T00:00:00.000Z"
updatedAt: "2026-09-01T00:00:00.000Z"
hidden: true
tags:
  - FastStore
---

FastStore `v4.7.0` lets buyers manage saved payment cards in My Account, improves how product recommendations start across the storefront, and fixes issues that caused broken redirects, incorrect SEO locale links, incomplete order pages, and invalid product markup in search results. See the sections below for more details.

> ⚠️ Follow the instructions in [Updating the CLI package version](https://developers.vtex.com/docs/guides/faststore/developer-tools-updating-the-cli-package-version) to upgrade to `v4.7.0` and keep your store up-to-date with the following improvements.

## Features

### Recommendation session gated by discovery feature flag (PR: [#3449](https://github.com/vtex/faststore/pull/3449))

Restores `experimental.enableRecommendations` in `discovery.config` so `Layout` can start the VTEX Recommendations personalization session on every page when the flag is enabled, without scanning CMS page data. When the flag is off (default), any mounted **Recommendation Shelf** starts the session as a fallback while `userId` is missing, in parallel with cookie retry. This release removes the CMS **Enable recommendations?** toggle from the Recommendation Shelf schema.

Stores get a clearer, store-wide way to turn recommendations on or off, and shelves can still load personalized products on the first visit without an extra CMS toggle per shelf. Stores that previously enabled the session through the CMS property should set `experimental.enableRecommendations: true` in `discovery.config` instead. With the flag off, mounting a Recommendation Shelf on a page is enough to trigger the fallback when no user id is available yet.

---

## Bug Fixes

### Correct item videos field casing in Search API types (PR: [#3447](https://github.com/vtex/faststore/pull/3447))

Renames the Intelligent Search item field from `Videos` to `videos` in `ProductSearchResult` and keeps `Videos` as an optional deprecated alias for backward compatibility.

Custom integrations and storefront code that read product video URLs from Search results can rely on consistent, standard field naming. Prefer `videos` in new or updated code; the deprecated `Videos` field will be removed in a future major version. No action is required if your store does not consume video URLs from Search API types directly.

### Separate hreflang slugs from locale-switch navigation (PR: [#3462](https://github.com/vtex/faststore/pull/3462))

Introduces `defaultLocaleSlug` on `StoreProduct` for locale-selector navigation fallback and limits `otherLocales` hreflang entries to slugs registered in the catalog's `availableLinkIds`. Intelligent Search `linkText` is no longer reused as an hreflang alternate when a localized slug is missing.

Shoppers switching locales land on working product URLs instead of broken links, and search engines receive accurate hreflang annotations that do not point to pages that return 404. Stores with the Localization feature enabled should verify alternate-locale links and locale-selector behavior on PDP after upgrading.

### Gate Cards route and sidebar entry on organization membership (PR: [#3463](https://github.com/vtex/faststore/pull/3463))

Adds the Cards route to `ROUTES_ONLY_FOR_B2B_MEMBERS` and redirects buyers without a unit or contract association to `/pvt/account/404` before calling the Saved-cards service. The sidebar entry is hidden for shoppers with no organization association.

Buyers who can't use saved cards no longer see a Cards menu item or reach a page that errors or shows an empty, unusable tab. Organization members keep full access; `useAdHocCard` continues to control Personal-tab rendering inside the page only. No configuration changes are required beyond upgrading to `v4.7.0`.

### Make PDP product JSON-LD Schema.org compliant (PR: [#3465](https://github.com/vtex/faststore/pull/3465))

Normalizes `StoreProduct.releaseDate` to an ISO 8601 calendar date regardless of whether Intelligent Search returns epoch milliseconds, epoch seconds, or date strings. PDP JSON-LD now omits empty `gtin`, `mpn`, `releaseDate`, and `offers` fields instead of publishing blank values, and offer prices are formatted for Schema.org compliance.

Product pages send cleaner structured data to search engines, which can improve rich-result eligibility and reduce validation warnings in tools such as Google Search Console. Upgrade to `v4.7.0` and rebuild; no store configuration changes are required.

### Resolve redirect matcher module explicitly (PR: [#3467](https://github.com/vtex/faststore/pull/3467))

Changes the local redirect matcher import to `src/customizations/src/redirects/index` so a store's `src/redirects.json` file cannot shadow the matcher function during bundling. When the exported matcher is not a function, FastStore logs a warning once and falls back to the platform redirect lookup instead of silently returning `null` and serving `404`.

Shoppers reach the correct destination when Admin redirect rules apply, even if the store also keeps a `src/redirects.json` file as documented. Stores using both `experimental.enableRedirects` and `src/redirects.json` should upgrade to restore redirect behavior. Custom redirect overrides via `src/redirects/index.ts` continue to work as before.

---

## My Account for B2B Buyer Portal

### My Account for Buyer Portal B2B Cards — Personal and Shared listing (PR: [#3443](https://github.com/vtex/faststore/pull/3443))

Adds a My Account **Cards** page at `/pvt/account/cards` with CMS-driven sections for listing personal and shared saved cards. The feature introduces GraphQL queries and resolvers for saved-card data, a `MyAccountListCards` component with Personal and Shared tabs, and CMS schemas for the new account page and list section.
Buyers with the required organization access can view and manage their saved payment cards in one place-personal cards and shared cards on separate tabs—without custom storefront code. After upgrading to `v4.7.0`, sync My Account CMS schemas, publish the Cards content type and sections in Admin, and ensure eligible buyers have the required B2B organization association. Review sidebar visibility and page gating together with PR [#3463](https://github.com/vtex/faststore/pull/3463).

### Restore Order Details layout and first-paint rendering in My Account (PR: [#3464](https://github.com/vtex/faststore/pull/3464))

Adds a `skipLazyLoading` option to `RenderSectionsBase` for authenticated My Account pages so CMS sections render on first paint instead of behind lazy-loading placeholders. Order Details grid CSS now targets CMS section wrapper classes rather than nested card data attributes, and server-side props omit undefined `orderStatusLabels` so pages without CMS order-status content serialize correctly.

Buyers opening an order in My Account see the full order layout immediately—status, payment, delivery, and summary sections in the correct grid—instead of placeholders or a broken two-column layout. Upgrade to `v4.7.0`; no CMS or theme changes are required.
