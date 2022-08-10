---
title: "Product Summary Attachment List"
slug: "chocolatdujour-product-summary-productsummaryattachmentlist"
excerpt: "chocolatdujour.product-summary@2.80.0"
hidden: true
createdAt: "2022-07-04T22:48:46.462Z"
updatedAt: "2022-07-04T22:48:46.462Z"
---
Product Summary Attachment is the block exported by the [Product Summary app](https://developers.vtex.com/vtex-developer-docs/docs/vtex-product-summary) responsible for rendering the [attachment](https://help.vtex.com/en/tutorial/o-que-e-um-anexo--aGICk0RVbqKg6GYmQcWUm) options available for a product.

![att-example](https://user-images.githubusercontent.com/67270558/156370029-833f68ce-a270-4e01-ae20-5d63061f0a03.png)


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

To apply CSS customizations in this and other blocks, follow the [Using CSS Handles for store customization](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-css-handles-for-store-customization) guide.

| CSS Handles  |
| ------------ |
| `attachmentListContainer`   |
| `attachmentItemContainer`   |
| `attachmentItem`            |
| `attachmentItemProductText` |