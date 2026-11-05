---
title: "FastStore: Next.js and sharp security updates for v2, v3, and v4"
slug: "2026-11-05-faststore-nextjs-sharp-security-updates"
type: "fixed"
excerpt: "FastStore v2, v3, and v4 now ship patched Next.js and sharp versions, closing several CVEs disclosed for the Next.js ecosystem."
createdAt: "2026-11-05T00:00:00.000Z"
updatedAt: "2026-11-05T00:00:00.000Z"
tags:
  - FastStore
---

FastStore now ships patched versions of Next.js and `sharp` across all actively maintained majors, closing several CVEs recently disclosed for the Next.js ecosystem.

## What has changed?

`@faststore/core` 4.x now depends on `next@^16.4.3` internally, and `@faststore/core` 2.x and 3.x now depend on `sharp@^0.35.5`. Your store doesn't need to declare these packages directly; the versions come in through the core's dependency tree.

Most of the critical and high-severity advisories in this range target the App Router, Server Actions, `use cache`, and `next/og`, none of which are used by the FastStore core. FastStore stores run on the Pages Router, with a custom image loader restricted to `{account}.vtexassets.com` by default. Because of this, the practical exploitation path for most of these advisories doesn't apply to a standard FastStore store. Stores that customized the image loader with broad `remotePatterns` (such as `hostname: '**'`), or that added the App Router on their own, are the main exception.

Even where exploitation isn't practical, the previously installed versions are still flagged by `yarn audit` and by security scanners. Updating removes your store from the affected range.

## Why did we make this change?

Several Next.js advisories were disclosed, including critical remote code execution issues in `use cache`, in the Image Optimization API (SVG and AVIF), and in `next/og`. One of the SVG-related RCEs comes from `librsvg`, bundled inside `sharp`, the library Next uses to optimize images. Updating both Next.js and `sharp` closes these CVEs and keeps your store's dependency tree clear of flagged packages, even when the affected code paths aren't reachable in a standard FastStore store.

## What needs to be done?

**v4 stores (Next 16)**

1. Update [`@faststore/cli`](https://developers.vtex.com/docs/guides/faststore/developer-tools-updating-the-cli-package-version) and run the install. If your installed `@faststore/cli` range doesn't yet set the `^16.4.3` floor, update your lockfile so it resolves to `16.4.3` or newer (on Yarn 1, remove the `next@^16...` block from `yarn.lock` and run `yarn install`; `yarn upgrade next` doesn't update transitive dependencies).
2. Run `yarn why next` and confirm the tree shows a single `16.4.3`+ version coming from `@faststore/core`.
3. Remove any store-added `resolutions` or `overrides` for `next`.

**v2 and v3 stores (Next 12 and Next 13)**

1. Update `@faststore/cli` (or `@faststore/core`) to the latest patched release of your line, which bumps `sharp` to `^0.35.5`.
2. Trigger a new build in WebOps.

Node `>= 20.9.0` is required across all of these updates. WebOps v4 stores already build on Node 24, and v2/v3 stores already build on Node 20 or 22, so no change is needed in production. If you still develop locally on Node 18, update to Node 20 or newer, since `yarn install` now fails `sharp`'s engine check on Node 18.

For the full list of advisories, their severity, the versions that fix each one, and a detailed breakdown of why most of them don't expose a standard FastStore store, see [Next.js and sharp security updates for FastStore stores](https://developers.vtex.com/docs/guides/faststore/security-nextjs-and-sharp-vulnerabilities).
