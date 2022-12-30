---
title: "How to use the page title control"
slug: "how-to-use-the-page-title-control"
hidden: false
createdAt: "2022-09-08T14:25:34.883Z"
updatedAt: "2022-09-08T14:25:34.883Z"
---
The `<vtex.cmc:searchTitle />` control displays the title of the following pages:
- Department
- Category
- Search

That is, it displays the information entered in the category page registration screen, in the __Name__ field.

The HTML code rendered by the Search Title control has the following pattern:

`<h2 class="titulo-sessao">Category</h2>`

That is, it renders a heading of level `<h2>`, with the `titulo-sessao` class.

By default, VTEX stores are already created with this control inserted into department and category templates.