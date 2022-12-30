---
title: "Order Integration overview"
slug: "external-marketplace-integration-orders"
hidden: false
createdAt: "2021-09-02T20:37:18.175Z"
updatedAt: "2022-08-01T19:42:23.035Z"
---
Learn how to integrate Orders in VTEX with external marketplaces. Before you start, check out what’s included in the Order Integration flow:

| **Included
   ** | **Not included
   ** |
|---|---|
| All valid orders made in the external marketplace, will be integrated in the main account.
    | Orders made in the external marketplace, integrated in third party sellers or franchise accounts.
    |
| SKUs in the order must be associated to the trade policy configured in the integration
    | SKUs not included in the chose trade policy
    |
| SKUs with stock valid level
    | SKUs without stock
    |
| SKUs with prices defined within the rules defined by the VTEX store
    | SKUs without prices set
    |
| Carriers configured to attend the order’s address
    | Carriers not configured in the main account
    |
|
    | Invalid orders made in the external marketplace
    |

## Glossary

- **Seller:** Owns the product, responsible for the fulfillment, or SKU delivery.
- **Marketplace/affiliate:** Owns the storefront, responsible for selling the SKU.
- **SKU:** item to be exchanged and sold between seller and marketplace
- **Sales channel/Trade policy:** product assortment, prices, and logistics configurations attached to a sales channel.
- **Connector:** party responsible for the integration, being either the marketplace itself, or an integration hub. Know more about [how to configure a marketplace trade policy](https://help.vtex.com/tutorial/configurando-a-politica-comercial-para-marketplace--tutorials_404).
- **Order Authorization:**order authorization rules are defined by the seller to deal with scenarios of price divergence.
- **MarketplaceServicesEndpoint:**Endpoint sent by the marketplace to the seller, that will be used to send the invoice and tracking data back to it.
