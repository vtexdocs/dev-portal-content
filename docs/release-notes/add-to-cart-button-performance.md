---
slug: "add-to-cart-button-performance"
title: "`Add to cart` button performance"
createdAt: 2020-11-26T18:43:15.322Z
hidden: false
type: "fixed"
---

<div class="badge" id="store-framework">Store Framework</div>
[block:html]
{
  "html": "<br/>"
}
[/block]
Shopping experience was being harmed because of the unexpected extra time needed to redirect users to the Minicart once the `Add to cart` button was clicked on. 

[Our wonderful team deployed a series of performance fixes and small improvements](https://github.com/vtex-apps/add-to-cart-button/pull/50), such as adding a native loading bar to the page, in order to enhance navigation during the shopping experience!