---
title: "Headless catalog"
slug: "headless-catalog"
hidden: true
createdAt: "2021-03-31T21:16:55.757Z"
updatedAt: "2021-03-31T21:16:55.757Z"
---

Be it through category menus, keyword searches, or product pages, shoppers accessing your headless store will need to browse through your products' information.

Below you can learn more about API endpoints you can use to help shoppers find what they need in your store. See the [catalog documentation](https://help.vtex.com/en/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/3rA2tTpIoEXdv2nzC27zxR) to learn how to manage products, SKUs and categories, among other things.

>ℹ️ You can filter the results of the endpoints below by [trade policy](https://help.vtex.com/en/tutorial/how-trade-policies-work--6Xef8PZiFm40kg2STrMkMV?&utm_source=autocomplete) with the query parameter `sc={tradePolicy}`.

## Categories

One of the ways shoppers will interact with your product information is by browsing through a categories menu.

Use the following endpoint to fetch category information:

- [Get category tree](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/category/tree/-categoryLevels-)

## Search

Instead of browsing categories, shoppers may prefer to type a keyword into your store’s search bar to find what they want. VTEX provides two different search solutions for your store. We recommend that you use [Intelligent Search](#intelligent-search), but you have the option to use the [Legacy CMS Portal search](#legacy-search) if you wish.

>ℹ️ Learn more about [VTEX Intelligent Search](https://help.vtex.com/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/3qgT47zY08biLP3d5os3DG).

### Intelligent Search

Before implementing Intelligent Search in your headless storefront, make sure to check this [Intelligent Search guide](https://help.vtex.com/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/3qgT47zY08biLP3d5os3DG) and make the necessary configurations.

To retrieve products with the Intelligent Search API, use this endpoint:

- [Get list of products for a query](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/product_search/-facets-)

For any given Intelligent Search query, you can get search facets and display them so that your shoppers can narrow their search.

- [Get list of the possible facets for a given query](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/facets/-facets-)

Shoppers may have trouble coming up with the optimal search term for their needs. Use these endpoints to help fill in the gaps:

- [Get attempt of correction of a misspelled term](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/correction_search)
- [Get list of suggested terms similar to the search term](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/search_suggestions)

#### Banners

You can use the Intelligent Search [banners feature](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/4ViKEivLJtJsvpaW0aqIQ5) with this endpoint:

- [Get list of banners registered for query](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/banners/-facets-)

#### Intelligent Search autocomplete

You can also improve shopping experience by implementing an [autocomplete feature](https://help.vtex.com/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/4gXFsEWjF7QF7UtI2GAvhL). Use this endpoint to get suggested search terms based on a provided term:

- [Get list of suggested terms and attributes similar to the search term](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/autocomplete_suggestions)

You can also get the most searched terms on your site:

- [Get list of the 10 most searched terms](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/top_searches)

### Legacy Search

To retrieve products with the Legacy Search, use this endpoint:

- [Search for Products with Filter, Order and Pagination](https://developers.vtex.com/docs/api-reference/search-api#get-/api/catalog_system/pub/products/search)

Note that this endpoint provides multiple filtering and ordering options that can be made available for the shopper to narrow their search, improving the user’s experience. Handy examples include:

- Searching within specific category levels (department, category and subcategory): `https://{accountName}.vtexcommerce{environment}.com.br/api/catalog_system/pub/products/search/{department}/{category}/{subcategory}`
- Filtering products by [collection](https://help.vtex.com/en/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/4hN41yU8IPeb8HKmmaXoca): query string `fq=productClusterIds:{collectionId}`
- Sorting by best discount: query string `O=OrderByBestDiscountDESC`

>ℹ️ See the [Search endpoint documentation](https://developers.vtex.com/docs/api-reference/search-api#get-/api/catalog_system/pub/products/search) to learn about all filtering and sorting options.

#### Legacy Search autocomplete

You can also implement an autocomplete feature to your store’s search bar using Legacu Search. To do this, use this endpoint:

- [Product Search Autocomplete](https://developers.vtex.com/docs/api-reference/search-api#get-/buscaautocomplete)

## Product details

On product pages and maybe other sections of your headless store, you will need to get information on specific products. To do this, you can use one of these endpoints:

- [Search Product by Product URL](https://developers.vtex.com/docs/api-reference/search-api#get-/api/catalog_system/pub/products/search/-product-text-link-/p)
- [Search for Products with Filter, Order and Pagination](https://developers.vtex.com/docs/api-reference/search-api#get-/api/catalog_system/pub/products/search)
  - Filter by product ID: `fq=productId:{productId}`
  - Filter by SKU ID: `fq=skuId:{skuId}`

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
