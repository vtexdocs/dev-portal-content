---
title: "Improving product discovery with autocomplete suggestions and search insights"
slug: "consult-store-search-terms-information"
hidden: false
createdAt: "2022-10-14T21:11:36.747Z"
updatedAt: "2022-11-02T14:39:45.843Z"
---

To deliver relevant search results to your store's shoppers, it's essential to understand how they search for products in your store. The [Intelligent Search API](https://developers.vtex.com/docs/api-reference/intelligent-search-api#overview) offers powerful insights into [popular search terms](#get-the-most-searched-terms) and [autocomplete suggestions](#get-autocomplete-suggested-terms-and-similar-attributes). The sections below outline how to utilize these tools to optimize your store's search experience.

## Retrieving the most searched terms

To identify the terms your customers search for most frequently, use the [Get list of the 10 most searched terms](https://developers.vtex.com/vtex-rest-api/reference/get_top-searches) endpoint. This endpoint allows you to filter results by specifying a `locale` in the query parameters.

The response will return the most searched terms in order of popularity along with the number of searches:

![Example of most searched terms on a store](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/consult-store-search-terms-information-0.png)

### Response body example

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

## Retrieving autocomplete suggested terms and similar attributes

To gather data on [autocomplete suggestions](https://developers.vtex.com/docs/guides/vtex-search-autocomplete) and similar attributes, use the [Get list of suggested terms and attributes similar to the search term](https://developers.vtex.com/vtex-rest-api/reference/get_autocomplete-suggestions) endpoint. You can refine the response by defining the `locale` and `query` parameters.

The response will return the searched terms by popularity order and the corresponding autocomplete suggestions for each term.

![Example of autocomplete suggested terms and similar attributes](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/consult-store-search-terms-information-1.png)

### Response body example

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
