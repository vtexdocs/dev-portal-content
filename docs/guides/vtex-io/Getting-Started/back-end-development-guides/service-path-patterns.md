---
title: "Service path patterns"
slug: "service-path-patterns"
excerpt: "Learn how to define the path for your VTEX IO service route to manage caching and session data effectively."
hidden: false
---

When developing a new [VTEX IO service](https://developers.vtex.com/docs/guides/vtex-io-documentation-service), you must define a proper path for your service to handle requests effectively. This guide provides insights into service path patterns, outlining the recommended approaches based on the desired behavior.

Paths are specified within the `service.json` file. Check the following example:

```json service.json mark=7:11
{
  "memory": 256,
  "ttl": 10,
  "timeout": 2,
  "minReplicas": 2,
  "maxReplicas": 4,
  "routes": {
    "status": {
      "path": "/_v/status/:code",
      "public": true
    }
  }
}
```

For more information on developing service apps, refer to [Developing services](https://developers.vtex.com/docs/guides/developing-services-on-vtex-io).

## Path patterns

There are three possible path formats, each influencing the behavior of your service.

Let's delve into these patterns using an illustrative example of implementing the service `/examplepath/123`. You can change how VTEX handles requests to this service by appending `/_v/segment` or `/_v/private` to the beginning of your path. This means you have three possible paths in this example:

- **Public:** `/examplepath/123`
- **Segment dependent:** `/_v/segment/examplepath/123`
- **Private:** `/_v/private/examplepath/123`

VTEX has an edge layer that handles all requests to the platform, including those related to VTEX IO apps. Given this architecture, each of these possible paths is handled differently in terms of caching and cookie management. Refer to the [Sessions System](https://developers.vtex.com/docs/guides/sessions-system-overview) guide to learn more about how VTEX handles cookies.

Check the table below for a comprehensive overview of the behavior of different path patterns:

| **Path type**     | **Pattern**              | **Cookies behavior**                                                                                                                                                                                                                                | **Caching behavior**                                                        | **Example use case**                                                                                                                             |
|-------------------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Public            | `{yourPath}`             | No guarantee that the app will receive the cookies from the request.                                                                                                                                                                           | VTEX edge will cache the service's response whenever possible.       | Retrieving information that does not vary according to user or segment, such as product images.                                                  |
| Segment dependent | `/_v/segment/{yourPath}` | The app will receive the [`vtex_segment` cookie](https://developers.vtex.com/docs/guides/sessions-system-overview#cookie-vtexsegment)                                                                                                                | VTEX edge will cache the service's response based on the received segment. | Retrieving information that may change depending on the segment. For instance, applying promotions according to the shopper's selected currency. |
| Private           | `/_v/private/{yourPath}` | The app will receive both the [`vtex_segment`](https://developers.vtex.com/docs/guides/sessions-system-overview#cookie-vtexsegment) and [`vtex_session`](https://developers.vtex.com/docs/guides/sessions-system-overview#cookie-vtexsession) cookies. | VTEX will not cache the service's response.                                | Retrieving information depending on the shopper's identity or session, such as the shopper's order history or registered address.       |

## Troubleshooting

### Unavailable cookies with CloudFront CDN

If your store uses CloudFront as a CDN and you encounter difficulties in obtaining the expected cookies from the app’s service context, [open a ticket](https://help.vtex.com/en/tutorial/opening-tickets-to-vtex-support--16yOEqpO32UQYygSmMSSAM) with the VTEX support team to report the issue.
