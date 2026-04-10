---

title: "FastStore v4: New major version with performance, localization, and architectural updates"  
slug: "2026-xx-xx-faststore-v4"  
type: "added"  
createdAt: "2026-xx-xxT11:00:00.000Z"  
updatedAt: "2026-xx-xxT11:00:00.000Z"  
excerpt: "FastStore v4 is here with improved performance, built-in localization feature, and a more robust architecture for scalable storefronts."  
tags:  
  - FastStore  
---

FastStore v4 is now available, introducing important updates to how storefronts are built and managed. This release brings architectural improvements, performance optimizations, and new capabilities such as native localization (beta), along with a new standard for project dependencies, which includes a Next.js upgrade that enables a more modern and consistent development environment.

## What has changed?

### Package updates

FastStore v4 centralizes the management of core dependencies such as Next.js within `@faststore/cli`. to ensure consistency across projects, reduce dependency conflicts, and improve long-term maintainability.

* Next.js is now internally managed and updated to version \`16\`.
* Node.js runtime updated (Node 20+).

### GraphQL performance improvements

FastStore v4 improves GraphQL performance through caching, resulting in faster data fetches and a more consistent storefront experience. As part of this update, GraphQL is now an explicit project dependency.

### Localization feature (Closed Beta)

FastStore v4 introduces native localization integrated with the \[CMS\](). This feature enables scalable global storefronts with localized experiences and centralized content management.

Key capabilities include:

* Multi-locale content management.
* Multi-locale catalog and support for multiple currencies (trade policies/sales channels).
* Default locale fallback behavior.

> ⚠️ This feature is currently in closed beta. If you're interested in using this feature in your store, contact the [VTEX Support team](https://support.vtex.com/hc/en-us).

## Why did we make this change?

By standardizing dependency management and runtime environments, this release reduces conflicts and simplifies maintenance. The introduction of native localization enables teams to build and manage global storefronts more efficiently.

## What needs to be done?

To start using FastStore v4, you must review and update your project. To do that, follow the instructions in [Upgrading FastStore to v4\](/tbd).
