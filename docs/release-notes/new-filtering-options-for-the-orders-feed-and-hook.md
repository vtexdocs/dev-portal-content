---
slug: "new-filtering-options-for-the-orders-feed-and-hook"
title: "New filtering options for the orders feed and hook"
createdAt: 2021-05-21T17:45:25.611Z
hidden: false
type: "added"
---

With the new configuration available for the [orders feed](https://developers.vtex.com/vtex-rest-api/docs/feed-v3-1), any changes made to orders can be tracked. This is done through [JSONata](https://jsonata.org/) expressions set in the Orders API, which allow for highly customized filtering. It is possible to combine filtering conditions and select specific subsets of orders that should generate events, for example.

## What needs to be done?

Existing feed and hook configurations are not affected by this change. This new configuration is an alternative to the default filtering by status.

You can implement the new configuration by using the [Feed v3 configuration](https://developers.vtex.com/vtex-rest-api/reference/feed-v3#feedconfiguration) or [Hook configuration](https://developers.vtex.com/vtex-rest-api/reference/order-hook#hookconfiguration) endpoints of the Order API. Learn more about how to configure this new filter in the [Feed v3 guide](https://developers.vtex.com/vtex-rest-api/docs/feed-v3-1).

If you need to test your JSONata filtering expressions, use our [JSONata expressions API endpoint](https://developers.vtex.com/vtex-rest-api/reference/feed-v3#testjsonataexpression).
