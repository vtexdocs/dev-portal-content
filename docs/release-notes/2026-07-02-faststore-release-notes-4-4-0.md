---
title: "FastStore Release Notes — Version 4.4.0"
slug: "2026-07-02-faststore-release-notes-4-4-0"
type: improved
excerpt: "My Account CMS customization and localized navigation, content-source aware cms-sync, Intelligent Search locale fixes, and authenticator API v1 routes"
createdAt: "2026-07-02T00:00:00.000Z"
updatedAt: "2026-07-02T00:00:00.000Z"
hidden: true
tags:
  - FastStore
---

FastStore 4.4.0 extends My Account with CMS-driven page composition and locale-aware navigation for localized stores. The CLI `cms-sync` command now detects Content Platform vs legacy Headless CMS from `discovery.config.js`. This release also fixes Intelligent Search locale drift after navigation and updates My Account password reset to versioned Authenticator API routes. See the sections below for details.

> ⚠️ Follow the instructions in [Updating the CLI package version](https://developers.vtex.com/docs/guides/faststore/developer-tools-updating-the-cli-package-version) to upgrade to `v4.4.0` and keep your store up-to-date with the following improvements.

## Bug Fix

### Version authenticator routes to v1 (PR: [#3398](https://github.com/vtex/faststore/pull/3398))

The Authenticator API now expects versioned routes. In `packages/core/src/sdk/account/useSetPassword.ts`, the `setpassword` and `start` fetch URLs insert the `v1` segment after `authenticator/` (for example, `/api/authenticator/v1/pub/authentication/classic/setpassword` and `/api/authenticator/v1/pub/authentication/start`). Unit tests in `useSetPassword.test.ts` assert the updated path substrings.

Stores using FastStore My Account password reset should upgrade to avoid failures when unversioned Authenticator paths are deprecated. No configuration changes are required.

---

## Feature

### Content-source aware cms-sync command (PR: [#3406](https://github.com/vtex/faststore/pull/3406))

Content Platform stores previously had to run `vtex content generate-schema` and `upload-schema` manually. The `cms-sync` command in `@faststore/cli` now reads `contentSource.type` from `discovery.config.js` and runs the appropriate flow: legacy Headless CMS sync unchanged, or CP with generate and upload built in. CP mode runs a pre-flight check (`vtex --version` and `vtex whoami` vs `api.storeId`) before interactive schema generation. When `experimental.enableFaststoreMyAccount` is enabled, core My Account CMS schemas are file-merged with the store's `cms/faststore/{components,pages}` into a staging directory under `.faststore` (store overrides core) and used as the generate/upload input.

Stores on Content Platform should upgrade and run `faststore cms-sync` (or `vtex cms sync`) instead of separate schema commands. Legacy Headless CMS stores see no workflow change.

---

## Localization feature (Closed Beta)

### Sync Intelligent Search locale with URL on navigation (PR: [#3405](https://github.com/vtex/faststore/pull/3405))

When `localization.enabled` is true, client-side Intelligent Search queries could use a stale locale after a hard locale switch or browser back/forward navigation. In `@faststore/core`, `useLocalizedVariables` now derives the locale facet from `router.locale` via `getSettings` instead of `session.locale`. In `@faststore/api`, `getSegmentLocale` prefers `ctx.storage.locale` (set from trusted `selectedFacets`) over the `vtex_segment` cookie `cultureInfo`, which can lag behind the URL.

Stores with localization enabled on PLPs, search, and shelves should see product names and slugs update immediately after switching locale. No configuration changes are required.

---

## My Account for B2B Buyer Portal (Closed Beta)

### CMS-backed My Account pages (PR: [#3354](https://github.com/vtex/faststore/pull/3354))

My Account pages previously used hardcoded English copy with no merchant customization path. This PR adds six CMS content-types (`myAccountProfile`, `myAccountOrders`, `myAccountOrderDetails`, `myAccountUserDetails`, `myAccountSecurity`, `myAccountUnauthorized`) and 14 section schemas under `packages/core/cms/faststore/my-account/`. Each route SSR-fetches CMS content via `fetchMyAccountPageContent` and falls back to default sections in `myAccountDefaultSections.ts` when CMS is empty or unavailable. Section wrappers in `packages/core/src/components/sections/Account/` map CMS `section.data` to UI label props; GraphQL still supplies account data through `accountPageData`.

Merchants on Content Platform can publish My Account content-types to localize labels, reorder sections, and customize order status badges. Pages render with English defaults when CMS content is not published—no Admin setup is required for basic functionality.

### i18n support for My Account navigation (PR: [#3400](https://github.com/vtex/faststore/pull/3400))

My Account private routes did not preserve the active locale prefix during navigation and SSR redirects (for example, dropping from `/pt-BR/pvt/account/orders` to `/pvt/account/orders`). Account menu, orders list, pagination, filters, and order detail links now resolve hrefs through `useLink` / `resolveLink`. SSR redirects on My Account GSSPs wrap destinations with `localizeRedirectDestination`. The proxy skips subdomain rewrite when the request locale differs from the root binding, avoiding double-prefix URLs. Price and date formatting read `useRouter().locale`, and `reconcileSessionLocale` keeps the URL-derived locale on session hydrate and tab focus.

Stores with `localization.enabled` and path-based bindings should verify My Account navigation, redirects, and formatting under locale-prefixed URLs. Stores without localization enabled are unaffected.
