---
title: "Avoiding CORS in your MasterData requests"
slug: "avoiding-cors-in-your-masterdata-requests"
hidden: false
createdAt: "2021-10-13T19:45:36.960Z"
updatedAt: "2022-08-03T13:35:59.361Z"
---
Cross-origin resource sharing (CORS) is not an error but a security mechanism designed to protect users from dangerous Javascript and unwarranted HTTP requests

CORS is triggered when an HTTP endpoint requests: 

- a different domain (e.g., vtex.com calls vtexcommercestable.com)
- a different subdomain (e.g., store.com calls blog.store.com)
- a different port (e.g., store.com calls store.com:3001)
- a different protocol (e.g., a site at https://store.com calls http://store.com)

Your browser blocks every request that fits into one of the four conditions above, this might cause unexpected site behavior and general frustration as some functionality might cease to function.

Furthermore, whenever the browser has to check if the backend supports cross-origin resource sharing, an additional `OPTION` request is sent back to Master Data.  Improperly configured websites generate a great deal of these avoidable requests.

## Incorrect example

Direct request to Master Data path:
```
https://account.vtexcommercestable.com.br/api/dataentities/SL/search
```
Notice how the account name and environment are part of the endpoint.


## Correct example

Below is a JQuery example of correctly searching a Master Data entity using a relative path.
```
$.getJSON("/foobar/dataentities/SL/search?_....
```
Notice how the account name and environment are omitted.