---
title: "Configuring GraphQL cache control for `GET` requests"
slug: "graphql-cache-control"
hidden: false
type: "added"
createdAt: "2025-05-30T00:00:00.219Z"
updatedAt: ""
excerpt: "Improve performance by reducing server load and speeding up page loads with the `graphqlCacheControl` flag"
---

FastStore projects can now configure caching for GraphQL `GET` requests using the `graphqlCacheControl` flag. This flag improves store performance by caching responses and reducing server load, ensuring faster page loads for visitors while maintaining data freshness.

> ⚠️ This is an experimental flag and may have limitations. Before using it in the production environment, make sure to test it to ensure compatibility with your store.

## What has changed?

The `graphqlCacheControl` flag supports two key caching parameters:

- `maxAge`: Defines how long a response remains fresh in the cache (e.g., `5 * 60` seconds for 5 minutes).
- `staleWhileRevalidate`: Allows stale cache to be served while fetching fresh data in the background (e.g., `60` seconds).

To configure caching for GraphQL `GET` requests using the `graphqlCacheControl` flag, follow the instructions in the [Configuring GraphQL cache control for `GET` requests](https://developers.vtex.com/docs/guides/faststore/faststore-api-configuring-graphql-cache-control) guide.
