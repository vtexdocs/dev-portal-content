---
title: 'Configuring GraphQL cache control for `GET` requests'
---

> ⚠ This is an experimental feature.

This guide explains how to configure caching for GraphQL `GET` requests using the `graphqlCacheControl` flag. Setting cache rules allows responses to be stored and reused for subsequent requests, reducing server load and improving store performance. For example, caching a product listing page (such as "Summer Collection") for five minutes allows the page to load faster for store visitors. The system serves cached content immediately, then updates it in the background, ensuring fresh results without slowing down the user experience, improving performance, and minimizing additional server load.

The `graphqlCacheControl` flag defines how long responses should be stored and reused when caching for GraphQL `GET` requests.

> ℹ POST requests are excluded from caching by default. This ensures that data sent in the request body, such as user input or sensitive information, is always processed in real time and not served from cache.

## Before you begin

Make sure that your project is using the latest version of the @faststore/cli package. To do so, follow the steps in [Updating the '@faststore/cli' package version](https://developers.vtex.com/docs/guides/faststore/project-structure-updating-the-cli-package-version).

## Instructions

Since the `graphqlCacheControl` flag is an experimental feature, declare it under the `experimental` section in the `discovery.config.js` file.

1. Open your FastStore project in a code editor.
2. Open the `discovery.config.js` file.
3. Under the `experimental` section, add the `graphqlCacheControl` flag:

    ```js discovery.config.js
    experimental: {
        …
        graphqlCacheControl: {},
    },
    ```

4. Inside the `graphqlCacheControl` flag, add the `maxAge` and `staleWhileRevalidate` objects and their values:

    ```js discovery.config.js
    experimental: {
        …
        graphqlCacheControl: {
        maxAge: 5 * 60, // 0 disables cache, 5 * 60 enable cache control maxAge 5 minutes
        staleWhileRevalidate: 60,
        },
    },
    ```

In the example above, the `maxAge` and `staleWhileRevalidate` objects received the following values:

| Object    | Description     |
| --------- | --------------- |
| `maxAge: 5 * 60` | Defines how long a response stays fresh in cache. <ul><li>Responses are cached for 5 minutes (300 seconds).</li><li>After 5 minutes, the cache is considered `stale`.</li><li>`maxAge: 0`: The `0` value disables caching entirely.</li></ul> |
| `staleWhileRevalidate: 60` | Defines how long stale cache can be used while new data is retrieved in the background. <ul><li>After the initial 5 minutes (when `maxAge expires`), stale cached data can still be served for up to 1 extra minute (60 seconds) while the system retrieves fresh data in the background.</li><li>This ensures users see slightly older data (for 1 minute maximum) instead of waiting for a full reload.</li></ul> |

This configuration creates a tiered caching system that balances immediate performance and data freshness. See in the table below what happens over time:

| **Object** | **Cache state** | **Behavior** |
| ------ | ----------- | -------- |
| 0s - 300s  | Fresh | <ul><li>Serves cached responses instantly.</li><li>No backend requests unless it's the first request.</li></ul> |
| 300 s - 360 s  | Stale | <ul><li>Continues serving stale data.</li><li>Simultaneously retrieves fresh data in the background.</li></ul> |
| After 360 s  | Expired | <ul><li>Cache fully expires.</li><li>The next request triggers a new data retrieval.</li></ul> |

5. Open a terminal and run `yarn dev` to sync the changes and start [testing the cache configuration](#testing-the-cache-configuration).

## Testing the cache configuration

After enabling the `graphqlCacheControl` flag in `discovery.config.js` and running `yarn dev` in a terminal, follow these steps to test the cache configuration:

1. Open the localhost path available in the terminal to view the store preview (example: `http://localhost:3000/`).
2. On the store preview page, open your browser's **Developer Tools**.
3. Go to the **Network** tab and look for the **Cache-Control** column as displayed in the image below:
![cache-hit](https://vtexhelp.vtexassets.com/assets/docs/src/graphql-cache-control-flag-localhost___70d2f2c3fbf40846180c7c0ed11d16f0.png)

{/* This is a next step section, some questions for it: Is that possible to recommend `maxAge` and `staleWhileRevalidate` values? See the example below for how we could present that.
### Recommended values for `maxAge` and `staleWhileRevalidate`

| **Use case** | **Suggested `maxAge`** | **Suggested `staleWhileRevalidate`** |
| PLPs | 300s (5m) | 60s (1m)
| Static content (user-specific data)? | --------------- |
| --------- | --------------- | */}
