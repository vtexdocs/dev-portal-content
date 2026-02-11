---
title: "FastStore Release Notes — Version 3.96.0"
slug: "2026-02-09-faststore-release-notes-version-3-96-0"
type: "added"
createdAt: "2026-02-06T11:00:00.000Z"
updatedAt: "2026-02-06T11:00:00.000Z"
excerpt: "This release improves My Account order details for B2B with item-level taxes and totals plus clearer order summaries. It also reduces stale data after login/logout."
tags:
  - FastStore
---

FastStore version `3.96.0` focuses on a clearer My Account order experience for B2B and more reliable data after authentication changes.

## General

**Fresher data after login/logout (PR: [#3152](https://github.com/vtex/faststore/pull/3152))**

GraphQL requests now add a cache-busting token when the auth cookie changes. This reduces stale data right after sign-in or sign-out, so storefront content updates more consistently.

**Logout clears client storage (PR: [#3163](https://github.com/vtex/faststore/pull/3163))**

Signing out now clears client-side storage used by session-aware features, preventing leftover data from affecting the next session. For more details on this fix, see the [FastStore: Cart and session management fixes](https://developers.vtex.com/updates/release-notes/2026-02-04-faststore-cart-and-session-management-fixes) Release Notes.

> ⚠️ After releasing `3.96.0`, an issue with cookie domain handling was identified and resolved in version 3.96.5 (hotfix). See the [FastStore: Cookie domain normalization fix](https://developers.vtex.com/updates/release-notes/docs/release-notes/2026-02-13-faststore-cookie-domain-normalization-fix) release notes for more information.

## My Account for B2B

**Item-level taxes and totals (PR: [#3144](https://github.com/vtex/faststore/pull/3144))**

Each item in the delivery accordion now shows its own tax amount and total, so customers can understand how taxes contribute to the final price.

**Payment surcharge visibility in the summary (PR: [#3144](https://github.com/vtex/faststore/pull/3144))**

If a payment method includes interest or a surcharge, the Summary card now adds an `Interest` line item before the Total, so the final amount is transparent.
