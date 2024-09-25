---
title: "Displaying asynchronous prices"
slug: "vtex-io-documentation-displaying-asynchronous-prices"
hidden: false
createdAt: "2020-11-23T13:33:26.379Z"
updatedAt: "2022-12-13T20:17:45.051Z"
---

When aiming to improve user experience, displaying the most up-to-date product prices is essential. However, fetching the latest prices from your store’s database for every product rendered on the page can significantly increase response time.

A more efficient solution is to fetch product prices asynchronously on the client side. This approach reduces page load times while still ensuring that users see accurate prices.

> ℹ️ Asynchronous prices do not mean outdated. They are product prices stored in the browser cache according to the user navigation. If your store does not routinely update product prices, it is strongly recommended to display asynchronous prices instead.

![priceasync](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-displaying-asynchronous-prices-0.gif)

Follow the steps below to configure asynchronous prices and improve your store's performance.

## Instructions

1. Set the `simulationBehavior` prop (from the [Search Result](https://developers.vtex.com/docs/guides/vtex-search-result/) app) to `skip` to ensure that your store is not fetching the price data on the server side:
    
    ```diff
    "store.search": {
      "blocks": [
        "search-result-layout"
      ],
      "props": {
        "context": {
    +     "simulationBehavior": "skip"
        }
      }
    },
    ```

2. Add the [Product Summary](https://developers.vtex.com/docs/guides/vtex-product-summary/) and the [Product Price](https://developers.vtex.com/docs/guides/vtex-product-price/) apps as dependencies in your theme's `manifest.json` file:
    
    ```json manifest.json
    "dependencies": {
      "vtex.product-summary": "2.x",
      "vtex.product-price": "1.x"
    }  
    ```

3. Add the `priceBehavior` prop to the [`product-summary.shelf`](https://developers.vtex.com/docs/guides/vtex-product-summary-productsummaryshelf) block and set its value to `async`:
    
    ```diff
    "product-summary.shelf": {
      "props": {
    +   "priceBehavior": "async"
      },
      "children": [
        // other children
        "product-list-price#summary",
        "flex-layout.row#selling-price-savings",
        "product-installments#summary",
        "add-to-cart-button",
      ]
    }
    ```

4. Wrap the all price blocks under the `product-price-suspense` block (from the [Product Prices app](https://developers.vtex.com/docs/guides/vtex-product-price/)):

    ```diff
    {
      "product-summary.shelf": {
        "props": {
         "priceBehavior": "async"
        },
        "children": [
          // other children
    -     "product-list-price#summary",
    -     "flex-layout.row#selling-price-savings",
    -     "product-installments#summary",
    -     "add-to-cart-button",
    +     "product-price-suspense"
       ]
      },
    + "product-price-suspense": {
    +   "children": [
    +     "product-list-price#summary",
    +     "flex-layout.row#selling-price-savings",
    +     "product-installments#summary",
    +     "add-to-cart-button"
    +   ]
    + }
    }
    ```
