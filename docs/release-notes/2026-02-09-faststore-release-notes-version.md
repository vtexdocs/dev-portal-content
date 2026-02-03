---
title: "FastStore Release Notes — Version 3.96.0"
slug: "2026-02-09-faststore-release-notes-version-3-96-0"
type: "added"
createdAt: "2026-02-06T11:00:00.000Z"
updatedAt: "2026-02-06T11:00:00.000Z"
excerpt: "This release improves My Account order details for B2B with clearer delivery grouping, item-level taxes and totals, and more accurate order summaries. It also reduces stale data after login/logout."
tags:
  - FastStore
---

FastStore version `3.96.0` focuses on a clearer My Account order experience for B2B and more reliable data after authentication changes.

## General

**Fresher data after login/logout (PR: [#3152](https://github.com/vtex/faststore/pull/3152))**

GraphQL requests now add a cache-busting token when the auth cookie changes. This reduces stale data right after sign-in or sign-out, so storefront content updates more consistently.

**Logout clears client storage (PR: [#3163](https://github.com/vtex/faststore/pull/3163))**

Signing out now clears client-side storage used by session-aware features, preventing leftover data from affecting the next session.

## My Account for B2B

**Richer order details with delivery grouping (PR: [#3161](https://github.com/vtex/faststore/pull/3161))**

Order details now group items by delivery option and display clearer delivery labels (channel + estimate), including neighborhood when available. Each group shows a summary total for that delivery option.

**Item-level taxes and totals (PR: [#3161](https://github.com/vtex/faststore/pull/3161))**

Each item in the delivery accordion now shows its own tax amount and total, so customers can understand how taxes contribute to the final price.

**Recipient and delivery address details (PR: [#3161](https://github.com/vtex/faststore/pull/3161))**

Delivery sections now include recipient info and address details (or store address for pickup), helping customers confirm shipment information quickly.

**Payment surcharge visibility in the summary (PR: [#3161](https://github.com/vtex/faststore/pull/3161))**

If a payment method includes interest or surcharge, the Summary card now adds an "Interest" line item before the Total, so the final amount is transparent.
