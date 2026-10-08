---
title: VTEX IO Highlights - Week 28/2019
excerpt: "See what is new in VTEX IO Week 28/2019"
createdAt: "2019-07-17T14:47:00.000Z"
type: 'info'
---
Welcome to the VTEX IO weekly release notes!

Here’s a sneak peek at the key changes made in the last week:

> :bell: Keep up with VTEX IO release notes! Just click on **Releases only** in the **Watch** box in the right upper corner of this page.

### New features :rocket:

- [Sidecar pixel app](https://developers.vtex.com/updates/release-notes/sidecar-pixel-app) - Get your hands on a first-party integrations with the Sidecar solution.
- [Native A/B Testing](https://developers.vtex.com/updates/release-notes/native-ab-testing) – Increase your store’s conversion rate by performing native VTEX IO A/B testing, now available to clients platform-wide.
- [Typography customization](https://developers.vtex.com/updates/release-notes/typography-customization) - Easily customize your store’s typography through Storefront.

### Improvements :heavy_plus_sign:

- [Submenu behaviour](https://developers.vtex.com/updates/release-notes/submenu-behavior) - The Menu component now has a better behavior when it is triggered to expand.
- [React render performance](https://developers.vtex.com/updates/release-notes/react-render-performance) - VTEX IO now implements the new React feature that allows component data reuse using hooks.

### Notable bug fixes :bug:

- [RichText content](https://github.com/vtex-apps/admin-pages/pull/241) - RichText fields edited through storefront no longer display a hash id.
- [Block title](https://github.com/vtex-apps/render-runtime/pull/345) - The block `title` prop was used to edit the block name displayed in the Storefront section, in the new CMS version. This Pull Request aims to fix it since it was broken during the latest releases.
- **“Socket Hang Up” errors** - Recurring problems with server-side rendering, asset fetching and graphql queries were solved, ensuring that the end user no longer faces page loading errors. > ℹ️ This bug fix pull Request was done is a VTEX private repository.
