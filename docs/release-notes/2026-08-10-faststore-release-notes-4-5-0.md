---
title: "FastStore Release Notes — Version 4.5.0"
slug: "2026-08-10-faststore-release-notes-4-5-0"
type: improved
excerpt: "FastStore version 4.5.0 focuses on My Account for B2B Buyer Portal (closed beta) quotes and contract switching, CMS-driven recommendations and custom account pages, localized PDP and PLP URLs, and Pricing Fallback support."
createdAt: "2026-08-10T00:00:00.000Z"
updatedAt: "2026-08-10T00:00:00.000Z"
hidden: false
tags:
  - FastStore
---

FastStore `v4.5.0` expands My Account for B2B Buyer Portal (closed beta) with a quotes list and contract switcher, adds CMS-configurable product recommendations and custom account pages, and improves multi-locale PDP and PLP URL resolution. It also forwards Intelligent Search Pricing Fallback tokens into Checkout and copies self-hosted fonts from `public/` during CLI generation. See the sections below for more details.

> ⚠️ Follow the instructions in [Updating the CLI package version](https://developers.vtex.com/docs/guides/faststore/developer-tools-updating-the-cli-package-version) to upgrade to `v4.5.0` and keep your store up-to-date with the following improvements.

## Features

### New `RecommendationShelf` native component (PRs: [#3403](https://github.com/vtex/faststore/pull/3403) | [#3414](https://github.com/vtex/faststore/pull/3414))

Adds a CMS-configurable `RecommendationShelf` section that fetches VTEX personalization recommendations for a campaign VRN and renders them with the shared core `ProductCard`. After upgrading to `v4.5.0`, add the **Recommendation Shelf** section in the CMS and on the desired page with a valid campaign VRN. <!-- TODO: add the guide about RecommendationShelf once we publish it: https://github.com/vtexdocs/dev-portal-content/pull/2904 -->

### Copy fonts and nested assets from `public/` folder to build (PR: [#3412](https://github.com/vtex/faststore/pull/3412))

`@faststore/cli` `copyPublicFiles` previously dropped nested directories and mismatched extensions, so self-hosted fonts under `public/fonts/` never reached the production build. Font formats (`.woff`, `.woff2`, `.ttf`, `.otf`, `.eot`) and nested directories are now copied correctly.

Stores that place fonts or nested assets in `public/` should upgrade to `v4.5.0` and re-run the build.

### Forward Pricing Fallback price token to Checkout (PR: [#3415](https://github.com/vtex/faststore/pull/3415))

When Intelligent Search emits a signed price token during a Pricing System incident, FastStore now forwards it through to Checkout so shelf prices can be trusted at add-to-cart. The field is optional: when Search omits it, behavior matches previous releases.

Accounts with the Intelligent Search Pricing Fallback flag enabled after upgrade to `v4.5.0` should ensure the store Pricing Fallback flag is on for the account.

---

## Localization feature (closed beta)

### Localized product URLs and breadcrumbs on PDP and PLP (PR: [#3402](https://github.com/vtex/faststore/pull/3402))

PDP and PLP slugs, breadcrumbs, and alternate-locale links now resolve correctly for multi-language catalogs.

Retiring `pagetype` on the collection path in favor of the typed `by-linkid` cascade changes two observable behaviors. Neither is a schema change (no query breaks), but both are worth calling out for stores that rely on them:

- **`StoreCollection.type` no longer returns `Cluster` or `SubCategory`.** Clusters and curated collections are both served by `collection/by-linkid`, so clusters now report as `Collection`. The category response doesn't expose tree depth beyond the root, so third-level categories now report as `Category`. Both enum values remain declared for backward compatibility.
- **Slugs that exhaust the cascade now return `404` instead of falling back to full-text search.** `pagetype` implicitly promoted unmatched single-segment slugs to a full-text search; the new cascade returns a not-found error when category, brand, and collection resolution all miss.

Stores that branch on `collection { type }` or rely on the search fallback for unmatched slugs should review those paths after upgrading to `v4.5.0`.

---

## My Account for B2B Buyer Portal (closed beta)

### Quotes list for B2B buyers in My Account B2B Buyer Portal (PR: [#3388](https://github.com/vtex/faststore/pull/3388))

B2B buyers with an organization unit can now open `/pvt/account/quotes` in My Account to review submitted quotes, with filtering (status and created/expiry date ranges), pagination, status badges, and navigation to order entry.

### B2B contract switcher in the account drawer (PR: [#3390](https://github.com/vtex/faststore/pull/3390))

B2B buyers can now view active contracts and switch between them for their Organization Unit directly from the FastStore account drawer. Confirming a switch refreshes the webstore token and reloads the page, so the commercial context resets. Local development may need `authenticator`/`vtexid` rewrites for non-WebOps environments.

### Prevent My Account 500s from an empty session profile and missing CMS content (PR: [#3417](https://github.com/vtex/faststore/pull/3417))

My Account routes could previously return error `500` when a representative session had an empty VTEX profile or when a My Account content type had no published CMS content. Both cases are now handled, including a fallback for `/pvt/account/404`.

### CMS-driven custom My Account pages (PR: [#3411](https://github.com/vtex/faststore/pull/3411))

Stores can now declare a My Account route bound to a CMS content type, so that new account pages are authored in CMS Admin rather than remaining code-only. An optional `contentType` on each `Route` in `navigation.ts` controls the mode: content type alone generates a CMS-only page; content type plus a `.tsx` page keeps a hybrid of CMS sections and code; omitting `contentType` preserves legacy code-only routes.

After upgrading to `v4.5.0`, add `contentType` on the desired route, sync CMS schemas, publish sections in Admin, and open the route while logged in. Existing routes without `contentType` are unchanged.
