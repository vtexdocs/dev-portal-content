---
title: "Marketplace / Seller architecture"
slug: "external-seller-integration-architecture"
hidden: false
createdAt: "2020-09-01T13:44:13.071Z"
updatedAt: "2022-01-25T20:09:23.064Z"
---
Given the separation of concerns between marketplace and seller, creating a custom connector for external systems requires mapping out the equivalent behavior observed in VTEX stores. This step provides an overview of what is expected of each subsystem.

## Business agreements

The starting point for a marketplace is defining the policies, agreements, and guidelines governing the business relationship between marketplace and sellers. 

These legal agreements will differ in scope and content depending on the specific type of industry and marketplace business model in place, but some concerns are common:

- Commission fees and receipt of sales proceeds
- Criteria for product selection and exposure
- Customer support requirements
- Delivery time and cost requirements
[block:callout]
{
  "type": "info",
  "body": "Consider skimming through the [Program Policies](https://sellercentral.amazon.com/gp/help/external/help.html?itemID=521&language=en_US&ref=efph_521_cont_SNV3657R94YP9DZ) enforced by Amazon for inspiration."
}
[/block]
From the technical standpoint, however, these are the requirements for each stakeholder:

|Who | What|
| --- | --- |
| Marketplace  | Owns the storefront and is responsible for the checkout process.  |
| Seller   | Owns the product and is responsible for the fulfillment process.  |

Everything else should be agreed upon between marketplace and sellers, taking into account that additional development may be needed to enforce certain policies.

## Catalog management

When dealing with product information, our core assumption is that every business should define its own catalog structure. Due to that, the interaction between marketplaces and sellers is based on offers, which include product information, price, and quantity in stock.

From a technical standpoint, this is what each stakeholder must do:

|Who | What|
| --- | --- |
| Marketplace  | Receive and manage offers made by sellers, deciding how they should be incorporated in their catalog through SKU matching and binding.  |
| Seller   | Send offers with the product information, price, and quantity in stock.  |

## Pricing & promotions

When dealing with prices, our core assumption is that every business should define its own pricing strategy. Due to that, order authorization rules are defined by the seller to deal with scenarios of price divergence.

From a technical standpoint, this is what each stakeholder must do:

|Who | What|
| --- | --- |
| Marketplace  | Receive price change notifications and update price records accordingly.  |
| Seller   | Define prices & promotions that should be applied to the marketplace, define price divergence rules for order authorization to deny orders, send price change notifications, and allow the marketplace to fetch updated prices.  |

## Inventory & shipping

When dealing with logistics, our core assumption is that sellers manage their shipping strategy, unless the marketplace requires them to adhere to their fulfillment services. This includes defining the inventory and shipping policies available to each sales channel. 

From a technical standpoint, this is what each stakeholder must do:

|Who | What|
| --- | --- |
| Marketplace  | Receive change notifications and update inventory accordingly.  |
| Seller   | Define inventory & shipping policies available to the marketplace, send inventory change notifications, and allow the marketplace to fetch updated inventory, freight costs, and delivery time for products.  |

## Storefront & checkout

In our architecture, the marketplace is responsible for the purchase flow and placing the order correctly to the seller. To avoid placing orders with price divergence (outdated prices) and stockouts (exhausted inventory), the marketplace storefront should perform cart simulations to get updated product information at multiple stages of the purchase flow.

Optionally, the marketplace may establish criteria for seller selection or exposure. This happens when the marketplace wants to incentivize competition between sellers to become the default selection in their buy box or allow shoppers to choose who they are buying their products from.

From a technical standpoint, this is what each stakeholder must do:

|Who | What|
| --- | --- |
| Marketplace  | Display products in its storefront, place orders to sellers upon checkout.  |
| Seller   | Receive orders placed by the marketplace. |

## Order fulfillment

In our architecture, each stakeholder is responsible for a part of the [order flow](https://help.vtex.com/tracks/pedidos--2xkTisx4SXOWXQel8Jg8sa/4811ExCe3WrEiRMV3sy9n8). Changes and cancellations can be made within a certain window, which can be configured by the marketplace.

## Payment conditions & commissioning

In our architecture, the marketplace is usually responsible for defining the payment conditions it will offer and the commission fees they will charge from sellers. If after negotiations, the marketplace decides to process payments, no development is needed from the seller. However, brazilian businesses can process payments, if agreed with the marketplace. Know more in [External seller processing payments](https://developers.vtex.com/docs/guides/external-seller-processing-payments) if that's the case.

|     Who     |                                    What                                    |
|:-----------:|:--------------------------------------------------------------------------:|
| Marketplace | Usually the system who processes payments, and who defines commissions.                                 |
| Seller      | May include other payment methods, if the ones configured in the marketplace do not meet the seller's sales agreements. May process payments, if agreed with the marketplace. |