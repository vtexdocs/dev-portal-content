---
title: "Best practices for avoiding rate limit errors"
slug: "best-practices-for-avoiding-rate-limit-errors"
createdAt: "2023-01-28T23:12:53.108Z"
updatedAt: "2023-11-28T13:19:52.868Z"
hidden: false
excerpt: "Learn how to responsibly manage rate limits for fair and reliable usage of VTEX Core Commerce APIs."
seeAlso:
    - "/docs/api-reference"
    - "/docs/guides/api-response-codes"
    - "/docs/guides/handling-errors-and-exceptions"
    - "/docs/guides/vtex-io-documentation-engineering-guidelines"
---

Rate limits serve as crucial control mechanisms for managing the volume and frequency of requests made to an API. Exceeding these limits can lead to disruptions in service and a temporary suspension of access to [VTEX Core Commerce APIs](https://developers.vtex.com/docs/api-reference). This article delves into the best practices for responsibly dealing with rate limits while ensuring your apps and store code adhere to ethical and responsible digital practices.

## Implement efficient data retrieval techniques

Implementing efficient data retrieval techniques is pivotal in optimizing system performance and ensuring seamless operations. This section delves into the best practices for minimizing resource usage while maximizing the efficiency of [VTEX IO apps](#vtex-io-apps) and [Storefront implementations](#storefront-implementation).

### VTEX IO apps

When developing VTEX IO apps, it is generally advised to avoid direct API communication in favor of implementing dedicated [Clients](https://developers.vtex.com/docs/guides/vtex-io-documentation-clients). VTEX IO Clients come equipped with several built-in features that enhance the functionality and performance of your apps:

* **Cache:** Clients come equipped with efficient caching mechanisms that store and retrieve data, reducing the strain on services and improving response times.
* **Native metrics support:** Clients integrate with performance monitoring and analytics tools, providing insights into service usage and performance.
* **Retry and timeout options:** Clients offer flexible configurations for retries and timeout, ensuring the robustness and resilience of your app when confronted with network issues or service unavailability.
* **Billing tracking:** Clients can track usage and resource consumption, aiding in billing and cost optimization.

Note that VTEX offers a selection of native Clients within the `@vtex/clients` library, streamlining the interaction with services like VTEX Core Commerce APIs and other internal resources. However, if your VTEX IO app requires integration with external services not covered by the  `@vtex/clients` library, you can employ the  `@vtex/api` to harness type support and develop your own custom clients.

### Storefront implementation

We strongly advise the adoption of GraphQL in storefront implementations as it offers various advantages, particularly in avoiding potential rate-limit errors. GraphQL allows developing applications that precisely request and receive only the necessary data to fulfill the frontend. This ability is key in reducing over-fetching and minimizing the data transferred, effectively alleviating the burden on API endpoints. Additionally, by aggregating multiple data requirements into a single request, GraphQL streamlines the data retrieval process, optimizing efficiency and decreasing the number of necessary requests for a given operation.

To leverage these capabilities, check our specialized [frontend solutions](https://help.vtex.com/tracks/store-development--3fHF3GIjK8UugnQKIakpl9/5DTcawNjc5MovtD7HNqURl) designed to harness the benefits of GraphQL.

## Cache data

Caching can play a crucial role in helping applications manage rate limits more effectively. Instead of always retrieving the data through a new request to VTEX Core Commerce APIs, this strategy retrieves data from a cache, which is usually a faster storage medium. By avoiding repeated queries to external APIs, the request volume decreases.

To effectively implement data caching and reduce the need for repeated API requests, consider the following:

* **Identify cacheable data:** Determine which data can benefit from caching. Typically, this includes data that is frequently read and relatively static.
* **Select a cache server close to the client:** Select a cache server close to the client so data can be retrieved with lower latency and faster response times. Note that the physical distance between the client and cache server plays a significant role in determining data retrieval speed.
* **Set expiry times:** Define how long data should be cached before it is considered stale. You may set it as cacheable for minutes, days, or longer.
* **Implement strategies for cache invalidation:** Implement strategies for cache invalidation, which ensure that the cache is updated when the underlying data changes.

## Prioritize requests

Some requests may be more critical than others. Prioritize essential requests over non-essential ones. This can be achieved by implementing a queue system or distinguishing between high and low-priority requests.

The business logic of your app or integration often dictates the importance of certain operations. For example, operations initiated by user interactions, like submitting a form, usually take precedence over background tasks.

* **Define priority levels:** Establish a hierarchy of request priority levels. For example, high, medium, and low.
* **Categorize requests:** Assign each request a priority level based. Consider the following:
  * **Business logic:** Identity requests crucial for core business functions, such as checkout processes, account management, or high-traffic pages.
  * **User interactions:** Prioritize requests that directly affect user experience, like loading times for key pages or features.
  * **Service Level Agreements (SLAs):** Ensure priority levels align with SLAs, giving precedence to requests stipulated in high-priority agreements.
  * **Interdependencies:** Consider the impact of delaying certain requests on subsequent actions or dependent processes.
* **Implement a queue system:** Use a queue or scheduling mechanism to manage and execute requests based on their priority.
* **Handle errors and exceptions:** Ensure that error handling takes into account request priority. For high-priority requests, implement more aggressive error recovery strategies.

### Example

Suppose that, during a sale event, a store starts experiencing a surge in traffic. To safeguard the user experience and ensure that critical functions remain accessible, the store employs a strategy of prioritizing incoming requests.

During this period, requests are categorized and handled with a deliberate focus on user needs and performance. For example, checkout requests are granted the highest priority. The store ensures that these requests are processed without any undue delays, allowing customers to successfully complete their purchases.

In contrast, non-essential features, such as social sharing options, are granted the lowest priority, meaning these features may be temporarily deprioritized or even disabled. By applying this prioritization approach, the store assures that critical functions are available to users without interruption, even during peak traffic.

## Implement optimized retries with exponential backoff

Proactively manage your requests by avoiding unnecessary or excessive API calls. Excessive API calls can degrade your app's performance, increasing response times. If the service responds with rate limit exceeded errors, consider implementing exponential backoff, which gradually increases the delay between retry attempts to reduce the load on the service.
