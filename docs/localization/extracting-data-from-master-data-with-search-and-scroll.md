---
title: "Extracting data from Master Data with search and scroll"
slug: "extracting-data-from-master-data-with-search-and-scroll"
hidden: false
createdAt: "2024-09-27T10:00:00.000Z"
updatedAt: "2024-09-27T10:00:00.000Z"
excerpt: "Learn how to extract data from Master Data using the search and scroll endpoints, with best practices for optimizing queries and handling large datasets."
seeAlso:
 - "/docs/guides/pagination-in-the-master-data-api"
---

In this guide, you will learn how to extract data from Master Data using the search and scroll endpoints, including when to use each route, how to optimize queries, and best practices.

>ℹ In Master Data v1, you can export data directly from the interface. See [Exporting data from Master Data v1](https://help.vtex.com/en/tutorial/exporting-data--tutorials_1125) for more information.

## Search

The search route is ideal when you need to find a specific set of documents within your store. It is particularly useful for paginated queries, where you want to retrieve up to 10000 documents in small chunks over multiple requests. Each page is limited to 100 documents.

>ℹ When paginating, the `_sort` parameter is recommended. The API does not guarantee a specific order by default; therefore, omitting the `_sort` parameter may lead to duplicate documents or return unexpected pages.

See the Search endpoint reference depending on the Master Data version you are using:

* [Master Data API v1 - Search](https://developers.vtex.com/docs/api-reference/masterdata-api#get-/api/dataentities/-acronym-/search)  
* [Master Data API v2 - Search](https://developers.vtex.com/docs/api-reference/master-data-api-v2#get-/api/dataentities/-dataEntityName-/search)

### Best practices

When using the search endpoint, these best practices will help enhance your data retrieval process:

* **Apply filters to narrow your search**: Improve performance by reducing the number of documents returned. This speeds up the query and ensures that your requests are more efficient.
* **Use exact values for queries instead of wildcards (`*`):** Heavy usage of wildcards may be subject to temporary blocks.
* **Avoid large datasets:** If you are querying many documents, break your query into smaller intervals.

>ℹ Learn more about [Search pagination in the Master Data API](https://developers.vtex.com/docs/guides/pagination-in-the-master-data-api#search-pagination).

## Scroll

The scroll route is designed for extensive data retrieval, especially when integrating Master Data with external systems. It is the best choice if you need to query the entire database or when dealing with over 10000 documents.

See the Scroll endpoint reference depending on the Master Data version you are using:

* [Master Data API v1 - Scroll](https://developers.vtex.com/docs/api-reference/masterdata-api#get-/api/dataentities/-acronym-/scroll)  
* [Master Data API v2 - Scroll](https://developers.vtex.com/docs/api-reference/master-data-api-v2#get-/api/dataentities/-dataEntityName-/scroll)

Your first scroll request will return a token in the `X-VTEX-MD-TOKEN` response header. Inform this value in the `_token` query parameter for your next requests until you receive an empty list, indicating that all documents have been retrieved.

>ℹ Learn more about [Scroll pagination in the Master Data API](https://developers.vtex.com/docs/guides/pagination-in-the-master-data-api#scroll-pagination).

### Scroll best practices

To ensure efficient and reliable data retrieval, follow these strategies when using the scroll endpoint:

* **Implement filters to divide the request into smaller batches,** reducing the likelihood of timeouts. For example, you might filter by creation date and process data month by month. Smaller batches are also easier to reprocess if a timeout occurs, making your operation more resilient.  
* **Run up to 10 scrolls simultaneously per account.** Limiting the number of parallel scrolls helps prevent errors and timeouts. By using filters to create smaller batches and parallelizing these batches in a controlled manner, you can speed up data retrieval while reducing the risk of overloading the account.

>⚠️ **Scroll behavior and limitations**
>
> * **Each scroll operation allows only one query for the duration of the token.** This means that you cannot change a scroll’s query by changing parameters after the first request: you can navigate pages of the original first request until the token expires, or initiate other scrolls (up to 10 simultaneously).
> * If Master Data stops receiving requests with the scroll `X-VTEX-MD-TOKEN` token, it will expire in **20 minutes**. After that, you can make new scroll requests, limited to 10 simultaneous scrolls.
> * The maximum number of documents per scroll request is **1000**.
