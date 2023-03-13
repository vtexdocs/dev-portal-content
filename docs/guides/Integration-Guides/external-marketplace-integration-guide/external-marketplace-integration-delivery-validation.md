---
title: "How to validate if items are available for delivery"
slug: "external-marketplace-integration-delivery-validation"
hidden: false
createdAt: "2021-09-02T20:51:46.911Z"
updatedAt: "2022-06-06T19:05:38.430Z"
---
To make sure all items in an order are available for delivery on the VTEX platform, the connector must validate them. Follow the steps below to make the validation:

1. Connector collects order information at the marketplace.
2. Connector sends a [Fulfillment simulation](https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-marketplace-orders#post-/api/checkout/pub/orderForms/simulation) request to collect updated information about items to check their availability on stock.
3. Connector notifies VTEX about stock in Marketplace through the `StockBalance` property, so that the stock availability is constantly updated.
4. After receiving the VTEX notification, connectors should validate the following:
- If the SKU is active, through the `isActive` property, .
- If the SKU is associated with the trade policy used in the marketplace integration through the `salesChannel` property.
- If there is a freight option configured to deliver the order in the Shipping strategy, through the object `logistics`.
- If there SKU available in stock through the `StockBalance` property.

All the fields mentioned above must be available for the validation of an item’s delivery. In case any of them are unavailable, the item will not be validated.
[block:callout]
{
  "type": "warning",
  "body": "In case the SKU is not included in the Shopping cart simulation's response, connectors must reduce stock to zero to avoid orders created for nonexistent SKUs.",
  "title": "Nonexistent SKUs"
}
[/block]