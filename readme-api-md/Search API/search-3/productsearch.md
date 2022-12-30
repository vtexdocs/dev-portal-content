---
title: "Search for Products"
slug: "productsearch"
excerpt: "Retrieves general information about the products related to the term searched. \r\nThis is the main search used by the store. The user can type anything to be searched.  \r\n\r\nFor example, if they search for a \"decanter\", this is the URL: `https://{{accountName}}.{{environment}}.com.br/api/catalog_system/pub/products/search/decanter`. \r\n\r\nNote that maybe the response can be HTTP 200 or 206, 206 means that it's a partial content response.\r\n\r\nIf it is a 206 take a look at the Headers, will be an entry called resources. E.g.: resources → 0-9/19. This means that the response is showing items from 0 to 9, 10 items, but there were 19 items found. See more information at the paging route example."
hidden: false
createdAt: "2019-12-30T03:21:07.203Z"
updatedAt: "2022-12-01T21:50:13.597Z"
---
