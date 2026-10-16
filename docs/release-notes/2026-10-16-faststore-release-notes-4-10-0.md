---
title: "FastStore Release Notes — Version 4.10.0"
slug: "2026-10-16-faststore-release-notes-4-10-0"
type: improved
excerpt: "FastStore 4.10.0 shows images in CMS rich text, lists pickup points that can fulfill the shopper location, and keeps catalog and preview carts on the correct sales channel"
createdAt: "2026-10-16T00:00:00.000Z"
updatedAt: "2026-10-16T00:00:00.000Z"
hidden: true
tags:
  - FastStore
---

> ⚠️ **Fixes included from FastStore 4.9.1 and 4.9.2:** Version 4.10.0 includes the 4.9.1 fix that [restores the original product release date format](https://developers.vtex.com/updates/release-notes/2026-10-02-faststore-restored-original-product-release-date-format) and the 4.9.2 fix for [session and cart validation after region changes](https://developers.vtex.com/updates/release-notes/2026-10-05-faststore-session-and-cart-validation-fix).

FastStore `v4.10.0` lets merchants show images inside CMS rich text, and shoppers see pickup points that can fulfill orders for their location and sales channel. Anonymous visitors on stores that do not use sales channel `1` keep their catalog, and preview environments stop looping cart validation. See the fixes and features below.

> ⚠️ Follow the instructions in [Updating the CLI package version](https://developers.vtex.com/docs/guides/faststore/developer-tools-updating-the-cli-package-version) to upgrade to `v4.10.0` and keep your store up-to-date with the following improvements.

## Bug Fixes

### Keep empty carts on the session sales channel and preserve the shopper catalog (PR: [#3509](https://github.com/vtex/faststore/pull/3509))

`validateCart` no longer treats the sales channel on an empty `orderForm` as authoritative. Checkout can answer with sales channel `1` when an `orderForm` that never had items is fetched without `sc`, and FastStore now refetches that cart with the session sales channel instead of adopting `1`. An `orderForm` sales channel is adopted only when the cart has items. A sales channel that comes from the URL (localization) is always sent and is never overwritten. If Session Manager rejects an adopted sales channel for the shopper, the session retries once without that channel and does not adopt it again.

Anonymous shoppers on stores whose sales channel is not `1` keep seeing products on shelves, product listing pages, and product pages, instead of an empty catalog after a cart check. Merchants avoid a storefront that looks out of stock for visitors who have not added items. Quick Order still keeps the cart's sales channel while the cart has items. No configuration change is required beyond upgrading.

### Restore cart validation in preview environments (PR: [#3513](https://github.com/vtex/faststore/pull/3513))

On allowlisted hosts (`*.vtex.app` and `localhost`), the GraphQL API drops the `Domain` attribute from upstream `Set-Cookie` headers so the browser stores host-only cookies. A single `x-forwarded-host` value only decides whether that attribute is removed. The header value is never written into the cookie. Multi-value or malformed forwarded hosts are ignored, and the request falls back to the `host` header.

Developers and QA teams can use `*.preview.vtex.app` without `validateCart` creating a new `orderForm` on every request. That loop left preview sessions without a checkout cookie and blocked cart testing. Production stores on custom domains are unchanged, and a client-supplied `x-forwarded-host` can no longer choose the cookie scope.

---

## Features

### Show CMS rich text images on the storefront (PR: [#3448](https://github.com/vtex/faststore/pull/3448))

`RichText` now understands a Lexical `image` node with `src`, `altText`, alignment (`left`, `center`, or `right`), and a width up to 100%. It renders a lazy-loaded image inside `[data-fs-rich-text-image-wrapper]`. VTEX asset URLs receive width and quality parameters, and a node without `src` is skipped. `RichText` is exported from `@faststore/core`. The starter Newsletter and Banner Newsletter privacy-policy fields use the `draftjs-rich-text-v2` CMS widget.

Merchants can insert, align, and resize images in CMS rich text, including newsletter privacy copy, and shoppers see those images in the storefront instead of missing blocks. Developers rendering that content should use `RichText` from `@faststore/core`. After upgrading, sync the CMS schema so the newsletter privacy fields pick up the v2 widget.

### Offer pickup points that can fulfill the shopper's order (PR: [#3515](https://github.com/vtex/faststore/pull/3515))

The `pickupPoints` query lists points from Intelligent Search `pickup-point-availability` instead of the logistics shipping search. New optional arguments are `postalCode`, `country`, and `channel` (the same channel JSON string used by search facets). When `channel` is set, Intelligent Search uses that sales channel instead of the store default. Delivery hashes are sent only when the requested postal code matches the segment; coordinates can locate points when there is no postal code. `pickupPointsHash` is deprecated and always `null`, and the query cache scope is private. The pickup slider refetches when the shopper channel or country changes, ignores a late response for a previous location, and retries after a failed request.

Shoppers using Delivery Promise see pickup points that have products for their postal code and sales channel, including localized and B2B channels, instead of points from another channel or a previous location. Merchants get a slider that matches what the shopper can collect. Developers calling `pickupPoints` can pass `postalCode`, `country`, and `channel`, and should not rely on `pickupPointsHash`.
