---
title: "FastStore Release Notes — Version 3.95.0" 
slug: "2025-12-17-faststore-release-notes-version"
type: "added"
createdAt: "2025-12-17T11:00:00.000Z"
excerpt: "Version 3.95.0 introduces SVG support in the `public` folder and includes fixes for cart synchronization, session validation, and SEO improvements for search results."
tags:
    - FastStore
---

FastStore version 3.95.0 introduces SVG support in the `public` folder and includes fixes for cart synchronization, session validation, and SEO improvements for search results.

## General

### Improvements

**Support for SVG files in the `public` folder** (PR:  [\#3123](https://github.com/vtex/faststore/pull/3123))

We've added support for `.svg` files in the `public` folder. Now, any SVG files placed in this directory will be correctly copied to the `/.faststore/public` folder during the build process, preventing them from being overwritten or deleted.

### Fixes

**Improved Cart Synchronization Across Multiple Sessions** (PR:  [\#3091](https://github.com/vtex/faststore/pull/3091))  

Fixed a bug where using the same shopping cart across different devices or browsers could cause conflicting updates, leading to items being incorrectly removed. The validateCart mutation now includes session data when checking for \`orderForm\` changes, ensuring cart state is synchronized correctly between different user sessions.

**Address session validation errors after postal code updates** (PR:  [\#3124](https://github.com/vtex/faststore/pull/3124))

Corrected an issue where the `validateSession` GraphQL mutation would fail, particularly after a user updated their postal code. The mutation payload was being sent with unnecessary fields, which have now been removed to ensure the request is processed successfully. This improves the stability of user session updates.

**Fixed Meta Description on Search Results Page** (PR:  [\#3128](https://github.com/vtex/faststore/pull/3128))  

Corrected an issue where the meta description for search result pages would display the term undefined in the page's source code. This change ensures the meta tag is correctly formatted at build time, improving SEO by preventing incorrect content from being shown to web crawlers.
