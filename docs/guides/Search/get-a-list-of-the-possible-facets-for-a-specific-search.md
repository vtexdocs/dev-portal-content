---
title: "Get a list of the possible facets for a specific search"
slug: "get-a-list-of-the-possible-facets-for-a-specific-search"
hidden: false
createdAt: "2023-03-13T21:11:36.747Z"
updatedAt: "2022-11-02T14:39:45.843Z"
---

Facets represent the combination of filters that are selected in a search. To retrieve a list of possible facets for a specific search, use the [Get list of the possible facets for a given query](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/facets/-facets-) endpoint. You can filter the endpoint response by defining the search's `facets` and the term's `locale` and `query`.

A facet value is only returned in the response if at least one of the products returned in the query has this value.

All information is synced with the Catalog. Therefore, if a specification is configured non-filterable, it will not be returned by the Search API.

**Response body example:**

```json
{
  "facets": [
    {
      "type": "TEXT",
      "name": "string",
      "hidden": false,
      "quantity": 0,
      "values": [
        {
          "id": "string",
          "quantity": 0,
          "name": "string",
          "key": "string",
          "value": "string",
          "selected": false
        }
      ]
    }
  ],
  "sampling": false,
  "breadcrumb": [
    {
      "name": "string",
      "href": "string"
    }
  ],
  "queryArgs": {
    "query": "string",
    "selectedFacets": [
      {
        "key": "string",
        "value": "string"
      }
    ]
  }
}
```
