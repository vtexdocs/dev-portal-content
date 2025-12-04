---
title: "VTEX Ads React Package Quickstart"
slug: "vtex-ads-react-package-quickstart"
excerpt: "Get started with @vtex/ads-react package for React-specific components and hooks to integrate VTEX Ads into React applications."
hidden: false
createdAt: "2025-12-02T00:00:00.000Z"
updatedAt: "2025-12-02T00:00:00.000Z"
---

The `@vtex/ads-react` package provides React-specific components and hooks for integrating VTEX Ads into React applications. It offers a declarative API with built-in loading states, error handling, and request batching.

## Installation

Install the package using npm or yarn:

```bash
npm install @vtex/ads-react
# or
yarn add @vtex/ads-react
```

The `@vtex/ads-react` package automatically includes `@vtex/ads-core` as a dependency.

## Basic Usage

### Setting up the AdsProvider

Before requesting any ads, wrap your app or page component tree with the `<AdsProvider>`. This provider is responsible for managing ad requests and distributing results to child components.

```jsx
import React from "react";
import { AdsProvider } from "@vtex/ads-react";
import {
  intelligentSearchFetcher,
  intelligentSearchMatcher,
} from "@vtex/ads-core";

function App() {
  return (
    <AdsProvider
      identity={{
        accountName: "your-account-name",
        publisherId: "your-publisher-id",
        userId: "user-123",
        sessionId: "session-456",
        channel: "web", // optional: "web" | "mobile"
      }}
      hydrationStrategy={{
        fetcher: intelligentSearchFetcher,
        matcher: intelligentSearchMatcher,
      }}
    >
      <YourAppContent />
    </AdsProvider>
  );
}

export default App;
```

You only need one `<AdsProvider>` around the subtree where ads will be requested.

Please refer to the [VTEX Ads Core Package Custom Hydration](https://developers.vtex.com/docs/guides/vtex-ads-core-package-custom-hydration) guide for more details on configuring the hydration strategy.

### Calling the useAds hook

Call `useAds()` inside your component to request ads for a specific placement:

```jsx
const { ads, isLoading, error } = useAds({
  placement: "search_top_product",
  type: "product",
  amount: 3,
  term: "smartphone",
});
```

The ads hooks will return an object with the following properties:

- `ads`, an array of sponsored items matching the criteria.
- `isLoading`, which is `true` while the request is in progress.
- `error`, that will be populated if the request fails.

You can call `useAds()` multiple times within the same component to request different placements.

```ts
const { ads: searchAds, isLoading: isSearchAdsLoading } = useAds({
  placement: "search_top_product",
  type: "product",
  amount: 2,
  term: "tv",
});

const { ads: shelfAds, isLoading: isShelfAdsLoading } = useAds({
  placement: "search_top-shelf_product",
  type: "product",
  amount: 10,
  term: "tv",
});
```
