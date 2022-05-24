---
slug: "product-summary-images-match-criteria"
title: "Product Summary Image's match criteria"
createdAt: 2021-04-01T16:05:00.000Z
hidden: false
type: "improved"
---

<div class="badge" id="store-framework">Store Framework</div>
[block:html]
{
  "html": "<br/>"
}
[/block]
The [Product Summary Images app](https://developers.vtex.com/vtex-developer-docs/docs/vtex-product-summary-productsummaryimage) can now identify and render images according to its label's substrings, set in the [Catalog module](https://help.vtex.com/en/tutorial/visao-geral-da-estrutura-do-catalogo--6ejJHhmTaoMMeoIgg4OgA0)'s `imageLabel` field. 

Previously, the `mainImageLabel` and the `hoverImageLabel` props, responsible for defining which images should be rendered by the app, did not take into account substrings, only the whole string. In practice, this means that the value passed to these props should be the same as the one defined in the Catalog's `imageLabel` field. 

The match criteria have now been broadened — from now on, render images using the Product Summary Images app based on their label's substrings as well.