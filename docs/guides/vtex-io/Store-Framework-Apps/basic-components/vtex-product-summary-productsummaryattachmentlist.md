---
title: "Product Summary Attachment List"
slug: "vtex-product-summary-productsummaryattachmentlist"
hidden: false
createdAt: "2020-06-09T14:48:52.814Z"
updatedAt: "2022-07-02T00:50:32.983Z"
---
Product Summary Attachment is the block exported by the [Product Summary app](https://developers.vtex.com/docs/guides/vtex-product-summary) responsible for rendering the [attachment](https://help.vtex.com/en/tutorial/o-que-e-um-anexo--aGICk0RVbqKg6GYmQcWUm) options available for a product.

![att-example](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-product-summary-productsummaryattachmentlist-0.png)


## Configuration

1. Import the `vtex.product-summary` app to your theme's dependencies in the `manifest.json`:

```json
  "dependencies": {
    "vtex.product-summary": "2.x"
  }
```

2. Add the `product-summary-attachment-list` block to a store template of your choice as a child of the `product-summary.shelf` block. For example:

```diff
   "product-summary.shelf": {
    "children": [
      "product-summary-image",
      "product-summary-name",
      "product-summary-sku-name",
+     "product-summary-attachment-list",
      "product-summary-space",
      "product-summary-column#1"
    ]
  },
```

After adding the `product-summary-attachment-list` block to your store theme, use the VTEX Admin to add attachments to your products to display the component in your store correctly. For more information, please refer to [Adding an attachment](https://help.vtex.com/en/tutorial/cadastrar-um-anexo--7zHMUpuoQE4cAskqEUWScU).

## Customization

To apply CSS customizations in this and other blocks, follow the [Using CSS Handles for store customization](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-css-handles-for-store-customization) guide.

| CSS Handles  |
| ------------ |
| `attachmentListContainer`   |
| `attachmentItemContainer`   |
| `attachmentItem`            |
| `attachmentItemProductText` |