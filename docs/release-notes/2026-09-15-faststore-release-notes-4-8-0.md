---
title: "FastStore Release Notes — Version 4.8.0"
slug: "2026-09-15-faststore-release-notes-4-8-0"
type: improved
excerpt: "FastStore v4.8.0 adds cart-drawer recommendations for higher conversion, safer BFF extensions, and more reliable builds on Windows, plus stronger SEO for localized stores"
createdAt: "2026-09-15T00:00:00.000Z"
updatedAt: "2026-09-15T00:00:00.000Z"
hidden: true
tags:
  - FastStore
---

FastStore `v4.8.0` helps merchants increase average order value with recommendations in the mini cart, gives developers safer and faster ways to extend the BFF and run the CLI, and improves storefront stability under bot traffic and in multilingual SEO. Shoppers get a more polished My Account for B2B Buyer Portal Cards experience, and teams on Windows or in monorepos spend less time on opaque build failures. See the sections below for details.

> ⚠️ Follow the instructions in [Updating the CLI package version](https://developers.vtex.com/docs/guides/faststore/developer-tools-updating-the-cli-package-version) to upgrade to `v4.8.0` and keep your store up todate with the following improvements.

## Features

### Mini cart recommendation shelf (PR: [#3466](https://github.com/vtex/faststore/pull/3466))

Adds an optional `CartRecommendationShelf` inside the cart drawer, between cart line items and the order summary. Merchants configure the shelf on the Cart Sidebar CMS group with a display toggle (off by default), campaign VRN, title, carousel settings, and product-card options. The shelf reuses recommendation shelf patterns and hides when the cart is empty.

Merchants can promote complementary products at the moment shoppers are ready to buy, without custom storefront code. Shoppers discover relevant items without leaving checkout flow, which supports higher conversion and basket size. For more information, see the [Displaying recommendations in the mini cart](https://developers.vtex.com/docs/guides/faststore/storefront-features-displaying-product-recommendations-with-recommendation-shelf#displaying-recommendations-in-the-mini-cart) section.

### Export `validateUserAuthentication` and `getAuthCookie` from `@faststore/api` (PR: [#3481](https://github.com/vtex/faststore/pull/3481))

Exports two helpers that already exist in the BFF but were not part of the public package entry: `validateUserAuthentication(ctx)` (calls `commerce.vtexid.validate()` and throws `UnauthorizedError` / `ForbiddenError` on failure) and `getAuthCookie(ctx)` (reads the VTEX ID auth cookie from the request context).

Teams building custom BFF routes spend less time reimplementing VTEX ID checks and reduce the risk of auth bugs that expose data or block legitimate buyers. Extensions behave consistently with the platform BFF. Upgrade `@faststore/api` to `v4.8.0` and import the helpers from `@faststore/api` in server-side extension code.

---

## Bug Fixes

### Stop forwarding unvalidated `ni` output to the shell in the CLI (PR: [#3422](https://github.com/vtex/faststore/pull/3422))

Validates the stdout of `ni` package-manager detection in `getPreferredPackageManager()` before callers interpolate it into shell commands. Previously, unexpected output could produce opaque `/bin/sh: syntax error` failures during `faststore` commands with no log context tying the error to package-manager detection.

Developers and CI pipelines get clearer, faster resolution when builds fail—you are less likely to lose hours chasing a generic shell error unrelated to your store code. No configuration changes are required after upgrading to `v4.8.0`.

### Stop retrying upstream HTTP 429 responses in GraphQL client hooks (PR: [#3453](https://github.com/vtex/faststore/pull/3453))

Updates `onErrorRetry` in the GraphQL SDK so client-side hooks never retry responses with status `429`, while preserving SWR’s default retry behavior for other error statuses.

Stores see more stable performance when crawlers or bursts of traffic hit rate limits-fewer wasted API calls, less load on VTEX services, and a lower chance of degraded checkout or catalog pages for real shoppers.

### Resolve the `next` binary from `@faststore/core` (Closed beta) (PR: [#3454](https://github.com/vtex/faststore/pull/3454))

Introduces `resolvePackageBin()` so `.faststore` scripts invoke the `next` binary shipped with `@faststore/core` instead of whichever copy wins in a hoisted monorepo `node_modules/.bin` (for example an older major that does not support `next build --webpack`).

Partners and merchants using [monorepos](https://developers.vtex.com/docs/guides/faststore/monorepo-overview) can ship FastStore on the same repo layout as the rest of their stack without surprise `next build` failures, so releases stay on schedule. After upgrading to `v4.8.0`, rebuild your project..

### Keep Yarn 1 from hoisting an incompatible `@inquirer/type` into the CLI (PR: [#3459](https://github.com/vtex/faststore/pull/3459))

Adjusts `@faststore/cli` dependencies and install behavior so Yarn 1 store installs do not hoist `@inquirer/type@3` over `@inquirer/core@9`, which removed `CancelablePromise` and crashed builds after regenerating `yarn.lock`.

Yarn 1 stores regain predictable `faststore dev` and `faststore build` runs after lockfile updates, with fewer blocked local development sessions and failed deploys. Upgrade and reinstall dependencies if interactive CLI prompts previously crashed at build time.

### Point localized canonical URLs and hreflang at the rendered locale (PR: [#3470](https://github.com/vtex/faststore/pull/3470))

Fixes SSR localization URL resolution so `getStoreURL()` no longer infers locale from `window.location` during server render. Collection and listing templates receive binding-aware URLs, and PLPs emit hreflang alternates for localized routes.

Multilingual stores improve organic search signals—search engines index the correct locale URLs, and shoppers land on the right language version from SERPs and shared links. Merchants reduce duplicate-content and wrong-locale ranking issues. After upgrading to `v4.8.0`, spot-check canonical and hreflang tags on a few localized PLPs and landing pages.

### Export `Resolver`, `GraphqlContext`, and helper types from the public `@faststore/api` entry (PR: [#3474](https://github.com/vtex/faststore/pull/3474))

Re-exports GraphQL resolver typings (`Resolver`, `GraphqlContext`, and related VTEX platform types) from `packages/api/src/index.ts` so custom BFF resolvers type-check under `strict` without reaching into internal paths. Includes compatibility adjustments so the public `Resolver` type stays aligned with v3 expectations.

Teams get faster, safer development-IDE autocomplete and compile-time checks catch resolver mistakes before production, and upgrades break fewer custom integrations. Import types from `@faststore/api` and remove fragile deep imports from internal modules.

### Generate GraphQL types when the project path contains spaces (PR: [#3476](https://github.com/vtex/faststore/pull/3476))

Quotes and escapes filesystem paths in the GraphQL code-generation step so `faststore build`, `faststore dev`, and `faststore generate` succeed when the store lives under directories with spaces (for example `My Store`).

Any developer can clone a store into a normal user folder on Windows or macOS without being forced to rename paths or maintain a second copy of the project just to run the CLI.

### Keep store Storybook stories and Jest mocks out of the `.faststore` type-check (PR: [#3477](https://github.com/vtex/faststore/pull/3477))

Extends storefront copy rules so `next build` type-checking inside `.faststore` excludes store-level Storybook stories and Jest mock files.

Teams that document components in Storybook or use mocks beside production code can ship production builds without stripping dev-only files or fighting TypeScript errors unrelated to the live storefront.

### Forward `contentSource.project` as `--storeId` in CMS `cms-sync` (PR: [#3482](https://github.com/vtex/faststore/pull/3482))

Passes `contentSource.project` through to `vtex content upload-schema` as `--storeId` in the CMS `cms-sync` flow. Previously the value was only used for the account preflight check, which forced interactive toolbelt prompts during CI or headless runs.

Merchants automate CMS schema sync in CI and onboarding scripts without manual prompts, so content goes live faster and human error from picking the wrong store ID drops. Confirm `discovery.config` defines the correct `contentSource.project` for your CMS workspace.

### Normalize `outputFileTracingRoot` to forward slashes on Windows (PR: [#3484](https://github.com/vtex/faststore/pull/3484))

Converts `process.cwd()` to forward slashes before writing `outputFileTracingRoot` into generated `next.config.js`, preventing JavaScript escape sequences (such as `\f`) from corrupting the config when paths contain backslashes on Windows.

Windows-based developers get parity with macOS/Linux—production builds complete reliably instead of failing on config parse errors that have nothing to do with store business logic.

My Account for B2B Buyer Portal

### Align the saved-cards list with the design reference (PR: [#3487](https://github.com/vtex/faststore/pull/3487))

Updates `MyAccountListCards` layout and styles so the Personal and Shared saved-card listings match design review for spacing, typography, and empty states introduced in `v4.7.0`.

B2B buyers see a clearer, more trustworthy payment experience when managing personal and shared cards—fewer layout surprises and empty states that look broken. No CMS or configuration changes beyond upgrading to `v4.8.0`.
