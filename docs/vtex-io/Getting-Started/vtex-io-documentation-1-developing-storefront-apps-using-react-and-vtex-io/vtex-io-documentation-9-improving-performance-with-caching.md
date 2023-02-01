---
title: "8. Improving performance with caching"
slug: "vtex-io-documentation-9-improving-performance-with-caching"
hidden: false
createdAt: "2021-03-25T20:58:43.052Z"
updatedAt: "2022-12-13T20:17:44.240Z"
category: "App Development"
seeAlso:
 - "/docs/guides/vtex-io-documentation-10-making-your-app-publicly-available"
---

Repeated searches for similar data can become an expensive and frustrating investment as they require a high number of responses from the server to deliver the requested information.

That is why the **ability to use *cache* and reuse data previously obtained on the server can be a critical point for optimizing your front app's performance and, consequently, your website**.

The VTEX IO development platform already applies advanced *cache* techniques to the [Store Framework](https://developers.vtex.com/docs/guides/getting-started-3) using the Apollo *cache* as a search and data management solution capable of interacting with VTEX's GraphQL services.

We highly recommended using the [Apollo solution](https://www.apollographql.com/docs/react/caching/cache-configuration/) in your app and, that way, define your own *cache* strategies that mold to the business scenario that applies to your store.

![React Apollo overview](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-9-improving-performance-with-caching-0.jpeg)

Once implemented, the solution operates without major configurations: two GraphQL *requests* with the same *query* and variables reach the server only once for data collection.

You can read about [Apollo usage rules and policies](https://medium.com/@galen.corey/understanding-apollo-fetch-policies-705b5ad71980) to understand more about possible data collection scenarios using this solution.

For example, if you use the `cache-and-network` rule, you will be able to immediately return the requested data if it is *cached* and still query the server to confirm if any data has been changed since then.
