---
title: "New Intelligent Search API v1"
slug: "2026-07-08-new-intelligent-search-api-v1"
excerpt: "The new Intelligent Search API v1 is now available for headless integrations. It adds HTTP caching, lower latency, explicit context parameters instead of the segment cookie, and a new endpoint for product detail pages."
hidden: false
createdAt: "2026-07-08T00:00:00.000Z"
updatedAt: "2026-07-08T00:00:00.000Z"
type: "added"
tags:
    - Search
---

The new [Intelligent Search API v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1) is now available for headless integrations at `/api/intelligent-search/v1/*`. It replaces [Intelligent Search API (Legacy)](https://developers.vtex.com/docs/api-reference/intelligent-search-api) at `/api/io/_v/api/intelligent-search/*` with HTTP caching, lower latency, and explicit context parameters.

## What has changed?

Here is a summary of the key differences between Intelligent Search API (Legacy) and Intelligent Search API v1. See the sections below for full details.

|  | Intelligent Search API (Legacy) | Intelligent Search API v1 |
| :---- | :---- | :---- |
| **[HTTP caching](#http-caching)** | Not cached | Responses include a `Cache-Control` header; read it at runtime to determine cacheability. |
| [**Context**](#explicit-context-no-segment-cookie) | VTEX segment cookie | Explicit query parameters |
| [**Single-product lookup**](#new-endpoint-get-product)  | Via product search pipeline | Dedicated `GET /products` endpoint |
| **[Base URL](#new-url-structure)** | `/api/io/_v/api/intelligent-search` | `/api/intelligent-search/v1` |
| **[Path format](#new-url-structure)** | `endpoint_name` (underscores) | `endpoint-name` (hyphens) |
| **[`attachments[]` schema](#breaking-change-attachments-object-structure-in-product-search)** | `id` string; `required`/`domainValues` fields | `id` number; `required`/`domainValues` replaced by `isRequired`/`fields[].domain_values` |

### HTTP caching

Responses from most endpoints now include a `Cache-Control` header, enabling CDN and browser caching for public sales channels. This reduces origin load and improves storefront response times.

> ℹ️ Always read the `Cache-Control` header at runtime to determine cacheability. Don't hardcode cache durations in your integration.

Exceptions:

* Responses containing sponsored products ([VTEX Ads](https://developers.vtex.com/docs/guides/vtex-ads)) are not cached, preventing ad impressions from being served from a shared cache.
* Private sales channel responses: not cached.

### Explicit context: No segment cookie

Intelligent Search API (Legacy) relied on the VTEX segment cookie to fill in locale, sales channel, regionalization, and marketing context. Intelligent Search API v1 does not read the segment cookie. All context must be passed explicitly as query parameters or facets in the URL path.

| Context | Intelligent Search API (Legacy) | Intelligent Search API v1 |
| :---- | :---- | :---- |
| Locale | Read from `segment.cultureInfo` | `locale` query parameter |
| Sales channel | Read from `segment.channel` | `sc` query parameter |
| Country | Read from `segment.countryCode` | `country` query parameter |
| Region | Read from `segment.regionId` | `regionId` query parameter |
| UTM / price tables | Read from `segment.utm_source`, `utm_campaign`, `utmi_campaign`, `campaigns`, `priceTables` | `utmSource`, `utmCampaign`, `utmiCampaign`, `campaigns`, `priceTables` query parameters |

If your store uses [Delivery Promise for headless stores](https://developers.vtex.com/docs/guides/delivery-promise-for-headless-stores), the following parameters were previously passed via the segment `facets` string and must now be passed as explicit query parameters on `GET` [Search products (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/product-search/-facets-), `GET` [List filters for a search (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/facets/-facets-), and `GET` [Get pickup point availability for Delivery Promise (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/pickup-point-availability/-facets-):

* `country`, `zip-code`, and optionally `coordinates` (buyer's address, the fundamental parameters)
* `deliveryZonesHash` and `pickupPointsHash` (pre-computed alternative for faster lookup; hashes expire and require a specific renewal flow, so always have the address available as a fallback)
* `pickupPoint`

### New URL structure

The IO prefix has been removed, underscores in path names have been replaced by hyphens, and `/v1` has been added to the path.

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

A new `GET` [Get product (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/products) endpoint is now available for product detail pages (PDP). Given a known identifier (product ID, slug, EAN, SKU ID, or reference), it returns a single product without going through the search pipeline, resulting in lower latency and better cache-hit rates than `GET` [Search products (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/product-search/-facets-).

### Breaking change: `attachments[]` object structure in product search

The `attachments[]` object structure has changed in `products[].items[]` between Intelligent Search API (Legacy) and Intelligent Search API v1, affecting the following endpoints:

* `GET` [Search products (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/product-search/-facets-) (previously `GET` [Get list of products for a query](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/product_search/-facets-))
* `GET` [Get product (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/products) (new)

Key changes:

* `id` changed from string to number.
* `required` and `domainValues` have been removed in favor of `isRequired` and `fields[].domain_values`.
* New fields `estimatedDateArrival` and `kitItems` are now returned.
* Fields previously returning incorrect or empty values, such as `isKit`, `modalType`, and `images[].imageText`, now return correctly, potentially resolving a [known issue](https://help.vtex.com/known-issues/unsupported-fields-by-the-intelligent-search-api-returning-empty).

If your integration reads attachment data, update it before migrating. See [Migrating to Intelligent Search API v1](https://developers.vtex.com/docs/guides/migrating-to-intelligent-search-api-v1) for the full before/after schema.

## What needs to be done?

For a step-by-step migration checklist, see [Migrating to Intelligent Search API v1](https://developers.vtex.com/docs/guides/migrating-to-intelligent-search-api-v1).

All new headless integrations must use [Intelligent Search API v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1).

[Intelligent Search API (Legacy)](https://developers.vtex.com/docs/api-reference/intelligent-search-api) remains available for existing integrations, but its endpoints will be deprecated in a future announcement. We recommend migrating existing integrations as soon as possible.

## Related resources

* [Intelligent Search API v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1)
* [Intelligent Search API (Legacy)](https://developers.vtex.com/docs/api-reference/intelligent-search-api)
* [Migrating to Intelligent Search API v1](https://developers.vtex.com/docs/guides/migrating-to-intelligent-search-api-v1)
