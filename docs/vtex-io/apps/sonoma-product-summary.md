---
title: "Product Summary"
slug: "sonoma-product-summary"
excerpt: "sonoma.product-summary@0.0.22"
hidden: true
createdAt: "2022-07-22T22:50:22.927Z"
updatedAt: "2022-08-09T01:24:15.723Z"
---
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

Product Summary is an app responsible for summarizing product information (such as name, price and image) in other store blocks, such as the [Shelf](https://vtex.io/docs/components/all/vtex.shelf/) and the [Minicart](https://vtex.io/docs/components/all/vtex.minicart/).

![image](https://user-images.githubusercontent.com/284515/70235170-1a503a80-1741-11ea-952d-07b178995f92.png)

## Configuration

1. Import the `vtex.product-summary` app to your theme's dependencies in the `manifest.json`:

```json
  "dependencies": {
    "sonoma.product-summary": "2.x"
  }
```

Now, you are able to use all blocks exported by the `product-summary` app. Check out the full list below:

| Block name     | Description | 
| -------------- | ----------- | 
| [`list-context.product-list`](https://vtex.io/docs/components/all/vtex.product-summary/product-summary-list) | ![https://img.shields.io/badge/-Mandatory-red](https://img.shields.io/badge/-Mandatory-red) Renders the list of products in the Product Summary component. It is responsible for fetching product data and providing it to the `product-summary.shelf` block. The last one, in turn, provides the product data to its children blocks. | 
| `product-summary.shelf` | ![https://img.shields.io/badge/-Mandatory-red](https://img.shields.io/badge/-Mandatory-red) Logical block responsible for providing the needed structure for the Product Summary component through its child blocks (listed below). 
| [`product-summary-attachment-list`](https://vtex.io/docs/components/all/vtex.product-summary/product-summary-attachmentlist) | Renders a list for the product [attachments](https://help.vtex.com/tutorial/adding-an-attachment--7zHMUpuoQE4cAskqEUWScU). | 
| [`product-summary-brand`](https://vtex.io/docs/components/all/vtex.product-summary/product-summary-brand)         | Renders the product brand. | 
| [`product-summary-buy-button`](https://vtex.io/docs/components/all/vtex.product-summary/product-summary-buy-button) | Renders the Buy Button. Notice that this block should only be configured if your store still uses the [Minicart v1](https://github.com/vtex-apps/minicart/blob/383d7bbd3295f06d1b5854a0add561a872e1515c/docs/README.md). When using the [Minicart v2](https://vtex.io/docs/components/all/vtex.minicart/), you should configure the [**Add To Cart Button**](https://vtex.io/docs/components/all/vtex.add-to-cart-button/) instead.  | 
| [`product-summary-description`](https://vtex.io/docs/components/all/vtex.product-summary/product-summary-description) | Renders the product description. | 
| [`product-summary-image`](https://vtex.io/docs/components/all/vtex.product-summary/product-summary-image) | Renders the product image. | 
| [`product-summary-name`](https://vtex.io/docs/components/all/vtex.product-summary/product-summary-name) | Renders the product name. | 
| [`product-summary-sku-name`](https://vtex.io/docs/components/all/vtex.product-summary/product-summary-sku-name) | Renders the selected sku name. | 
| `product-summary-price` | ![https://img.shields.io/badge/-Deprecated-red](https://img.shields.io/badge/-Deprecated-red) The Product Summary Price block, responsible for rendering the product price, has been deprecated in favor of the [Product Price](https://vtex.io/docs/components/all/vtex.product-price/) app. Although support for this block is still granted, we strongly recommend you to use the Product Price app's blocks instead. | 
| [`product-summary-sku-selector`](https://vtex.io/docs/components/all/vtex.product-summary/product-summary-sku-selector) | Renders the SKU Selector block. | 
| [`product-specification-badges`](https://vtex.io/docs/components/all/vtex.product-summary/product-summary-specification-badges) | Renders badges based on the product specifications. |

2. Add the `list-context.product-list` block to the store theme template where you desire to display a product list and declare the `product-summary.shelf` in its block list. For example:

```json
{
  "list-context.product-list": {
    "blocks": ["product-summary.shelf"]
  },
```

:information_source: *Notice that although the `product-summary.shelf` refers to the shelf component in its name, the block does not need to be necessarily used  when building a Shelf component. It can and should be used whenever you want to render summarizing product information in other components as well, such as the [Minicart](https://vtex.io/docs/components/all/vtex.minicart/) and those found on the [Search Results](https://vtex.io/docs/components/all/vtex.search-result/) page.
    
3. Then, based on the product information you desire to have rendered in the product list, choose which blocks from the exported list above will be sent as the `product-summary.shelf` children. In a scenario in which we want to display the product name, description, image, price, a SKU selector and then a Buy Button, it would go as follows:

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

:information_source: *In order to configure and better understand each of the Product Summary exported blocks, go through their respective documentation.*

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

<!-- DOCS-IGNORE:start -->

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/gustavopvasconcellos"><img src="https://avatars1.githubusercontent.com/u/49173685?v=4" width="100px;" alt=""/><br /><sub><b>gustavopvasconcellos</b></sub></a><br /><a href="https://github.com/vtex-apps/product-summary/commits?author=gustavopvasconcellos" title="Code">💻</a></td>
    <td align="center"><a href="http://imdanielpiva.me"><img src="https://avatars0.githubusercontent.com/u/26178791?v=4" width="100px;" alt=""/><br /><sub><b>Daniel Piva</b></sub></a><br /><a href="https://github.com/vtex-apps/product-summary/commits?author=imdanielpiva" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!
<!-- DOCS-IGNORE:end -->