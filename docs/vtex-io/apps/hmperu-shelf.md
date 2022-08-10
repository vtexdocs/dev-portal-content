---
title: "Shelf"
slug: "hmperu-shelf"
excerpt: "hmperu.shelf@1.47.3"
hidden: true
createdAt: "2022-07-14T20:40:39.577Z"
updatedAt: "2022-07-18T18:09:45.957Z"
---
>⚠️ Warning
>
> Aiming to display a flexible product list, the `shelf` and `shelf.relatedProducts` block is deprecated and is now configured using the [Product Summary List](https://developers.vtex.com/vtex-developer-docs/docs/vtex-product-summary-productsummarylist), the [Product Summary Shelf](https://developers.vtex.com/vtex-developer-docs/docs/vtex-product-summary) and the [Slider Layout](https://developers.vtex.com/vtex-developer-docs/docs/vtex-slider-layout) blocks. To learn how to configure it, access [Building a Shelf](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-building-a-shelf).


The Shelf app displays a list of products on your store pages, helping you build your shop window and work on your store's visual merchandising.

![shelf](https://user-images.githubusercontent.com/52087100/70079904-60dc5280-15e4-11ea-8ef6-0aa69cadd61d.png)

## Configuration

1. Add the `shelf` app to your theme's dependencies in the `manifest.json` file:

```json
  "dependencies": {
    "vtex.shelf": "1.x",
  }
```

Now, you can use all the blocks exported by the `shelf` app. Check out the complete list below:

| Block name          |  Description |
| --------------------| -------- |
|`shelf`| ![https://img.shields.io/badge/-Deprecated-red](https://img.shields.io/badge/-Deprecated-red) Renders in the store home page a list of products. | 
| `shelf.relatedProducts` | ![https://img.shields.io/badge/-Deprecated-red](https://img.shields.io/badge/-Deprecated-red) Renders in the product details page a list of related products. |


2. Declare the `shelf.relatedProduct` in the product template (`store.product`) using its props. For example:

```json
{
  "store.product": {
    "children": [
      "breadcrumb",
      "flex-layout.row#main",
      "shelf.relatedProducts"
    ]
  }
}
```

| Prop name        | Type                | Description                                                                                                                                            | Default value                     |
| ---------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------- |
| `recommendation` | `Enum`              | Type of recommendations that will be displayed in the Shelf. Possible values: `similars`, `suggestions`, `accessories` (these first three depend on the product's data given in the admin's catalog) and `view`, `buy`, `viewandBought` (These 3 are automatically generated according to the store’s activity) | `similars` |
| `hideOutOfStockItems` | `Boolean` | Whether out of stock items should be hidden (`true`) or not (`false`) | `false` |
| `productList`    | `ProductListSchema` | Product list schema. See `ProductListSchema`                                                                                                           | -                                 |

`ProductListSchema`:

| Prop name         | Type      | Description  | Default value |
| ----------------- | --------- | --------------------------------------------------------- | ------------- |
| `maxItems`        | `number`  | Maximum number of items to be displayed on the related product shelf.  | `10`   |
| `scroll`          | `enum`    | Slide transition scroll type. Possible values are: `BY_PAGE` or `ONE_BY_ONE`.  | `BY_PAGE`     |
| `arrows`          | `boolean` | Whether the arrows should be displayed on the shelf (`true`) or not (`false`).    | `true`  | 
| `showTitle`       | `boolean` | Whether a title should be displayed in the product related shelf (`true`) or not (`false`). | `true`        |
| `titleText`       | `string`  | Related product shelf title.  | `null`        |
| `gap`             | `enum`    | Gap between items being displayed. Possible values are: `ph0`, `ph3`,`ph5`, or `ph7`.   | `ph3`         |
| `minItemsPerPage` | `number`  | Minimum number of items per shelf slides. This prop can be used to control how many items will be displayed on the related product shelf even in the smallest screen size. Its value can be a float,  which means that you can choose a multiple of `0.5` to indicate that you want to show a *peek* of the next slide on the shelf. | `1`   |
| `itemsPerPage`    | `number`  | Maximum number of items per shelf slides. This prop can be used to control how many items will be displayed on the related product shelf even in the biggest screen size. Its value can be a float, which means that you can choose a multiple of `0.5` to indicate that you want to show a *peek* of the next slide on the Shelf.   | `5`   |
| `summary`         | `object`  | Schema declaring the desired related product shelf's items. This prop object must contain the [`product-summary.shelf` block's props](https://developers.vtex.com/vtex-developer-docs/docs/vtex-product-summary#configuration).   | `undefined` | 

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-css-handles-for-store-customization).

| CSS Handles               |
| ------------------------- |
| `relatedProducts`         |

>⚠️ Warning 
>
> The CSS Handles list above refers to the `shelf.relatedProducts` block. Since the `shelf` block is deprecated, your traditional shelf customization must be done using the CSS Handles available for the [Product Summary List](https://developers.vtex.com/vtex-developer-docs/docs/vtex-product-summary-productsummarylist), the [Product Summary Shelf](https://developers.vtex.com/vtex-developer-docs/docs/vtex-product-summary) and the [Slider Layout](https://developers.vtex.com/vtex-developer-docs/docs/vtex-slider-layout) blocks. 


## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/sahanljc"><img src="https://avatars2.githubusercontent.com/u/42151054?v=4" width="100px;" alt=""/><br /><sub><b>Sahan Jayawardana</b></sub></a><br /><a href="https://github.com/vtex-apps/shelf/commits?author=sahanljc" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/lucaspacheco-acct"><img src="https://avatars0.githubusercontent.com/u/59736416?v=4" width="100px;" alt=""/><br /><sub><b>Lucas Pacheco</b></sub></a><br /><a href="https://github.com/vtex-apps/shelf/commits?author=lucaspacheco-acct" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!