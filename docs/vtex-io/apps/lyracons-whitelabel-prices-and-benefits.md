---
title: "Whitelabel Prices and Benefits"
slug: "lyracons-whitelabel-prices-and-benefits"
excerpt: "lyracons.whitelabel-prices-and-benefits@0.0.18"
hidden: true
createdAt: "2022-08-04T00:59:02.599Z"
updatedAt: "2022-08-04T01:59:57.414Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

This app can be used to show clustered promotions and prices based on whitelabel prices lists.

## Configuration 

To use the **Whitelabel Prices and Benefits** components you should:

1. Install the **whitelabel-prices-and-benefits** app in your store.
2. Add the **whitelabel-prices-and-benefits** as theme dependency in the manifest.json file.
3. Create the promotion(s) based on specific client clusters like "seller=test"
4. Include the seller field in the clients masterdata entity
5. Fill the client field value (for testing purposes), it should be fille during the client registration process
6. Include the **whitelabel-price-and-benefits-provider** as product-summary.shelf children. The **whitelabel-price-and-benefits-provider** block will contain all your regular shelf blocks as childrens (see blocks section examples). For the Product Detail Page you should include the **whitelabel-price-and-benefits-provider** as direct block in the "store.product" block and add the regular blocks as childrens of the provider block. if you will use the component in both sides, you should use names for each one. Example: "whitelabel-price-and-benefits-provider#product-summary" and "whitelabel-price-and-benefits-provider#product-detail".
7. Include the **whitelabel-price-and-benefits-highlight** where you want to show your promotions highlights based on the clustered seller (optional). It will include the regular promotions, not teaser or collection based promotions.
8. Aditionally, you can use the other provided blocks "whitelabel-price-and-benefits-listPrice", "whitelabel-price-and-benefits-sellingPrice" and "whitelabel-price-and-benefits-price" to show the prices based on price list for the seller.

#### Blocks

The blocks to include in the store theme: 

Blocks Implementation examples:

1. Provider Block Product Detail Page
```json
  "store.product": {
    "blocks": [
      "whitelabel-price-and-benefits-provider#product-detail"
    ]
  },
  "whitelabel-price-and-benefits-provider#product-detail": {
    "children": [
      "responsive-layout.desktop#product",
      "responsive-layout.tablet#product",
      "responsive-layout.phone#product"
    ]
  },
  "responsive-layout.desktop#product": {
    "title": "Ficha Producto Desktop",
    "children": [
      "whitelabel-price-and-benefits-highlight",
      "vtex.store-components:product-brand",
      "sku-selector",
      "add-to-cart-button"
      // ... others regular blocks
      "whitelabel-price-and-benefits-sellingPrice",
      "whitelabel-price-and-benefits-listPrice" 
    ]
  }, ...
```

2. Provider Block Product Summary Shelf
```json
  "product-summary.shelf": {
    "children": [
      "whitelabel-price-and-benefits-provider#product-summary"
    ]
  },
  "whitelabel-price-and-benefits-provider#product-summary": {
    "children": [      
      "whitelabel-price-and-benefits-highlight",
      "product-summary-brand",
      "product-summary-name",
      "product-summary-space",
      "product-summary-sku-selector",
      "product-summary-space",
      "whitelabel-price-and-benefits-sellingPrice",
      "whitelabel-price-and-benefits-listPrice"     
    ]
  }, ...
```

## Customization

`In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).`

| CSS Handles |
| ----------- | 
| `highlights` | 
| `highlightText` | 
| `listPrice` | 
| `listPriceAmmount` | 
| `price` |
| `priceAmmount` |
| `sellingPrice` |
| `sellingPriceAmmount` |
| `addTocart` |
| `addToCartContainer` |
| `addToCartSpinner` |


<!-- DOCS-IGNORE:start -->

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!

<!-- DOCS-IGNORE:end -->