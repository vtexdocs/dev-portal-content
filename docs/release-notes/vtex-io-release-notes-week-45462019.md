---
slug: "vtex-io-release-notes-week-45462019"
title: "VTEX IO Release Notes - Week 45&46/2019"
createdAt: 2019-11-26T14:04:00.000Z
hidden: false
type: "info"
---
![App Development](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-release-notes-week-45462019-0.png)

Hey, team! Welcome to the **Black** VTEX IO Release Notes.

Yep, that's right. If this Friday is **Black Friday**, you can call us **Black Release Notes** this week because we are thrilled with this long awaited event being just around the corner.

Whether retailer or end user, I do hope that your checklist for this black week is ready, because mine is :heavy_check_mark: And guess what else? It envolves reading the entire Release Notes.

### New features 🚀

- [Site Editor](https://github.com/vtex-apps/release-notes/blob/master/docs/2019-week-45-46/site-editor.md) - They say 1 is few, 2 is good and 3 is a party. If a release for the Site Editor is already incredible, picture 3? Check out the new Topbar, complete with tooltips and new modal texts for the admin section.

### Improvements ➕

- [Platform performance](https://github.com/vtex-apps/release-notes/blob/master/docs/2019-week-45-46/platform-performance.md) - We always rejoice from performance improvements, and I promise you that this one involving data fetching is legit. Check out the VTEX IO performance improvement for week 45 and 46 of 2019.
- [Product Specifications](https://github.com/vtex-apps/release-notes/blob/master/docs/2019-week-45-46/product-specifications.md) - The Product Specifications `visibleSpecifications` and `hiddenSpecifications` props can now be edited using the admin's Site Editor. This Site Editor never tires of being a hero for code-less people, for real...
- [Breadcrumb](https://github.com/vtex-apps/release-notes/blob/master/docs/2019-week-45-46/breadcrumb.md) - If you've had a good week, Breadcrumb had a better one! The component gained two new props (`homeIconSize` and `caretIconSize`), new Handles (`homeLink` and `termArrow`) and other improvements.
- [CSS Handles](https://github.com/vtex-apps/release-notes/blob/master/docs/2019-week-45-46/css-handles.md) - The Breadcrumb was not the only one to have been gifted Handles this week. `savingPriceValue` and `savingPriceLabel` also had a lucky week and gained their own CSS Handles.
- [Search query](https://github.com/vtex-apps/release-notes/blob/master/docs/2019-week-45-46/search-query.md) - Shall we celebrate search query's independence from the facets query? Even when the latter doesn't return any results, the former renders data fetched by the `productSearch` query, providing users with search results regardless.
- [Search Result Gallery](https://github.com/vtex-apps/release-notes/blob/master/docs/2019-week-45-46/search-result-gallery.md) - During the Black Friday week, the e-commerce gods have bestowed the blessing upon the Gallery component, making it responsive and willing to accept different values for (almost) any existing device.
- [Search Result OrderBy](https://github.com/vtex-apps/release-notes/blob/master/docs/2019-week-45-46/search-result-orderby.md) - OrderBy’s new `hiddenOptions` prop does away with the component’s forced exhibitionism. Its options can now either be hidden or displayed according to the retailer’s chosen scenario.

### Notable bug fixes 🐛

- [Filter Navigator](https://github.com/vtex-apps/search-result/pull/272) - The release of the `preventRouteChange` prop in search result pages was [announced](link Release) during the last Release Notes and, believe it or not, was already cause for uncertainty. When a category was selected and then removed from the Filter Navigator, the URL was keeping the former category, showing inaccurate data to the user. This bug was already fixed and the prop is alive and well. Booyah!
- [Highlight resize](https://github.com/vtex-apps/admin-pages/pull/303) - When editing a block with the admin's Site Editor, its height may change according to its new configurations, right? The problem was that the `HighlightOverlay`, responsible for highlighting the block was being edited on the Site Editor's interface, was shy and kept the original height, thereby impairing the display of the new configurations. It's now learned to be more receptive to change and adapts according to the block's new height.
