---
title: "Orders"
slug: "orders-overview"
hidden: false
createdAt: "2020-09-21T22:46:46.589Z"
updatedAt: "2022-10-04T15:07:06.478Z"
---

> **Help us improve our documentation!** Tell us about your experience with this article by filling out [this form](https://forms.gle/fQoELRA1yfKDqmAb8).

This overview article goes over VTEX’s Order Management System (OMS), including relevant links from our developer documentation about this topic. In the following sections you will find information about setting up and managing your orders, creating order integrations with external partners and making optional configurations.

[block:html]
{
  "html": "<!--- STYLE SHEET -->\n\n<style type=\"text/css\">\n    .doc-type {\n        font-size: 16px;\n        padding: 20px 0;\n        width: 100%;\n    }\n\n    .doc-type ul {\n        border-left: 1px rgb(202, 203, 204) solid;\n        color: #78757a;\n        font-size: 13px;\n        padding-left: 1.5em;\n    }\n\n    .doc-type ol {\n        border-left: 1px rgb(202, 203, 204) solid;\n        color: #78757a;\n        font-size: 13px;\n        padding-left: 2.5em;\n    }\n\n    li .see-more {\n        color: #78757a;\n    }\n\n    .see-more::after {\n        content: url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='30' height='14' viewBox='0 -8 59 14' fill='none'><path d='M0 7H57' stroke='rgb(120, 117, 122)'></path><path d='M49 1L57.5 7L49 13' stroke='rgb(120, 117, 122)'></path></svg>\");\n        display: inline-block;\n        margin-left: 6px;\n        text-decoration: none !important;\n    }\n\n    .see-more:hover:after {\n        content: url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='30' height='14' viewBox='0 -8 59 14' fill='none'><path d='M0 7H57' stroke='rgb(20, 32, 50)'></path><path d='M49 1L57.5 7L49 13' stroke='rgb(20, 32, 50)'></path></svg>\");\n        margin-left: 8px;\n    }\n\n    .see-more:hover {\n        color: #0a1019;\n    }\n\n    .column1 {\n        display: inline;\n        width: 100%;\n        float: left;\n        width: 40px;\n        margin: 10px 10px 40px 0;\n    }\n\n    .column2 {\n        display: inline;\n        width: 50%;\n    }\n\n    .column2 .section-title {\n        margin-bottom: 0.5rem;\n        text-decoration: none !important;\n        font-size: 18px;\n        font-weight: 400;\n    }\n\n    .row3 {\n        margin-top: 2rem;\n        list-style: none !important;\n        font-size: 16px;\n        display: block;\n        margin-left: 50px;\n    }\n\n    .row3 li a {\n        text-decoration: none !important;\n    }\n\n    .row4 {\n        margin-top: 2rem;\n        font-size: 16px;\n        display: block;\n        margin-left: 50px;\n    }\n\n    .row4 li a {\n        text-decoration: none !important;\n    }\n  \n  .row5 {\n        margin-top: 2rem;\n        list-style: none !important;\n        font-size: 16px;\n        display: block;\n    }\n\n    .row5 li a {\n        text-decoration: none !important;\n    }\n\n    #faq {\n        background: #fff7f9;\n        padding: 20px;\n        border: none;\n        border-radius: 10px;\n        font-size: 16px;\n        color: #142032;\n    }\n</style>"
}
[/block]

<OverviewCard icon='Integration'>

### Importing orders from an ERP or Back office

If your store has an ERP integration or another kind of integration for managing orders, it will be necessary to make an integration with VTEX’s platform. The links below provide a general view of the integration flow between a back office system and a VTEX store regarding orders.
- [Back office (ERP/PIM/WMS)](https://developers.vtex.com/vtex-rest-api/docs/erp-integration-guide)
- [Set up order integration](https://developers.vtex.com/vtex-rest-api/docs/erp-integration-set-up-order-integration)
- [Set up order processing](https://developers.vtex.com/vtex-rest-api/docs/erp-integration-set-up-order-processing)
- [Change order](https://developers.vtex.com/vtex-rest-api/docs/change-order)
- [FAQ: ERP Integration](https://developers.vtex.com/vtex-rest-api/docs/faq-erp-integration)

</OverviewCard>

## Understanding order flow types

The order flow describes the status, possibilities, and actions throughout the life cycle of an order. In VTEX, there are four [order flows types](https://help.vtex.com/en/tutorial/order-flow-and-status--tutorials_196):

### Marketplace flow

The order flow visible to the store responsible for the sale only.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/orders-overview-0.jpg)

### Seller flow

The order flow visible to the store responsible for handling the order.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/orders-overview-1.png)

### Complete flow

The order flow visible to the store responsible for the order's sale and delivery. In this case, the store acts both as a seller and marketplace.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/orders-overview-2.png)

### Chain flow

The order flow visible to the store that acts as an intermediary between the marketplace and the seller. This flow is similar to the marketplace flow. However, the payment is made only in the marketplace, not in the store that acts as a chain. This flow occurs in [Multilevel Omnichannel Inventory](https://help.vtex.com/en/tutorial/multilevel-omnichannel-inventory--7M1xyCZWUyCB7PcjNtOyw4) sales scenarios.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/orders-overview-3.png)

## Creating an order integration

In the following sections, you will learn how to build order integrations with the Feed and Hook. This is useful when you want to develop an integration between your store’s ERP and the VTEX platform, for example.

[block:html]
{
  "html": "<div>\n  \n<blockquote id='faq' >\n     <svg width=\"24\" height=\"24\" viewBox=\"0 0 24 24\" fill=\"none\" xmlns=\"http://www.w3.org/2000/svg\" style=\"vertical-align: bottom\" >\n            <path fill-rule=\"evenodd\" clip-rule=\"evenodd\"\n                d=\"M3.495 13.465L4.69 15.029L4.948 16.976C5.091 18.056 5.94 18.906 7.02 19.05L8.972 19.311L10.535 20.505C11.4 21.166 12.599 21.166 13.464 20.505L15.028 19.31H15.026L16.974 19.052C18.054 18.909 18.904 18.06 19.048 16.98L19.308 15.028C19.308 15.029 19.912 14.238 20.503 13.465C21.164 12.6 21.163 11.401 20.503 10.536L19.31 8.971L19.052 7.024C18.909 5.944 18.06 5.094 16.98 4.95L15.027 4.69L13.464 3.496C12.599 2.835 11.4 2.835 10.535 3.496L8.971 4.69H8.973L7.025 4.949C5.945 5.092 5.095 5.941 4.951 7.021L4.69 8.973C4.69 8.972 4.086 9.763 3.495 10.536C2.835 11.4 2.835 12.6 3.495 13.465V13.465Z\"\n                stroke=\"#323232\" stroke-width=\"1.5\" stroke-linecap=\"round\" stroke-linejoin=\"round\" />\n            <path d=\"M14.803 10.602L11.302 14.103L9.19901 12.002\" stroke=\"#F71963\" stroke-width=\"1.5\"\n                stroke-linecap=\"round\" stroke-linejoin=\"round\" />\n        </svg>\n    <p style=\"display: inline; padding-left: 10px;\">We strongly recommend you to create an order integration using the <a href=\"https://developers.vtex.com/vtex-rest-api/docs/orders-feed\">Orders Feed v3</a>, instead of using the List orders API request or external services. If you already use an integration based on the API request, you should migrate to using the Feed. Keep in mind that this means changing the integration flow. To learn how to implement this change, see the <a href=\"https://developers.vtex.com/docs/guides/erp-integration-set-up-order-integration \">Set up order integration</a>.\n  </p>\n</blockquote>\n</div>"
}
[/block]

<OverviewCard icon='SearchList'>

### Feed v.3
  
The Orders Feed is a list of order updates, meaning that whenever there is an event in an order, like an order status update, it will be included as a new item in the Feed.
  
- [Feed v3 Guide](https://developers.vtex.com/vtex-rest-api/docs/orders-feed)
- [Get feed configuration](https://developers.vtex.com/vtex-rest-api/reference/getfeedconfiguration)
- [Create or update feed configuration](https://developers.vtex.com/vtex-rest-api/reference/feedconfiguration)
- [Delete feed configuration](https://developers.vtex.com/vtex-rest-api/reference/feedconfigurationdelete)
- [Retrieve feed items](https://developers.vtex.com/vtex-rest-api/reference/getfeedorderstatus1)
- [Commit feed items](https://developers.vtex.com/vtex-rest-api/reference/commititemfeedorderstatus)
- [Test JSONata expression](https://developers.vtex.com/vtex-rest-api/reference/testjsonataexpression)

</OverviewCard>

<OverviewCard icon='FileConfiguration'>

### Hook

The Hook is a complement to the Feed, which allows an integration to consume order updates data by sending items to an URL provided by the user in the Hook configuration.

- [Get hook configuration](https://developers.vtex.com/vtex-rest-api/reference/gethookconfiguration)
- [Create or update hook configuration](https://developers.vtex.com/vtex-rest-api/reference/hookconfiguration)
- [Delete hook configuration](https://developers.vtex.com/vtex-rest-api/reference/deletehookconfiguration)

</OverviewCard>

## Managing orders

There are several actions a VTEX store can perform on orders. In the next sections, you will find the main actions related to a store’s order management routine.

<OverviewCard icon='Cart'>

### Placing an order

The action of placing an order involves both the Orders Management module and the [Checkout](https://developers.vtex.com/vtex-rest-api/docs/checkout-overview), and there are different paths to create orders. For more information about order placement, see the links below.

- [Place order](https://developers.vtex.com/vtex-rest-api/reference/placeorder)
- [Process order](https://developers.vtex.com/vtex-rest-api/reference/processorder)
- [Using APIs to place a regular order](https://developers.vtex.com/vtex-rest-api/docs/using-apis-to-place-a-regular-order)
- [Place order from an existing cart](https://developers.vtex.com/vtex-rest-api/reference/placeorderfromexistingorderform)

</OverviewCard>

[block:html]
{
  "html": "<blockquote id='faq'>\n    <svg width=\"24\" height=\"24\" viewBox=\"0 0 24 24\" fill=\"none\" xmlns=\"http://www.w3.org/2000/svg\" style=\"vertical-align: bottom\" >\n            <path fill-rule=\"evenodd\" clip-rule=\"evenodd\"\n                d=\"M3.495 13.465L4.69 15.029L4.948 16.976C5.091 18.056 5.94 18.906 7.02 19.05L8.972 19.311L10.535 20.505C11.4 21.166 12.599 21.166 13.464 20.505L15.028 19.31H15.026L16.974 19.052C18.054 18.909 18.904 18.06 19.048 16.98L19.308 15.028C19.308 15.029 19.912 14.238 20.503 13.465C21.164 12.6 21.163 11.401 20.503 10.536L19.31 8.971L19.052 7.024C18.909 5.944 18.06 5.094 16.98 4.95L15.027 4.69L13.464 3.496C12.599 2.835 11.4 2.835 10.535 3.496L8.971 4.69H8.973L7.025 4.949C5.945 5.092 5.095 5.941 4.951 7.021L4.69 8.973C4.69 8.972 4.086 9.763 3.495 10.536C2.835 11.4 2.835 12.6 3.495 13.465V13.465Z\"\n                stroke=\"#323232\" stroke-width=\"1.5\" stroke-linecap=\"round\" stroke-linejoin=\"round\" />\n            <path d=\"M14.803 10.602L11.302 14.103L9.19901 12.002\" stroke=\"#F71963\" stroke-width=\"1.5\"\n                stroke-linecap=\"round\" stroke-linejoin=\"round\" />\n        </svg>\n    <p style=\"display: inline; padding-left: 10px;\">The <a href=\"https://developers.vtex.com/docs/guides/orderform-fields\">orderForm</a> is the main object processed by the <a href=\"https://developers.vtex.com/vtex-rest-api/docs/checkout-overview\">Checkout</a> and it stores a lot of contextual information about an order. The orderForm fields will be present in most of OMS's API calls.</p>\n</blockquote>\n"
}
[/block]

<OverviewCard icon='SearchDetails'>

### Retrieving order’s details

You can fetch information related to orders in multiple ways and about specific topics. To know more about retrieving orders’ content, see the links below.

#### Orders

- [Get order](https://developers.vtex.com/vtex-rest-api/reference/getorder)
- [List orders](https://developers.vtex.com/vtex-rest-api/reference/listorders)

#### Conversation

- [Retrieve order conversation](https://developers.vtex.com/vtex-rest-api/reference/getconversation)

#### User

- [Retrieve user's orders](https://developers.vtex.com/vtex-rest-api/reference/userorderslist)
- [Retrieve user order details](https://developers.vtex.com/vtex-rest-api/reference/userorderdetails)

#### Payment

- [Retrieve payment transaction](https://developers.vtex.com/vtex-rest-api/reference/getpaymenttransaction)

#### Marketplace

- [Fetching marketplace information with the Orders API](https://developers.vtex.com/vtex-rest-api/docs/get-marketplace-data-orders-api)
- [Fetching payment details from a Mercado Libre order with Orders API](https://developers.vtex.com/vtex-rest-api/docs/get-payment-data-mercado-libre-orders-api)

</OverviewCard>

<OverviewCard icon='SwitchArrows'>

### Changing an order status

Every order has a life cycle registered in the form of an [order flow](https://help.vtex.com/en/tutorial/order-flow-and-status--tutorials_196), which describes the order’s status, possibilities, and updates. For more information, see the following links.
- [Start handling order](https://developers.vtex.com/vtex-rest-api/reference/starthandling)
- [Cancel order](https://developers.vtex.com/vtex-rest-api/reference/cancelorder)

</OverviewCard>

<OverviewCard icon='ChangeCart'>

### Changing an order

Change order is a feature that allows your store to modify the items or prices of an order. This allows you to handle eventual changes motivated by customer mistakes or product unavailability, for example. To know more, see the links below.
- [Change order](https://deploy-preview-200--elated-hoover-5c29bf.netlify.app/docs/guides/(https://developers.vtex.com/vtex-rest-api/docs/change-order)
- [Register change on order](https://developers.vtex.com/vtex-rest-api/reference/registerchange)

</OverviewCard>

<OverviewCard icon='ToStore'>

### Changing seller

It is possible to choose another seller to fulfill a given order after the original seller canceled it. The period during which this action can be performed is called window to change seller, and you can use the endpoints below for this scenario.

- [Get window to change seller](https://developers.vtex.com/vtex-rest-api/reference/getwindowtochangeseller-1)
- [Update window to change seller](https://developers.vtex.com/vtex-rest-api/reference/updatewindowtochangeseller-1)

</OverviewCard>

<OverviewCard icon='PaymentHand'>

### Sending payment notification

For your payment provider to notify the Order Management System that the payment of a given order is completed, use te endpoint [Send a payment notification](https://developers.vtex.com/vtex-rest-api/reference/sendpaymentnotification).

In case your store receives the payments outside VTEX’s platform, like payments in cash or with promissories, the store must call this endpoint to notify the OMS, so that the order can follow its flow and be fulfilled.

[block:html]
{
  "html": "<blockquote id='faq'>\n    <svg width=\"24\" height=\"24\" viewBox=\"0 0 24 24\" fill=\"none\" xmlns=\"http://www.w3.org/2000/svg\" style=\"vertical-align: bottom\" >\n            <path fill-rule=\"evenodd\" clip-rule=\"evenodd\"\n                d=\"M3.495 13.465L4.69 15.029L4.948 16.976C5.091 18.056 5.94 18.906 7.02 19.05L8.972 19.311L10.535 20.505C11.4 21.166 12.599 21.166 13.464 20.505L15.028 19.31H15.026L16.974 19.052C18.054 18.909 18.904 18.06 19.048 16.98L19.308 15.028C19.308 15.029 19.912 14.238 20.503 13.465C21.164 12.6 21.163 11.401 20.503 10.536L19.31 8.971L19.052 7.024C18.909 5.944 18.06 5.094 16.98 4.95L15.027 4.69L13.464 3.496C12.599 2.835 11.4 2.835 10.535 3.496L8.971 4.69H8.973L7.025 4.949C5.945 5.092 5.095 5.941 4.951 7.021L4.69 8.973C4.69 8.972 4.086 9.763 3.495 10.536C2.835 11.4 2.835 12.6 3.495 13.465V13.465Z\"\n                stroke=\"#323232\" stroke-width=\"1.5\" stroke-linecap=\"round\" stroke-linejoin=\"round\" />\n            <path d=\"M14.803 10.602L11.302 14.103L9.19901 12.002\" stroke=\"#F71963\" stroke-width=\"1.5\"\n                stroke-linecap=\"round\" stroke-linejoin=\"round\" />\n        </svg>\n    <p style="display: inline; padding-left: 10px;">The endpoint <a href="https://developers.vtex.com/vtex-rest-api/reference/sendpaymentnotificatio">Send a payment notification</a>  must be called only after the order payment has been approved. The store might not receive the payment if there is an issue with the settlement and the endpoint has already been called.</p>\n</blockquote>\n"
}
[/block]
  
</OverviewCard>

<OverviewCard icon='Integration'>

### Invoicing an order

When you [invoice an order](https://help.vtex.com/en/tracks/orders--2xkTisx4SXOWXQel8Jg8sa/2WgQrlHTyVo4hLjhUs1LMT), its status in the [order flow](https://help.vtex.com/en/tutorial/order-flow-and-status--tutorials_196) changes to Invoiced, which means the order was successfully completed. After an order is invoiced, you can no longer modify it’s status, except when you wish to send a return invoice.

In that case, the endpoint [Order invoice notification](https://developers.vtex.com/vtex-rest-api/reference/invoicenotification) must be called, and instead of having the field `type` value determined as Output, it will be Input.

- [Order invoice notification](https://developers.vtex.com/vtex-rest-api/reference/invoicenotification)
- [Update order's partial invoice (send tracking number)](https://developers.vtex.com/vtex-rest-api/reference/updatepartialinvoicesendtrackingnumber)
- [Adding a second address for invoicing an order](https://developers.vtex.com/vtex-rest-api/docs/adding-a-second-address-to-the-order)
- [Formatting order invoicing time via API](https://developers.vtex.com/vtex-rest-api/docs/formatting-order-invoicing-time)

</OverviewCard>

<OverviewCard icon='GlobeCart'>

### Tracking an order

Every order has a tracking number that allows you to keep track of its status in the [order flow](https://help.vtex.com/en/tutorial/order-flow-and-status--tutorials_196). To send a tracking event to an order that already has a tracking number, use the endpoint [Update order's partial invoice](https://developers.vtex.com/vtex-rest-api/reference/updatepartialinvoicesendtrackingnumber).

If you wish to register a tracking number and URL to an order’s invoice, use the endpoint [Update order's partial invoice](https://developers.vtex.com/vtex-rest-api/reference/updatepartialinvoicesendtrackingnumber).

</OverviewCard>

## Integrating with the Multilevel Omnichannel Inventory

[Multilevel Omnichannel Inventory](https://help.vtex.com/pt/tutorial/multilevel-omnichannel-inventory--7M1xyCZWUyCB7PcjNtOyw4) is the VTEX setting that allows [franchises](https://help.vtex.com/en/tutorial/o-que-e-conta-franquia--kWQC6RkFSCUFGgY5gSjdl) or [white label sellers](https://help.vtex.com/en/tutorial/white-label-seller--5orlGHyDHGAYciQ64oEgKa)' inventory to be sold in marketplaces to which the main account is connected.

In other words, the feature allows VTEX sellers to sell products from its franchises or white label sellers in a marketplace, without the need to set up the integration with the desired marketplace. For marketplaces, this means selling products from their direct sellers and also physical stores and white label sellers associated with those sellers in a scalable way. For more information, see the article [Multilevel Omnichannel Inventory](https://help.vtex.com/en/tutorial/multilevel-omnichannel-inventory--7M1xyCZWUyCB7PcjNtOyw4).

## Integrating orders from an external marketplace

A VTEX’s store can act both as a [seller](https://help.vtex.com/en/tutorial/configuring-a-seller-on-vtex-marketplace--6g045OkRSjNpqhkExbQRlP) and a [marketplace](https://help.vtex.com/en/tutorial/configuring-vtex-marketplace--7splyp5MqIyt2Iyz5jsNzb) to another VTEX store or an external partner. If you are an [external marketplace](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-guide) that wishes to integrate with VTEX sellers, see the links below to learn how to develop a custom connector to connect with VTEX's architecture and sellers’ orders.
[block:html]
{
  "html": "<!--- Integrating orders from an external marketplace -->\n\n\n<div class=\"doc-type\"> \n\t<div class=\"column2\">\n\t<p>\n    <ul class=\"row5\">\n        <li><a class=\"vtex-section-option\"\n                href=\"https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-orders\">Order Integration overview</a></li>\n        <li><a class=\"vtex-section-option\"\n                href=\"https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-collect-orders\">New Order Integration</a>\n        </li>\n        <li><a class=\"vtex-section-option\"\n                href=\"https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-update-order-status\">Update Order Status</a>\n      \t</li>\n        <li><a class=\"vtex-section-option\"\n                href=\"https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-canceled-orders\">How to update a canceled order’s status in VTEX</a></li>\n    </ul>\n  </p>\n</div>\n</div>"
}
[/block]

## Adding optional configurations

There are optional settings available for you to manage your store’s orders. This allows you to take advantage of other VTEX capabilities, such as [inStore](https://help.vtex.com/en/tracks/instore-getting-started-and-setting-up--zav76TFEZlAjnyBVL5tRc), [VTEX DO](https://help.vtex.com/en/tutorial/understanding-the-task-list-vtex-do--tutorials_203), [B2B](https://help.vtex.com/en/tutorial/b2b-overview--5vb9SNXhX2bZnkpAh7ADdC) and [Master Data](https://help.vtex.com/en/tutorial/what-is-master-data--4otjBnR27u4WUIciQsmkAw).

<OverviewCard icon='StoreCart'>

### VTEX inStore

- [Enable order filter by sales associate](https://developers.vtex.com/vtex-rest-api/docs/enable-order-filter-by-sales-associate)
- [Get invoiced orders placed in inStore](https://developers.vtex.com/vtex-rest-api/docs/get-invoiced-orders-placed-in-instore)

</OverviewCard>

<OverviewCard icon='List'>

### VTEX DO

- [Create Note](https://developers.vtex.com/vtex-rest-api/reference/newnote)
- [Get Notes by orderId](https://developers.vtex.com/vtex-rest-api/reference/getnotesbyorderid)
- [Retrieve Note](https://developers.vtex.com/vtex-rest-api/reference/getnote)
- [Create Task](https://developers.vtex.com/vtex-rest-api/reference/newtask)
- [List tasks](https://developers.vtex.com/vtex-rest-api/reference/listtasksbyassignee)
- [Retrieve Task](https://developers.vtex.com/vtex-rest-api/reference/gettask)
- [Update Task](https://developers.vtex.com/vtex-rest-api/reference/edittask)
- [Add Comment on a Task](https://developers.vtex.com/vtex-rest-api/reference/addcomment)

</OverviewCard>

<OverviewCard icon='Blocks'>

### B2B

- [How to add and handle custom information in the order (B2B)](https://developers.vtex.com/vtex-rest-api/docs/how-to-add-and-handle-custom-information-in-the-order)

</OverviewCard>

<OverviewCard icon='StoreData'>

### Master Data

- [Use v2 triggers to interact with orders](https://developers.vtex.com/vtex-rest-api/docs/use-master-data-with-orders)

</OverviewCard>
