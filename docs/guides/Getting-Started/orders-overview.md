---
title: "Orders"
slug: "orders-overview"
hidden: false
createdAt: "2020-09-21T22:46:46.589Z"
updatedAt: "2023-03-28t15:07:06.478z"
---

> **Help us improve our documentation!** Tell us about your experience with this article by completing [this form](https://forms.gle/fQoELRA1yfKDqmAb8).

This overview article covers the VTEX Order Management System (OMS), including relevant links from our developer documentation. In the following sections, you will find information about setting up and managing your orders, creating order integrations with external partners, and configuring optional settings.

### Importing orders from an ERP or Back office

If your store has an ERP integration or another integration for managing orders, you will need to create an integration with the VTEX platform. The links below provide an overview of the order integration flow between a back-office system and a VTEX store.

- [Back office (ERP/PIM/WMS)](https://developers.vtex.com/docs/guides/erp-integration-guide)
- [Set up order integration](https://developers.vtex.com/docs/guides/erp-integration-set-up-order-integration)
- [Set up order processing](https://developers.vtex.com/docs/guides/erp-integration-set-up-order-processing)
- [Change order](https://developers.vtex.com/docs/guides/change-order)
- [FAQ: ERP Integration](https://developers.vtex.com/docs/guides/faq-erp-integration)

## Understanding order flow types

The order flow describes the status, possible flows, and actions throughout the life cycle of an order. On VTEX, there are four [order flow types](https://help.vtex.com/en/tutorial/order-flow-and-status--tutorials_196):

### Marketplace flow

The marketplace order flow is only visible to the store responsible for the sale.

![marketplace_flow](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/orders-overview-0.jpg)

### Seller flow

The seller order flow is only visible to the store responsible for handling the order.

![seller_flow](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/orders-overview-1.png)

### Complete flow

The complete order flow is only visible to the store responsible for the sale and delivery. In this case, the store acts both as seller and marketplace.

![complete_flow](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/orders-overview-2.png)

### Chain flow

The chain order flow is visible to the store acting as an intermediary between the marketplace and the seller. This flow is similar to the marketplace flow. However, the payment is only made to the marketplace, not to the store that acts as a chain. This flow is followed in [Multilevel Omnichannel Inventory](https://developers.vtex.com/docs/guides/multilevel-omnichannel-inventory) sales situations.

![chain_flow](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/orders-overview-3.png)

## Creating an order integration

In the following sections, you will learn how to build order integrations with Feed and Hook. For example, this can be useful for developing an integration between your store ERP and the VTEX platform.

> We strongly recommend you to create an order integration using the [Orders Feed v3](https://developers.vtex.com/docs/guides/orders-feed), instead of using the List orders API request or external services. If you already use an integration based on the API request, you should migrate to using the Feed. Keep in mind that this means changing the integration flow. To learn how to implement this change, see the [Set up order integration](https://developers.vtex.com/docs/guides/erp-integration-set-up-order-integration).

### Feed v.3
  
The Orders feed is a list of order updates, meaning that an order status update will be included as a new item in the feed whenever there is an event in an order.
  
- [Feed v3 Guide](https://developers.vtex.com/docs/guides/orders-feed)
- [Get feed configuration](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/orders/feed/config)
- [Create or update feed configuration](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/orders/feed/config)
- [Delete feed configuration](https://developers.vtex.com/vtex-rest-api/reference/feedconfigurationdelete)
- [Retrieve feed items](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/orders/feed)
- [Commit feed items](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/orders/feed)
- [Test JSONata expression](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/orders/expressions/jsonata)

### Hook

Hook works as a complement to Feed, because it allows an integration to consume order updates data by sending items to a URL provided by the user in the Hook configuration.

- [Get hook configuration](https://developers.vtex.com/vtex-rest-api/reference/gethookconfiguration)
- [Create or update hook configuration](https://developers.vtex.com/vtex-rest-api/reference/hookconfiguration)
- [Delete hook configuration](https://developers.vtex.com/vtex-rest-api/reference/deletehookconfiguration)

## Managing orders

There are several actions a VTEX store can perform on orders. In the following sections, you will find the main actions related to a store’s order management routine.

> This module may process personal or sensitive information. Learn more about how VTEX handles data privacy at our [Data privacy](https://developers.vtex.com/docs/guides/data-privacy) guide.

### Placing an order

Placing an order involves the Order Management module and [Checkout](https://developers.vtex.com/vtex-rest-api/docs/checkout-overview). There are different paths to create orders. For more information about placing orders, see the links below.

- [Place order](https://developers.vtex.com/docs/api-reference/checkout-api#put-/api/checkout/pub/orders)
- [Place order from an existing cart](https://developers.vtex.com/vtex-rest-api/reference/placeorderfromexistingorderform)
- [Process order](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/gatewayCallback/-orderGroup-)
- [Create a regular order using the Checkout API](https://developers.vtex.com/docs/guides/create-a-regular-order-using-the-checkout-api)

> The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the main object processed by the [Checkout](https://developers.vtex.com/vtex-rest-api/docs/checkout-overview) and it stores a lot of contextual information about an order. The orderForm fields will be present in most of OMS's API calls.

### Retrieving order’s details

> You can only access information from orders created in the last two years, and that same period is valid for customers through [My Account](https://help.vtex.com/en/tutorial/how-my-account-works--2BQ3GiqhqGJTXsWVuio3Xh).

You can fetch information about orders in multiple ways and about specific topics. To learn more about retrieving order content, see the links below.

#### Orders

- [Get order](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/oms/pvt/orders/-orderId-)
- [List orders](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/oms/pvt/orders)

#### Conversation

- [Retrieve order conversation](https://developers.vtex.com/vtex-rest-api/reference/getconversation)

#### User

- [Retrieve user's orders](https://developers.vtex.com/vtex-rest-api/reference/userorderslist)
- [Retrieve user order details](https://developers.vtex.com/vtex-rest-api/reference/userorderdetails)

#### Payment

- [Retrieve payment transaction](https://developers.vtex.com/vtex-rest-api/reference/getpaymenttransaction)

#### Marketplace

- [Fetching marketplace information with the Orders API](https://developers.vtex.com/docs/guides/get-marketplace-data-orders-api)
- [Fetching payment details from a Mercado Libre order with Orders API](https://developers.vtex.com/docs/guides/get-payment-data-mercado-libre-orders-api)

### Changing an order status

Every order has a life cycle registered as an [order flow](https://help.vtex.com/en/tutorial/order-flow-and-status--tutorials_196), which describes the order status, options, and updates. For more information, see the links below.

- [Start handling order](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/oms/pvt/orders/-orderId-/start-handling)
- [Cancel order](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/oms/pvt/orders/-orderId-/cancel)

### Changing an order

Changing orders is a feature that allows your store to edit the items or prices of an order. For example, this allows you to handle eventual changes due to customer mistakes or product unavailability. To learn more, see the links below.

- [Change order](https://developers.vtex.com/docs/guides/change-order)
- [Register change on order](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/oms/pvt/orders/-orderId-/changes)

### Changing seller

Another seller can be selected to fulfill a given order after the original seller canceled it. The period when this can be done is called the change seller window. You can use the endpoints below for this.

- [Get window to change seller](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/checkout/pvt/configuration/window-to-change-seller)
- [Update window to change seller](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/checkout/pvt/configuration/window-to-change-seller)

### Sending payment notification

For your payment provider to notify the Order Management System that the payment of a given order is completed, use the [Send payment notification](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/oms/pvt/orders/-orderId-/payments/-paymentId-/payment-notification) endpoint.

If your store receives payments outside the VTEX platform, such as cash or notes payable, it must call this endpoint to notify the OMS, so the order can follow its flow and be fulfilled.
  
> The endpoint [Send payment notification](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/oms/pvt/orders/-orderId-/payments/-paymentId-/payment-notification) must be called only after the order payment has been approved. The store might not receive the payment if there is an issue with the settlement and the endpoint has already been called.

### Invoicing an order

When you [invoice an order](https://help.vtex.com/en/tracks/orders--2xkTisx4SXOWXQel8Jg8sa/2WgQrlHTyVo4hLjhUs1LMT), its status in the [order flow](https://help.vtex.com/en/tutorial/order-flow-and-status--tutorials_196) changes to Invoiced, which means the order was successfully completed. After an order is invoiced, you can no longer modify its status, except when you want to send a return invoice.

In that case, the [Order invoice notification](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/oms/pvt/orders/-orderId-/invoice) endpoint must be called, and instead of having the field `type` value defined as Output, it will be Input.

- [Order invoice notification](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/oms/pvt/orders/-orderId-/invoice)
- [Update order's partial invoice (send tracking number)](https://developers.vtex.com/docs/api-reference/orders-api#patch-/api/oms/pvt/orders/-orderId-/invoice/-invoiceNumber-)
- [Adding a second address for invoicing an order](https://developers.vtex.com/docs/guides/adding-a-second-address-to-the-order)
- [Formatting order invoicing time via API](https://developers.vtex.com/docs/guides/formatting-order-invoicing-time)

### Tracking an order

Every order has a tracking number that allows you to keep track of its status in the [order flow](https://help.vtex.com/en/tutorial/order-flow-and-status--tutorials_196). To send a tracking event to an order with a tracking number, use the [Update order's partial invoice](https://developers.vtex.com/vtex-rest-api/reference/updatepartialinvoicesendtrackingnumber) endpoint.

If you want to add a tracking number and URL to an order invoice, use the [Update order's partial invoice](https://developers.vtex.com/vtex-rest-api/reference/updatepartialinvoicesendtrackingnumber) endpoint.

## Integrating with the Multilevel Omnichannel Inventory

[Multilevel Omnichannel Inventory](https://developers.vtex.com/docs/guides/multilevel-omnichannel-inventory) is the VTEX setting that allows the inventory of [franchises](https://help.vtex.com/en/tutorial/what-is-a-franchise-account--kWQC6RkFSCUFGgY5gSjdl) or [white label sellers](https://help.vtex.com/en/tutorial/white-label-seller--5orlGHyDHGAYciQ64oEgKa) to be sold in marketplaces the main account is connected to.

In other words, the feature allows VTEX sellers to sell products from its franchises or white label sellers in a marketplace, without the need to set up the integration with the desired marketplace. For marketplaces, this means selling products from their direct sellers and also physical stores and white label sellers associated with those sellers in a scalable way.

> For more information, see the article [Multilevel Omnichannel Inventory](https://help.vtex.com/en/tutorial/multilevel-omnichannel-inventory--7M1xyCZWUyCB7PcjNtOyw4).

## Integrating orders from an external marketplace

A VTEX store can act as both a [seller](https://help.vtex.com/en/tutorial/configuring-a-seller-on-vtex-marketplace--6g045OkRSjNpqhkExbQRlP) and a [marketplace](https://help.vtex.com/en/tutorial/configuring-vtex-marketplace--7splyp5MqIyt2Iyz5jsNzb) in relation to another VTEX store or an external partner. If you are an [external marketplace](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-guide) that wants to integrate with VTEX sellers, see the links below to learn how to develop a custom connector to integrate with the VTEX architecture and seller orders.

- [Order Integration overview](https://developers.vtex.com/docs/guides/external-marketplace-integration-orders)
- [New Order Integration](https://developers.vtex.com/docs/guides/external-marketplace-integration-collect-orders)
- [Update Order Status](https://developers.vtex.com/docs/guides/external-marketplace-update-order-status)
- [How to update the status of a canceled order on VTEX](https://developers.vtex.com/docs/guides/external-marketplace-integration-canceled-orders)

## Adding optional configurations

There are additional configurations available for you to manage your store orders. This allows you to take advantage of other VTEX features, such as [VTEX Sales App](https://developers.vtex.com/docs/guides/how-to-customize-vtex-sales-app), [VTEX DO](https://help.vtex.com/en/tutorial/vtex-do-interface--7KMbRL4OslN8DTX9oiuCiu), [B2B](https://help.vtex.com/en/tutorial/b2b-overview--5vb9SNXhX2bZnkpAh7ADdC), and [Master Data](https://developers.vtex.com/docs/guides/master-data-introduction).

### VTEX Sales App

- [Enable order filter by sales associate](https://developers.vtex.com/docs/guides/enable-order-filter-by-sales-associate)
- [Enable partial cancellation for Debit or Credit Direct sales](https://developers.vtex.com/docs/guides/enable-partial-cancellation)

### VTEX DO

- [Create Note](https://developers.vtex.com/vtex-rest-api/reference/newnote)
- [Get Notes by orderId](https://developers.vtex.com/vtex-rest-api/reference/getnotesbyorderid)
- [Retrieve Note](https://developers.vtex.com/vtex-rest-api/reference/getnote)
- [Create Task](https://developers.vtex.com/vtex-rest-api/reference/newtask)
- [List tasks](https://developers.vtex.com/vtex-rest-api/reference/listtasksbyassignee)
- [Retrieve Task](https://developers.vtex.com/vtex-rest-api/reference/gettask)
- [Update Task](https://developers.vtex.com/docs/api-reference/vtex-do-api#put-/tasks/-taskId-)
- [Add Comment on a Task](https://developers.vtex.com/docs/api-reference/vtex-do-api#post-/tasks/-taskId-/comments)

### B2B

- [B2B Suite](https://developers.vtex.com/docs/apps/vtex.b2b-suite)

### Master Data

- [Use v2 triggers to interact with orders](https://developers.vtex.com/vtex-rest-api/docs/use-master-data-with-orders)
