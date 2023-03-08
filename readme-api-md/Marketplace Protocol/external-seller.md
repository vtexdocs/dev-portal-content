---
title: "External Seller"
slug: "external-seller"
hidden: false
createdAt: "2020-09-01T13:10:07.457Z"
updatedAt: "2022-02-03T21:29:11.359Z"
---
Here you will find the endpoints involved in the integration between a VTEX marketplace and an external seller. Note that some of these requests are typically sent by the seller while others are received.

| **Request**                                                                                                                    | **From**    | **To**      |
|--------------------------------------------------------------------------------------------------------------------------------|-------------|-------------|
| [Fulfillment simulation](https://developers.vtex.com/vtex-rest-api/reference/fulfillment-simulation)           | Marketplace | Seller      |
| [Order placement](https://developers.vtex.com/vtex-rest-api/reference/order-placement)                         | Marketplace | Seller      |
| [Authorize fulfillment](https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-seller-fulfillment#post-/pvt/orders/-sellerOrderId-/fulfill)             | Marketplace | Seller      |
| [Marketplace order cancellation](https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-seller-fulfillment#post-/pvt/orders/-orderId-/cancel)   | Marketplace | Seller      |
| [Send invoice](https://developers.vtex.com/docs/api-reference/marketplace-protocol#post-/pvt/orders/-marketplaceOrderId-/invoice)                               | Seller      | Marketplace |
| [Send tracking information](https://developers.vtex.com/vtex-rest-api/reference/send-tracking-information)     | Seller      | Marketplace |
| [Update tracking status](https://developers.vtex.com/vtex-rest-api/reference/update-tracking-status)           | Seller      | Marketplace |
| [Cancel order in marketplace](https://developers.vtex.com/docs/api-reference/marketplace-protocol#post-/pvt/orders/-marketplaceOrderId-/cancel) | Seller      | Marketplace |

For a detailed explanation of the steps required to develop a custom connector to sell products from an external seller in your storefront, check out our complete [External Seller Integration Guide](https://developers.vtex.com/docs/external-seller-integration-guide).