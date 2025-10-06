---
slug: "vtex-io-highlights-week-372019"
title: "VTEX IO Release Notes - Week 37/2019"
createdAt: 2019-09-23T17:54:00.000Z
hidden: false
type: "info"
---
![App Development](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-highlights-week-372019-0.png)

Hey! 👋 Welcome to VTEX IO Release Notes for week 37 of 2019!

You might have noticed that last week’s Release Notes didn’t reach you. Not to worry. To put you on track with VTEX IO, this week will have **two** publications! 🎉

Thrilled to announce that this week's first Release Notes brings several long awaited releases and innovative such as **SEO strategy** improvement and the **new Search GraphQL app**.

Don't get left behind with the latest on these and other key changes. Get a sneak peek at this week's main releases:

### New features 🚀

- [Hot Reload](https://github.com/vtex-apps/release-notes/blob/master/docs/2019-week-37/hot-reload.md) - The time when you had to hit the refresh button to be able to see your code changes is long gone thanks to our Hot Reload.
- [Bazaarvoice first party app](https://github.com/vtex-apps/release-notes/blob/master/docs/2019-week-37/bazaarvoice-first-party-app.md) - Get your hands on a first-party integration with the Bazaarvoice solution.
- [Flexible Search Results Page](https://github.com/vtex-apps/release-notes/blob/master/docs/2019-week-37/flexible-search-results-page.md) - Search Results Pages customization just became more powerful with `flex-layout`.

### Improvements ➕

- [Platform performance](https://github.com/vtex-apps/release-notes/blob/master/docs/2019-week-37/platform-performance.md) - Understand what were the VTEX IO performance improvement key points for week 37 of 2019.
- [SEO strategies](https://github.com/vtex-apps/release-notes/blob/master/docs/2019-week-37/seo-strategies.md) - If there is anything as sought after as a stable platform, it's SEO improvement. Therefore, check out our latest SEO releases for your VTEX IO store.
- [Search GraphQL](https://github.com/vtex-apps/release-notes/blob/master/docs/2019-week-37/search-graphql.md) - The `store-graphql` morphed into `search-graphql`, which took over responsibility for your store's GraphQL search related queries.

### Notable bug fixes  🐛

- [Site Editor blocks code](https://github.com/vtex-apps/admin-pages/pull/275) - Whenever a block is selected in Site Editor, the server responds with the latest code, allowing blocks to be edited with the most up-to-date content.
- [Site Editor `HiglightOverlay` component](https://github.com/vtex-apps/admin-pages/pull/278) - Previously, when clicking on a block that did not exist in your store, the Site Editor's section iframe would not work due to an unexpected behavior of the HighlightOverlay component (responsible for displaying on the screen which component from the list the user is currently editing). This behavior was remedied.
- [Child block customization on Site Editor](https://github.com/vtex-apps/admin-pages/pull/269) - Site Editor encountered rendering problems when users tried to edit a child block listed in a parent block. This fix enables the customization of blocks which are listed in another Site Editor block list to occur normally.
