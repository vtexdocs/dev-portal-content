---
title: "Order Integration overview"
slug: "external-marketplace-integration-orders"
hidden: false
createdAt: "2021-09-02T20:37:18.175Z"
updatedAt: "2022-08-01T19:42:23.035Z"
---
Learn how to integrate Orders in VTEX with external marketplaces. Before you start, check out what’s included in the Order Integration flow:


<table>
  <tr>
   <td><strong>Included</strong>
   </td>
   <td><strong>Not included</strong>
   </td>
  </tr>
  <tr>
   <td>All valid orders made in the external marketplace, will be integrated in the main account.
   </td>
   <td>Orders made in the external marketplace, integrated in third party sellers or franchise accounts.
   </td>
  </tr>
  <tr>
   <td>SKUs in the order must be associated to the trade policy configured in the integration
   </td>
   <td>SKUs not included in the chose trade policy
   </td>
  </tr>
  <tr>
   <td>SKUs with stock valid level
   </td>
   <td>SKUs without stock
   </td>
  </tr>
  <tr>
   <td>SKUs with prices defined within the rules defined by the VTEX store
   </td>
   <td>SKUs without prices set
   </td>
  </tr>
  <tr>
   <td>Carriers configured to attend the order’s address
   </td>
   <td>Carriers not configured in the main account
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Invalid orders made in the external marketplace
   </td>
  </tr>
</table>



## Glossary



- **Seller:** Owns the product, responsible for the fulfillment, or SKU delivery.
- **Marketplace/affiliate:** Owns the storefront, responsible for selling the SKU.
- **SKU:** item to be exchanged and sold between seller and marketplace
- **Sales channel/Trade policy:** product assortment, prices, and logistics configurations attached to a sales channel.
- **Connector:** party responsible for the integration, being either the marketplace itself, or an integration hub. Know more about [how to configure a marketplace trade policy](https://help.vtex.com/tutorial/configurando-a-politica-comercial-para-marketplace--tutorials_404).
- **Order Authorization: **order authorization rules are defined by the seller to deal with scenarios of price divergence.
- **MarketplaceServicesEndpoint: **Endpoint sent by the marketplace to the seller, that will be used to send the invoice and tracking data back to it.