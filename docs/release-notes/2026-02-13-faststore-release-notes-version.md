---
title: "FastStore Release Notes — Version 3.97.0"
slug: "2026-02-13-faststore-release-notes-version"
type: "added"
createdAt: "2026-02-03T11:00:00.000Z"
updatedAt: "2026-02-03T11:00:00.000Z"
excerpt: "This release lets you align product price formatting in SEO meta tags, improving consistency for crawlers and social previews."
tags:
    - FastStore
---

FastStore version `3.97.0` adds a new SEO configuration for product price formatting.

> ⚠️ This release also includes the hotfix for cookie domain handling from the `3.96.5`. For more information, see the [FastStore: Cookie domain normalization fix](https://developers.vtex.com/updates/release-notes/docs/release-notes/2026-02-13-faststore-cookie-domain-normalization-fix) release notes.

## Fixed fraction digits for the SEO product price meta tag (PR: [#3179](https://github.com/vtex/faststore/pull/3179))

You can now configure fixed fraction digits for the `product:price:amount` meta tag through PDP SEO settings, ensuring consistent price formatting for crawlers and social previews. To configure it:

1. Open your FastStore project and locate the `discovery.config.js` file.
2. In the `pdp` section, add the `minPriceAmountFractionDigits` field with the desired number of decimal places. For example:

        ```js
        seo: {
        // ...
        pdp: {
            titleTemplate: '%s | FastStore PDP',
            descriptionTemplate: '%s products on FastStore Product Detail Page',
            minPriceAmountFractionDigits: 2,
        },
        }
        ```

3. Deploy the change above.
4. Open a PDP, open DevTools (or View Page Source), search for `product:price:amount`, and check if the `<meta>` tag now uses the configured number of decimal places.
