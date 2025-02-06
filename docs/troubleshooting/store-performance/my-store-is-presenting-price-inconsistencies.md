---
title: "My store is presenting price inconsistencies"
slug: "my-store-is-presenting-price-inconsistencies"
excerpt: "Product price is different on Search Results and Product Detail pages."
hidden: false
createdAt: "2025-01-30T14:25:00.00Z"
updatedAt: "2025-01-30T14:25:00.00Z"
tags:
    - inconsistencies
---

**Keywords:** Inconsistencies | Store | Pricing

The Search Results and Product Details pages have different indexing processes. This can lead to differences in the price.

If your store is presenting inconsistencies, follow the instructions below.

## Reindex Catalog and disable Search Result cache

To correct the inconsistencies, You can manually trigger the in

1. [Reindex](https://help.vtex.com/en/tutorial/i-cant-index-a-product-in-the-catalog--5ZKLTqnCyGbWEYGPTCBIxI) the products in Catalog presenting inconsistencies.
2. Check the value set for the [Search Result](https://developers.vtex.com/docs/apps/vtex.search-result) app's `simulationBehavior` property. If set to `skip`, change it to `default`.

>ℹ️ When the `simulationBehavior` is set to `skip`, the Search Results page displays the cold price based on the user cache. In order to fetch and display the latest price registered in the Catalog, change it to `default`.
