---
title: "Search for products"
slug: "productsearch"
excerpt: "Retrieves general information about the products related to the term searched."
hidden: false
createdAt: "2019-12-30T03:21:07.203Z"
updatedAt: "2021-08-31T18:21:45.713Z"
---
This is the main search used by the store. The user can type anything to be searched.  

For example, if they search for a "decanter", this is the URL:
[block:code]
{
  "codes": [
    {
      "code": "https://{{accountName}}.{{environment}}.com.br/api/catalog_system/pub/products/search/decanter",
      "language": "text"
    }
  ]
}
[/block]
Note that maybe the response can be HTTP 200 or 206, 206 means that it's a partial content response.

If it is a 206 take a look at the Headers, will be an entry called resources  
Ex.: resources → 0-9/19  
This means that the response is showing items from 0 to 9, 10 items, but there were 19 items found. See more information at the paging route example.