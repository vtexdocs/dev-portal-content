---
title: "External Marketplace"
slug: "external-marketplace-integration-guide"
hidden: false
createdAt: "2020-09-01T20:23:42.523Z"
updatedAt: "2020-10-27T23:15:58.017Z"
---

In our native multi-seller architecture, VTEX stores decouple different aspects of an e-commerce operation in order to clearly divide responsibilities between marketplace and seller.
![VTEX Seller and VTEX Marketplace](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/external-marketplace-integration-guide-0.png)
This allows VTEX stores to become marketplaces themselves or become sellers in other VTEX stores without requiring any additional development. Store settings connect the marketplace subsystem of a store to the seller subsystem of another.
![VTEX Seller and VTEX Marketplace 2](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/external-marketplace-integration-guide-1.png)
This behavior can be leveraged in endless combinations. VTEX accounts can both set up a marketplace storefront to sell products from multiple sellers, including their own, and distribute products to multiple other marketplaces. This creates our [collaborative commerce](https://vtex.com/en/blog/strategy/collaborative-commerce-imperative-why-digital-first-collaboration-is-at-the-core-of-todays-business-success/) network.
![External Marketplace](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/external-marketplace-integration-guide-2.png)
However, there may be a strategic partner for your business operating outside our collaborative commerce network. This guide presents the steps needed to develop a **custom connector to sell your products in an external marketplace**.
[block:callout]
{
  "type": "warning",
  "body": "This guide is currently being written and published as content become available.",
  "title": "Work in progress"
}
[/block]
