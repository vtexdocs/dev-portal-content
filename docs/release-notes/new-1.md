---
slug: "new-1"
title: "Search results page customization per display mode [CSS Handles]"
createdAt: 2020-07-14T17:46:00.000Z
hidden: false
type: "improved"
---

![Store Framework](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/new-1-0.png)

It became possible to apply CSS classes to search results according to the way they are displayed on the interface!

This release marvel is all thanks to the way `galleryItem` CSS Handle (exported by the [Search Result app](https://vtex.io/docs/components/all/vtex.store-components/productspecifications/)) presently behaves when inspected.

It now accepts an HTML modifier  (`{displayMode}`) meaning that the handle name changes according to the display mode used to render search results.
![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/new-1-1.png)

In the example above, the CSS Handle `galleryItem` presents itself as `galleryItem-inline` when inspected. Notice that the new Handle name is defined according to the display mode set in the search results page.
