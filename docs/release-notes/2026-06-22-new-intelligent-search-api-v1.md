---
title: "New Intelligent Search API v1"
slug: "2026-06-22-new-intelligent-search-api-v1"
excerpt: "The new Intelligent Search API v1 is now available for headless integrations. It adds HTTP caching, lower latency, explicit regionalization, and a new endpoint for product detail pages."
hidden: false
createdAt: "2026-06-22T00:00:00.000Z"
updatedAt: "2026-06-22T00:00:00.000Z"
type: "added"
tags:
    - Search
---

The new [Intelligent Search API (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1) is now available for headless integrations at `/api/intelligent-search/v1/*`. It replaces [Intelligent Search API (Legacy)](https://developers.vtex.com/docs/api-reference/intelligent-search-api) at `/api/io/_v/api/intelligent-search/*` with HTTP caching, lower latency, and explicit context parameters.

## What has changed?

### HTTP caching

Responses from most endpoints are now returned with `Cache-Control: public, max-age=600`, enabling CDN and browser caching for public sales channels. This reduces origin load and improves storefront response times.

Exceptions:

- Responses containing sponsored products: `Cache-Control: no-store`.
- Private sales channel responses: not cached.

### Explicit context: No segment cookie

Intelligent Search API (Legacy) relied on the VTEX segment cookie to fill in locale, sales channel, regionalization, and marketing context. Intelligent Search API v1 does not read the segment cookie. All context must be passed explicitly as query parameters or facets in the URL path.

| Context | Intelligent Search API (Legacy) | Intelligent Search API v1 |
| --- | --- | --- |
| Locale | Read from segment cookie | `locale` query parameter |
| Sales channel | Read from segment cookie | `trade-policy/{id}` facet or `sc` query parameter |
| Region | Read from segment cookie | `regionId`, `country`, `zip-code`, `coordinates` query parameters |
| UTM / price tables | Read from segment cookie | `utmSource`, `utmCampaign`, `utmiCampaign`, `campaigns`, `priceTables` query parameters |

### New URL structure

The IO prefix and underscores in path names have been removed, and `/v1` has been added to the path.

| Intelligent Search API (Legacy) | Intelligent Search API v1 |
| --- | --- |
| `GET /api/io/_v/api/intelligent-search/top_searches`<br />[Get list of the 10 most searched terms](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/top_searches) | `GET /api/intelligent-search/v1/top-searches`<br />[Get list of the 10 most searched terms (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/top-searches) |
| `GET /api/io/_v/api/intelligent-search/autocomplete_suggestions`<br />[Get list of suggested terms and attributes similar to the search term](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/autocomplete_suggestions) | `GET /api/intelligent-search/v1/autocomplete-suggestions`<br />[Get list of suggested terms and attributes similar to the search term (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/autocomplete-suggestions) |
| `GET /api/io/_v/api/intelligent-search/search_suggestions`<br />[Get list of suggested terms similar to the search term](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/search_suggestions) | `GET /api/intelligent-search/v1/search-suggestions`<br />[Get list of suggested terms similar to the search term (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/search-suggestions) |
| `GET /api/io/_v/api/intelligent-search/correction_search`<br />[Get attempt of correction of a misspelled term](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/correction_search) | `GET /api/intelligent-search/v1/correction-search`<br />[Get attempt of correction of a misspelled term (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/correction-search) |
| `GET /api/io/_v/api/intelligent-search/banners/{facets}`<br />[Get list of banners registered for query](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/banners/-facets-) | `GET /api/intelligent-search/v1/banners/{facets}`<br />[Get list of banners registered for query (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/banners/-facets-) |
| `GET /api/io/_v/api/intelligent-search/product_search/{facets}`<br />[Get list of products for a query](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/product_search/-facets-) | `GET /api/intelligent-search/v1/product-search/{facets}`<br />[Search products (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/product-search/-facets-) |
| `GET /api/io/_v/api/intelligent-search/facets/{facets}`<br />[Get list of the possible facets for a given query](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/facets/-facets-) | `GET /api/intelligent-search/v1/facets/{facets}`<br />[List filters for a search (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/facets/-facets-) |
| `GET /api/io/_v/api/intelligent-search/pickup-point-availability/{facets}`<br />[Get pickup point availability for Delivery Promise](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/pickup-point-availability/-facets-) | `GET /api/intelligent-search/v1/pickup-point-availability/{facets}`<br />[Get pickup point availability for Delivery Promise (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/pickup-point-availability/-facets-) |
| N/A | `GET /api/intelligent-search/v1/products`<br />[Get product (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/products) |

### New endpoint: Get product

A new `GET` [Get product](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/products) endpoint is now available for product detail pages (PDP). Given a known identifier (product ID, slug, EAN, SKU ID, or reference), it returns a single product without going through the search pipeline, resulting in lower latency and better cache-hit rates than `GET` [Search products](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/product-search/-facets-).

### Updated parameters on product search and facets

Intelligent Search API v1 adds explicit regionalization parameters to `GET` [Search products](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/product-search/-facets-) and `GET` [List filters for a search](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/facets/-facets-):

- `regionId`
- `country`
- `zip-code`
- `coordinates`
- `pickupPoint`
- `deliveryZonesHash`
- `pickupPointsHash`

### Updated `simulationBehavior` enum

The `simulationBehavior` parameter now accepts two additional values:

| Value | Description |
| --- | --- |
| `only3P` | Calls simulation for third-party sellers only. |
| `regionalize1p` | Calls regionalized simulation for first-party sellers only. |

### Updated parameters and response fields

Several endpoints expose new parameters and response fields compared to Intelligent Search API (Legacy).

| Endpoint | What's new |
| --- | --- |
| `GET` [Get list of the 10 most searched terms (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/top-searches) | New `query` parameter: filters results to terms containing the given text (case-insensitive). |
| `GET` [Get list of suggested terms similar to the search term (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/search-suggestions) | Response: each suggestion now includes an optional `attributes` array with facet attributes, using the same shape as `GET` [Get list of suggested terms and attributes similar to the search term (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/autocomplete-suggestions). |
| `GET` [List filters for a search (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/facets/-facets-) | New `removeHiddenFacets` parameter: omits hidden facets from the response when set to `true`.<br />Response: `facets[].type` now includes `DELIVERY` in addition to `TEXT` and `PRICERANGE`. |
| `GET` [Search products (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/product-search/-facets-) | Response: new `searchId` (analytics identifier), `correction` (spelling correction), `redirect` (redirect rule URL), and `options` (sort options and delivery promise data) fields. |
| `GET` [Get pickup point availability for Delivery Promise (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/pickup-point-availability/-facets-) | New `locale` parameter for localized results and `pickupPoint` parameter to filter by a specific pickup point ID. |

### Resolved: Incomplete product item data on product search

A [known issue](https://help.vtex.com/known-issues/unsupported-fields-by-the-intelligent-search-api-returning-empty) affecting `products[].items[]` fields in the legacy API has been resolved in Intelligent Search API v1. Some fields previously returned incorrect or empty values, including `isKit`, `modalType`, and `images[].imageText`. In addition, the attachment schema has been updated and new fields such as `estimatedDateArrival`, `kitItems`, and `PaymentOptions` are now returned.

## What needs to be done?

For a step-by-step migration checklist, see [Migrating to Intelligent Search API (v1)](https://developers.vtex.com/docs/guides/migrating-to-intelligent-search-api-v1).

All new headless integrations must use [Intelligent Search API (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1). [Intelligent Search API (Legacy)](https://developers.vtex.com/docs/api-reference/intelligent-search-api) remains available for existing integrations, but its endpoints will be deprecated in a future announcement. We recommend migrating existing integrations as soon as possible.

## Related resources

- [Intelligent Search API (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1)
- [Intelligent Search API (Legacy)](https://developers.vtex.com/docs/api-reference/intelligent-search-api)
- [Migrating to Intelligent Search API (v1)](https://developers.vtex.com/docs/guides/migrating-to-intelligent-search-api-v1)
