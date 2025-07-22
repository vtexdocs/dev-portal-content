---
title: "Implementing cache in GraphQL APIs for IO apps"
slug: "implementing-cache-in-graphql-apis-for-io-apps"
hidden: false
excerpt: "Learn how to implement and configure cache in your GraphQL APIs for faster responses."
createdAt: "2025-07-22T14:00:00.000Z"
updatedAt: "2025-07-22T14:00:00.000Z"
---

In the context of APIs, caching is a technique that allows applications to serve the same data for repeated requests to the same endpoint, avoiding unnecessary computational costs and improving response times.

When [implementing GraphQL APIs](https://developers.vtex.com/docs/guides/developing-a-graphql-api-in-service-apps) in VTEX IO, you can enable caching and control its behavior using the `@cacheControl` directive. Queries using this directive can define the scope of users and how long the content stays cached.

Because serving cached data is faster than reprocessing data for each request, caching is usually recommended when applicable.

## When to use caching

Caching is recommended in the following scenarios:

- High volume of requests to the same queries and data.
- Response data doesn't mutate frequently.
- It is acceptable to have stale data in a small time window.

On the other hand, caching is not recommended when:

- Response data changes frequently.
- Stale data is not acceptable. Responses must always be up-to-date.

## Before you begin

This guide assumes you have already implemented a GraphQL API in a VTEX IO service app, as described in the [Developing a GraphQL API in Service Apps](https://developers.vtex.com/docs/guides/developing-a-graphql-api-in-service-apps) guide. Before enabling caching, review your API's data characteristics and the user experience in case of stale data.

## Using the `@cacheControl` directive

The `@cacheControl` directive defines the scope of access and duration of cached responses for specific queries and fields in your GraphQL schema.

### `@cacheControl` arguments

The `@cacheControl` directive uses the following arguments:

- `scope`: Scope of users who can access the cached endpoint or field. Choose the scope based on the level of privacy you want for the cached data. The possible values are:
  - `PUBLIC`: Cached data can be accessed by any authenticated user.
  - `SEGMENT`: Cached data can be accessed by users of the same segment as the one who made the first request. Users are divided into segments using various criteria such as region, audience, or sales channel. VTEX handles segmentation automatically using [`vtex_segment` cookie](https://developers.vtex.com/docs/guides/sessions-system-overview#vtexsegment-cookie) data.
  - `PRIVATE`: Cached data can only be accessed by the user who made the first request.
- `maxAge`: Time in seconds for the endpoint response or field to stay cached. When responding within the `maxAge` time from the last request, the app returns the cached value instead of reprocessing it. If this value is 0, the data won't be cached.

> ℹ️ The `@cacheControl` directive affects only cached results. This directive doesn't provide any access control to requests with uncached data. For details about access control with GraphQL using VTEX IO, see [GraphQL Authorization in IO apps](https://developers.vtex.com/docs/guides/graphql-authorization-in-io-apps).

### Example

The following example caches the userProfile query for 5 minutes (300 seconds) and restricts access to the user who initiated the request:

```graphql
type Query {
  userProfile: UserProfile
    @cacheControl(scope: PRIVATE, maxAge: 300)
}
```
