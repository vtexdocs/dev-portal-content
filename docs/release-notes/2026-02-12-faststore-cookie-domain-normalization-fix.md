---
title: "FastStore: Cookie domain normalization fix"
slug: "2026-02-12-faststore-cookie-domain-normalization-fix"
type: "fixed"
createdAt: "2026-02-12T00:00:00.000Z"
updatedAt: "2026-02-12T00:00:00.000Z"
excerpt: "FastStore now normalizes Set-Cookie domains to the current host, preventing session cookies from being dropped on preview and localhost environments."
tags:
    - FastStore
---

Stores using FastStore now benefit from improved cookie handling across preview, localhost, and production environments. This fix ensures `Set-Cookie` headers, the response headers that store session cookies, use a domain that matches the current host, preventing session and cart issues caused by cookies being rejected by the browser.

## What has changed?

### Set-Cookie domain normalization

FastStore now rewrites the cookie domain in GraphQL responses to match the request host for allowed environments (such as `localhost` and `vtex.app`). This makes sure browsers accept and store the cookie.

### Prevented `validateCartMutation` loops

When cookies were rejected on preview or localhost, the cart validation flow could not persist state and kept retrying. With the normalized domain, the cookie is saved correctly and the validation flow stops as expected.

## Why did we make these changes?

This update improves reliability when developing and testing with FastStore by ensuring session and cart cookies are stored consistently across non-production hosts. It also prevents repeated cart validation requests and reduces UI flicker caused by missing session state.

## What needs to be done?

To apply this fix in your store, update the FastStore packages to their latest version by running `yarn upgrade -L --scope @faststore` in your terminal.
