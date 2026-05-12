---
title: "FastStore: PLP 'Load more' fix"
slug: "faststore-plp-load-more-fix"
excerpt: "Clicking 'Load more products' on PLPs now appends additional pages instead of replacing the current list."
type: "bug-fix"
publishedAt: "2026-05-11"
---

## What changed

On Product Listing Pages (PLPs), clicking **Load more products** now appends additional pages (24, 36, ...) to the current list instead of replacing it. Filter and sort changes continue to reset the gallery to the first page as expected.

## Why this matters

This fix restores the expected infinite scroll behavior on PLPs. Without it, users would lose their browsing context every time the URL changed.

## Behavior details

- Deep-linking to `?page=N` continues to work as before.
- Browser back/forward navigation continues to work as before.
- Filter or sort changes still correctly reset the gallery to the first page.

## Developer impact

This is an internal fix in `@faststore/sdk` with no public API changes required. Code that relied on `resetInfiniteScroll` running on every URL change may observe fewer resets.

## Action required

No action required. The fix is included automatically when you update `@faststore/sdk`.

## Reference

- PR: [#3308](https://github.com/vtex/faststore/pull/3308)
- Jira: [SFS-3162](https://vtex-dev.atlassian.net/browse/SFS-3162)
