---
slug: "vtex-io-highlights-week-362019"
title: "VTEX IO Release Notes - Week 36/2019"
createdAt: 2019-09-13T16:04:00.000Z
hidden: false
type: "info"
---
![App Development](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-highlights-week-362019-0.png)

Welcome to yet another VTEX IO weekly release notes, this one being more than special because we are announcing the release of our brand new VTEX IO documentation website.

Honestly, why are still reading the into after such news? Scroll down and have a look at last week's key changes:

### New features 🚀

- [VTEX IO docs](https://github.com/vtex-apps/release-notes/blob/master/docs/2019-week-36/vtex-io-docs.md) - You didn't misread! The dim light at the end of the tunnel just got brighter: the new VTEX IO documentation website is up and ready for you to access.
- [Minicart Sandbox blocks](https://github.com/vtex-apps/release-notes/blob/master/docs/2019-week-36/minicart-sandbox-blocks.md) - Customize your Minicart footer using Sandbox blocks.
- [Google Analytics `productView` event](https://github.com/vtex-apps/release-notes/blob/master/docs/2019-week-36/google-analytics-productview-event.md) - Get more insight into your store's user behavior by tracking their navigation between SKUs.

### Improvements ➕

- [Platform performance](https://github.com/vtex-apps/release-notes/blob/master/docs/2019-week-36/platform-performance.md) - Understand last week's VTEX IO performance improvement key points.
- _Storefront name change_ - Your account Admin's Storefront section, responsible for defining your store's frontend content is now called **Site Editor**. Commit to memory!
- [Events context](https://github.com/vtex-apps/release-notes/blob/master/docs/2019-week-36/events-context.md) - Create a web app with more ease with help from Events' expanding functionalities.
- [Google Analytics `orderPlaced` event](https://github.com/vtex-apps/release-notes/blob/master/docs/2019-week-36/google-analytics-orderplaced-event.md) - Make your Google Analytics metrics more reliable with the `orderPlaced` event trigger improvement.

### Notable bug fixes 🐛

- [Site Editor's component list](https://github.com/vtex-apps/admin-pages/pull/268) - Previously, site-wide components were not displayed in Site Editor's component list. With this bug fix, the full list will be displayed to the user.
- [Pickup point ID](https://github.com/vtex-apps/store-components/pull/577) - The Pickup point ID should not have been displayed in the Shipping Simulator as was the case. This bug fix remedies this scenario.
- [Google Tag Manager app events](https://github.com/vtex-apps/google-tag-manager/pull/25) - Events sent by the Google Tag Manager app were inconsistent with regards to the sent ID, which sometimes pertained to the SKU while other times to the product. This fix ensures that all events are now sent using SKU IDs.
