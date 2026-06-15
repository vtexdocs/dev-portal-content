---
title: 'FastStore Release Notes — Version 4.2.0'  
slug: '2026-06-19-faststore-release-notes-4-2-0'  
type: improved
excerpt: 'FastStore version 4.2.0 focuses on Product Listing Page (PLP) performance improvements, localization reliability, session handling fixes, and CLI stability.'  
createdAt: 2026-06-01T00:00:00.000Z  
updatedAt: 2026-06-08T00:00:00.000Z  
---
 
This release brings targeted improvements across performance, localization, session handling, and CLI reliability. Highlights include faster PLP image loading and SSR behavior, fixes for localized routing and session hydration, and Windows-specific CLI import normalizations. See the sections below for details and upgrade notes.

## Performance

### Image preloading for Product Listing Pages to improve LCP score (PR: [#3348](https://github.com/vtex/faststore/pull/3348))

`ProductListingPage` now injects a preload link for the first product card image on the page, and `ProductGrid` sets `fetchPriority: 'high'` on the first row of product images (up to 4). `ProductCard` also forwards the `fetchPriority` prop to the underlying image component.

This improves the Largest Contentful Paint (LCP) score on mobile by prioritizing the first product image load. No public API changes — `fetchPriority` is additive via `imgProps` on `ProductCard`.

### SSR ProductGallery and reduced CLS (PR: [#3349](https://github.com/vtex/faststore/pull/3349))

`ProductGallery` is now server-side rendered by replacing the previous `React.lazy` dynamic import with a static import. Additionally, `useScreenResize` was updated to use an isomorphic `useLayoutEffect` so screen-size flags are set synchronously before the first paint.

This eliminates Cumulative Layout Shift (CLS) on PLP first paint. Note that `ProductGallery` is no longer lazily loaded, so the parent bundle may grow slightly in exchange for a reduced layout shift.

### PLP first-page refetch anchored to page-load time (PR: [#3350](https://github.com/vtex/faststore/pull/3350))

The first-page refetch decision for PLP queries now uses a per-mount client-side page-load timestamp instead of the server build time. This prevents an unnecessary client-side refetch immediately after SSR hydration and preserves the SSR-injected cache. The 5-minute refetch window is maintained but is now anchored to the user's session (page open time).

---

## Bug Fixes

### Session refresh bypassed on localhost (PR: [#3325](https://github.com/vtex/faststore/pull/3325))

Adds a shared `isLocalHost` utility and uses it to bypass the cross-origin refresh-token flow on localhost in both the `useRefreshToken` hook and the `/pvt/account/403` `getServerSideProps` logic.

This prevents an always-failing refresh POST from triggering logout when developers manually inject a `VtexIdclientAutCookie_<account>` cookie while running the app locally. Behavior on non-local hosts is unchanged.

### `packageManager` field stripped from generated `.faststore/package.json` (PR: [#3335](https://github.com/vtex/faststore/pull/3335))

The CLI now builds `.faststore/package.json` without leaking the upstream `packageManager` or `exports` fields, and injects the store root's `volta` config when present. The CLI also now always prints tool `stdout/stderr` on failure (no need for `DISCOVERY_DEBUG`).

### CLI `createNextJsPages` errors no longer block `discovery.config` copy (PR: [#3356](https://github.com/vtex/faststore/pull/3356))

The CLI initialization flow now catches errors thrown by `createNextJsPages` so that a failure to create Next.js pages/APIs no longer prevents copying the store's `discovery.config` into the `.faststore` folder. This is an internal error-handling fix with no breaking changes.

### Windows URL resolution fixed in CLI (PR: [#3337](https://github.com/vtex/faststore/pull/3337))

Normalizes module URLs used by `@faststore/cli` when loading user/project configs, plugins, and discovery files. This fixes dynamic import failures on Windows caused by Windows-style (`C:/`) ESM paths. CLI commands, including `build`, `dev`, `start`, `cache`, `cms-sync`, `i18n`, and `test`, are affected. No changes for macOS/Linux users.

For Windows users:

- If you haven't seen any import/path errors, do nothing.
- If you experienced failures (errors like `module-not-found` or dynamic import errors when running those commands), upgrade `@faststore/cli` to version `4.2.0` and re-run the command.

### Pages backed by CMS silently missed content beyond the first batch (PR: [#3282](https://github.com/vtex/faststore/pull/3282))

`ContentService.getPage` now follows the CMS scroll token when calling `listEntries`, replacing a single API call with a loop that accumulates all entries across paginated responses before passing them to `fillEntriesWithData`.

Stores using the CMS data source will now receive all entries for a content type that span multiple pages (previously, only the first batch was returned).

### SlideOver uses dynamic viewport height on mobile (PR: [#3333](https://github.com/vtex/faststore/pull/3333))

Updated `SlideOver` styles to use `100dvh` (dynamic viewport height) in addition to `100vh` for non-`bottomSide` variants. This is a CSS-only fix that prevents bottom content (such as the Locale Switcher) from being cropped on mobile browsers where the browser chrome affects the effective viewport height. Desktop behavior is unchanged.

### Image loader error at VTEX assets (PR: [#3363](https://github.com/vtex/faststore/pull/3363))

Corrected how the image loader handles VTEX asset URLs so images served from VTEX assets are loaded reliably. This is a backward-compatible bug fix with no API or configuration changes.

### Flex alignment standardized in component styles (PR: [#3357](https://github.com/vtex/faststore/pull/3357))

Replaced bare `start`/`end` flex alignment keywords with `flex-start`/`flex-end` in `LocalizationSelector/styles.scss`, `OrganizationDrawer/section.module.scss`, and `Toast/styles.scss` to remove autoprefixer warnings and ensure consistent behavior across browsers. No visual changes expected.

---

## Localization feature (Closed Beta)

### Locale validation fixed for disabled localization and private routes (PR: [#3358](https://github.com/vtex/faststore/pull/3358))

`validateLocaleForHostname` now imports the merged `discovery.config` (not just the default config), short-circuits when `storeConfig.localization?.enabled` is `false`, and skips validation for routes under `/pvt/`.

This fixes 404 errors on SSR pages after upgrading to FastStore v4 when localization is disabled (the default setting). Private authenticated routes under `/pvt/` — such as `/pvt/account` and organization account pages — are no longer blocked by hostname-based locale validation. No developer action is required beyond upgrading.

### Localization race condition on session hydration (PR: [#3281](https://github.com/vtex/faststore/pull/3281))

Seeds the client session store with the URL-derived locale, currency, and sales channel at module load time, and installs a one-shot locale corrector to prevent stale IndexedDB-hydrated sessions from overwriting the URL-derived locale.

This fixes visible flickering in the `LocalizationSelector` on first load and reduces two `ValidateSession` mutations to a single URL-aligned call. No public API changes.
