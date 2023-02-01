---
title: "Shelf"
slug: "vtex-shelf"
hidden: false
createdAt: "2020-06-03T15:19:31.603Z"
updatedAt: "2022-02-01T21:09:11.415Z"
---

>⚠️ Aiming to display a flexible product list, the `shelf` and `shelf.relatedProducts` block is deprecated and is now configured using the [Product Summary List](https://developers.vtex.com/docs/guides/vtex-product-summary-productsummarylist), the [Product Summary Shelf](https://developers.vtex.com/docs/guides/vtex-product-summary) and the [Slider Layout](https://developers.vtex.com/docs/guides/vtex-slider-layout) blocks. To learn how to configure it, access [Building a Shelf](https://developers.vtex.com/docs/guides/vtex-io-documentation-building-a-shelf).

The Shelf app displays a list of products on your store pages, helping you build your shop window and work on your store's visual merchandising.

![shelf](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-shelf-0.png)

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
|`shelf`| ![https://img.shields.io/badge/-Deprecated-red](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-shelf-1.png) Renders in the store home page a list of products. |
| `shelf.relatedProducts` | ![https://img.shields.io/badge/-Deprecated-red](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-shelf-2.png) Renders in the product details page a list of related products. |

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
| `summary`         | `object`  | Schema declaring the desired related product shelf's items. This prop object must contain the [`product-summary.shelf` block's props](https://developers.vtex.com/docs/guides/vtex-product-summary#configuration).   | `undefined` |

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-css-handles-for-store-customization).

| CSS Handles               |
| ------------------------- |
| `relatedProducts`         |

>⚠️ Warning
>
> The CSS Handles list above refers to the `shelf.relatedProducts` block. Since the `shelf` block is deprecated, your traditional shelf customization must be done using the CSS Handles available for the [Product Summary List](https://developers.vtex.com/docs/guides/vtex-product-summary-productsummarylist), the [Product Summary Shelf](https://developers.vtex.com/docs/guides/vtex-product-summary) and the [Slider Layout](https://developers.vtex.com/docs/guides/vtex-slider-layout) blocks.
