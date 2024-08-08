---
title: The Price in the shelf or in the search results is different from the product page
slug: the-price-in-the-shelf-or-in-the-search-results-is-different-from-the-product-page
hidden: false
createdAt: 2024-06-04T11:15:35.508Z
updatedAt: 2024-06-04T11:15:35.508Z
excerpt: Inconsistent pricing when comparing shelves or search results with product pages in stores using Intelligent Search.
tags:
  - intelligent-search
  - store-framework
  - pricing
  - promotions
---

**Keywords:** Price | PDP | Product | SKU | Shelf | Search | Search Result | Promotion

When [updating a SKU price](https://help.vtex.com/en/tutorial/alteracao-de-preco-de-sku--tutorials_95) or applying a [promotion](https://help.vtex.com/en/tracks/promotion--6asfF1vFYiZgTQtOzwJchR), the price on the shelf or in the search results might differ from the price on the product page. This issue can happen in [Store Framework](https://developers.vtex.com/docs/guides/store-framework) stores using the [Search Result](https://developers.vtex.com/docs/apps/vtex.search-result) component in the [store theme](https://developers.vtex.com/docs/guides/vtex-io-documentation-3-settingyourstoretheme). This component receives and renders search results from [Intelligent Search](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb).

The Search Result component's configuration, specifically setting the `simulationBehavior` property to `skip`, can cause outdated prices to display in shelves and search results. This occurs because this configuration makes the component rely on cached data rather than fetching the latest price updates.

> ⚠️ The `skip` setting is only recommended for stores where prices are not updated frequently and promotions are not used often. In these cases, this configuration can increase loading speed by displaying cached information. Learn more in [Displaying asynchronous prices](https://developers.vtex.com/docs/guides/vtex-io-documentation-displaying-asynchronous-prices).

## Solution

To ensure consistent and up-to-date pricing across your store, follow the instructions below:

1. Locate the theme files that define the [Search Result](https://developers.vtex.com/docs/apps/vtex.search-result) component.

2. Locate the `simulationBehavior` property in your theme’s code, as in the example below. You can also find an example in the [store theme boilerplate](https://github.com/vtex-apps/store-theme/blob/main/store/blocks/search.jsonc) repository.

   ```json
   "store.search": {
       "blocks": [
           "search-result-layout"
       ],
       "props": {
           "context": {
               "simulationBehavior": "skip"
           }
       }
   }
   ```

3. Change the value of `simulationBehavior` from `skip` to `default`, as in the example below. This adjustment instructs the component always to fetch the latest data, eliminating the discrepancy caused by cached information.

   ```json
   "store.search": {
       "blocks": [
           "search-result-layout"
       ],
       "props": {
           "context": {
               "simulationBehavior": "default"
           }
       }
   }
   ```

4. Run `vtex link` to see your changes reflected in the workspace.

Make sure this change is applied consistently across all instances of the Search Result component used throughout your store's theme.
