---
title: "Creating app service paths"
slug: "creating-app-service-paths"
hidden: false
---

When [developing a new VTEX IO service](https://developers.vtex.com/docs/guides/vtex-io-documentation-developing-service-configuration-apps), you must define a path so that the service is available to receive requests.

In this article you will learn about the pattern for service paths according to the desired behavior. To know more about how to implement the path in your app's code, check the guide [Developing service configuration apps](https://developers.vtex.com/docs/guides/vtex-io-documentation-developing-service-configuration-apps).

## Patterns

There are three possible path formats, depending on the behavior you wish for your service.

For the purpose of this tutorial, consider you are implementing the service `/examplepath/123`. You may change how VTEX handles requests to this service by adding `/_v/segment` or `/_v/private` to the beginning of your path. This means you have three possible paths in this example:

- **Public:** `/examplepath/123`
- **Segment dependant:** `/_v/segment/examplepath/123`
- **Private:** `/_v/private/examplepath/123`

VTEX has an edge layer that handles all requests to VTEX, including VTEX IO apps, in order to improve performance. Because of this, VTEX will handle requests to each of these possible paths in a different way when it comes to caching and handling cookies. See the table below.

| **Path type**     | **Pattern**              | **Cookies behavior**                                                                                                                                                                                                                                | **Caching behavior**                                                        | **Example use case**                                                                                                                             |
|-------------------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Public            | `{yourPath}`             | There is no guarantee your app will receive the cookies from the request.                                                                                                                                                                           | VTEX edge will cache your service's response whenever it is possible.       | Retrieving information that does not vary according to user or segment, such as product images.                                                  |
| Segment dependant | `/_v/segment/{yourPath}` | Your app will receive the [tvex_segment cookie](https://developers.vtex.com/docs/guides/sessions-system-overview#cookie-vtexsegment)                                                                                                                | VTEX edge will cache your service's response based on the received segment. | Retrieving information that may change depending on the segment. For instance, applying promotions according to the shopper's selected currency. |
| Private           | `/_v/private/{yourPath}` | Your app will receive both the [tvex_segment](https://developers.vtex.com/docs/guides/sessions-system-overview#cookie-vtexsegment) and [vtex_session](https://developers.vtex.com/docs/guides/sessions-system-overview#cookie-vtexsession) cookies. | VTEX will not cache your service's response.                                | Retrieving information depending on the shopper identity or specific session, such as the shopper's order history or registered addresses.       |