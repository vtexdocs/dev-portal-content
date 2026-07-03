---
title: "FastStore Release Notes — Version 4.4.0"
slug: "2026-07-02-faststore-release-notes-4-4-0"
type: improved
excerpt: "This release brings CMS-backed My Account pages, smarter cms-sync for Content Platform, Intelligent Search locale fixes, and updated Authenticator API routes."
createdAt: "2026-07-02T00:00:00.000Z"
updatedAt: "2026-07-02T00:00:00.000Z"
hidden: true
tags:
  - FastStore
---


FastStore `v4.4.0` version introduces CMS-backed pages for My Account for B2B Buyer Portal (Closed Beta), an improved CMS sync flow, locale fixes for the Localization feature (Closed Beta), and versioned Authenticator API routes.

> ⚠️ Follow the instructions in [Updating the CLI package version](https://developers.vtex.com/docs/guides/faststore/developer-tools-updating-the-cli-package-version) to upgrade to `v4.4.0` and keep your store up-to-date with the following improvements.

## Bug Fix

### Versioned Authenticator routes (PR: [#3398](https://github.com/vtex/faststore/pull/3398))

FastStore now uses versioned Authenticator API routes for password reset flows. The password reset and authentication start requests now include the `v1` segment in the API path, following the expected Authenticator route format.

Stores using FastStore My Account password reset should upgrade to `v4.4.0` to avoid issues when unversioned Authenticator paths are deprecated. No configuration changes are required.

---

## Improvements

### CMS aware `cms-sync` command (PR: [#3406](https://github.com/vtex/faststore/pull/3406))

The `vtex cms-sync` command now supports stores using the CMS. Previously, these stores had to run schema generation and upload commands separately. Now, the command identifies the store's CMS setup and runs the appropriate sync flow automatically.

For stores using the [CMS](https://developers.vtex.com/docs/guides/cms-for-faststore-storefronts), the command includes schema generation and upload in the sync process. It also checks the VTEX CLI version and verifies the authenticated VTEX account before running schema generation.

Stores using the CMS should upgrade to `v4.4.0` and run `faststore cms-sync` or `vtex cms sync` instead of separate schema commands. Stores using the Headless CMS (legacy) integration see no workflow change.

---

## Localization feature (Closed Beta)

### Sync Intelligent Search locale with URL on navigation (PR: [#3405](https://github.com/vtex/faststore/pull/3405))

FastStore now keeps Intelligent Search queries aligned with the active URL locale during client-side navigation.

Previously, stores using the Localization feature (Closed Beta) could experience stale locale data after switching locales or using browser back and forward navigation. This could cause Product Listing Pages, search results, or shelves to display product information in the wrong locale.

With this update, FastStore derives the search locale from the active route and prioritizes the locale selected in the URL. This helps ensure product names and slugs update correctly after a locale switch.

Stores with `localization.enabled` should upgrade to `v4.4.0` and verify Product Listing Pages, search pages, and shelves under locale-prefixed URLs. No configuration changes are required.

---

## My Account for B2B Buyer Portal (Closed Beta)

### CMS-backed My Account pages (PR: [#3354](https://github.com/vtex/faststore/pull/3354))

My Account for B2B Buyer Portal pages can now use CMS content. Previously, these pages relied on hardcoded English copy and could not be customized.

This update adds CMS content types and section schemas for My Account for B2B Buyer Portal pages, including profile, orders, order details, user details, security, and unauthorized access pages. If CMS content is available, My Account for B2B Buyer Portal pages render the published content. If CMS content is empty or unavailable, pages continue to render with default English content.

Merchants can use the CMS to localize labels, reorder sections, and customize order status badges. Stores with `localization.enabled` should upgrade to `v4.4.0` and no Admin setup is required.

### i18n support for My Account navigation (PR: [#3400](https://github.com/vtex/faststore/pull/3400))

My Account for B2B Buyer Portal routes now preserve the active locale during navigation and server-side redirects.

Previously, private My Account routes could drop the locale prefix when users navigated between account pages or were redirected on the server side. For example, a user could be redirected from `/pt-BR/pvt/account/orders` to `/pvt/account/orders`.

With this update, My Account links, filters, pagination, order details, and server-side redirects preserve the active locale. Price and date formatting also follow the locale from the current route.

Stores with `localization.enabled` and path-based bindings should upgrade to `v4.4.0` and verify My Account navigation, redirects, and formatting under locale-prefixed URLs.
