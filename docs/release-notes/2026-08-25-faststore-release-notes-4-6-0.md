---
title: "FastStore Release Notes — Version 4.6.0"
slug: "2026-08-25-faststore-release-notes-4-6-0"
type: improved
excerpt: "FastStore version 4.6.0 improves CLI reliability on Windows and in hoisted monorepos, cart sales-channel synchronization after external checkout flows, ISR recovery for transient PDP and PLP 404s, and default Twitter Card meta tags for social previews."
createdAt: "2026-08-25T00:00:00.000Z"
updatedAt: "2026-08-25T00:00:00.000Z"
hidden: true
tags:
  - FastStore
---

FastStore `v4.6.0` keeps carts aligned after external checkout flows, hardens CLI behavior on Windows and in hoisted monorepos, and recovers PDP and PLP pages from stale ISR 404 caches. It also refactors the observability stack to use `@faststore/diagnostics` instead of `@vtex/diagnostics-nodejs`, extracts the recommendation data layer into a reusable SDK module, and adds Twitter Card meta tags for richer social previews. See the sections below for details.

> ⚠️ Follow the instructions in [Updating the CLI package version](https://developers.vtex.com/docs/guides/faststore/developer-tools-updating-the-cli-package-version) to upgrade to `v4.6.0` and keep your store up-to-date with the following improvements.

## Bug Fixes

### Custom GraphQL typeDefs ignored on Windows (PR: [#3419](https://github.com/vtex/faststore/pull/3419))

Custom GraphQL type definitions under `src/graphql/**/typeDefs/*.graphql` were silently dropped on Windows during CLI schema merge and codegen, so custom Query and Mutation extensions could be missing from the merged schema without a clear error.

The CLI now converts paths to glob-safe forward-slash patterns and expands `**/*.graphql` explicitly, including when parent directories contain glob-special characters such as parentheses. Custom extensions now behave the same on Windows, macOS, and Linux, so you can extend the GraphQL schema without platform-specific workarounds or hard-to-debug missing resolvers after codegen.

After upgrading to `v4.6.0`, re-run `faststore dev` or `faststore build` so custom extensions are included in the merged schema again.

### Twitter Card meta tag for store pages (PR: [#3425](https://github.com/vtex/faststore/pull/3425))

Links shared on Twitter/X previously rendered as plain text snippets because the default Next SEO configuration did not include a Twitter Card meta tag.

FastStore now adds `twitter:card` with value `summary_large_image` to the default SEO configuration. Product and content pages get richer social previews out of the box, without wiring Twitter-specific meta tags yourself or maintaining a custom SEO override for this tag alone.

No action is required beyond upgrading. Stores with custom SEO overrides should confirm their configuration does not remove the new Twitter Card tag.

### Preserve orderForm sales channel in `validateCart` (PR: [#3435](https://github.com/vtex/faststore/pull/3435))

After external checkout flows such as Quick Order, the browser session sales channel could lag behind the orderForm trade policy, causing cart validation to send a stale `sc` query parameter.

`validateCart` now omits a stale `sc` parameter on existing carts, adopts the orderForm sales channel into the session context, and exposes an optional `salesChannel` field on the mutation response so the client can align `session.channel`. Carts stay on the correct trade policy after external checkout flows, so you avoid pricing, availability, and checkout mismatches without building custom session-sync logic around `validateCart`.

No configuration changes are required; session synchronization happens automatically on the next cart validation.

### ISR revalidation for transient `notFound` PDP and PLP paths (PR: [#3436](https://github.com/vtex/faststore/pull/3436))

PDP, PLP, and slug pages that first resolved as `notFound` during a transient Search or stock miss could be cached indefinitely by Next.js ISR, leaving valid product and listing pages stuck as 404 until a full rebuild.

Affected paths now revalidate on a configurable interval (default five minutes) via `experimental.revalidate404` in `discovery.config.js`. Transient catalog or stock misses no longer require manual redeploys, so you recover valid pages automatically during Search or inventory blips.

After upgrading to `v4.6.0`, adjust `experimental.revalidate404` if your catalog needs a shorter or longer recovery window.

### Resolve `node_modules/.bin` when running scripts inside `.faststore` (PR: [#3440](https://github.com/vtex/faststore/pull/3440))

CLI commands that run scripts inside the generated `.faststore` directory could fail when that folder had no local `node_modules`, because binaries such as `next` were not found on `PATH`.

The CLI now prepends ancestor `node_modules/.bin` directories (nearest first) to `PATH` for `dev`, `build`, and `test`. `faststore dev`, `build`, and `test` work in hoisted monorepos and nested store layouts without symlink hacks or duplicate dependency installs in `.faststore`, so you can keep your preferred package-manager and repo structure.

Developers in hoisted monorepos should upgrade to `v4.6.0`. No configuration changes are required.
