---
title: "FastStore Release Notes — Version 4.11.3"
slug: "2026-11-17-faststore-release-notes-4-11-3"
type: improved
excerpt: "FastStore 4.11.3 applies API directives to store fields, adds the preserveCartLines flag, and fixes cart validation, CMS requests, and My Account templates"
createdAt: "2026-11-17T00:00:00.000Z"
updatedAt: "2026-11-17T00:00:00.000Z"
hidden: true
tags:
  - FastStore
---

FastStore `v4.11.3` covers the changes from `v4.11.0` through `v4.11.3`. It fixes how store API extensions apply the `@auth` and `@cacheControl` directives, improves cart validation for assembly options and split cart lines, and reduces CMS requests while resolving templates. It also adds the opt-in `preserveCartLines` flag. See the fixes and the feature below.

> ⚠️ Follow the instructions in [Updating the CLI package version](https://developers.vtex.com/docs/guides/faststore/developer-tools-updating-the-cli-package-version) to upgrade to `v4.11.3` and keep your store up to date with the following improvements.

## Bug Fixes

### Store API extension fields honor `@auth` and `@cacheControl` (PR: [#3524](https://github.com/vtex/faststore/pull/3524))

Store fields declared in your GraphQL extensions now run the `@auth` and `@cacheControl` directives. Before this fix, the directives were added to the schema but were not applied to store fields: `@auth` didn't validate the shopper's session, and `@cacheControl` didn't contribute to the response `cache-control` header. FastStore's own fields were not affected.

Stores that already annotate fields with these directives see the annotations take effect after upgrading, as described in [Authentication in API extensions](https://developers.vtex.com/docs/guides/faststore/api-extensions-authentication-in-api-extensions). Review your annotated store fields and test them after upgrading.

### Cart keeps its lines when an assembly child SKU is missing from Search (PR: [#3536](https://github.com/vtex/faststore/pull/3536))

Stores that sell services as assembly options often hide the service SKUs from the storefront. Before this fix, when Intelligent Search didn't return one of these SKUs, cart validation failed with `Search API didn't find the following SKUs`, and the next validation could remove the product and its service from Checkout.

Cart validation now builds an assembly option child that Search doesn't return from its line in the Checkout order form. Other missing SKUs still fail the mutation, so a Search outage is not hidden. Stores with hidden assembly option SKUs get this behavior after upgrading, and no configuration change is needed. See [Keeping split cart lines](https://developers.vtex.com/docs/guides/faststore/developer-tools-keeping-split-cart-lines#step-2---test-the-cart-behavior-locally) for how to test assembly option carts.

### Shipping data stops updating on every cart validation (PR: [#3554](https://github.com/vtex/faststore/pull/3554))

When the address in the order form had no `geoCoordinates`, cart validation resent `shippingData` on every call. Each call increased the `CheckoutOrderFormOwnership` cookie, which could cause HTTP `431` errors. Address changes are still detected by postal code, so an update is sent only when the postal code changes.

Stores that save addresses without coordinates, for example through a headless checkout, no longer see the cookie grow during cart updates. No action is required beyond upgrading.

### Fewer CMS requests for PLP and PDP templates (PR: [#3551](https://github.com/vtex/faststore/pull/3551))

FastStore now reads list content for CMS templates inline, so refilling the template cache no longer requests each entry separately. PDP templates are matched from the cached list instead of a direct lookup by product slug, which never matched a template — see [PDP template selection criteria](https://developers.vtex.com/docs/guides/faststore/headless-cms-multiple-page-template#pdp-template-selection-criteria).

Stores with many PLP templates make far fewer CMS requests while resolving PDP and PLP templates. Previews still load entries individually. No action is required beyond upgrading.

### Setting `subDomainPrefix` to an empty array replaces the default `www` prefix (PR: [#3577](https://github.com/vtex/faststore/pull/3577))

In `discovery.config.js`, an empty `api.subDomainPrefix` array now replaces the default `www` prefix instead of being merged with it. Before this fix, `www` was always kept, so Checkout received the root domain and set its cookies on it. Those cookies were then sent in duplicate, which could cause the `Cookie` header to exceed the server limit.

Stores that set `subDomainPrefix` to an empty array see Checkout cookies set on `www.<domain>` instead of `<domain>`. Cookies already set on the root domain stay in the browser until they expire. If `secureSubdomain` uses a different host, FastStore prints a warning during build and development. Stores that set a non-empty prefix or don't set the option keep the current behavior.

---

## Features

### Keep split cart lines with the `preserveCartLines` flag (PR: [#3535](https://github.com/vtex/faststore/pull/3535))

FastStore now supports the opt-in `api.preserveCartLines` flag in `discovery.config.js`. By default, FastStore merges cart lines that share the same SKU into a single line. When a store splits a line in Checkout, for example, so that each unit can have its own assembly options, the flag keeps each unit as a separate cart line, and editing or removing one line affects only that line. FastStore doesn't split lines on its own.

The flag is off by default, so stores that don't set it keep the current behavior. Checkout can also return multiple lines of the same SKU due to promotions, so enable the flag only when your store needs to keep split lines. For setup steps, see [Keeping split cart lines](https://developers.vtex.com/docs/guides/faststore/developer-tools-keeping-split-cart-lines).

---

## My Account for B2B Buyer Portal

### My Account CLI templates use the `isB2BBuyer` prop (PR: [#3574](https://github.com/vtex/faststore/pull/3574))

The CLI templates that generate custom My Account pages passed `isRepresentative`, but `@faststore/core` renamed that prop to `isB2BBuyer`. Pages generated from FastStore `4.10.2` through `4.11.0` no longer matched the core types, so `next build` failed in stores with custom account pages.

Upgrading to `v4.11.3` generates pages with `isB2BBuyer`. If your store has a custom My Account page based on those templates, update the prop from `isRepresentative` to `isB2BBuyer`.
