---
title: "Consult store search terms information"
slug: "consult-store-search-terms-information"
hidden: false
createdAt: "2022-10-14T21:11:36.747Z"
updatedAt: "2022-11-02T14:39:45.843Z"
---

To present great search results to your customer, it is essential to understand how they search for products in your store. You can use the [Intelligent Search API](https://developers.vtex.com/vtex-rest-api/reference/intelligent-search-api-overview), as detailed in the following sections, to gather [the most popular search terms](#get-the-most-searched-terms) and [autocomplete suggestions](#get-autocomplete-suggested-terms-and-similar-attributes).

## Get the most searched terms

To get your customers' most searched terms, you must use the [Get list of the 10 most searched terms](https://developers.vtex.com/vtex-rest-api/reference/get_top-searches) endpoint. You can filter the endpoint response by defining the term's `locale` on the query.

![Example of most searched terms on a store](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Search/consult-store-search-terms-information-0_14.png)

The response will return the most searched terms by popularity order and the number of searches for each term.

**Response body example**

```json
{
  "searches": [
    {
      "term": "home",
      "count": 14
    },
    {
      "term": "shirt",
      "count": 10
    },
    {
      "term": "top",
      "count": 9
    },
    {
      "term": "tops",
      "count": 6
    },
    {
      "term": "camera",
      "count": 5
    },
    {
      "term": "kit",
      "count": 5
    },
    {
      "term": "work shirt",
      "count": 2
    },
    {
      "term": "shirts",
      "count": 2
    },
    {
      "term": "clothing",
      "count": 2
    },
    {
      "term": "classic shoes",
      "count": 1
    }
  ]
}
```

## Get autocomplete suggested terms and similar attributes

To get information about the [autocomplete](https://developers.vtex.com/vtex-developer-docs/docs/vtex-search-autocomplete) suggested terms and similar attributes presented to your customers, use the [Get list of suggested terms and attributes similar to the search term](https://developers.vtex.com/vtex-rest-api/reference/get_autocomplete-suggestions) endpoint. You can filter the endpoint response by defining the term's `locale` and `query`.

![Example of autocomplete suggested terms and similar attributes](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Search/consult-store-search-terms-information-1_71.png)

The response will return the searched terms by popularity order and the corresponding autocomplete suggestions for each term.

**Response body example**

```json
{
  "searches": [
 {
   "term": "tv",
   "count": 28861,
   "attributes": [
     {
       "key": "departamento",
       "value": "tvs-e-video",
       "labelKey": "Departamento",
       "labelValue": "TVs e Vídeo"
     },
     {
       "key": "categoria",
       "value": "tvs",
       "labelKey": "Categoria",
       "labelValue": "TVs"
     },
     {
       "key": "subcategoria",
       "value": "receptor-de-controle-de-acesso",
       "labelKey": "Subcategoria",
       "labelValue": "Receptor de Controle de Acesso"
     }
   ]
 },
 {
   "term": "smarth tv",
   "count": 2308
 },
 {
   "term": "painel para tv",
   "count": 975
 },
 {
   "term": "rack tv",
   "count": 589
 }
  ]
}
```
