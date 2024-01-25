---
title: "Service path patterns"
slug: "service-path-patterns"
hidden: false
---

When developing a new [VTEX IO service](https://developers.vtex.com/docs/guides/vtex-io-documentation-service), you must define a path so that the service is available to receive requests.


In this article, you will learn about the pattern for service paths according to the desired behavior. To know more about how to implement the path in your app's code, check the guide [Developing service configuration apps](https://developers.vtex.com/docs/guides/vtex-io-documentation-developing-service-configuration-apps).


## Path patterns


There are three possible path formats, depending on the behavior you wish for your service.


For the purpose of this tutorial, consider you are implementing the service `/examplepath/123`. You may change how VTEX handles requests to this service by adding `/_v/segment` or `/_v/private` to the beginning of your path. This means you have three possible paths in this example:


- **Public:** `/examplepath/123`
- **Segment dependant:** `/_v/segment/examplepath/123`
- **Private:** `/_v/private/examplepath/123`


VTEX has an edge layer that handles all requests to the platform, including those related to VTEX IO apps. Given this architecture, each of these possible paths is handled differently in terms of caching and cookie management. Refer to the [Sessions System](https://developers.vtex.com/docs/guides/sessions-system-overview) guide to learn more about how VTEX handles cookies.

Check the table below for a comprehensive overview of the behavior of different path patterns:

>⚠️ Custom endpoints must follow the same path patterns to access cookies.

| **Path type**     | **Pattern**              | **Cookies behavior**                                                                                                                                                                                                                                | **Caching behavior**                                                        | **Example use case**                                                                                                                             |
|-------------------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Public            | `{yourPath}`             | There is no guarantee your app will receive the cookies from the request.                                                                                                                                                                           | VTEX edge will cache your service's response whenever it is possible.       | Retrieving information that does not vary according to user or segment, such as product images.                                                  |
| Segment dependant | `/_v/segment/{yourPath}` | Your app will receive the [vtex_segment cookie](https://developers.vtex.com/docs/guides/sessions-system-overview#cookie-vtexsegment)                                                                                                                | VTEX edge will cache your service's response based on the received segment. | Retrieving information that may change depending on the segment. For instance, applying promotions according to the shopper's selected currency. |
| Private           | `/_v/private/{yourPath}` | Your app will receive both the [vtex_segment](https://developers.vtex.com/docs/guides/sessions-system-overview#cookie-vtexsegment) and [vtex_session](https://developers.vtex.com/docs/guides/sessions-system-overview#cookie-vtexsession) cookies. | VTEX will not cache your service's response.                                | Retrieving information depending on the shopper identity or specific session, such as the shopper's order history or registered addresses.       |

## Troubleshooting

### Unavailable cookies with Cloudfront CDN

If your store uses Cloudfront as a CDN and you encounter difficulties in obtaining the desirable cookies from the app’s service context, [open a ticket](https://help.vtex.com/en/tutorial/opening-tickets-to-vtex-support--16yOEqpO32UQYygSmMSSAM) to the VTEX support team reporting the issue.
