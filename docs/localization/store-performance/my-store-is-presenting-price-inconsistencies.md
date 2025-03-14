---
title: "My store is presenting price inconsistencies"
slug: "my-store-is-presenting-price-inconsistencies"
excerpt: "Product price is different on Search Results and Product Detail pages."
hidden: false
createdAt: "2025-01-30T14:25:00.00Z"
updatedAt: "2025-01-30T14:25:00.00Z"
tags:
    - catalog
    - search
    - pricing
---

**Keywords:** Catalog | Search | Pricing

The Search Results and Product Details pages have different indexing processes. This can lead to differences in price.

If your store is presenting inconsistencies, follow the instructions below.

## Reindex Catalog and disable Search Result cache

To correct the inconsistencies:

1. [Reindex](https://help.vtex.com/en/tutorial/i-cant-index-a-product-in-the-catalog--5ZKLTqnCyGbWEYGPTCBIxI) the products that have inconsistencies in Catalog.
2. Check the value set for the `simulationBehavior` property of the [Search Result](https://developers.vtex.com/docs/apps/vtex.search-result) app. If it's set to `skip`, change it to `default`.

>ℹ️ When the `simulationBehavior` is set to `skip`, the Search Results page displays the old price based on the user cache. To fetch and display the latest price in Catalog, change it to `default`.
