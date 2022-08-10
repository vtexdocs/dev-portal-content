---
title: "Orders"
slug: "orders-overview"
hidden: false
createdAt: "2020-09-21T22:46:46.589Z"
updatedAt: "2022-08-08T17:12:41.281Z"
---
[block:callout]
{
  "type": "info",
  "body": "📣 Help us improve our documentation! Share your feedback by filling out [this form](https://forms.gle/s5Z9fALPd4mDqEgS9)."
}
[/block]
This overview article goes over VTEX’s Order Management System (OMS), including relevant links from our developer documentation about this topic. In the following sections you will find information about setting up and managing your orders, creating order integrations with external partners and making optional configurations. 

<br>

## Importing orders from an ERP or Back office

If your store has an ERP integration or another kind of integration for managing orders, it will be necessary to make an integration with VTEX’s platform. The links below provide a general view of the integration flow between a back office system and a VTEX store regarding orders.

* [Back office (ERP/PIM/WMS)](https://developers.vtex.com/vtex-rest-api/docs/erp-integration-guide)
* [Set up order integration](https://developers.vtex.com/vtex-rest-api/docs/erp-integration-set-up-order-integration)
* [Set up order processing](https://developers.vtex.com/vtex-rest-api/docs/erp-integration-set-up-order-processing)
* [Change order](https://developers.vtex.com/vtex-rest-api/docs/change-order)
* [FAQ: ERP Integration](https://developers.vtex.com/vtex-rest-api/docs/faq-erp-integration)

<br>

## Managing orders

There are several actions a VTEX store can perform on orders. In the next sections, you will find the main actions related to a store’s order management routine.

### Placing an order

The action of placing an order involves both the Orders Management module and the [Checkout](https://developers.vtex.com/vtex-rest-api/docs/checkout-overview), and there are different paths to create orders. For more information about order placement, see the links below.

* [Place order](https://developers.vtex.com/vtex-rest-api/reference/placeorder)
* [Process order](https://developers.vtex.com/vtex-rest-api/reference/processorder)
* [Using APIs to place a regular order](https://developers.vtex.com/vtex-rest-api/docs/using-apis-to-place-a-regular-order)
* [Place order from an existing cart](https://developers.vtex.com/vtex-rest-api/reference/placeorderfromexistingorderform)

[block:callout]
{
  "type": "info",
  "body": "The [orderForm](https://developers.vtex.com/vtex-rest-api/reference/orderform-fields) is the main object processed by the [Checkout](https://developers.vtex.com/vtex-rest-api/docs/checkout-overview) and it stores a lot of contextual information about an order. The orderForm fields will be present in most of OMS's API calls."
}
[/block]
### Retrieving order’s details

You can fetch information related to orders in multiple ways and about specific topics. To know more about retrieving orders’ content, see the links below.

#### Orders

* [Get order](https://developers.vtex.com/vtex-rest-api/reference/getorder)
* [List orders](https://developers.vtex.com/vtex-rest-api/reference/listorders)

#### Conversation

* [Retrieve order conversation](https://developers.vtex.com/vtex-rest-api/reference/getconversation)

#### User

* [Retrieve user's orders](https://developers.vtex.com/vtex-rest-api/reference/userorderslist)
* [Retrieve user order details](https://developers.vtex.com/vtex-rest-api/reference/userorderdetails)

#### Payment

* [Retrieve payment transaction](https://developers.vtex.com/vtex-rest-api/reference/getpaymenttransaction)

#### Marketplace

* [Fetching marketplace information with the Orders API](https://developers.vtex.com/vtex-rest-api/docs/get-marketplace-data-orders-api)
* [Fetching payment details from a Mercado Libre order with Orders API](https://developers.vtex.com/vtex-rest-api/docs/get-payment-data-mercado-libre-orders-api)

### Changing an order status

Every order has a life cycle registered in the form of an [order flow](https://help.vtex.com/en/tutorial/order-flow-and-status--tutorials_196), which describes the order’s status, possibilities, and updates. For more information, see the following links.

* [Start handling order](https://developers.vtex.com/vtex-rest-api/reference/starthandling)
* [Cancel order](https://developers.vtex.com/vtex-rest-api/reference/cancelorder)

### Changing an order

_Change order_ is a feature that allows your store to modify the items or prices of an order. This allows you to handle eventual changes motivated by customer mistakes or product unavailability, for example. To know more, see the links below.

* [Change order](https://developers.vtex.com/vtex-rest-api/docs/change-order)
* [Register change on order](https://developers.vtex.com/vtex-rest-api/reference/registerchange)

### Changing seller

It is possible to choose another seller to fulfill a given order after the original seller canceled it. The period during which this action can be performed is called _window to change seller_, and you can use the endpoints below for this scenario.

* [Get window to change seller](https://developers.vtex.com/vtex-rest-api/reference/getwindowtochangeseller-1)
* [Update window to change seller](https://developers.vtex.com/vtex-rest-api/reference/updatewindowtochangeseller-1)

### Sending payment notification

For your payment provider to notify the Order Management System that the payment of a given order is completed, use te endpoint [Send a payment notification](https://developers.vtex.com/vtex-rest-api/reference/sendpaymentnotification).

In case your store receives the payments outside VTEX’s platform, like payments in cash or with promissories, the store must call this endpoint to notify the OMS, so that the order can follow its flow and be fulfilled.
[block:callout]
{
  "type": "warning",
  "body": "The endpoint [Send a payment notification](https://developers.vtex.com/vtex-rest-api/reference/sendpaymentnotification) must be called only after the order payment has been approved. The store might not receive the payment if there is an issue with the settlement and the endpoint has already been called."
}
[/block]
### Invoicing an order

When you [invoice an order](https://help.vtex.com/en/tracks/orders--2xkTisx4SXOWXQel8Jg8sa/2WgQrlHTyVo4hLjhUs1LMT), its status in the [order flow](https://help.vtex.com/en/tutorial/order-flow-and-status--tutorials_196) changes to `Invoiced`, which means the order was successfully completed. After an order is invoiced, you can no longer modify it’s status, except when you wish to send a return invoice. In that case, the endpoint [Order invoice notification](https://developers.vtex.com/vtex-rest-api/reference/invoicenotification) must be called, and instead of having the field `type` value determined as `Output`, it will be `Input`.

* [Order invoice notification](https://developers.vtex.com/vtex-rest-api/reference/invoicenotification)
* [Update order's partial invoice (send tracking number)](https://developers.vtex.com/vtex-rest-api/reference/updatepartialinvoicesendtrackingnumber)

### Tracking an order

Every order has a tracking number that allows you to keep track of its status in the [order flow](https://help.vtex.com/en/tutorial/order-flow-and-status--tutorials_196). To send a tracking event to an order that already has a tracking number, use the endpoint [Update order's partial invoice](https://developers.vtex.com/vtex-rest-api/reference/invoice#updatepartialinvoicesendtrackingnumber). 

If you wish to register a tracking number and URL to an order’s invoice, use the endpoint [Update order's partial invoice](https://developers.vtex.com/vtex-rest-api/reference/updatepartialinvoicesendtrackingnumber).

<br>

## Creating an order integration

In the following sections you will learn how to build order integrations with the Feed and Hook. This is useful when you want to develop an integration between your store’s ERP and the VTEX platform, for example.

[block:callout]
{
  "type": "warning",
  "body": "We strongly recommend you to create an order integration using the [Orders Feed v3](https://developers.vtex.com/vtex-rest-api/docs/orders-feed), instead of using the List orders API request or external services. If you already use an integration based on the API request, you should migrate to using the Feed. Keep in mind that this means changing the integration flow. To learn how to implement this change, see the [Set up order integration](https://developers.vtex.com/vtex-rest-api/docs/erp-integration-set-up-order-integration)."
}
[/block]
### Feed v.3

The Orders Feed is a list of order updates, meaning that whenever there is an event in an order, like an order status update, it will be included as a new item in the Feed. 

* [Feed v3 Guide](https://developers.vtex.com/vtex-rest-api/docs/orders-feed) 
* [Get feed configuration](https://developers.vtex.com/vtex-rest-api/reference/getfeedconfiguration)
* [Create or update feed configuration](https://developers.vtex.com/vtex-rest-api/reference/feedconfiguration)
* [Delete feed configuration](https://developers.vtex.com/vtex-rest-api/reference/feedconfigurationdelete)
* [Retrieve feed items](https://developers.vtex.com/vtex-rest-api/reference/getfeedorderstatus1)
* [Commit feed items](https://developers.vtex.com/vtex-rest-api/reference/commititemfeedorderstatus)
* [Test JSONata expression](https://developers.vtex.com/vtex-rest-api/reference/testjsonataexpression)

### Hook

The Hook is a complement to the Feed, which allows an integration to consume order updates data by sending items to an URL provided by the user in the [Hook configuration](https://developers.vtex.com/vtex-rest-api/docs/orders-feed#hook).

* [Get hook configuration](https://developers.vtex.com/vtex-rest-api/reference/gethookconfiguration)
* [Create or update hook configuration](https://developers.vtex.com/vtex-rest-api/reference/hookconfiguration)
* [Delete hook configuration](https://developers.vtex.com/vtex-rest-api/reference/deletehookconfiguration)

<br>

## Integrating with the Multilevel Omnichannel Inventory

_[Multilevel Omnichannel Inventory](https://help.vtex.com/pt/tutorial/multilevel-omnichannel-inventory--7M1xyCZWUyCB7PcjNtOyw4)_ is the VTEX setting that allows [franchises](https://help.vtex.com/en/tutorial/o-que-e-conta-franquia--kWQC6RkFSCUFGgY5gSjdl) or [white label sellers](https://help.vtex.com/en/tutorial/white-label-seller--5orlGHyDHGAYciQ64oEgKa)' inventory to be sold in marketplaces to which the main account is connected. 

In other words, the feature allows VTEX sellers to sell products from its franchises or white label sellers in a marketplace, without the need to set up the integration with the desired marketplace. For marketplaces, this means selling products from its direct sellers and also physical stores and white label sellers associated with those sellers in a scalable way. For more information, see the link below.

* [Multilevel Omnichannel Inventory](https://help.vtex.com/pt/tutorial/multilevel-omnichannel-inventory--7M1xyCZWUyCB7PcjNtOyw4)

<br>

## Integrating orders from an external marketplace

A VTEX’s store can act both as a [seller](https://help.vtex.com/en/tutorial/configuring-a-seller-on-vtex-marketplace--6g045OkRSjNpqhkExbQRlP) and a [marketplace](https://help.vtex.com/en/tutorial/configuring-vtex-marketplace--7splyp5MqIyt2Iyz5jsNzb) to another VTEX store or an external partner. If you are an [external marketplace](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-guide) that wishes to integrate with VTEX sellers, see the links below to learn how to develop a custom connector to connect with VTEX's architecture and sellers’ orders.

* [Order Integration overview](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-orders)
* [New Order Integration](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-collect-orders)
* [Update Order Status](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-update-order-status)
* [How to update a canceled order’s status in VTEX](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-canceled-orders)

<br>

## Adding optional configurations

There are optional settings available for you to manage your store’s orders. This allows you to take advantage of other VTEX capabilities, such as [inStore](https://help.vtex.com/en/tracks/instore-getting-started-and-setting-up--zav76TFEZlAjnyBVL5tRc), [VTEX DO](https://help.vtex.com/en/tutorial/understanding-the-task-list-vtex-do--tutorials_203), [B2B](https://help.vtex.com/en/tutorial/b2b-overview--5vb9SNXhX2bZnkpAh7ADdC) and [Master Data](https://help.vtex.com/en/tutorial/what-is-master-data--4otjBnR27u4WUIciQsmkAw).

### VTEX inStore

* [Enable order filter by sales associate](https://developers.vtex.com/vtex-rest-api/docs/enable-order-filter-by-sales-associate)
* [Get invoiced orders placed in inStore](https://developers.vtex.com/vtex-rest-api/docs/get-invoiced-orders-placed-in-instore)

### VTEX Do

* [Create Note](https://developers.vtex.com/vtex-rest-api/reference/newnote)
* [Get Notes by orderId](https://developers.vtex.com/vtex-rest-api/reference/getnotesbyorderid)
* [Retrieve Note](https://developers.vtex.com/vtex-rest-api/reference/getnote)
* [Create Task](https://developers.vtex.com/vtex-rest-api/reference/newtask)
* [List tasks](https://developers.vtex.com/vtex-rest-api/reference/listtasksbyassignee)
* [Retrieve Task](https://developers.vtex.com/vtex-rest-api/reference/gettask)
* [Update Task](https://developers.vtex.com/vtex-rest-api/reference/edittask)
* [Add Comment on a Task](https://developers.vtex.com/vtex-rest-api/reference/addcomment)

### B2B

* [How to add and handle custom information in the order (B2B)](https://developers.vtex.com/vtex-rest-api/docs/how-to-add-and-handle-custom-information-in-the-order)

### Master Data

* [Use v2 triggers to interact with orders](https://developers.vtex.com/vtex-rest-api/docs/use-master-data-with-orders)