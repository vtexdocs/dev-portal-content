---
title: "Integration flow"
slug: "integration-flow"
hidden: false
createdAt: "2021-04-29T19:54:03.640Z"
updatedAt: "2022-04-08T20:19:03.880Z"
---
The typical cycle of an order shipped through a carrier that is integrated with VTEX goes through these stages:

1. **Invoice**: a package starts its path in VTEX Shipping Network only after the order is invoiced.

2. **Notification**: after the order has been invoiced, the VTEX hub notifies the carrier app. It informs the carrier that there is a package to be collected, specifying the details.

3. **Shipping**: then, the store can print a shipping label with the appropriate shipping information and dispatch it to the carrier.

4. **Tracking**: while the package is in transit, the carrier app sends tracking updates to the VTEX tracking hub, so that information can be made available to the store and customer.

5. **Delivery**: finally, the package gets to the customer.

Since the notification and tracking stages consist of exchanging information between the carrier and VTEX, these are the processes that should be handled by your apps.

One of the advantages of building IO apps is modularity, which allows for flexible customization of a store’s features. Because of that, we provide separate boilerplate repositories for [notification](https://github.com/vtex-apps/carrier-hubs-examples/tree/main/carrier-notifier-example) and [tracking](https://github.com/vtex-apps/carrier-hubs-examples/tree/main/carrier-tracking-example). You can develop one app to perform the two tasks or two separate apps for each of them.

Both apps should be able to read data that will be sent from VTEX in a specific format and respond with the appropriate information in a specific format. Below you can find out more about the particularities of each of those tasks.


## Learn more

See this guide on [how to develop carrier apps on IO](https://developers.vtex.com/vtex-rest-api/docs/getting-started-with-vtex-io-for-carriers). Also, learn more about [notification](https://developers.vtex.com/vtex-rest-api/docs/notification-1) and [tracking](https://developers.vtex.com/vtex-rest-api/docs/tracking-1) for carrier apps.