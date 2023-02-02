---
title: "Product Summary"
slug: "vtex-product-summary"
hidden: false
createdAt: "2020-06-03T15:19:18.061Z"
updatedAt: "2022-07-02T00:50:32.579Z"
---

Product Summary is an app responsible for summarizing product information (such as name, price and image) in other store blocks, such as the [Shelf](https://developers.vtex.com/docs/guides/vtex-shelf/) and the [Minicart](https://developers.vtex.com/docs/guides/vtex-minicart/).

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-product-summary-0.png)

## Configuration

1. Import the `vtex.product-summary` app to your theme's dependencies in the `manifest.json`:

```json
  "dependencies": {
    "vtex.product-summary": "2.x"
  }
```

Now, you are able to use all blocks exported by the `product-summary` app. Check out the full list below:

| Block name     | Description |
| -------------- | ----------- |
| [`list-context.product-list`](https://developers.vtex.com/docs/guides/vtex-product-summary-productsummarylist) | ![https://img.shields.io/badge/-Mandatory-red](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-product-summary-1.png) Renders the list of products in the Product Summary component. It fetches product data and provides it to the `product-summary.shelf` block. This block, then, provides its child blocks with the product data. |
| `product-summary.shelf` | ![https://img.shields.io/badge/-Mandatory-red](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-product-summary-2.png).
| [`product-summary-attachment-list`](https://developers.vtex.com/docs/guides/vtex-product-summary-productsummaryattachmentlist) | Renders a list for the product [attachments](https://help.vtex.com/tutorial/adding-an-attachment--7zHMUpuoQE4cAskqEUWScU). |
| [`product-summary-brand`](https://developers.vtex.com/docs/guides/vtex-product-summary-productsummarybrand)         | Renders the product brand. |
| [`product-summary-buy-button`](https://developers.vtex.com/docs/guides/vtex-product-summary-productsummarybuybutton) | Renders the Buy Button. This block must be configured only if your store uses the [Minicart v1](https://github.com/vtex-apps/minicart/blob/383d7bbd3295f06d1b5854a0add561a872e1515c/docs/README.md). If your store uses the [Minicart v2](https://developers.vtex.com/docs/guides/vtex-minicart), please configure the [**Add To Cart Button**](https://developers.vtex.com/docs/guides/vtex-add-to-cart-button) instead.  |
| [`product-summary-description`](https://developers.vtex.com/docs/guides/vtex-product-summary-productsummarydescription) | Renders the product description. |
| [`product-summary-image`](https://developers.vtex.com/docs/guides/vtex-product-summary-productsummaryimage) | Renders the product image. |
| [`product-summary-name`](https://developers.vtex.com/docs/guides/vtex-product-summary-productsummaryname) | Renders the product name. |
| [`product-summary-sku-name`](https://developers.vtex.com/docs/guides/vtex-product-summary-productsummaryskuname) | Renders the selected sku name. |
| `product-summary-price` | ![https://img.shields.io/badge/-Deprecated-red](https://img.shields.io/badge/-Deprecated-red) Renders the product price. This block has been deprecated in favor of the [Product Price](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-product-summary-3.png) app. Although support for this block is still available, we strongly recommend that you use the Product Price app. |
| [`product-summary-sku-selector`](https://developers.vtex.com/docs/guides/vtex-product-summary-productsummaryskuselector) | Renders the SKU Selector block. |
| `product-specification-badges` | ![https://img.shields.io/badge/-Deprecated-red](https://img.shields.io/badge/-Deprecated-red) Renders badges based on the product specifications. This block has been deprecated in favor of the [VTEX Product Specification Badges](https://developers.vtex.com/docs/guides/vtex-product-specification-badges) app. Although support for this block is still available, we strongly recommend that you use the VTEX Product Specification Badges app.|

2. Add the `list-context.product-list` block to a store template of your choice and declare the `product-summary.shelf` in its block list. For example:

```json
{
  "list-context.product-list": {
    "blocks": ["product-summary.shelf"]
  },
```

> ℹ️ Although the name of the block 'product-summary.shelf' alludes to the Shelf component, this block is not required to create a Shelf component. The Product Summary Shelf is used to present summary product information in other components, such as the [Minicart](https://developers.vtex.com/docs/guides/vtex-minicart) and the [Search Results](https://developers.vtex.com/docs/guides/vtex-search-result) page.

3. Add the blocks from the list above as children of the `product-summary.shelf`, considering the product information you want to present in the product list. Take the following example in which the product name, description, image, price, SKU selector, and Buy Button are all displayed in the Product Summary:

```json
{
  "list-context.product-list": {
    "blocks": ["product-summary.shelf"]
  },

  "product-summary.shelf": {
    "children": [
      "product-summary-name",
      "product-summary-description",
      "product-summary-image",
      "product-summary-price",
      "product-summary-sku-selector",
      "product-summary-buy-button"
    ]
  }
}
```

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles                |
| -------------------------- |
| `aspectRatio`              |
| `buyButton`                |
| `buyButtonContainer`       |
| `clearLink`                |
| `column`                   |
| `container`                |
| `containerNormal`          |
| `containerSmall`           |
| `containerInline`          |
| `description`              |
| `element`                  |
| `image`                    |
| `imageContainer`           |
| `imagePlaceholder`         |
| `information`              |
| `isHidden`                 |
| `nameContainer`            |
| `priceContainer`           |
| `quantityStepperContainer` |
| `spacer`                   |
