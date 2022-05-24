---
slug: "new-1"
title: "Search results page customization per display mode [CSS Handles]"
createdAt: 2020-07-14T17:46:00.000Z
hidden: false
type: "improved"
---

![https://img.shields.io/badge/-VTEX%20Store%20Framework-red](https://img.shields.io/badge/-VTEX%20Store%20Framework-red)

It became possible to apply CSS classes to search results according to the way they are displayed on the interface! 

This release marvel is all thanks to the way `galleryItem` CSS Handle (exported by the [Search Result app](https://vtex.io/docs/components/all/vtex.store-components/productspecifications/)) presently behaves when inspected. 

It now accepts an HTML modifier  (`{displayMode}`) meaning that the handle name changes according to the display mode used to render search results. 
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/bacaa3a-release-displaymode-modifier.png",
        "release-displaymode-modifier.png",
        1562,
        733,
        "#5f5c59"
      ],
      "caption": "In the example above, the CSS Handle `galleryItem` presents itself as `galleryItem-inline` when inspected. Notice that the new Handle name is defined according to the display mode set in the search results page."
    }
  ]
}
[/block]