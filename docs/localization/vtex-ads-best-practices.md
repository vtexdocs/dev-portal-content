---
title: "VTEX Ads best practices"
slug: "vtex-ads-best-practices"
excerpt: "Learn best practices for integrating with the VTEX Ads API to ensure optimal performance and reliability."
hidden: false
createdAt: "2025-10-13T00:00:00.000Z"
updatedAt: "2025-10-13T00:00:00.000Z"
---
To optimize integration performance with the VTEX Ads API, implement the following practices.

## HTTP persistence

For server-side integrations, use persistent HTTP connections to minimize connection overhead per API request.

HTTP connection reuse allows multiple requests to share the same TCP connection, eliminating the performance cost of establishing and tearing down connections for each request. This approach prevents network resource degradation during high-traffic periods on both client and server sides.

The following diagram illustrates the performance difference between multiple connections and persistent connections:

![vtex-ads-best-practices](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX%20Ads/getting-started-with-vtex-ads-api/vtex-ads-best-practices.png)

To implement HTTP persistence, configure your HTTP client to include the following header:

```curl
Connection: keep-alive
```

This header instructs the client to maintain the connection for subsequent requests from the same origin.

> ℹ️ Learn more about HTTP persistence in the [Mozilla Developer documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Connection_management_in_HTTP_1.x). 

## Timeout implementation

While the VTEX Ads API maintains high availability standards, network conditions and processing loads can affect response times. Extended response delays may degrade user experience during ad display.

Implement request timeouts between 500-600ms for all VTEX Ads API calls to maintain optimal performance. This range balances response time requirements with network variability considerations.
