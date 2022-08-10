---
title: "RelatedProductSummaryList"
slug: "chocolatdujour-product-summary-productsummaryrelatedproductlist"
excerpt: "chocolatdujour.product-summary@2.80.0"
hidden: true
createdAt: "2022-07-04T22:48:46.452Z"
updatedAt: "2022-07-04T22:48:46.452Z"
---
The `list-context.related-product-list` interface is a instance of the `list-context` interfaces, which means its part of a set of special interfaces that enables you to create lists of content that can be edited via Site Editor.

In order to create a list of products, you need to use the `list-context.related-product-list` block and a `product-summary.shelf`.

## related-product-list-block

This block is used to specify what variation of `product-summary` to be used to create the list of products, and the `list-context.related-product-list` you want as follows:

```json
  "product-summary.shelf#demo1": {
    "children": [
      "stack-layout#prodsum",
      "product-summary-name",
      "product-rating-inline",
      "product-summary-space",
      "product-summary-price",
      "product-summary-buy-button"
    ]
  },
  "list-context.related-product-list#demo1": {
    "blocks": ["product-summary.shelf#demo1"],
    "children": ["slider-layout#demo-products"]
  },
```

`list-context.product-list` is also responsible for performing the GraphQL query that fetches the list of products, so it can receive the following props:

| Prop name             | Type               | Description                                           | Default value       |
| --------------------- | ------------------ | ----------------------------------------------------- | ------------------- |
| `hideOutOfStockItems` | `Boolean`          | Hides items that are unavailable.                     | `false`             |
| `listName`            | `String`           | Name of the list property on Google Analytics events. | ``                  |
| `maxItems`            | `Number`           | Max items to be showed.                               | `10`                |
| `preferredSKU`        | `PreferredSKUEnum` | Controls which SKU will be selected in the summary    | `"FIRST_AVAILABLE"` |

For `SkusFilterEnum`:

| Name            | Value             | Description                                                                                                                                            |
| --------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| First Available | `FIRST_AVAILABLE` | Most performant, ideal if you do not have a SKU selector in your shelf. Will return only the first available SKU for that product in your shelf query. |
| All Available   | `ALL_AVAILABLE`   | A bit better performace, will only return SKUs that are available, ideal if you have a SKU selector but still want a better performance.               |
| All             | `ALL`             | Returns all SKUs related to that product, least performant option.                                                                                     |

For `PreferredSKUEnum`:

| Name            | Value             | Description                                        |
| --------------- | ----------------- | -------------------------------------------------- |
| First Available | `FIRST_AVAILABLE` | Selects the first available SKU in stock it finds. |
| Last Available  | `LAST_AVAILABLE`  | Selects the last available SKU in stock it finds.  |
| Cheapest        | `PRICE_ASC`       | Selects the cheapest SKU in stock it finds.        |
| Most Expensive  | `PRICE_DESC`      | Selects the most expensive SKU in stock it finds.  |

⚠️ There's a way to select which SKU should take preference over this prop. You can create a Product (field) specification and per product assign the value of the desired SKU to be initially selected. Keep in mind that If the specification doesn't exist or if the value is empty, it will use the `preferredSKU` prop as fallback. You can read more about it, and how to implement it in [Recipes](https://vtex.io/docs/recipes/all)