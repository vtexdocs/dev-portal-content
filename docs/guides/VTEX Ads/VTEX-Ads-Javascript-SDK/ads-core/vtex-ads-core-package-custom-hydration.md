---
title: "VTEX Ads Core Package Custom Hydration"
slug: "vtex-ads-core-package-custom-hydration"
excerpt: "Build your own hydration strategy to fetch product data and associate it with ad offers using custom fetchers and matchers."
hidden: false
createdAt: "2025-12-02T00:00:00.000Z"
updatedAt: "2025-12-02T00:00:00.000Z"
---

By default, VTEX Ads expects you to provide a hydration strategy that defines how to fetch product data and how to associate it with the offers returned by the ad server. This gives you full control over where and how product data is retrieved — whether it’s via a REST API, a GraphQL endpoint, or any custom service.

To build your own hydration strategy, you’ll need to implement two functions:

- Fetcher: a function that receives a list of ad offers and returns the corresponding product data.
- Matcher: a function that determines which offer belongs to which product, so they can be merged into hydrated ads.

Below are a couple of examples to help you get started, using both a REST API and a GraphQL endpoint.

## REST API hydration

```javascript
const customRestFetcher = async (offers, identity) => {
  const skuIds = offers.map((offer) => offer.skuId);

  const response = await fetch(`/api/products/batch`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      skuIds,
      accountName: identity.accountName,
    }),
  });

  if (!response.ok) {
    throw new Error(`Failed to fetch products: ${response.statusText}`);
  }

  return response.json();
};

const customMatcher = (product, offer) => {
  return product.skuId === offer.skuId && product.sellerId === offer.sellerId;
};
```

## GraphQL hydration

```javascript
const graphqlFetcher = async (offers, identity) => {
  const skuIds = offers.map((offer) => offer.skuId);

  const query = `
    query GetProducts($skuIds: [String!]!) {
      products(skuIds: $skuIds) {
        id
        sku
        name
        price
        description
        images
        brand
        seller {
          id
          name
        }
      }
    }
  `;

  const response = await fetch("/graphql", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      query,
      variables: { skuIds },
    }),
  });

  const data = await response.json();
  return data.data.products;
};

const customMatcher = (product, offer) => {
  return product.sku === offer.skuId && product.seller.id === offer.sellerId;
};
```
