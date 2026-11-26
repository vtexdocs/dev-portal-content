---
title: VTEX IO Highlights - Week 27/2019
excerpt: "See what is new in VTEX IO Week 27/2019"
createdAt: "2019-07-10"
type: 'info'
---
# VTEX IO Highlights - Week 27/2019

Welcome to the VTEX IO weekly release notes!

Here's a sneak peek at the key changes made in the last week:

> 🔔 Keep up with VTEX IO release notes! Just click on **Releases only** in the **Watch** box on the right upper corner of this page.

### New features 🚀

- [Storefront page customization by URL](https://developers.vtex.com/updates/release-notes/storefront-page-customization-by-url) - Customize your store through Storefront faster by simply navigating to the desired page using its URL.
- [Product Identifier component](https://developers.vtex.com/updates/release-notes/product-identifier-component) - Display products/SKU IDs and reference anywhere on your Product page, Shelf and Search Results.
- [Search Bar component behavior](https://developers.vtex.com/updates/release-notes/search-bar-component-behavior) - Use its new prop as `true` and enable store users to search by the desired category, brand and collection.

### Improvements :heavy_plus_sign:

- [Warning disclaimer when in master](https://developers.vtex.com/updates/release-notes/warning-disclaimer-when-in-master) - Storefront now send a warning when editing a store in a master workspace.
- [Search query](https://developers.vtex.com/updates/release-notes/search-query) - The Search component now takes 50% less time to display results to users.
- [Shelf rendering](https://developers.vtex.com/updates/release-notes/shelf-rendering) - The Shelf component now has a faster user loading time.

### Notable bug fixes :bug:

- [Auto scroll](https://github.com/vtex-apps/admin-pages/pull/233) - With this fix, users will no longer have a negative experience when trying to select a block to customize in Storefront in the new CMS.
- [Blocks without schema](https://github.com/vtex-apps/admin-pages/pull/230) – When editing a store using Storefront, users can now click on blocks that don’t have schema, such as rows and columns, without getting back an error.
- [SKU Selector](https://github.com/vtex-apps/store-components/pull/517) - The SKU Selector no longer vanishes for the user when there is just one specification to be chosen.
- [Shelf image](https://github.com/vtex-apps/shelf/pull/156) - Issues with Shelf Component image size shifting are fixed. This bug fix removes the image flickering that were negatively impacting mobile browsing.
