---
slug: "negative-saving-on-search-results-page"
title: "Negative saving on Search Results page"
createdAt: 2020-08-04T15:17:00.000Z
hidden: false
type: "fixed"
---

![Store Framework](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/negative-saving-on-search-results-page-0.png)

The Search Results page used to display the product list price even if it was lower than the product selling price, leading to a negative saving for users.

![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/negative-saving-on-search-results-page-1.png)

The image above shows a product (whose value previously was R$199,90) being now sold for R$ 299,90.
This behavior is now [fixed](https://github.com/vtex-apps/product-price/pull/38), meaning the product list price is only displayed if it actually helps user savings.
