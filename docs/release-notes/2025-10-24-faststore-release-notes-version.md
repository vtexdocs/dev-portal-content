---
title: "FastStore Release Notes — Version 3.91.0"
slug: "2025-10-24-faststore-release-notes-version"
type: "added"
createdAt: "2025-10-24T11:00:00.000Z"
updatedAt: "2025-10-24T11:05:00.000Z"
excerpt: "Version 3.91.0 improves authentication stability via centralized GraphQL validation and fixes facets for ProductShelf and ProductTiles to respect Headless CMS filters and Delivery Promise."
tags:
    - FastStore
---

This FastStore release focuses on improving stability and developer experience across authentication and product component handling. It enhances user session reliability, simplifies GraphQL security validation, and ensures accurate behavior for Headless CMS-configured facets.

**Improved user session and authentication handling** (PR: [\#3065](https://github.com/vtex/faststore/pull/3065))  

We've enhanced the authentication flow by improving user session validation and fixing server-side refresh token issues. This update resolves inconsistencies in cookie handling and data types, resulting in a more stable and predictable login experience for shoppers.

For developers, session validation has been centralized at the GraphQL layer using the `@auth` directive. This refactoring consolidates security checks, simplifies query protection, and enhances the robustness and maintainability of the overall authentication process.

**Fixed `ProductShelf` and `ProductTiles` facet handling** (PR: [\#3073](https://github.com/vtex/faststore/pull/3073))

We've fixed issues in the `ProductShelf` and `ProductTiles` components where `selectedFacets` were being incorrectly applied. Facets configured in the CMS, such as `productClusterIds (collections)`, are now correctly respected.

Additionally, for stores using [Delivery Promise](https://developers.vtex.com/docs/guides/faststore/delivery-promise-implementation), these components now rely on the global pickup point facet rather than inheriting shipping method filters from the Product Listing Page (PLP).
