---
title: "FastStore: Simplified domain configuration for stores hosted on Vercel"
slug: "2025-07-01-faststore-single-domain-configuration"
hidden: false
type: "added"
createdAt: "2025-07-01T10:00:00.000Z"  
excerpt: "FastStore now defaults to a single domain for Checkout and My Account pages, simplifying domain management."
---

FastStore has simplified its domain configuration by adopting the single-domain feature for Checkout and My Account pages. This change removes the requirement for a separate secure subdomain (e.g., `secure.domain.com`).

> ⚠️ This update is currently available only for stores hosted on [Vercel](https://vercel.com/).

## What has changed?

Previously, FastStore required a distinct secure domain for Checkout and My Account pages. Now, FastStore operates with a single domain by default. This means all store URLs, including those for secure operations, will use the same base domain. See a comparison of the changes in the `discovery.config.js` file:

- **Before:** Stores required a separate `secure.domain.com` subdomain for secure pages.

    ```js
    storeUrl: "https://www.domain.com",
    secureSubdomain: "https://secure.domain.com",
    checkoutUrl: "https://secure.domain.com/checkout",
    loginUrl: "https://secure.domain.com/api/io/login",
    accountUrl: "https://secure.domain.com/api/io/account",
    ```

- **After:** All URLs (store, checkout, login, and account) use the same domain.

    ```js
    storeUrl: "https://www.domain.com",
    secureSubdomain: "https://www.domain.com",
    checkoutUrl: "https://www.domain.com/checkout",
    loginUrl: "https://www.domain.com/api/io/login",
    accountUrl: "https://www.domain.com/api/io/account",
    ```

## Why did we make this change?

The single-domain feature simplifies domain management for FastStore stores, reducing the need to configure and maintain multiple secure domains.

## What needs to be done?

To implement the single domain feature, follow these steps:

1. Open a ticket with [VTEX Support](https://help.vtex.com/en/support) requesting that the account be configured for a single-domain setup. Please include the following information in the ticket:

   - Account name
   - FastStore version

    > ⚠️ For existing stores that set up the single domain before June 26, 2025, you must open a new ticket to request re-implementation, as the feature has been improved since then.

2. Once you receive confirmation that the single-domain setup is configured in your store account, review and update the `Production URLs` section in the discovery.config.js file to ensure all URLs are consistent. For more information, see the [TBD](/tbd) instructions.
