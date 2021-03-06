---
slug: "flexible-search-results-page"
title: "Flexible search results page"
createdAt: 2021-03-31T17:53:22.959Z
hidden: false
type: "improved"
---

<div class="badge" id="store-framework">Store Framework</div>
[block:html]
{
  "html": "<br/>"
}
[/block]
Thanks to the two new props added to the `gallery` block from the [Search Results app](https://developers.vtex.com/vtex-developer-docs/docs/vtex-search-result), namely the`customSummaryInterval` and the `CustomSummary`,  it is now possible to build a custom product summary in your search result page. 

Together, both props allow you to choose a block to be rendered in a specific product interval.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ee5fb9e-gallery-custom.png",
        "gallery-custom.png",
        448,
        1392,
        "#d4d4d2"
      ],
      "caption": "Notice how the search results page above has a flexible layout to show fetched products."
    }
  ]
}
[/block]
Do not forget to check out the [Search Results documentation](https://developers.vtex.com/vtex-developer-docs/docs/vtex-search-result) to read further about the props and learn how to set them up in your store! 
[block:callout]
{
  "type": "info",
  "title": "Praise",
  "body": "This release was possible thanks to [Julio Moreira](https://github.com/juliomoreira)! Cheers!"
}
[/block]