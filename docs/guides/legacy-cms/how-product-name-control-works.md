---
title: "How product name control works"
slug: "how-product-name-control-works"
hidden: false
createdAt: "2022-09-08T14:26:26.496Z"
updatedAt: "2022-09-08T14:26:26.496Z"
---
The `<vtex.cmc:productName/>` control renders the product name as registered in the catalog.

Therefore, it works only on product pages.

<div class="alert alert-info">
The name rendered by this control is that of the <b>product</b>, not the SKU.
</div>

This is an example of the HTML code rendered by the Product Name control.

```html
<div class="fn productName  Oculos-de-natacao-Speedo-Glypse ">Óculos de natação Speedo Glypse</div>
<input id="___rc-p-id" type="hidden" value="2">
<input id="___rc-p-dv-id" type="hidden" value="39,1">
<input id="___rc-p-sku-ids" type="hidden" value="2">
<input id="___rc-p-kit-ids" type="hidden" value="">
```

Notice that the product name appears inside a `<div>` tag, which receives the `productName` class.

You don't have to worry about the four `<input>` tags also rendered by the control. They have internal function to the platform.