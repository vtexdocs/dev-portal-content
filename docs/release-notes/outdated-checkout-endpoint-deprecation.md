---
slug: "outdated-checkout-endpoint-deprecation"
title: "Outdated Checkout endpoint deprecation"
createdAt: 2023-01-16T14:01:00.322Z
hidden: false
type: "deprecated"
---

Beginning June 25, 2023, there is an Outdated Checkout endpoint that will be deprecated and all integrations that use this route will have to migrate to OMS endpoints, as indicated in the following table:

| **From Checkout endpoint** | **To OMS endpoints** |
|---|---|
| Outdated Checkout endpoint GET - `api/checkout/pub/orders` | <ul><li><a href="https://developers.vtex.com/docs/api-reference/orders-api#get-/api/oms/user/orders">Retrieve user's orders</a><br>GET - <code>https://{accountName}.{environment}.com.br/api/oms/user/orders</code></li><li><a href="https://developers.vtex.com/docs/api-reference/orders-api#get-/api/oms/user/orders/-orderId-">Retrieve user order details</a><br>GET - <code>https://{accountName}.{environment}.com.br/api/oms/user/orders/{orderId}</code></li></ul>

The Outdated Checkout endpoint is an old endpoint that will be discontinued. Using the OMS endpoints ensures that your store is using the latest and most performant VTEX solution.

To know more about the benefits of this change and for technical information, see [Outdated Checkout endpoint deprecation](https://developers.vtex.com/docs/guides/outdated-checkout-api-deprecation).
