---
title: "FastStore Release Notes — Version 4.3.0"
slug: "2026-06-19-faststore-release-notes-4-3-0"
type: improved
excerpt: "FastStore version 4.3.0 focuses on storefront password protection, QuickOrder file upload through the Order Entry Service, GraphQL BFF error handling, and My Account reliability fixes."
createdAt: "2026-06-19T00:00:00.000Z"
updatedAt: "2026-06-19T00:00:00.000Z"
hidden: true
tags:
  - FastStore
---

This release introduces storefront password protection and QuickOrder file upload through the VTEX Order Entry Service (OES), along with fixes for My Account authentication, password reset routing, and GraphQL BFF error status propagation. It also migrates Partytown to the maintained `@qwik.dev` package. See the sections below for details and upgrade notes.

> ⚠️ Follow the instructions in [Updating the CLI package version](https://developers.vtex.com/docs/guides/faststore/developer-tools-updating-the-cli-package-version) to upgrade to `v4.3.0` and keep your store up-to-date with the following improvements.

## Features

### Password Protection ([#3276](https://github.com/vtex/faststore/pull/3276))

FastStore now ships a password-protection flow for gated storefront access. The change adds middleware that validates a secure session cookie, a `/api/fs/password-protection/unlock` endpoint that verifies passwords and returns a safe redirect URL, and a login page for protected environments. WebOps settings continue to drive which domains require authentication. The CLI also removes localization-based proxy filename toggling from `dev` and `build` commands.

Merchants can restrict preview URLs and production domains to authorized users, reducing accidental public exposure during development and launch. Upgrade your store to `v4.3.0` and configure password protection in [FastStore WebOps](https://developers.vtex.com/docs/guides/faststore/webops-dashboard#password-protection) to enable the storefront login flow.

### File upload via Order Entry Service (OES) ([#3334](https://github.com/vtex/faststore/pull/3334))

QuickOrder file upload now uses the VTEX Order Entry Service instead of a rigid CSV parser. `@faststore/api` adds GraphQL operations (`uploadFileToOrderEntry`, `startOrderEntryOperation`, `orderEntryOperation`, `orderFormItems`) and VTEX commerce client methods for the OES flow. `@faststore/core` introduces `useOrderEntryUpload`, `useOrderEntryOperation`, `useOrderFormItems`, and the orchestration hook `useOrderEntry`. `@faststore/components` adds a `Processing` state to `FileUploadStatus` with a configurable `processingStatusText` label. `SearchInput` is refactored to use the OES-backed flow end-to-end, and the legacy `useCSVParser` hook and `useBulkProductsQuery` are removed.

Stores using QuickOrder file upload can accept more file formats and benefit from server-side parsing with AI-assisted extraction. The UI flow remains upload → processing → drawer, but processing is now distinct from upload. No configuration changes are required beyond upgrading your store to `v4.3.0` and republishing CMS content if you customize `processingStatusText` in the Navbar schema.

---

## Bug Fixes

### Propagate upstream error status instead of always 500 ([#3379](https://github.com/vtex/faststore/pull/3379))

The GraphQL BFF at `/api/graphql` previously returned HTTP `500` for all errors because masked `GraphQLError` instances hid the nested `FastStoreError` that carries `extensions.status`. The handler now unwraps masked errors via `recoverFastStoreError` and returns the upstream status (for example, `400` for invalid shipping `postalCode`). Non-production responses include structured `extensions.type` and `extensions.status`; upstream messages are omitted in production.

API consumers and debugging workflows now receive accurate HTTP status codes instead of generic `500` responses. The storefront SDK still builds errors from `response.status` before reading the body. Upgrade your store to `v4.3.0` and review any custom error handling that assumed all BFF failures were `500`.

### Order Entry header authentication fix ([#3395](https://github.com/vtex/faststore/pull/3395))

After #3381 removed the `withAutCookie` helper, the Order Entry Service client methods introduced in #3334 still referenced the helper, breaking builds and file upload requests. The five `orderEntry` methods now use the same `withCookie` header pattern as other authenticated commerce calls, preserving `multipart/form-data` for file upload.

Stores using OES-backed QuickOrder file upload should upgrade to `4.3.0` together with [#3334](https://github.com/vtex/faststore/pull/3334). No separate configuration is required.

---

## Dependencies updates

### Migrate Partytown to @qwik.dev ([#3394](https://github.com/vtex/faststore/pull/3394))

`@faststore/core` replaces `@builder.io/partytown@^0.6.1` with `@qwik.dev/partytown@^0.14.0`, following the official Partytown package relocation. Runtime behavior is unchanged: the CLI still runs `partytown copylib` at `predev`/`prebuild` and loads static assets from `/~partytown/partytown.js`.

After upgrading to `v4.3.0`, re-run `faststore dev` or `faststore build` so `public/~partytown/` is regenerated. No store configuration changes are required.

---

## My Account for B2B Buyer Portal (Closed Beta)

### Forward auth token only via account-scoped cookie (PR: [#3381](https://github.com/vtex/faststore/pull/3381))

Logged-in shoppers were redirected to `/pvt/account/403` when accessing FastStore My Account because `@auth`-protected GraphQL queries forwarded the VTEX ID token twice—via the account-scoped cookie and a duplicated top-level header. The platform rejected the duplicate with `401` even for valid sessions. This PR standardizes authenticated VTEX requests on the account-scoped cookie pattern used elsewhere in `@faststore/api`.

Stores with `experimental.enableFaststoreMyAccount` enabled should regain access to My Account routes after upgrading. No configuration changes are required.

### Use authenticator route for set password ([#3380](https://github.com/vtex/faststore/pull/3380))

The My Account **Reset password** flow in `useSetPassword` now posts to `/api/authenticator/pub/authentication/classic/setpassword` instead of the deprecated `/api/vtexid/pub/authentication/classic/setpassword` endpoint. The account name is passed explicitly via the `an` query parameter, sourced from the hook argument with a fallback to `config.api.storeId`. The request method, credentials, form body, and success/error toast mapping remain unchanged.

Stores using FastStore My Account security settings should verify the password reset after upgrading. No configuration is required.
