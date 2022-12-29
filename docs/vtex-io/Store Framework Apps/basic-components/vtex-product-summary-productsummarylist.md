---
title: "ProductSummaryList"
slug: "vtex-product-summary-productsummarylist"
excerpt: "vtex.product-summary@2.80.1-perftest.1"
hidden: false
createdAt: "2020-06-09T14:48:52.857Z"
updatedAt: "2022-07-02T00:50:32.864Z"
---
The  Product Summary List app (`list-context.product-list`) is an instance of the `list-context` interface - a set of special interfaces used to create lists of content, such as a list of products.

![list-context-example](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-product-summary-productsummarylist-0.png)

To create a list of products, you must use the `list-context.product-list` and `product-summary.shelf` blocks.

## product-list-block

This block is used to specify what variation of `product-summary` to be used to create the list of products, and the `list-context.product-list` you want as follows:

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
  "list-context.product-list#demo1": {
    "blocks": ["product-summary.shelf#demo1"],
    "children": ["slider-layout#demo-products"]
  },
```

`list-context.product-list` is also responsible for performing the GraphQL query that fetches the list of products, so it can receive the following props:

| Prop name              | Type                                   | Description                                                                                                                                                                                                | Default value            |
| ---------------------- | -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| `category`             | `String`                               | Category ID of the listed items. For sub-categories, use "/" (e.g. "1/2/3")                                                                                                                                | -                        |
| `specificationFilters` | `Array({ id: String, value: String })` | Specification Filters of the listed items.                                                                                                                                                                 | []                       |
| `collection`           | `String`                               | Filter by collection.                                                                                                                                                                                      | -                        |
| `orderBy`              | `Enum`                                 | Ordination type of the items. Possible values: `''`, `OrderByTopSaleDESC`, `OrderByReleaseDateDESC`, `OrderByBestDiscountDESC`, `OrderByPriceDESC`, `OrderByPriceASC`, `OrderByNameASC`, `OrderByNameDESC` | `OrderByTopSaleDESC`     |
| `hideUnavailableItems` | `Boolean`                              | Hides items that are unavailable.                                                                                                                                                                          | `false`                  |
| `maxItems`             | `Number`                               | Maximum items to be fetched.                                                                                                                                                                               | `10`                     |
| `skusFilter`           | `SkusFilterEnum`                       | Control SKUs returned for each product in the query. The less SKUs needed to be returned, the more performant your shelf query will be.                                                                    | `"ALL_AVAILABLE"`        |
| `installmentCriteria`  | `InstallmentCriteriaEnum`              | Control what price to be shown when price has different installments options.                                                                                                                              | `"MAX_WITHOUT_INTEREST"` |
| `listName`             | `String`                               | Name of the list property on Google Analytics events.                                                                                                                                                      | ``                       |
| `preferredSKU`         | `PreferredSKUEnum`                     | Controls which SKU will be selected in the summary                                                                                                                                                         | `"FIRST_AVAILABLE"`      |

For `SkusFilterEnum`:

| Name            | Value             | Description                                                                                                                                            |
| --------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| First Available | `FIRST_AVAILABLE` | Most performant, ideal if you do not have a SKU selector in your shelf. Will return only the first available SKU for that product in your shelf query. |
| All Available   | `ALL_AVAILABLE`   | A bit better performace, will only return SKUs that are available, ideal if you have a SKU selector but still want a better performance.               |
| All             | `ALL`             | Returns all SKUs related to that product, least performant option.                                                                                     |

For `InstallmentCriteriaEnum`:

| Name                     | Value                  | Description                                                         |
| ------------------------ | ---------------------- | ------------------------------------------------------------------- |
| Maximum without interest | `MAX_WITHOUT_INTEREST` | Will display the maximum installment option with no interest.       |
| Maximum                  | `MAX_WITH_INTEREST`    | Will display the maximum installment option having interest or not. |

For `PreferredSKUEnum`:

| Name            | Value             | Description                                        |
| --------------- | ----------------- | -------------------------------------------------- |
| First Available | `FIRST_AVAILABLE` | Selects the first available SKU in stock it finds. |
| Last Available  | `LAST_AVAILABLE`  | Selects the last available SKU in stock it finds.  |
| Cheapest        | `PRICE_ASC`       | Selects the cheapest SKU in stock it finds.        |
| Most Expensive  | `PRICE_DESC`      | Selects the most expensive SKU in stock it finds.  |

> ⚠️ 
>
> To select which SKU will take preference over this prop, create a Product (field) specification and assign the value of the desired SKU to be initially set for each product. If the specification doesn't exist or the value is empty, the `preferredSKU` prop will be used as a fallback. For more information, please refer to [this guide](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-configuring-custom-images-for-the-sku-selector).