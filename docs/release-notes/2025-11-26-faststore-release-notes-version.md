---
title: "FastStore Release Notes — Version 3.92.0"
slug: "2025-11-26-faststore-release-notes-version"
type: "added"
createdAt: "2025-11-26T11:00:00.000Z"
excerpt: "This release introduces right-to-left (RTL) language support, improves search page metadata for better discoverability, and delivers UI refinements and stability for components."
tags:
    - FastStore
---

This release improves search page metadata for better discoverability and delivers UI refinements and stability for components.

## General

### Improvements

**Enhanced image optimization, navigation behavior, and UI improvements (PR:  [\#3092](https://github.com/vtex/faststore/pull/3092))**

* **Optimized image loading:** The default image loader now uses FastStore, providing enhanced image optimization and improved performance.  
* **Smoother navigation with scroll restoration:** An experimental scroll restoration feature has been introduced. This preserves the user's scroll position when navigating back, providing a more fluid browsing experience.  
* **Improved `TextareaField` readability:** Long text within the `TextareaField` component no longer scrolls underneath the floating label. The label now maintains its correct position, significantly improving readability.

**Improved SEO for search pages (PR:  [\#3081](https://github.com/vtex/faststore/pull/3081))**

The Search SDK now includes dynamic SEO metadata for search results pages. The `seo` object in the search response automatically populates a descriptive title and a formatted description, such as "Products for: `<search-term>`, which improves the discoverability of these pages. This is an automatic improvement and requires no action.

Search result pages are `noindex/nofollow` by default; update your search SEO settings if you want them indexed. If Search SSR is disabled, the initial HTML contains default metadata, and dynamic values are applied after hydration; enabling Search SSR helps surface dynamic metadata in the initial HTML.

### Fixes

**Fixed flickering SignIn button (PR:  [\#3078](https://github.com/vtex/faststore/pull/3078))**

Fixed an issue that caused the `SignIn` button to appear during session validation for logged-in users. The component now displays a loading skeleton, ensuring a smoother visual transition during authentication checks.

## My Account B2B

**Data consistency (PR:  [\#3092](https://github.com/vtex/faststore/pull/3092))**

The deprecated `purchaseAgentId` property has been removed to ensure data consistency and eliminate redundant query parameters.

**Buying policy alert now displays a dynamic description (PR:  [\#3076](https://github.com/vtex/faststore/pull/3076))**

The alert message on the Order Details page now dynamically displays the description from the buying policy condition. This provides approvers with a clearer context about why an order requires review.
