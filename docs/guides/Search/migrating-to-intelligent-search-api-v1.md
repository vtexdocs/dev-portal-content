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

## Migration benefits

Intelligent Search API v1 offers:

- **HTTP caching:** most responses now include a `Cache-Control` header, enabling CDN and browser caching. This reduces origin load and speeds up storefronts. Always read this header at runtime. Don't hardcode cache durations in your integration.
- **Lower latency:** the new `GET` [Get product](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/products) endpoint skips the search pipeline entirely for single-product lookups.
- **Explicit context:** all inputs are passed as query parameters or path facets. Responses are deterministic and cache-friendly because they no longer vary by segment cookie.

## Before you begin

- You must have [VTEX Intelligent Search](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/3qgT47zY08biLP3d5os3DG) installed in your account.
- Identify all places in your codebase that call Intelligent Search API (Legacy) at `/api/io/_v/api/intelligent-search/*`.

## Step 1 - Update the base URL

Change the base URL from the legacy IO path to the v1 path.

**Before:**

```text
https://{accountName}.vtexcommercestable.com.br/api/io/_v/api/intelligent-search
```

**After:**

```text
https://{accountName}.vtexcommercestable.com.br/api/intelligent-search/v1
```

## Step 2 - Update endpoint paths

Rename paths to match the new URL structure. Underscores become hyphens, the IO prefix is removed, and `/v1` is added.

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

## Step 3 - Replace segment cookie context with explicit parameters

Intelligent Search API (Legacy) reads locale, sales channel, regionalization, marketing context, and Delivery Promise parameters from the VTEX segment cookie. Intelligent Search API v1 does not read the segment cookie. You must pass this context explicitly.

Read the current segment values from the VTEX segment cookie (or your session/context store) and map them to the corresponding query parameters:

| Segment field | Intelligent Search API v1 parameter | Affected endpoints |
| --- | --- | --- |
| `cultureInfo` | `locale` | All endpoints |
| `channel` | `sc` query param | All endpoints |
| `regionId` | `regionId` | `GET /product-search/{facets}`<br />[Search products (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/product-search/-facets-)<br />`GET /facets/{facets}`<br />[List filters for a search (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/facets/-facets-)<br />`GET /products`<br />[Get product (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/products) |
| `countryCode` | `country` | `GET /product-search/{facets}`<br />[Search products (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/product-search/-facets-)<br />`GET /facets/{facets}`<br />[List filters for a search (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/facets/-facets-)<br />`GET /pickup-point-availability/{facets}`<br />[Get pickup point availability for Delivery Promise (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/pickup-point-availability/-facets-)<br />`GET /products`<br />[Get product (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/products) |
| `utm_source` | `utmSource` | `GET /product-search/{facets}`<br />[Search products (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/product-search/-facets-)<br />`GET /products`<br />[Get product (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/products) |
| `utm_campaign` | `utmCampaign` | `GET /product-search/{facets}`<br />[Search products (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/product-search/-facets-)<br />`GET /products`<br />[Get product (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/products) |
| `utmi_campaign` | `utmiCampaign` | `GET /product-search/{facets}`<br />[Search products (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/product-search/-facets-)<br />`GET /products`<br />[Get product (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/products) |
| `campaigns` | `campaigns` | `GET /product-search/{facets}`<br />[Search products (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/product-search/-facets-)<br />`GET /products`<br />[Get product (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/products) |
| `priceTables` | `priceTables` | `GET /product-search/{facets}`<br />[Search products (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/product-search/-facets-)<br />`GET /products`<br />[Get product (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/products) |

**Before:**

```sh
curl 'https://{accountName}.vtexcommercestable.com.br/api/io/_v/api/intelligent-search/product_search/trade-policy/1' \
  --header 'Cookie: vtex_segment=...'
```

**After:**

```sh
curl 'https://{accountName}.vtexcommercestable.com.br/api/intelligent-search/v1/product-search?locale=en-US&sc=1'
```

### Parsing the segment `facets` field

The segment cookie's `facets` field is a semicolon-separated `key=value` string, for example:

```text
zip-code=22250-040;country=BRA;brand=samsung;category-1=tv
```

Six keys from this string map to v1 query parameters: `zip-code`, `coordinates`, `country`, `pickupPoint`, `deliveryZonesHash`, and `pickupPointsHash`. All other keys become path facets in the URL.

> **Note on `country`:** if `countryCode` is present as a top-level segment field, it takes precedence over the `country` key in the `facets` string. The TypeScript reference implementation below handles this automatically.
> **Note on `campaigns`:** this field is only forwarded when the segment carries it as a non-empty string. Segments often have `campaigns: null` — in that case, omit the parameter entirely.

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

  const facetPath = pathFacets.map(f => `${f.key}/${f.value}`).join('/')
  const search = new URLSearchParams(params).toString()

  return `https://{accountName}.vtexcommercestable.com.br/api/intelligent-search/v1/product-search${facetPath ? `/${facetPath}` : ''}?${search}`
}
```

### Regionalization parameter (if applicable)

If your store uses regionalization, `regionId` was a top-level segment field in Intelligent Search API (Legacy). In Intelligent Search API v1, pass it explicitly on `GET` [Search products (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/product-search/-facets-) and `GET` [List filters for a search (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/facets/-facets-):

```text
?regionId=v2.C0FC2DE04D6A7C9E1DC22C0D7EBD939B
```

### Delivery Promise parameters (if applicable)

If your store uses [Delivery Promise for headless stores](https://developers.vtex.com/docs/guides/delivery-promise-for-headless-stores), pass the buyer's location as explicit query parameters on `GET` [Search products (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/product-search/-facets-), `GET` [List filters for a search (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/facets/-facets-), and `GET` [Get pickup point availability for Delivery Promise (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/pickup-point-availability/-facets-).

The fundamental parameters are the buyer's address: `country`, `zip-code`, and optionally `coordinates`:

```text
?country=BRA&zip-code=22271020&coordinates=-43.19532775878906,-22.955032348632812
```

As an alternative, `deliveryZonesHash` and `pickupPointsHash` can be passed for faster lookup. They are pre-computed in `POST` [Search delivery zones](https://developers.vtex.com/docs/api-reference/delivery-promise-suggestions-api#post-/api/logistics-shipping/delivery-zones/_search/v2) and `POST` [Search pickup points](https://developers.vtex.com/docs/api-reference/delivery-promise-suggestions-api#post-/api/logistics-shipping/pickuppoints/_search), respectively. Since hashes expire and require a specific renewal flow, always have the buyer's address available as a fallback.

If your integration reads a VTEX segment cookie, all of these values may already be present in the segment `facets` string (`country`, `zip-code`, `coordinates`, `pickupPoint`, `deliveryZonesHash`, `pickupPointsHash`). Extract and forward them as explicit query parameters.

## Step 4 - Replace single-product search with the new Get product endpoint

If you use `GET` [Search products](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/product-search/-facets-) to fetch a single known product (for example, to render a product detail page from a URL slug), replace it with `GET` [Get product](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/products).

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

## Step 5 - Verify product item data in your integration

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
| `attachments[].required` | `boolean` | Removed. Use `isRequired` instead. |
| `attachments[].domainValues` | `string` | Removed. Use `fields[].domain_values` instead. |
| `attachments[].isRequired` | Not present | `boolean` |
| `attachments[].isActive` | Not present | `boolean` |
| `attachments[].schema` | Not present | `object` (free-form JSON schema) |
| `attachments[].fields[]` | Not present | Array of `{ field_name, max_characters, domain_values }` |

**New fields now returned:**

- `products[].items[].estimatedDateArrival` (string): Estimated arrival date for the SKU, when configured.
- `products[].items[].kitItems[]` (array): Component SKUs when `isKit` is `true`. Each entry has `itemId` and `amount`.
- `products[].items[].sellers[].commertialOffer.PaymentOptions` (object): Available payment options and installment plans for the seller's offer.

## Caching behavior

Responses from most endpoints now include a `Cache-Control` header, enabling CDN and browser caching for public sales channels. This reduces origin load and improves storefront response times.

> ℹ️ Always read the `Cache-Control` header at runtime to determine cacheability. Don't hardcode cache durations in your integration.

Exceptions:

- Responses containing sponsored products ([VTEX Ads](https://developers.vtex.com/docs/guides/vtex-ads)) are not cached, preventing ad impressions from being served from a shared cache.
- Private sales channel responses: not cached.

## Migration checklist

| Task | Step | Required |
| --- | --- | --- |
| <input type="checkbox"></input> Updated base URL to `/api/intelligent-search/v1` | [Step 1](#step-1---update-the-base-url) | Yes |
| <input type="checkbox"></input> Renamed all endpoint paths (underscores to hyphens) | [Step 2](#step-2---update-endpoint-paths) | Yes |
| <input type="checkbox"></input> Passing `locale` explicitly | [Step 3](#step-3---replace-segment-cookie-context-with-explicit-parameters) | Yes |
| <input type="checkbox"></input> Passing `sc` query parameter explicitly | [Step 3](#step-3---replace-segment-cookie-context-with-explicit-parameters) | Yes |
| <input type="checkbox"></input> Passing `regionId` explicitly | [Step 3](#regionalization-parameter-if-applicable) | If applicable |
| <input type="checkbox"></input> Passing Delivery Promise parameters explicitly (`country`, `zip-code`, `coordinates`, `pickupPoint`, `deliveryZonesHash`, `pickupPointsHash`) | [Step 3](#delivery-promise-parameters-if-applicable) | If applicable |
| <input type="checkbox"></input> Passing UTM and marketing parameters explicitly (`utmSource`, `utmCampaign`, `utmiCampaign`, `campaigns`, `priceTables`) | [Step 3](#step-3---replace-segment-cookie-context-with-explicit-parameters) | If applicable |
| <input type="checkbox"></input> Replaced single-product search calls with `GET` [Get product (v1)](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1#get-/products) | [Step 4](#step-4---replace-single-product-search-with-the-new-get-product-endpoint) | If applicable |
| <input type="checkbox"></input> Verified `isKit`, `modalType`, and `imageText` fields now return correct data | [Step 5](#step-5---verify-product-item-data-in-your-integration) | If applicable |
| <input type="checkbox"></input> Updated code reading attachment data to match new schema | [Step 5](#step-5---verify-product-item-data-in-your-integration) | If applicable |
| <input type="checkbox"></input> Handled new fields: `estimatedDateArrival`, `kitItems[]`, `PaymentOptions` | [Step 5](#step-5---verify-product-item-data-in-your-integration) | If applicable |

## Related resources

- [Intelligent Search API v1](https://developers.vtex.com/docs/api-reference/intelligent-search-api-v1)
- [Intelligent Search API (Legacy)](https://developers.vtex.com/docs/api-reference/intelligent-search-api)
