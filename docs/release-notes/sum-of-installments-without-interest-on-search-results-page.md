---
slug: "sum-of-installments-without-interest-on-search-results-page"
title: "Sum of installments without interest on search results page"
createdAt: 2020-09-28T16:43:00.000Z
hidden: false
type: "fixed"
---

![https://img.shields.io/badge/-VTEX%20Store%20Framework-red](https://img.shields.io/badge/-VTEX%20Store%20Framework-red) 

Previously, the search query was presenting price errors when displaying product data on the search results page. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/356e86e-installments-bug.png",
        "installments-bug.png",
        1490,
        859,
        "#ebe7e4"
      ]
    }
  ]
}
[/block]
As shown in the image above, the sum of installments without interest was higher than the product price itself, leading to a poor and frustrating user experience. 

The search query for this page was [fixed](https://github.com/vtex-apps/search-resolver/pull/84) and the bug removed, meaning that the sum of installments without interest is now displayed mathematically correct on search results pages as well.