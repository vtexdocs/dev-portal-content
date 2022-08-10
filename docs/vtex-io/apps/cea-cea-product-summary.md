---
title: "Product Summary"
slug: "cea-cea-product-summary"
excerpt: "cea.cea-product-summary@0.23.0"
hidden: true
createdAt: "2022-07-08T12:23:00.849Z"
updatedAt: "2022-08-09T12:32:18.917Z"
---
Product Summary is an app responsible for summarizing product information (such as name, price and image) in other store blocks, such as the [Shelf](https://vtex.io/docs/components/all/vtex.shelf/) and the [Minicart](https://vtex.io/docs/components/all/vtex.minicart/).

![image](https://user-images.githubusercontent.com/284515/70235170-1a503a80-1741-11ea-952d-07b178995f92.png)

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
| `product-summary.shelf` | ![https://img.shields.io/badge/-Mandatory-red](https://img.shields.io/badge/-Mandatory-red)   The [entity](https://help.vtex.com/tutorial/creating-data-entity--tutorials_1265) Provides product summary data to other blocks. As a parent block, it also provides the needed structure and context for its children (listed below) to be rendered. 
| `product-summary-attachment-list` | Renders a list for the product's [attachments](https://help.vtex.com/tutorial/adding-an-attachment--7zHMUpuoQE4cAskqEUWScU) | 
| `product-summary-brand`         | Renders the product's brand | 
| `product-summary-buy-button` | Renders the Buy Button | 
| `product-summary-description` | Renders the product's description | 
| `product-summary-image` | Renders the product's image | 
| `list-context.product-list` | Renders a list of products in the Product Summary | 
| `product-summary-name` | Renders the product's name | 
| `product-summary-price` | Renders the product's price | 
| `product-summary-sku-selector` | Renders the SKU Selector block | 
| `product-specification-badges` | Renders badges based on the product's specifications |


2. Add the `product-summary.shelf` block to the block that will host the product information, such as the Shelf. Notice that although the block's name refers to the Shelf block, it can and should be used in any block that is able to render product information, such as the Minicart and those found on the [Search Results](https://vtex.io/docs/components/all/vtex.search-result/) page.

```json
    "shelf#home": {
    "blocks": [
      "product-summary.shelf"
    ],
    }
```
    
3. Then, based on the product information you desire to have rendered, choose which blocks from the exported list above will be sent as the `product-summary.shelf` children. In a scenario in which we want to display the product name, description, image, price, a SKU selector and then a Buy Button, it would go as follows:

```json
   {
  "shelf#home": {
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

In order to configure and better understand each of the Product Summary exported blocks, go through their respective documentation in the [Docs](https://github.com/vtex-apps/product-summary/tree/master/docs) folder.

#### Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles                | 
| -------------------------- |
| `container`                |
| `containerNormal`          |
| `containerSmall`           |
| `containerInline`          |
| `element`                  |
| `clearLink`                |
| `information`              |
| `imageContainer`           |
| `image`                    |
| `aspectRatio`              |
| `nameContainer`            |
| `priceContainer`           |
| `buyButtonContainer`       |
| `buyButton`                |
| `isHidden`                 |
| `description`              |
| `quantityStepperContainer` |
| `imagePlaceholder`         |
| `column`                   |
| `spacer`                   |

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!