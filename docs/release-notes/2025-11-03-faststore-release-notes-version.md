---
title: "FastStore Release Notes — Version 3.92.0"
slug: "2025-11-03-faststore-release-notes-version"
type: "added"
createdAt: "2025-11-03T11:00:00.000Z"
updatedAt: "2025-11-03T11:05:00.000Z"
excerpt: "This release introduces right-to-left (RTL) language support, improves search page metadata for better discoverability, and delivers UI refinements and stability for components."
tags:
    - FastStore
---

## My Account B2B

**Data consistency** (PR: [#3092](https://github.com/vtex/faststore/pull/3092))

The deprecated `purchaseAgentId` property has been removed to ensure data consistency and eliminate redundant query parameters.

**Buying policy alert now displays a dynamic description** (PR:  [\#3076](https://github.com/vtex/faststore/pull/3076))  
The alert message on the Order Details page now dynamically displays the description from the buying policy condition. This provides approvers with a clearer context about why an order requires review.

## General

### Added

**Right-to-Left (RTL) language support** (PR: [#3098](https://github.com/vtex/faststore/pull/3098)) - Alpha release  
This feature, which is currently in alpha, enables seamless localization for other languages, ensuring a consistent and accessible experience for global users. FastStore UI components now offer full support for right-to-left (RTL) layouts. By applying the `dir="rtl"` attribute to the `<html>` tag of your site, components like carousels, shelves, and forms will automatically adjust their layout for RTL languages. This enhancement ensures seamless localization and a consistent, accessible experience for global users.

### Improvements

**Enhanced image optimization, navigation behavior, and UI improvements** (PR: [#3092](https://github.com/vtex/faststore/pull/3092))

* **Optimized image loading:** The default image loader now uses FastStore, providing enhanced image optimization and improved performance.  
* **Smoother navigation with scroll restoration:** An experimental scroll restoration feature has been introduced. This preserves the user's scroll position when navigating back, providing a more fluid browsing experience.  
* **Improved `TextareaField` readability:** Long text within the `TextareaField` component no longer scrolls underneath the floating label. The label now maintains its correct position, significantly improving readability.

**Improved SEO for search pages** (PR: [#3081](https://github.com/vtex/faststore/pull/3081))
The Search SDK now includes dynamic SEO metadata for search results pages. The `seo` object in the search response automatically populates a descriptive title and a formatted description like Products for: `<search-term>`, improving the discoverability of these pages. This is an automatic improvement and requires no action.

### Fixes

**Fixed flickering SignIn button** (PR: [#3078](https://github.com/vtex/faststore/pull/3078))
Fixed an issue that caused the `SignIn` button to appear during session validation for logged-in users. The component now displays a loading skeleton, ensuring a smoother visual transition during authentication checks.
