---
title: "Search and scroll API queries"
slug: "search-and-scroll-api-queries"
hidden: false
createdAt: "2022-10-17T18:52:12.887Z"
updatedAt: "2022-10-17T19:03:58.837Z"
---
To query the Master Data, you can use the `search` or the `scroll` endpoints. In this article, you will learn the main differences between these two routes, and details of how `scroll` works.

## Search

The `search` route is the best solution for cases where we need to find a collection of documents directly in the store. This route is mainly used for paginated queries. However, the greater the interval of documents, the slower the query will be.

To get better performance in these cases, create a filter. Reducing the number of documents in the final result is the best way to achieve an efficient query.

## Scroll

The `scroll` route was developed for cases of external integration. If you need to query the entire database of VTEX Master Data or if you have stored more than 10.000 documents, use this tool.

To use `scroll` send your API request using the same filtering resources available for the `search` route. In response to your first request, you will get a `X-VTEX-MD-TOKEN` token in the response header.

Use this token for your next requests until an empty list is returned.

> ⚠️ **Scroll limitations**
>
> 1. **Only one operation is allowed at a time.** This means that when you receive a token on your first request, you must complete the search, or wait until the token expires.
> 2. If Master Data stops receiving requests with the token, it will expire in **20 minutes**. After that, you can then make new scroll requests.
> 3. The maximum number of documents per request is **1000**.
