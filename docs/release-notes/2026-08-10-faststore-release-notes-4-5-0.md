---
title: "FastStore Release Notes — Version 4.5.0"
slug: "2026-08-10-faststore-release-notes-4-5-0"
type: improved
excerpt: "B2B My Account quotes and contract switching, CMS-driven RecommendationShelf and custom account pages, localized PDP/PLP URLs, Pricing Fallback tokens, and CLI public font copying"
createdAt: "2026-08-10T00:00:00.000Z"
updatedAt: "2026-08-10T00:00:00.000Z"
hidden: true
tags:
  - FastStore
---

FastStore 4.5.0 expands My Account for B2B Buyer Portal (Closed Beta)  with a quotes list and contract switcher, adds CMS-configurable product recommendations and custom account pages, and improves multi-locale PDP/PLP URL resolution. It also forwards Intelligent Search Pricing Fallback tokens into Checkout and copies self-hosted fonts from `public/` during CLI generate. See the sections below for more details.

> ⚠️ Follow the instructions in [Updating the CLI package version](https://developers.vtex.com/docs/guides/faststore/developer-tools-updating-the-cli-package-version) to upgrade to `v4.5.0` and keep your store up-to-date with the following improvements.

## Features

### Localized product URLs and breadcrumbs on PDP and PLPs (PR: [#3402](https://github.com/vtex/faststore/pull/3402))

PDP and PLP slugs, breadcrumbs, and alternate-locale links now resolve correctly for multi-language catalogs.

`StoreCollection.type` no longer returns `Cluster` or `SubCategory` (clusters report as `Collection`, deeper categories as `Category`). Unmatched single-segment slugs that previously fell back to full-text search now return `404`. Stores that branch on `collection { type }` or relied on search fallback should review those paths after upgrading to `v4.5.0`.

### CMS-configurable product recommendations (PRs: [#3403](https://github.com/vtex/faststore/pull/3403) | [#3414](https://github.com/vtex/faststore/pull/3414))

Adds a CMS-configurable `RecommendationShelf` section that fetches VTEX personalization recommendations for a campaign VRN and renders them with the shared core `ProductCard`. After upgrading to `v4.5.0`, add the **Recommendation Shelf** section in the CMS and on the desired page with a valid campaign VRN.

### Copy fonts and nested assets from public/ to build (PR: [#3412](https://github.com/vtex/faststore/pull/3412))

`@faststore/cli` `copyPublicFiles` previously dropped nested directories and mis-matched extensions, so self-hosted fonts under `public/fonts/` never reached the production build. Font formats (`.woff`, `.woff2`, `.ttf`, `.otf`, `.eot`) and nested directories are now copied correctly.

Stores that place fonts or nested assets in `public/` should upgrade to `v4.5.0` and re-run build so files copy into `.faststore/public/`.

### Forward Pricing Fallback price token to Checkout (PR: [#3415](https://github.com/vtex/faststore/pull/3415))

When Intelligent Search emits a signed price token during a Pricing System incident, FastStore now forwards it through to Checkout so shelf prices can be trusted at add-to-cart. The field is optional: when Search omits it, behavior matches previous releases.

Accounts with the Intelligent Search Pricing Fallback flag enabled should upgrade to `v4.5.0` and ensure the store Pricing Fallback flag is on for the account.

---

## My Account for B2B Buyer Portal (Closed Beta)

### Quotes list for B2B buyers in My Account B2B Buyer Portal (PR: [#3388](https://github.com/vtex/faststore/pull/3388))

B2B buyers with an organization unit can now open `/pvt/account/quotes` in My Account to review submitted quotes, with filtering (status and created/expiry date ranges), pagination, status badges, and navigation to order entry.

Stores with FastStore My Account for B2B Buyer Portal (Closed Beta) and the Quotes module enabled should upgrade to `v4.5.0` to surface the Quotes page for eligible B2B members. No extra storefront configuration is required.

### B2B contract switcher in the account drawer (PR: [#3390](https://github.com/vtex/faststore/pull/3390))

B2B buyers can now view the active contract and switch among contracts for their Organization Unit directly from the FastStore account drawer. Confirming a switch refreshes the webstore token and reloads the page so commercial context resets.

Stores using My Account for B2B Buyer Portal (Closed Beta) should upgrade to `v4.5.0`. Local development may need `authenticator`/`vtexid` rewrites for non-WebOps environments.

### Prevent My Account 500s from empty session profile and missing CMS content (PR: [#3417](https://github.com/vtex/faststore/pull/3417))

My Account routes could previously return HTTP 500 when a representative session had an empty VTEX profile or when a My Account content type had no published CMS document. Both cases are now handled gracefully, including a fallback for `/pvt/account/404`.

B2B stores on FastStore My Account should upgrade to `v4.5.0` to avoid store-wide 500s in those session and CMS states. No configuration changes are required.

### CMS-driven custom My Account pages (PR: [#3411](https://github.com/vtex/faststore/pull/3411))

Stores can now declare a My Account route bound to a CMS content type so new account pages are authored in CMS Admin instead of remaining code-only. An optional `contentType` on each `Route` in `navigation.ts` controls the mode: content type alone generates a CMS-only page; content type plus a `.tsx` page keeps a hybrid of CMS sections and code; omitting `contentType` preserves legacy code-only routes.

Upgrade to `v4.5.0`, add `contentType` on the desired route, sync CMS schemas, publish sections in Admin, and open the route while logged in. Existing routes without `contentType` are unchanged.
