---
title: "Change to the availableQuantity field in the search API"
slug: "2024-09-10-change-available-quantity-field-search-api"
type: "Improved"
excerpt: "VTEX changed how the `availableQuantity` field works, which is returned by the API routes of the legacy search. This change may impact existing integrations."
createdAt: "2024-09-10T11:00:00.000Z"
updatedAt: "2024-09-10T11:30:00.000Z"
---

VTEX changed how the `availableQuantity` field works, which is returned by the API routes of the legacy search. This change may impact existing integrations.

> Stores that use VTEX Intelligent Search are not affected.

## What has changed?

The `availableQuantity` field no longer represents the exact number of available items in the store inventory. The field now returns an estimate based on order of magnitude. The possible values for `availableQuantity` are:

* `0`: 0 inventory quantity.
* `1`: inventory quantity of 1.
* `10`: inventory quantity between 2 and 10.
* `100`: inventory quantity between 11 and 100.
* `99999`: inventory quantity above 100.

This change affects all routes that return this field:

* [Search for products](https://developers.vtex.com/docs/api-reference/search-api#get-/api/catalog_system/pub/products/search/-search-?endpoint=get-/api/catalog_system/pub/products/search/-search-) 
* [Search for products with Filter, Order and Pagination](https://developers.vtex.com/docs/api-reference/search-api#get-/api/catalog_system/pub/products/search?endpoint=get-/api/catalog_system/pub/products/search) 
* [Search product by product URL](https://developers.vtex.com/docs/api-reference/search-api#get-/api/catalog_system/pub/products/search/-product-text-link-/p?endpoint=get-/api/catalog_system/pub/products/search/-product-text-link-/p) 
* [Search product offers](https://developers.vtex.com/docs/api-reference/search-api#get-/api/catalog_system/pub/products/offers/-productId-?endpoint=get-/api/catalog_system/pub/products/offers/-productId-) 
* [Search SKU offers](https://developers.vtex.com/docs/api-reference/search-api#get-/api/catalog_system/pub/products/offers/-productId-/sku/-skuId-?endpoint=get-/api/catalog_system/pub/products/offers/-productId-/sku/-skuId-) 
* [Get product search of who saw also saw (deprecated)](https://developers.vtex.com/docs/api-reference/search-api#get-/api/catalog_system/pub/products/crossselling/whosawalsosaw/-productId-?endpoint=get-/api/catalog_system/pub/products/crossselling/whosawalsosaw/-productId-) 
* [Get product search of who saw also bought (deprecated)](https://developers.vtex.com/docs/api-reference/search-api#get-/api/catalog_system/pub/products/crossselling/whosawalsobought/-productId-?endpoint=get-/api/catalog_system/pub/products/crossselling/whosawalsobought/-productId-) 
* [Get product search of who bought also bought (deprecated)](https://developers.vtex.com/docs/api-reference/search-api#get-/api/catalog_system/pub/products/crossselling/whoboughtalsobought/-productId-?endpoint=get-/api/catalog_system/pub/products/crossselling/whoboughtalsobought/-productId-) 
* [Get product search of show together](https://developers.vtex.com/docs/api-reference/search-api#get-/api/catalog_system/pub/products/crossselling/showtogether/-productId-?endpoint=get-/api/catalog_system/pub/products/crossselling/showtogether/-productId-) 
* [Get product search of accessories](https://developers.vtex.com/docs/api-reference/search-api#get-/api/catalog_system/pub/products/crossselling/accessories/-productId-?endpoint=get-/api/catalog_system/pub/products/crossselling/accessories/-productId-) 
* [Get product search of similars](https://developers.vtex.com/docs/api-reference/search-api#get-/api/catalog_system/pub/products/crossselling/similars/-productId-?endpoint=get-/api/catalog_system/pub/products/crossselling/similars/-productId-) 
* [Get product search of suggestions](https://developers.vtex.com/docs/api-reference/search-api#get-/api/catalog_system/pub/products/crossselling/suggestions/-productId-?endpoint=get-/api/catalog_system/pub/products/crossselling/suggestions/-productId-)

## Why did we make this change?

Previously, it was possible to check the product quantity in a store inventory through the legacy API. However, since inventory is a sensitive piece of data and the API is public, we decided to hide it.

## What needs to be done?

If your store has any integration that returns the `availableQuantity` field in any of the routes mentioned above, check the feature to take into account the new behavior.