---
title: "Avoiding CORS in Master Data requests"
slug: "avoiding-cors-in-master-data-requests"
excerpt: "Learn how to avoid CORS issues in your Master Data requests."
hidden: false
createdAt: "2021-10-13T19:45:36.960Z"
updatedAt: "2022-08-03T13:35:59.361Z"
---

Cross-origin resource sharing (CORS) is not an error but a security mechanism designed to protect users from dangerous Javascript and unwarranted HTTP requests.

CORS is triggered when an HTTP endpoint requests:

- a different domain (e.g., `vtex.com` calls `vtexcommercestable.com`)
- a different subdomain (e.g., `store.com` calls `blog.store.com`)
- a different port (e.g., `store.com` calls `store.com:3001`)
- a different protocol (e.g., a site at `https://store.com` calls `http://store.com`)

Your browser blocks every request that fits into one of the four conditions above. This might cause unexpected site behavior and frustration as some functionality may stop functioning.

Furthermore, whenever the browser has to check if the backend supports CORS, an additional `OPTION` request is sent back to **Master Data**. Improperly configured websites generate a great deal of these avoidable requests.

## Best practices

This section will cover best practices for using **Master Data** API endpoints. These practices will help you create more efficient and maintainable code.

|✅ Do|❌ Don't|
|---|----|
|`$.getJSON("/foobar/dataentities/SL/search?_....`|`https://account.vtexcommercestable.com.br/api/dataentities/SL/search`|

To perform Master Data entity searches correctly, opt for relative paths, as demonstrated in the jQuery example. This approach simplifies your code by eliminating the need to include account names and environments in each request.

Do not make direct requests to **Master Data** endpoints, and avoid including account names and environments directly in the endpoint.

