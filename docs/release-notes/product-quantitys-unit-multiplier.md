---
slug: "product-quantitys-unit-multiplier"
title: "Styleguide's unit multiplier"
createdAt: 2021-03-31T22:18:00.000Z
hidden: false
type: "fixed"
---

<div class="badge" id="store-framework">Store Framework</div>
[block:html]
{
  "html": "<br/>"
}
[/block]
Previously, the VTEX Styleguide's unit multiplier, used by other storefront components such as the [Product Quantity](https://developers.vtex.com/vtex-developer-docs/docs/vtex-product-quantity), was not accepting inputs of any values other than 1.

In practice, the component was automatically multiplying values different than 1, whereas users were still typing, causing a misleading experience.

[This bug is now fixed](https://github.com/vtex/styleguide/pull/1366/files), and the unit multiplier is working as expected.