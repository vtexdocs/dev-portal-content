---
title: "New Intelligent Search API v1"
slug: "2026-06-22-new-intelligent-search-api-v1"
excerpt: "The new Intelligent Search API v1 is now available for headless integrations. It adds HTTP caching, lower latency, explicit regionalization, and a new endpoint for product detail pages."
hidden: false
createdAt: "2026-06-22T00:00:00.000Z"
type: "added"
tags:
    - Search
---

The new [Intelligent Search API v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1) is now available for headless integrations. It replaces [Intelligent Search API (Legacy)](https://developers.vtex.com/docs/api-reference/intelligent-search-api) at `/api/io/_v/api/intelligent-search/*` with a cleaner URL structure and significant performance improvements.

## What has changed?

### HTTP caching

Responses from most endpoints are now returned with `Cache-Control: public, max-age=600`, enabling CDN and browser caching for public sales channels. This reduces origin load and improves storefront response times.

Exceptions:

- Responses containing sponsored products: `Cache-Control: no-store`.
- Private sales channel responses: not cached.

### Explicit context — no segment cookie

Intelligent Search API (Legacy) relied on the VTEX segment cookie to fill in locale, sales channel, regionalization, and marketing context. Intelligent Search API v1 does not read the segment cookie. All context must be passed explicitly as query parameters or facets in the URL path.

| Context | Intelligent Search API (Legacy) | Intelligent Search API v1 |
| --- | --- | --- |
| Locale | Read from segment cookie | `locale` query parameter |
| Sales channel | Read from segment cookie | `trade-policy/{id}` facet or `sc` query parameter |
| Region | Read from segment cookie | `regionId`, `country`, `zip-code`, `coordinates` query parameters |
| UTM / price tables | Read from segment cookie | `utmSource`, `utmCampaign`, `utmiCampaign`, `campaigns`, `priceTables` query parameters |

### New URL structure

The IO prefix and underscores in path names have been removed.

| Intelligent Search API (Legacy) | Intelligent Search API v1 |
| --- | --- |
| `GET /top_searches`<br>[Get list of the 10 most searched terms](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/top_searches) | `GET /top-searches`<br>[Get list of the 10 most searched terms](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/top-searches) |
| `GET /autocomplete_suggestions`<br>[Get list of suggested terms and attributes similar to the search term](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/autocomplete_suggestions) | `GET /autocomplete-suggestions`<br>[Get list of suggested terms and attributes similar to the search term](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/autocomplete-suggestions) |
| `GET /search_suggestions`<br>[Get list of suggested terms similar to the search term](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/search_suggestions) | `GET /search-suggestions`<br>[Get list of suggested terms similar to the search term](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/search-suggestions) |
| `GET /correction_search`<br>[Get attempt of correction of a misspelled term](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/correction_search) | `GET /correction-search`<br>[Get attempt of correction of a misspelled term](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/correction-search) |
| `GET /banners/{facets}`<br>[Get list of banners registered for query](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/banners/-facets-) | `GET /banners/{facets}`<br>[Get list of banners registered for query](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/banners/-facets-) |
| `GET /product_search/{facets}`<br>[Get list of products for a query](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/product_search/-facets-) | `GET /product-search/{facets}`<br>[Search products](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/product-search/-facets-) |
| `GET /facets/{facets}`<br>[Get list of the possible facets for a given query](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/facets/-facets-) | `GET /facets/{facets}`<br>[List filters for a search](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/facets/-facets-) |
| `GET /pickup-point-availability/{facets}`<br>[Get pickup point availability for Delivery Promise](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/pickup-point-availability/-facets-) | `GET /pickup-point-availability/{facets}`<br>[Get pickup point availability for Delivery Promise](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/pickup-point-availability/-facets-) |
| — | `GET /products`<br>[Get product](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/products) |

### New endpoint: Get product

A new `GET` [Get product](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/products) endpoint is now available for product detail pages (PDP). Given a known identifier — product ID, slug, EAN, SKU ID, or reference — it returns a single product without going through the search pipeline, resulting in lower latency and better cache-hit rates than `GET` [Search products](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/product-search/-facets-).

### Updated parameters on product search and facets

Intelligent Search API v1 adds explicit regionalization parameters to `GET` [Search products](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/product-search/-facets-) and `GET` [List filters for a search](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/facets/-facets-):

- `regionId`
- `country`
- `zip-code`
- `coordinates`
- `pickupPoint`
- `deliveryZonesHash`
- `pickupPointsHash`

Marketing and simulation parameters are also now explicit query parameters instead of being read from the segment:

- `utmSource`, `utmCampaign`, `utmiCampaign`, `campaigns`, `priceTables`

### Updated `simulationBehavior` enum

The `simulationBehavior` parameter now accepts two additional values:

| Value | Description |
| --- | --- |
| `only3P` | Calls simulation for third-party sellers only. |
| `regionalize1p` | Calls regionalized simulation for first-party sellers only. |

### Fixed parameter name on pickup point availability

Intelligent Search API (Legacy) documented `pickupsHash` as a query parameter on the pickup point availability endpoint. The correct name is `pickupPointsHash`, which is what Intelligent Search API v1 uses.

## What needs to be done?

For a step-by-step migration checklist, see [Migrating to Intelligent Search API v1](https://developers.vtex.com/docs/guides/migrating-to-intelligent-search-api-v1).

[Intelligent Search API (Legacy)](https://developers.vtex.com/docs/api-reference/intelligent-search-api) remains available. We recommend migrating headless integrations to [Intelligent Search API v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1) to benefit from HTTP caching and lower latency.

## Related resources

- [Intelligent Search API v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1) — new API reference
- [Intelligent Search API (Legacy)](https://developers.vtex.com/docs/api-reference/intelligent-search-api) — legacy API reference
- [Migrating to Intelligent Search API v1](https://developers.vtex.com/docs/guides/migrating-to-intelligent-search-api-v1) — step-by-step migration guide
