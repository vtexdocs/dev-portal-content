---
title: "External marketplace protocol: new order integration method"
slug: "external-marketplace-protocol-new-order-integration-method"
type: "added"
createdAt: "2022-06-10T14:00:00.000Z"
hidden: false
excerpt: "We have released a new method for integrating orders from external marketplaces, as a part of our Marketplace Protocol. For the new method, we have developed two new endpoints."
---

![Commerce APIs](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/external-marketplace-protocol-new-order-integration-method-0.png)

We have released a new method for integrating orders from external marketplaces, as a part of our Marketplace Protocol. For the new method, we have developed two new endpoints:

- <span class="APIMethod APIMethod_fixedWidth APIMethod_post">post</span> [New Order Integration API Reference](https://developers.vtex.com/vtex-rest-api/reference/new-order-integration)
- <span class="APIMethod APIMethod_fixedWidth APIMethod_put">put</span> [Update Order Status API Reference](https://developers.vtex.com/vtex-rest-api/reference/update-order-status)

You can learn more about their implementation and use case scenarios in the following articles:

- [New Order Integration guide](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-collect-orders)
- [Update Order Status guide](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-update-order-status)

The other steps for the External Marketplace Protocol have not been changed.

If you used our previous method for integrating orders from external marketplaces, you can still find their documentation in [Order Logs](https://developers.vtex.com/vtex-rest-api/docs/deprecated-order-logs) and [How to collect orders from sales channels](https://developers.vtex.com/vtex-rest-api/docs/deprecated-how-to-collect-orders-from-sales-channels). The previous method, however, will not be maintained. If you are integrating orders for the first time, we recommend you use the instructions in this article.
