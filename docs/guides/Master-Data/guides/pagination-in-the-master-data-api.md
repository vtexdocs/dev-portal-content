---
title: "Pagination in the Master Data API"
slug: "pagination-in-the-master-data-api"
hidden: true
createdAt: "2024-09-06T18:10:15.623Z"
updatedAt: "2024-09-06T18:10:15.623Z"
---

When working with the Master Data API, whether you're using v1 or v2, you may need to handle a large volume of data. Pagination breaks down these large datasets into smaller, manageable parts. This guide will walk you through using pagination in the search and scroll endpoints in the Master Data API.

>ℹ️ Learn more about [Extracting data from Master Data](https://developers.vtex.com/docs/guides/search-and-scroll-api-queries) using the search and scroll endpoints.

## Search pagination

When using the search endpoint, the results are paginated by specifying a range in the `REST-Range` header. This method allows you to define the subset of documents you want to retrieve from the dataset.

See the search endpoint reference according to the Master Data version you are using:

* [Master Data API v1 - Search](https://developers.vtex.com/docs/api-reference/masterdata-api#get-/api/dataentities/-acronym-/search)
* [Master Data API v2 - Search](https://developers.vtex.com/docs/api-reference/master-data-api-v2#get-/api/dataentities/-dataEntityName-/search)

### Setting up pagination

To paginate your results using the search endpoint, include the `REST-Range` header in your request. The value of this header should follow the format: `resources={x}-{y}`.

* **`x`**: The index of the first document in the returned array.
* **`y`**: The index of the last document in the returned array + 1.

For example, `resources=0-100` would return the first 100 documents from index 0 to 99. Note that you are limited to retrieving 100 documents per query.

>ℹ When paginating, the `_sort` parameter is recommended. The API by itself does not guarantee order, so without a defined `_sort`, documents may return duplicate or not return at the expected page.

### Retrieving subsequent pages

To retrieve the next set of results, adjust the `x` and `y` values accordingly. For example, to get the next 100 documents after the first set, your `REST-Range` header would look like this: `resources=100-200`.

### Checking if more pages are available

The `REST-Content-Range` response header provides information about the range of documents returned in the current response and the total number of documents available. It follows this format: `resources={x}-{y}/{total}`.

* **`x`**: The index of the first document in the returned array.
* **`y`**: The index of the last document in the returned array + 1.
* **`total`**: The total number of documents that match the query.

For example, `resources=0-100/250` indicates that the response contains documents from index 0 to 99 out of 250. If `y` is less than `total`, you can retrieve more pages.

## Scroll pagination

The scroll endpoint is used when you need to retrieve a large dataset that might exceed the typical pagination limits since it allows you to retrieve up to 1000 documents per request.

See the scroll endpoint reference according to the Master Data version you are using:

* [Master Data API v1 - Scroll](https://developers.vtex.com/docs/api-reference/masterdata-api#get-/api/dataentities/-acronym-/scroll)
* [Master Data API v2 - Scroll](https://developers.vtex.com/docs/api-reference/master-data-api-v2#get-/api/dataentities/-dataEntityName-/scroll)

### Setting up pagination

Pagination with the scroll endpoint is managed using three parameters:

* `_size`: Specifies the number of documents returned per request. The maximum value is 1000.
* `_token`: A unique token returned in the `X-VTEX-MD-TOKEN` header of the first request. This token is passed as a query parameter in subsequent requests to retrieve the next page of results. It expires in 20 minutes.
* `_page`: Specifies the page to retrieve.

In the initial request, you should only use `_size` to determine the number of results per page, as you will obtain the `_token` value in the  `X-VTEX-MD-TOKEN` response header.

Example of an initial request:

`GET /api/dataentities/{data_entity}/scroll?_size={page_size}`

>ℹ️ You can only define the page size in the first request. It cannot be changed in subsequent requests.

To obtain the next pages, you can choose between retrieving subsequent pages or retrieving a specific page. See details about each option in the following sections.

### Retrieving subsequent pages

Use the `X-VTEX-MD-TOKEN` header returned from the previous request as the `_token` query parameter in your next request to retrieve the subsequent pages. You can repeat this request until the response body is empty, indicating that there are no more documents to retrieve.

Subsequent requests to retrieve additional pages:

`GET /api/dataentities/{data_entity}/scroll?_token={X-VTEX-MD-TOKEN}`

### Retrieving specific pages

In case you want to specify the page to retrieve, include the `_page` query parameter. This is useful when you need direct access to a particular page without sequentially navigating through all prior pages.

Request to retrieve a specific page:

`GET /api/dataentities/{data_entity}/scroll?_token={X-VTEX-MD-TOKEN}&_page={page_number}`

### Checking if more pages are available

The `REST-Content-Total` response header provides the total number of documents that match your query, allowing you to calculate the number of pages available based on the `_size` parameter.

For example, if the response header is `REST-Content-Total: 5000` and you are retrieving 1000 documents per page (`_size=1000`), you know that there are 5 pages of data available.

You can use this information to determine if there are more pages to retrieve and to set up logic in your application to continue retrieving data until all pages are processed.
