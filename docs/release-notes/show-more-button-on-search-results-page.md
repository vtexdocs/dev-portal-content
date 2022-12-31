---
slug: "show-more-button-on-search-results-page"
title: "Show more button on the Search Results page"
createdAt: 2020-08-05T21:27:00.000Z
hidden: false
type: "fixed"
---

Due to some changes on Google Chrome, the `Show more` button from the Search Results page was presenting an unexpected behavior when clicked on.

Even though new products were duly rendered, the interface followed the button, automatically leading users to the last visible product on the page.

This behavior was harming user experience on the Search Results page since users were not able to focus on the new products being displayed but on the button itself.
![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/show-more-button-on-search-results-page-0.gif)

Notice how the interface follows the button once it is clicked on, leading users to the last visible product on the page.
This behavior is now [fixed](https://github.com/vtex-apps/search-result/pull/402) and the `Show more` button works as expected.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/show-more-button-on-search-results-page-1.gif)

Notice how the interface does not follow the `Show more` button when it is clicked on. Instead, it shows the new  loaded products.
