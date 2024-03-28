---
title: "Querying documents in Master Data v1"
slug: "querying-documents-in-master-data-v1"
hidden: false
createdAt: "2022-08-09T22:09:42.358Z"
updatedAt: "2022-08-09T22:09:42.358Z"
---
There are two ways to search for Master Data v1 documents:

* [Query a specific document by ID](#query-by-document-id)
* [Query a collection of documents](#query-a-collection-of-documents)

## Query by document ID

The ID is the most efficient reference to the exact storage address, so this type of query is the fastest way of recovering data. We recommend using the `GET` [Get document](https://developers.vtex.com/docs/api-reference/masterdata-api#get-/api/dataentities/-acronym-/documents/-id-) endpoint to retrieve a document by its ID.

## Query a collection of documents

In this type of search, the fields marked as **Is searchable?** or **Is filterable?** and the fields set as [indices](https://help.vtex.com/en/tutorial/setting-up-an-index-on-master-data--tutorials_785) in Master Data v1 data entity settings determine results. But they are not the only ones you should use. The **indices** are also part of this process. The best way of understanding the flow of this type of search is to look at an example.

In the example below, there is a data entity called `Client`, with the `CL` acronym, configured as follows:

| Field name | Type | **Is filterable?** |  **Is searchable?** |
| - | - | - | - |
| Email | Email | Yes | Yes |
| Name | Varchar 100 | No | Yes |
| Age | Integer | Yes | No |
| Size | Varchar 10 | No | No |

### Is filterable?

The **Is filterable?** attribute indicates that we can use a filter via a specific field or fields. Following the example, we can filter through the fields `Email` and `Age`.

Using the `GET` [Search documents](https://developers.vtex.com/docs/api-reference/masterdata-api#get-/api/dataentities/-acronym-/search) endpoint of [Master Data API - v1](https://developers.vtex.com/docs/api-reference/masterdata-api), we can make the following queries:

* Filter by `Email`: `/dataentities/CL/search?Email=meuemail@provider.com`
* Filter by `Age`: `/dataentities/CL/search?Age=18`

If a filter is used in the `Name`, field, which is not marked as a filter, the answer will be `Bad Request` indicating that the `Name` field is not configured as a filter.

### Is searchable?

The attribute **Is searchable?** indicates that we can search this field's values via the `_keyword` attribute in the `GET` [Search documents](https://developers.vtex.com/docs/api-reference/masterdata-api#get-/api/dataentities/-acronym-/search) endpoint of [Master Data API - v1](https://developers.vtex.com/docs/api-reference/masterdata-api).

The `_keyword` would be used, for example, to retrieve all the documents containing the value `mary`.

In this case, the API path would be: `/dataentities/CL/search?_keyword=maria`

Asterisks are indicators for a partial query. In other words, documents with the exact value `mary`, will not be searched for, but only those showing this group of characters somewhere.

The result of this query would return documents with values such as the following in the attributes `Name` and `Email`: `Name=Mary Lee | Email=mary@mail.com`.

### Indices

An [index](https://help.vtex.com/en/tutorial/setting-up-an-index-on-master-data--tutorials_785) works as a shortcut to find documents. Using this resource, the query is quicker than with a normal filter or keyword search.

However, the greater the number of indexes, the more slowly documents are written. The use of the index is recommended for search results of up to 1 thousand documents.

Queries by indexes can be made through the `GET` [Search documents](https://developers.vtex.com/docs/api-reference/masterdata-api#get-/api/dataentities/-acronym-/search) endpoint. In the search flow, when Master Data interprets a query, it checks if the filter is part of an index and, if so, the search is done through the index.

### Reindexing

Master Data reindexing is a background process that works as follows:

1. It reads the configurations of fields marked as **Is filterable?** and **Is searchable?**.
2. It updates the search engine with the new fields.
3. It searches all stored documents and updates the values in the search engine.

When the fields of a document are written in the search engine, it means this document is indexed.

This process only happens when fields marked as **Is filterable?** or **Is searchable?** are changed.
