---
title: "FastStore: Simplified domain configuration"
slug: "2025-11-14-faststore-single-domain-configuration"
hidden: false
type: "improved"
createdAt: "2025-11-14T10:00:00.000Z"  
excerpt: "FastStore now defaults to a single domain for Checkout and My Account pages, simplifying domain management for stores."
---

FastStore now routes Checkout and My Account pages through the store's primary domain (e.g., `www.domain.com`), removing the need for a separate `secure.domain.com` subdomain. This reduces configuration steps and avoids cross-domain redirects.

## What has changed?

Previously, FastStore required a [distinct secure domain for Checkout and My Account pages](https://developers.vtex.com/docs/guides/faststore/go-live-1-configuring-external-dns#step-3-configuring-domains-in-vtex-account-settings). Now, FastStore operates with a single domain by default. This means all store URLs, including those for secure operations, will use the same base domain. The following compares the changes in the [`discovery.config.js`](https://developers.vtex.com/docs/guides/faststore/project-structure-config-options) file:

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

To enable the single-domain feature, request the account configuration from VTEX. This ensures proper routing and security settings for your store.

1. Open a ticket with [VTEX Support](https://help.vtex.com/en/support) requesting the account be configured for a single-domain setup. Please include the following information in the ticket:

   - Account name
   - FastStore version

    > ⚠️ For existing stores that set up the single-domain feature before June 26, 2025, you must open a new ticket to request re-implementation, as the feature has been improved since then.

2. After receiving confirmation that the single-domain setup is configured, update the `Production URLs` section in the `discovery.config.js` file to ensure all URLs are consistent. For more information, see [Step 4 - Associating your custom domain with your FastStore project](https://developers.vtex.com/docs/guides/faststore/go-live-1-configuring-external-dns#step-4-associating-your-custom-domain-with-your-faststore-project).

### Verifying the single-domain configuration for `/checkout`

To confirm that your store is using single-domain routing for Checkout, open an incognito/private browsing window and navigate to your store’s domain (for example, `https://www.yourstore.com/checkout`). The VTEX Checkout should load under the same main domain, without redirecting to any secure subdomain. You can also test by adding a product to the cart and proceeding to checkout, ensuring that the URL remains on your main domain throughout the process. If `/checkout` fails to load correctly or you are redirected to a different domain, open a ticket with [VTEX Support](https://help.vtex.com/en/support). In the ticket, indicate that you are enabling the single-domain configuration for Checkout and include your VTEX account name.
