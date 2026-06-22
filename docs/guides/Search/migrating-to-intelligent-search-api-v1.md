---
title: "Migrating to Intelligent Search API v1"
slug: "migrating-to-intelligent-search-api-v1"
hidden: false
excerpt: "Step-by-step guide for migrating headless integrations from Intelligent Search API (Legacy) to Intelligent Search API v1."
createdAt: "2026-06-22T00:00:00.000Z"
updatedAt: "2026-06-22T00:00:00.000Z"
---

This guide covers everything you need to migrate a headless integration from [Intelligent Search API (Legacy)](https://developers.vtex.com/docs/api-reference/intelligent-search-api) to [Intelligent Search API v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1).

All new headless integrations must use [Intelligent Search API v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1). The legacy API endpoints will be deprecated in a future announcement.

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

> **Note on pickup point availability:** this endpoint was already being served by the v1 service in the legacy API. The path itself does not change, only the base URL and how context is passed (see steps 3 and 4).

| Intelligent Search API (Legacy) | Intelligent Search API v1 |
| --- | --- |
| `GET /api/io/_v/api/intelligent-search/top_searches`<br />[Get list of the 10 most searched terms](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/top_searches) | `GET /api/intelligent-search/v1/top-searches`<br />[Get list of the 10 most searched terms v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/top-searches) |
| `GET /api/io/_v/api/intelligent-search/autocomplete_suggestions`<br />[Get list of suggested terms and attributes similar to the search term](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/autocomplete_suggestions) | `GET /api/intelligent-search/v1/autocomplete-suggestions`<br />[Get list of suggested terms and attributes similar to the search term v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/autocomplete-suggestions) |
| `GET /api/io/_v/api/intelligent-search/search_suggestions`<br />[Get list of suggested terms similar to the search term](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/search_suggestions) | `GET /api/intelligent-search/v1/search-suggestions`<br />[Get list of suggested terms similar to the search term v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/search-suggestions) |
| `GET /api/io/_v/api/intelligent-search/correction_search`<br />[Get attempt of correction of a misspelled term](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/correction_search) | `GET /api/intelligent-search/v1/correction-search`<br />[Get attempt of correction of a misspelled term v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/correction-search) |
| `GET /api/io/_v/api/intelligent-search/banners/{facets}`<br />[Get list of banners registered for query](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/banners/-facets-) | `GET /api/intelligent-search/v1/banners/{facets}`<br />[Get list of banners registered for query v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/banners/-facets-) |
| `GET /api/io/_v/api/intelligent-search/product_search/{facets}`<br />[Get list of products for a query](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/product_search/-facets-) | `GET /api/intelligent-search/v1/product-search/{facets}`<br />[Search products v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/product-search/-facets-) |
| `GET /api/io/_v/api/intelligent-search/facets/{facets}`<br />[Get list of the possible facets for a given query](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/facets/-facets-) | `GET /api/intelligent-search/v1/facets/{facets}`<br />[List filters for a search v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/facets/-facets-) |
| `GET /api/io/_v/api/intelligent-search/pickup-point-availability/{facets}`<br />[Get pickup point availability for Delivery Promise](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/pickup-point-availability/-facets-) | `GET /api/intelligent-search/v1/pickup-point-availability/{facets}`<br />[Get pickup point availability for Delivery Promise v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/pickup-point-availability/-facets-) |
| N/A | `GET /api/intelligent-search/v1/products`<br />[Get product v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/products) |

## Step 3 - Replace segment cookie context with explicit parameters

Intelligent Search API (Legacy) read locale, sales channel, regionalization, and marketing context from the VTEX segment cookie. Intelligent Search API v1 does not read the segment cookie. You must pass this context explicitly.

Read the current segment values from the VTEX segment cookie (or your session/context store) and map them to the corresponding query parameters:

| Segment field | Intelligent Search API v1 parameter | Affected endpoints |
| --- | --- | --- |
| `cultureInfo` | `locale` | All endpoints |
| `channel` | `sc` query param or `trade-policy/{id}` facet | All endpoints |
| `regionId` | `regionId` | `GET /product-search/{facets}`<br />[Search products v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/product-search/-facets-)<br />`GET /facets/{facets}`<br />[List filters for a search v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/facets/-facets-)<br />`GET /pickup-point-availability/{facets}`<br />[Get pickup point availability for Delivery Promise v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/pickup-point-availability/-facets-)<br />`GET /products`<br />[Get product v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/products) |
| `utm_source` | `utmSource` | `GET /product-search/{facets}`<br />[Search products v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/product-search/-facets-)<br />`GET /products`<br />[Get product v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/products) |
| `utm_campaign` | `utmCampaign` | `GET /product-search/{facets}`<br />[Search products v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/product-search/-facets-)<br />`GET /products`<br />[Get product v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/products) |
| `utmi_campaign` | `utmiCampaign` | `GET /product-search/{facets}`<br />[Search products v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/product-search/-facets-)<br />`GET /products`<br />[Get product v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/products) |
| `campaigns` | `campaigns` | `GET /product-search/{facets}`<br />[Search products v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/product-search/-facets-)<br />`GET /products`<br />[Get product v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/products) |
| `priceTables` | `priceTables` | `GET /product-search/{facets}`<br />[Search products v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/product-search/-facets-)<br />`GET /products`<br />[Get product v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/products) |

**Before**

```sh
curl 'https://{accountName}.vtexcommercestable.com.br/api/io/_v/api/intelligent-search/product_search/trade-policy/1' \
  --header 'Cookie: vtex_segment=...'
```

**After**

```sh
curl 'https://{accountName}.vtexcommercestable.com.br/api/intelligent-search/v1/product-search/trade-policy/1?locale=en-US&sc=1'
```

### Parsing the segment `facets` field

The segment cookie's `facets` field is a semicolon-separated `key=value` string, for example:

```
zip-code=22250-040;country=BRA;brand=samsung;category-1=tv
```

Six keys from this string map to v1 query parameters: `zip-code`, `coordinates`, `country`, `pickupPoint`, `deliveryZonesHash`, and `pickupPointsHash`. All other keys become path facets in the URL.

The following TypeScript snippet shows a reference implementation of the full segment-to-v1 translation for `product-search`:

```ts
type Segment = {
  channel?: string | number
  regionId?: string
  countryCode?: string
  cultureInfo?: string
  // Semicolon-separated "key=value" string, e.g. "zip-code=22250-040;country=BRA;brand=samsung"
  facets?: string
  utm_source?: string
  utm_campaign?: string
  utmi_campaign?: string
  campaigns?: string
  priceTables?: string
}

const SHIPPING_KEYS = new Set([
  'zip-code', 'coordinates', 'country', 'pickupPoint',
  'deliveryZonesHash', 'pickupPointsHash',
])

function segmentToProductSearchV1(segment: Segment, query?: string): string {
  const shipping: Record<string, string> = {}
  const pathFacets: Array<{ key: string; value: string }> = []

  for (const pair of (segment.facets ?? '').split(';')) {
    const eq = pair.indexOf('=')
    if (eq < 0) continue
    const key = pair.slice(0, eq)
    const value = pair.slice(eq + 1)
    if (!key || !value) continue

    if (SHIPPING_KEYS.has(key)) {
      shipping[key] = value
    } else {
      pathFacets.push({ key, value })
    }
  }

  const params: Record<string, string> = {}
  const set = (name: string, value?: string | number) => {
    if (value !== undefined && value !== null && value !== '') {
      params[name] = String(value)
    }
  }

  set('sc', segment.channel)
  set('locale', segment.cultureInfo)
  set('regionId', segment.regionId)
  set('country', segment.countryCode ?? shipping.country)
  set('zip-code', shipping['zip-code'])
  set('coordinates', shipping.coordinates)
  set('pickupPoint', shipping.pickupPoint)
  set('deliveryZonesHash', shipping.deliveryZonesHash)
  set('pickupPointsHash', shipping.pickupPointsHash)
  set('utmSource', segment.utm_source)
  set('utmCampaign', segment.utm_campaign)
  set('utmiCampaign', segment.utmi_campaign)
  set('campaigns', segment.campaigns)
  set('priceTables', segment.priceTables)

  if (query) params.query = query

  const sc = params.sc ?? '1'
  const facetPath = pathFacets.map(f => `${f.key}/${f.value}`).join('/')
  const path = ['trade-policy', sc, facetPath].filter(Boolean).join('/')
  const search = new URLSearchParams(params).toString()

  return `https://{accountName}.vtexcommercestable.com.br/api/intelligent-search/v1/product-search/${path}?${search}`
}
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

## Step 6 - Handle new response fields

Intelligent Search API v1 returns several fields that were absent or undocumented in the legacy API. Review each one and update your integration as needed.

**`GET /product-search` response additions:**

- `searchId` (string): Unique identifier for the search request. Pass this value in analytics events to tie impressions and clicks back to the originating search.
- `correction` (object): Spelling correction applied to the query. Check this field to display "Did you mean?" messaging.
- `redirect` (string): When the query matches a redirect rule, this field contains the target URL. Redirect the user instead of displaying search results.
- `options` (object): Available sort options, result counts, and delivery promise metadata.

**`GET /search-suggestions` response addition:**

Each suggestion now optionally includes an `attributes` array describing facet attributes associated with the term, using the same shape as `GET /autocomplete-suggestions`.

**`GET /facets` response addition:**

`facets[].type` can now be `DELIVERY` in addition to `TEXT` and `PRICERANGE`. If your integration filters or switches on `type`, add a handler for `DELIVERY`.

## Step 7 - Verify product item data in your integration

A [known issue](https://help.vtex.com/known-issues/unsupported-fields-by-the-intelligent-search-api-returning-empty) affecting `products[].items[]` fields in Intelligent Search API (Legacy) is resolved in v1. If your integration reads any of the following fields, verify that your code handles the updated values correctly after migrating:

**Fields that previously returned incorrect data, now correct:**

- `products[].items[].isKit`
- `products[].items[].modalType`
- `products[].items[].images[].imageText`

**Attachment schema change:** the `attachments[]` object structure changed significantly. Update any code that reads attachment data:

| Field | Intelligent Search API (Legacy) | Intelligent Search API v1 |
| --- | --- | --- |
| `attachments[].id` | `string` | `number` |
| `attachments[].name` | `string` | `string` (unchanged) |
| `attachments[].required` | `boolean` | Removed — use `isRequired` |
| `attachments[].domainValues` | `string` | Removed — use `fields[].domain_values` |
| `attachments[].isRequired` | Not present | `boolean` |
| `attachments[].isActive` | Not present | `boolean` |
| `attachments[].schema` | Not present | `object` (free-form JSON schema) |
| `attachments[].fields[]` | Not present | Array of `{ field_name, max_characters, domain_values }` |

**New fields now returned:**

- `products[].items[].estimatedDateArrival` (string): Estimated arrival date for the SKU, when configured.
- `products[].items[].kitItems[]` (array): Component SKUs when `isKit` is `true`. Each entry has `itemId` and `amount`.
- `products[].items[].sellers[].commertialOffer.PaymentOptions` (object): Available payment options and installment plans for the seller's offer.

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
- [ ] Updated analytics code to use `searchId` from product search response (if applicable)
- [ ] Added `DELIVERY` handler to facet type switch/filter (if applicable)
- [ ] Verified attachment schema and new product item fields after migrating (if applicable)
