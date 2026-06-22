---
title: "Migrating to Intelligent Search API v1"
slug: "migrating-to-intelligent-search-api-v1"
hidden: false
excerpt: "Step-by-step guide for migrating headless integrations from Intelligent Search API (Legacy) to Intelligent Search API v1."
createdAt: "2026-06-22T00:00:00.000Z"
updatedAt: "2026-06-22T00:00:00.000Z"
---

This guide covers everything you need to migrate a headless integration from [Intelligent Search API (Legacy)](https://developers.vtex.com/docs/api-reference/intelligent-search-api) to [Intelligent Search API v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1).

## Why migrate?

Intelligent Search API v1 offers:

- **HTTP caching:** most responses are returned with `Cache-Control: public, max-age=600`, enabling CDN and browser caching. This reduces origin load and speeds up storefronts.
- **Lower latency:** the new `GET` [Get product](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/products) endpoint skips the search pipeline entirely for single-product lookups.
- **Explicit context:** all inputs are passed as query parameters or path facets. Responses are deterministic and cache-friendly because they no longer vary by segment cookie.
- **Simpler URLs:** no IO prefix, no underscores.

## Before you begin

- You must have [VTEX Intelligent Search](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/3qgT47zY08biLP3d5os3DG) installed in your account.
- Identify all places in your codebase that call Intelligent Search API (Legacy) at `/api/io/_v/api/intelligent-search/*`.

## Step 1 - Update the base URL

Change the base URL from the legacy IO path to the v1 path.

**Before**

```
https://{accountName}.vtexcommercestable.com.br/api/io/_v/api/intelligent-search
```

**After**

```
https://{accountName}.vtexcommercestable.com.br/api/intelligent-search/v1
```

## Step 2 - Update endpoint paths

Rename paths to match the new URL structure. Underscores become hyphens, the IO prefix is removed, and `/v1` is added.

| Intelligent Search API (Legacy) | Intelligent Search API v1 |
| --- | --- |
| `GET /api/io/_v/api/intelligent-search/top_searches`<br>[Get list of the 10 most searched terms](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/top_searches) | `GET /api/intelligent-search/v1/top-searches`<br>[Get list of the 10 most searched terms v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/top-searches) |
| `GET /api/io/_v/api/intelligent-search/autocomplete_suggestions`<br>[Get list of suggested terms and attributes similar to the search term](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/autocomplete_suggestions) | `GET /api/intelligent-search/v1/autocomplete-suggestions`<br>[Get list of suggested terms and attributes similar to the search term v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/autocomplete-suggestions) |
| `GET /api/io/_v/api/intelligent-search/search_suggestions`<br>[Get list of suggested terms similar to the search term](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/search_suggestions) | `GET /api/intelligent-search/v1/search-suggestions`<br>[Get list of suggested terms similar to the search term v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/search-suggestions) |
| `GET /api/io/_v/api/intelligent-search/correction_search`<br>[Get attempt of correction of a misspelled term](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/correction_search) | `GET /api/intelligent-search/v1/correction-search`<br>[Get attempt of correction of a misspelled term v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/correction-search) |
| `GET /api/io/_v/api/intelligent-search/banners/{facets}`<br>[Get list of banners registered for query](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/banners/-facets-) | `GET /api/intelligent-search/v1/banners/{facets}`<br>[Get list of banners registered for query v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/banners/-facets-) |
| `GET /api/io/_v/api/intelligent-search/product_search/{facets}`<br>[Get list of products for a query](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/product_search/-facets-) | `GET /api/intelligent-search/v1/product-search/{facets}`<br>[Search products v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/product-search/-facets-) |
| `GET /api/io/_v/api/intelligent-search/facets/{facets}`<br>[Get list of the possible facets for a given query](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/facets/-facets-) | `GET /api/intelligent-search/v1/facets/{facets}`<br>[List filters for a search v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/facets/-facets-) |
| `GET /api/io/_v/api/intelligent-search/pickup-point-availability/{facets}`<br>[Get pickup point availability for Delivery Promise](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/pickup-point-availability/-facets-) | `GET /api/intelligent-search/v1/pickup-point-availability/{facets}`<br>[Get pickup point availability for Delivery Promise v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/pickup-point-availability/-facets-) |
| N/A | `GET /api/intelligent-search/v1/products`<br>[Get product v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/products) |

## Step 3 - Replace segment cookie context with explicit parameters

Intelligent Search API (Legacy) read locale, sales channel, regionalization, and marketing context from the VTEX segment cookie. Intelligent Search API v1 does not read the segment cookie. You must pass this context explicitly.

Read the current segment values from the VTEX segment cookie (or your session/context store) and map them to the corresponding query parameters:

| Segment field | Intelligent Search API v1 parameter | Affected endpoints |
| --- | --- | --- |
| `cultureInfo` | `locale` | All endpoints |
| `channel` | `sc` query param or `trade-policy/{id}` facet | All endpoints |
| `regionId` | `regionId` | `product-search`, `facets`, `pickup-point-availability` |
| `utm_source` | `utmSource` | `product-search`, `products` |
| `utm_campaign` | `utmCampaign` | `product-search`, `products` |
| `utmi_campaign` | `utmiCampaign` | `product-search`, `products` |
| `campaigns` | `campaigns` | `product-search`, `products` |
| `priceTables` | `priceTables` | `product-search`, `products` |

**Before**

```sh
curl 'https://{accountName}.vtexcommercestable.com.br/api/io/_v/api/intelligent-search/product_search/trade-policy/1' \
  --header 'Cookie: vtex_segment=...'
```

**After**

```sh
curl 'https://{accountName}.vtexcommercestable.com.br/api/intelligent-search/v1/product-search/trade-policy/1?locale=en-US&sc=1'
```

## Step 4 - Add regionalization parameters (if applicable)

If your store uses regionalization, you previously relied on the segment to pass this context. In Intelligent Search API v1, pass it explicitly on `product-search`, `facets`, and `pickup-point-availability` requests.

You can provide the buyer's location in one of two ways:

**With country and ZIP code**

```
?country=BRA&zip-code=22271020
```

**With pre-computed hashes** (faster, avoids a geolocation lookup)

```
?deliveryZonesHash=4bab2513d897914b0b33f25c8c74f571&pickupPointsHash=d41d8cd98f00b204e9800998ecf8427e
```

> `deliveryZonesHash` is obtained from `POST` [Search delivery zones](https://developers.vtex.com/docs/api-reference/delivery-promise-suggestions-api#post-/api/logistics-shipping/delivery-zones/_search/v2). `pickupPointsHash` is obtained from `POST` [Search pickup points](https://developers.vtex.com/docs/api-reference/delivery-promise-suggestions-api#post-/api/logistics-shipping/pickuppoints/_search). Both endpoints are part of the Delivery Promise Suggestions API.

Optionally include coordinates to sort pickup results by proximity:

```
?country=BRA&zip-code=22271020&coordinates=-43.19532775878906,-22.955032348632812
```

## Step 5 - Replace single-product search with the new Get product endpoint

If you use `GET` [Search products](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/product-search/-facets-) to fetch a single known product — for example, to render a product detail page from a URL slug — replace it with `GET` [Get product](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/products).

This endpoint accepts a `value` and a `field` parameter, skips the search pipeline, and responds faster with a higher cache-hit rate.

**Before:** Fetching a single product via product search

```sh
curl 'https://{accountName}.vtexcommercestable.com.br/api/io/_v/api/intelligent-search/product_search/trade-policy/1?query=product.link:blue-shirt'
```

**After:** Fetching a single product by slug

```sh
curl 'https://{accountName}.vtexcommercestable.com.br/api/intelligent-search/v1/products?sc=1&field=slug&value=blue-shirt'
```

Supported `field` values:

| Value | Identifier type |
| --- | --- |
| `id` (default) | Product ID (fastest, skips search pipeline entirely) |
| `slug` | Product slug (link text) |
| `ean` | SKU EAN |
| `sku` | SKU ID |
| `reference` | SKU reference ID |

## Step 6 - Fix pickup point availability parameter name

If you use the pickup point availability endpoint, rename the `pickupsHash` parameter to `pickupPointsHash`.

**Before**

```
?pickupsHash=d41d8cd98f00b204e9800998ecf8427e
```

**After**

```
?pickupPointsHash=d41d8cd98f00b204e9800998ecf8427e
```

## Step 7 - Remove the Host header workaround (if applicable)

Intelligent Search API (Legacy) required sending a `Host` header with the store's production domain in fully headless setups with no configured store domain. Intelligent Search API v1 does not require this header.

**Before**

```sh
curl 'https://{accountName}.vtexcommercestable.com.br/api/io/_v/api/intelligent-search/product_search/' \
  --header 'Host: {configured domain}'
```

**After**

```sh
curl 'https://{accountName}.vtexcommercestable.com.br/api/intelligent-search/v1/product-search/'
```

## Caching behavior reference

| Endpoint | Cache behavior |
| --- | --- |
| `GET /top-searches` [Get list of the 10 most searched terms v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/top-searches) | `Cache-Control: public, max-age=600` |
| `GET /autocomplete-suggestions` [Get list of suggested terms and attributes similar to the search term v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/autocomplete-suggestions) | `Cache-Control: public, max-age=600` |
| `GET /search-suggestions` [Get list of suggested terms similar to the search term v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/search-suggestions) | `Cache-Control: public, max-age=600` |
| `GET /correction-search` [Get attempt of correction of a misspelled term v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/correction-search) | `Cache-Control: public, max-age=600` |
| `GET /banners/{facets}` [Get list of banners registered for query v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/banners/-facets-) | `Cache-Control: public, max-age=600` |
| `GET /product-search/{facets}` [Search products v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/product-search/-facets-) (organic, public sales channel) | `Cache-Control: public, max-age=600` |
| `GET /product-search/{facets}` [Search products v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/product-search/-facets-) (with sponsored products) | `Cache-Control: no-store` |
| `GET /facets/{facets}` [List filters for a search v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/facets/-facets-) | `Cache-Control: public, max-age=600` |
| `GET /products` [Get product v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/products) (public sales channel) | `Cache-Control: public, max-age=600` |
| `GET /pickup-point-availability/{facets}` [Get pickup point availability for Delivery Promise v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/pickup-point-availability/-facets-) (public sales channel) | `Cache-Control: public, max-age=600` |
| Any endpoint on a private sales channel | Not cached |

## Related resources

- [Intelligent Search API v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1): New API reference
- [Intelligent Search API (Legacy)](https://developers.vtex.com/docs/api-reference/intelligent-search-api): Legacy API reference
- [New Intelligent Search API v1](https://developers.vtex.com/docs/release-notes/2026-06-22-new-intelligent-search-api-v1): Release note

## Migration checklist

- [ ] Updated base URL to `/api/intelligent-search/v1`
- [ ] Renamed all endpoint paths (underscores to hyphens)
- [ ] Passing `locale` explicitly instead of relying on segment cookie
- [ ] Passing `sc` or `trade-policy` facet explicitly instead of relying on segment cookie
- [ ] Passing regionalization parameters explicitly (if applicable)
- [ ] Passing UTM and marketing parameters explicitly (if applicable)
- [ ] Replaced single-product search calls with `GET /products` (if applicable)
- [ ] Renamed `pickupsHash` to `pickupPointsHash` (if applicable)
- [ ] Removed `Host` header workaround (if applicable)
