---
title: "VTEX Ads Core Package Quickstart"
slug: "vtex-ads-core-package-quickstart"
excerpt: "Get started with @vtex/ads-core package for fundamental advertising functionality in any JavaScript environment."
hidden: false
createdAt: "2025-12-02T00:00:00.000Z"
updatedAt: "2025-12-02T00:00:00.000Z"
---

The `@vtex/ads-core` package provides the fundamental advertising functionality for any JavaScript environment. This package is ideal when you're not using React or need maximum flexibility and control.

## Installation

Install the package using npm or yarn:

```bash
npm install @vtex/ads-core
# or
yarn add @vtex/ads-core
```

## Minimal example

Here's a minimal example to get you started:

```javascript
import { getRawAds } from "@vtex/ads-core";

// Configure your ad request
const adRequest = {
  identity: {
    accountName: "your-account-name",
    publisherId: "your-publisher-id",
    userId: "user-123",
    sessionId: "session-456",
    channel: "web", // optional: 'web' | 'mobile'
  },
  search: {
    term: "smartphone", // optional search term
    selectedFacets: [
      // optional filters
      { key: "brand", value: "Acme" },
      { key: "category", value: "Tools" },
    ],
    skuId: "SKU-123", // optional specific product
  },
  placements: {
    search_top_product: {
      quantity: 3,
      types: ["product"],
    },
  },
};

// Get raw ads
try {
  const rawAds = await getRawAds(adRequest);
  console.log("Raw ads:", rawAds.sponsoredProducts);
} catch (error) {
  console.error("Failed to fetch ads:", error);
}
```
