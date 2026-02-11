---
title: "FastStore Release Notes — Version 3.97.0"
slug: "2026-02-19-faststore-release-notes-version"
type: "added"
createdAt: "2026-02-19T11:00:00.000Z"
updatedAt: "2026-02-19T11:00:00.000Z"
excerpt: "This release lets you align product price formatting in SEO meta tags, improving consistency for crawlers and social previews."
tags:
    - FastStore
---

FastStore version `3.97.0` adds a new SEO configuration for product price formatting in PDP meta tags.

> ⚠️ This release also includes the hotfix for cookie domain handling from the `3.96.5`. For more information, see the [FastStore: Cookie domain normalization fix](https://developers.vtex.com/updates/release-notes/docs/release-notes/2026-02-13-faststore-cookie-domain-normalization-fix) release notes.

**Fixed fraction digits for the SEO product price meta tag** (PR: #3179)

You can now configure fixed fraction digits for the `product:price:amount` meta tag through PDP SEO settings, ensuring consistent price formatting for crawlers and social previews.

For full setup and validation steps, see the [Configuring product price meta tag formatting on PDP](https://developers.vtex.com/docs/guides/faststore/seo-configuring-product-price-meta-tag-on-pdp).
