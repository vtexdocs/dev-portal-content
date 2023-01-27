---
title: "How the queries in Master Data v1 work"
slug: "how-the-queries-in-master-data-v1-work"
hidden: false
createdAt: "2022-08-09T22:09:42.358Z"
updatedAt: "2022-08-09T22:09:42.358Z"
---
The VTEX Master Data can be extended to configure fields such as **Buscável** or **Filtro**. But what do these settings mean? The purpose of this article is to answer this question.

First we will describe the flow of searches. There are two types:

1. Query by the ID;
2. Query a collection of documents.

## Query by the ID

This type of query is the quickest way of recovering data. The ID is the most efficient reference to give us the exact storage address.
_We suggest you always use the attribute **id**. It will always be quicker than any other method of querying the VTEX Master Data._

## Query a collection of documents

In this type of search the fields marked **Buscável** or **Filtro** are important. But they are not the only ones you should use. The **índices** are also part of this process. The best way of understanding the flow of this type of search is to look at an example.

In our example, we have the data entity `Cliente`, code `CL`. It is configured as follows:

| Nome do campo     | Tipo     | é filtro     | é buscável     |
| ---------- | ---------- | ---------- | ---------- |
| Email       | Email       | Sim       | Sim       |
| Nome       | Varchar 100       | não       | sim       |
| Idade       | Integer       | sim       | não       |
| TamanhoRoupa       | Varchar 10       | não       | não       |


## É filtro

The attribute `é filtro` indicates that we can use a filter via a specific field or fields. In our example, we can filter through the fields `Email` and `Idade`.

In the API, we can make the following query using the `search` path:

1. `/dataentities/CL/search?Email=meuemail@provider.com`
2. `/dataentities/CL/search?Idade=18`

If a filter is used in the `Nome`, field, which is not marked as a filter, the answer will be `Bad Request` indicating that the `Nome` field is not configured for a filter.

## É buscável

The attribute `é buscável` indicates that we can search via the `_keyword` attribute in the `search`. path. The `_keyword` is used in the follow circumstances: “I want all the documents containing the value `maria`.&#8221;

The API call, in this case will be:

`/dataentities/CL/search?_keyword=maria`

The asterisks are indicators for a partial query. In other words, documents with the exact value `maria`, will not be searched for, but only those showing this group of characters somewhere.

The result of this query would give documents with values such as the following in the attributes `Nome` and `Email`: Nome=Maria Joaquina | Email=maria@provider.com.

## Query by indexes

The index is a feature of VTEX Master Data which works as a shortcut to find documents. It does not use the search engine (technology used for queries with filters, fulltext search and aggregation).

Using this feature, the query is quicker than with a normal filter. However, the greater the number of indexes, the more slowly documents are written. Always make sure that the writing and reading process in your model is as efficient as possible in resolving problems.

Queries by indexes are made via the `search`. path. In the search flow, when the VTEX Master Data is interpreting a query, it asks the following question:

`Esse filtro compõe um índice?`

If the answer is yes (the filter is part of an index), the search is done through the index.

## Reindexing

Reindexing is a background process that works as follows:

1. It reads the configurations of fields marked as `Filtro` and `Buscável`;
2. It updates the search engine with the new fields;
3. It searches all stored documents and updates the values in the search engine.

When the fields of a document are written in the search engine, we say that this document is indexed. This is why we talk about “reindexing”.

_Note that this feature only works in cases where fields marked as `é filtro` or `é buscável` are changed._