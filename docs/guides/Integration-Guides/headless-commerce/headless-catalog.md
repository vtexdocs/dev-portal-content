---
title: "Headless catalog"
slug: "headless-catalog"
hidden: true
createdAt: "2021-03-31T21:16:55.757Z"
updatedAt: "2021-03-31T21:16:55.757Z"
excerpt: "Explore API endpoints for retrieving product information, categories, and search results to build headless commerce experiences with VTEX."
---

> ℹ️ The Intelligent Search sections of this guide use [Intelligent Search API v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1). If you are migrating from [Intelligent Search API (Legacy)](https://developers.vtex.com/docs/api-reference/intelligent-search-api), see [Migrating to Intelligent Search API v1](https://developers.vtex.com/docs/guides/migrating-to-intelligent-search-api-v1).

Be it through category menus, keyword searches, or product pages, shoppers accessing your headless store will need to browse through your products' information.

Below you can learn more about API endpoints you can use to help shoppers find what they need in your store. See the [catalog documentation](https://help.vtex.com/en/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/3rA2tTpIoEXdv2nzC27zxR) to learn how to manage products, SKUs and categories, among other things.

>ℹ️ You can filter the results of the endpoints below by [trade policy](https://help.vtex.com/en/tutorial/how-trade-policies-work--6Xef8PZiFm40kg2STrMkMV?&utm_source=autocomplete) with the query parameter `sc={tradePolicy}`.

## Categories

One of the ways shoppers will interact with your product information is by browsing through a categories menu.

Use the following endpoint to fetch category information:

- [Get category tree](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/category/tree/-categoryLevels-)

## Search

Instead of browsing categories, shoppers may prefer to type a keyword into your store’s search bar to find what they want. VTEX provides two different search solutions for your store. We recommend that you use [Intelligent Search](#intelligent-search), but you have the option to use the [VTEX Search (Legacy)](#vtex-search-legacy) if you wish.

>ℹ️ Learn more about [VTEX Intelligent Search](https://help.vtex.com/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/3qgT47zY08biLP3d5os3DG).

### Intelligent Search

Before implementing Intelligent Search in your headless storefront, make sure to check this [Intelligent Search guide](https://help.vtex.com/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/3qgT47zY08biLP3d5os3DG) and make the necessary configurations.

To retrieve products with the Intelligent Search API, use this endpoint:

- `GET` [Search products (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/product-search/-facets-)

For any given Intelligent Search query, you can get search facets and display them so that your shoppers can narrow their search.

- `GET` [List filters for a search (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/facets/-facets-)

Shoppers may have trouble coming up with the optimal search term for their needs. Use these endpoints to help fill in the gaps:

- `GET` [Get attempt of correction of a misspelled term (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/correction-search)
- `GET` [Get list of suggested terms similar to the search term (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/search-suggestions)

#### Banners

You can use the Intelligent Search [banners feature](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/4ViKEivLJtJsvpaW0aqIQ5) with this endpoint:

- `GET` [Get list of banners registered for query (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/banners/-facets-)

#### Intelligent Search autocomplete

You can also improve shopping experience by implementing an [autocomplete feature](https://help.vtex.com/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/4gXFsEWjF7QF7UtI2GAvhL). Use this endpoint to get suggested search terms based on a provided term:

- `GET` [Get list of suggested terms and attributes similar to the search term (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/autocomplete-suggestions)

You can also get the most searched terms on your site:

- `GET` [Get list of the 10 most searched terms (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/top-searches)

### VTEX Search (Legacy)

To retrieve products with VTEX Search (Legacy), use this endpoint:

- [Search for Products with Filter, Order and Pagination](https://developers.vtex.com/docs/api-reference/search-api#get-/api/catalog_system/pub/products/search)

Note that this endpoint provides multiple filtering and ordering options that can be made available for the shopper to narrow their search, improving the user’s experience. Handy examples include:

- Searching within specific category levels (department, category and subcategory): `https://{accountName}.vtexcommerce{environment}.com.br/api/catalog_system/pub/products/search/{department}/{category}/{subcategory}`
- Filtering products by [collection](https://help.vtex.com/en/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/4hN41yU8IPeb8HKmmaXoca): query string `fq=productClusterIds:{collectionId}`
- Sorting by best discount: query string `O=OrderByBestDiscountDESC`

>ℹ️ See the [Search endpoint documentation](https://developers.vtex.com/docs/api-reference/search-api#get-/api/catalog_system/pub/products/search) to learn about all filtering and sorting options.

#### VTEX Search (Legacy) autocomplete

You can also implement an autocomplete feature to your store’s search bar using VTEX Search (Legacy). To do this, use this endpoint:

- [Product Search Autocomplete](https://developers.vtex.com/docs/api-reference/search-api#get-/buscaautocomplete)

## Product details

On product pages and in other sections of your headless store, you will need to retrieve information about specific products.

### Recommended approach (Intelligent Search)

We recommend using the [Intelligent Search API v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1) for Product Detail Pages (PDP), as it provides:

* **Better search performance:** Optimized for faster response times.
* **Consistent user experience:** When using [Delivery Promise](https://developers.vtex.com/docs/guides/delivery-promise), using Intelligent Search ensures delivery estimates and availability match between Product Listing Pages (PLP) and Product Detail Pages (PDP).
* **Location-based availability:** Supports filtering by ZIP code for accurate product availability.

Use the `GET` [Get product (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/products) endpoint to retrieve a specific product by a known identifier. It accepts a `field` and `value` parameter and skips the search pipeline, resulting in lower latency.

| `field` value | Identifier type |
| --- | --- |
| `id` (default) | Product ID |
| `slug` | Product slug |
| `ean` | SKU EAN |
| `sku` | SKU ID |
| `reference` | SKU reference ID |

**Examples:**

```txt
https://{accountName}.vtexcommercestable.com.br/api/intelligent-search/v1/products?sc=1&field=id&value=1234
```

```txt
https://{accountName}.vtexcommercestable.com.br/api/intelligent-search/v1/products?sc=1&field=slug&value=apple-magic-mouse
```

>⚠️ **For stores using [Delivery Promise](https://developers.vtex.com/docs/guides/delivery-promise):** Include delivery promise parameters in your requests to ensure accurate delivery estimates and product availability. See the [Delivery Promise for headless stores](https://developers.vtex.com/docs/guides/delivery-promise-for-headless-stores) guide for implementation details.

### Alternative approach (VTEX Search (Legacy))

Alternatively, you can use VTEX Search (Legacy) API endpoints to retrieve product information:

- [Search Product by Product URL](https://developers.vtex.com/docs/api-reference/search-api#get-/api/catalog_system/pub/products/search/-product-text-link-/p)
- [Search for Products with Filter, Order and Pagination](https://developers.vtex.com/docs/api-reference/search-api#get-/api/catalog_system/pub/products/search)
  - Filter by product ID: `fq=productId:{productId}`
  - Filter by SKU ID: `fq=skuId:{skuId}`

>⚠️ VTEX Search (Legacy) endpoints do not support Delivery Promise features. If your store uses [Delivery Promise](https://developers.vtex.com/docs/guides/delivery-promise), you must use the Intelligent Search API v1 as described above.

### Cross selling

When a shopper is interested in a product, it may be a good idea to display related products that they may be interested in purchasing as well.

See this guide  to learn [how to set up cross selling](https://help.vtex.com/en/tutorial/configurando-produto-similar-sugestoes-acessorios-e-genericos--tutorials_280) capabilities and use the endpoints below to retrieve this information on your storefront:

- [Get Product Search of Show Together](https://developers.vtex.com/docs/api-reference/search-api#get-/api/catalog_system/pub/products/crossselling/showtogether/-productId-)
- [Get Product Search of Accessories](https://developers.vtex.com/docs/api-reference/search-api#get-/api/catalog_system/pub/products/crossselling/accessories/-productId-)
- [Get Product Search of Similars](https://developers.vtex.com/docs/api-reference/search-api#get-/api/catalog_system/pub/products/crossselling/similars/-productId-)
- [Get Product Search of Suggestions](https://developers.vtex.com/docs/api-reference/search-api#get-/api/catalog_system/pub/products/crossselling/suggestions/-productId-)

## Learn more

See these other guides to learn more about building a headless shopping experience using VTEX:

- [Headless commerce overview](https://developers.vtex.com/docs/guides/headless-commerce)
- [Headless cart and checkout](https://developers.vtex.com/docs/guides/headless-cart-and-checkout)
- [Headless profile management and order history](https://developers.vtex.com/docs/guides/headless-profile-management-and-order-history)
