---
title: "VTEX Ads Core Package Basic Usage"
slug: "vtex-ads-core-package-basic-usage"
excerpt: "Learn the fundamental patterns and APIs for using the @vtex/ads-core package effectively."
hidden: false
createdAt: "2025-12-02T00:00:00.000Z"
updatedAt: "2025-12-02T00:00:00.000Z"
---

Learn the fundamental patterns and APIs for using the `@vtex/ads-core` package effectively. This section walks you through how to build ad requests and choose between raw or hydrated ad responses, depending on your use case.

## Building an ad request

To fetch ads, you first need to construct a request that identifies the user and describes the search context. This request includes:

- An `identity` block: who is making the request (account, user, session).
- A `search` block: the search term, selected facets, or SKU.
- A list of `placements`: where you want ads to appear in your UI.

### Identity

The identity tells the ad server who the user is and what session they're in. It also optionally includes the channel (like `'web'` or `'mobile'`), which helps with targeting and analytics.

```ts
const identity = {
  accountName: "your-account-name",
  publisherId: "your-publisher-id",
  userId: "user-123",
  sessionId: "session-456",
  channel: "web", // Optional
};
```

### Ad request

Here's how to combine the identity with a search context and ad placements:

```ts
const adRequest = {
  identity,
  search: {
    term: "smartphone",
    selectedFacets: [
      { key: "brand", value: "Acme" },
      { key: "category", value: "Tools" },
    ],
    skuId: "SKU-123",
  },
  placements: {
    search_top_product: {
      quantity: 3,
      types: ["product"],
    },
    home_shelf_product: {
      quantity: 6,
      types: ["product"],
    },
  },
};
```

## Fetching raw or hydrated Ads

You can choose to fetch either **raw ads** or **hydrated ads**, depending on your needs:

- **Raw ads**: lightweight, fast, and ideal if you already have access to product data.
- **Hydrated ads**: include full product info, ready to render.

### Using raw ads

Use `getRawAds` when you want just the ad metadata and plan to enrich it later:

```ts
import { getRawAds } from "@vtex/ads-core";

const rawAds = await getRawAds(adRequest);
console.log(rawAds.sponsoredProducts.search_top_product);
```

When to use:

- You already cache product data
- You want to implement custom hydration

### Using hydrated ads

Use `getHydratedAdsFromIS` (or a custom hydration strategy) to fetch ads that include full product details:

```ts
import { getHydratedAdsFromIS } from "@vtex/ads-core";

const hydratedAds = await getHydratedAdsFromIS(adRequest);
console.log(hydratedAds.sponsoredProducts.byPlacement.search_top_product);
```

When to use:

- You want to skip writing a custom fetcher/matcher
- You need full product details out-of-the-box

To implement your own fetcher and matcher for hydration, see the [VTEX Ads Core Package Custom Hydration](https://developers.vtex.com/docs/guides/vtex-ads-core-package-custom-hydration).

#### Handling partial hydration failures

Hydration may fail for some ads — for example, if the product is no longer in stock. You can inspect and gracefully handle these cases:

```ts
import { getHydratedAds } from "@vtex/ads-core";

const hydratedAds = await getHydratedAds(adRequest, fetcher, matcher);

if (hydratedAds.sponsoredProducts.failed.length > 0) {
  console.warn(
    "Some ads failed to hydrate:",
    hydratedAds.sponsoredProducts.failed,
  );

  const successful = hydratedAds.sponsoredProducts.byPlacement;
  // Use fallback logic or continue with successful ads
}
```
