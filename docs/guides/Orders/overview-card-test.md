<OverviewCard icon='Integration'>

  ## Importing orders from an ERP or Back office
  
  If your store has an ERP integration or another kind of integration for managing orders, it will be necessary to make an integration with VTEX’s platform. The links below provide a general view of the integration flow between a back office system and a VTEX store regarding orders.
  - [Back office (ERP/PIM/WMS)](https://developers.vtex.com/vtex-rest-api/docs/erp-integration-guide)
  - [Set up order integration](https://developers.vtex.com/vtex-rest-api/docs/erp-integration-set-up-order-integration)
  - [Set up order processing](https://developers.vtex.com/vtex-rest-api/docs/erp-integration-set-up-order-processing)
  - [Change order](https://developers.vtex.com/vtex-rest-api/docs/change-order)
  - [FAQ: ERP Integration](https://developers.vtex.com/vtex-rest-api/docs/faq-erp-integration)

</OverviewCard>

<OverviewCard icon='SearchList'>

## Feed v.3
  
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

## Hook

The Hook is a complement to the Feed, which allows an integration to consume order updates data by sending items to an URL provided by the user in the Hook configuration.

- [Get hook configuration](https://developers.vtex.com/vtex-rest-api/reference/gethookconfiguration)
- [Create or update hook configuration](https://developers.vtex.com/vtex-rest-api/reference/hookconfiguration)
- [Delete hook configuration](https://developers.vtex.com/vtex-rest-api/reference/deletehookconfiguration)

</OverviewCard>

<OverviewCard icon='Cart'>

## Placing an order

The action of placing an order involves both the Orders Management module and the [Checkout](https://developers.vtex.com/vtex-rest-api/docs/checkout-overview), and there are different paths to create orders. For more information about order placement, see the links below.

- [Place order](https://developers.vtex.com/vtex-rest-api/reference/placeorder)
- [Process order](https://developers.vtex.com/vtex-rest-api/reference/processorder)
- [Using APIs to place a regular order](https://developers.vtex.com/vtex-rest-api/docs/using-apis-to-place-a-regular-order)
- [Place order from an existing cart](https://developers.vtex.com/vtex-rest-api/reference/placeorderfromexistingorderform)

</OverviewCard>

<OverviewCard icon='SearchDetails'>

## Retrieving order’s details

You can fetch information related to orders in multiple ways and about specific topics. To know more about retrieving orders’ content, see the links below.

### Orders

- [Get order](https://developers.vtex.com/vtex-rest-api/reference/getorder)
- [List orders](https://developers.vtex.com/vtex-rest-api/reference/listorders)

### Conversation

- [Retrieve order conversation](https://developers.vtex.com/vtex-rest-api/reference/getconversation)

### User

- [Retrieve user's orders](https://developers.vtex.com/vtex-rest-api/reference/userorderslist)
- [Retrieve user order details](https://developers.vtex.com/vtex-rest-api/reference/userorderdetails)

### Payment

- [Retrieve payment transaction](https://developers.vtex.com/vtex-rest-api/reference/getpaymenttransaction)

### Marketplace

- [Fetching marketplace information with the Orders API](https://developers.vtex.com/vtex-rest-api/docs/get-marketplace-data-orders-api)
- [Fetching payment details from a Mercado Libre order with Orders API](https://developers.vtex.com/vtex-rest-api/docs/get-payment-data-mercado-libre-orders-api)

</OverviewCard>

<OverviewCard icon='SwitchArrows'>

## Changing an order status

Every order has a life cycle registered in the form of an order flow, which describes the order’s status, possibilities, and updates. For more information, see the following links.
- [Start handling order](https://developers.vtex.com/vtex-rest-api/reference/starthandling)
- [Cancel order](https://developers.vtex.com/vtex-rest-api/reference/cancelorder)

</OverviewCard>

<OverviewCard icon='ChangeCart'>

## Changing an order

Change order is a feature that allows your store to modify the items or prices of an order. This allows you to handle eventual changes motivated by customer mistakes or product unavailability, for example. To know more, see the links below.
- [Change order](https://deploy-preview-200--elated-hoover-5c29bf.netlify.app/docs/guides/(https://developers.vtex.com/vtex-rest-api/docs/change-order)
- [Register change on order](https://developers.vtex.com/vtex-rest-api/reference/registerchange)

</OverviewCard>

<OverviewCard icon='ToStore'>

## Changing seller

It is possible to choose another seller to fulfill a given order after the original seller canceled it. The period during which this action can be performed is called window to change seller, and you can use the endpoints below for this scenario.

- [Get window to change seller](https://developers.vtex.com/vtex-rest-api/reference/getwindowtochangeseller-1)
- [Update window to change seller](https://developers.vtex.com/vtex-rest-api/reference/updatewindowtochangeseller-1)

</OverviewCard>

<OverviewCard icon='PaymentHand'>

## Sending payment notification

For your payment provider to notify the Order Management System that the payment of a given order is completed, use te endpoint Send a payment notification.

In case your store receives the payments outside VTEX’s platform, like payments in cash or with promissories, the store must call this endpoint to notify the OMS, so that the order can follow its flow and be fulfilled.

</OverviewCard>

<OverviewCard icon='Integration'>

## Invoicing an order

When you invoice an order, its status in the order flow changes to Invoiced, which means the order was successfully completed. After an order is invoiced, you can no longer modify it’s status, except when you wish to send a return invoice.

In that case, the endpoint Order invoice notification must be called, and instead of having the field `type` value determined as Output, it will be Input.

- [Order invoice notification](https://developers.vtex.com/vtex-rest-api/reference/invoicenotification)
- [Update order's partial invoice (send tracking number)](https://developers.vtex.com/vtex-rest-api/reference/updatepartialinvoicesendtrackingnumber)
- [Adding a second address for invoicing an order](https://developers.vtex.com/vtex-rest-api/docs/adding-a-second-address-to-the-order)
- [Formatting order invoicing time via API](https://developers.vtex.com/vtex-rest-api/docs/formatting-order-invoicing-time)

</OverviewCard>

<OverviewCard icon='GlobeCart'>

## Tracking an order

Every order has a tracking number that allows you to keep track of its status in the order flow. To send a tracking event to an order that already has a tracking number, use the endpoint Update order's partial invoice.

If you wish to register a tracking number and URL to an order’s invoice, use the endpoint Update order's partial invoice.

</OverviewCard>

<OverviewCard icon='StoreCart'>

## VTEX inStore

- [Enable order filter by sales associate](https://developers.vtex.com/vtex-rest-api/docs/enable-order-filter-by-sales-associate)
- [Get invoiced orders placed in inStore](https://developers.vtex.com/vtex-rest-api/docs/get-invoiced-orders-placed-in-instore)

</OverviewCard>

<OverviewCard icon='List'>

## VTEX DO

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

## B2B

- [How to add and handle custom information in the order (B2B)](https://developers.vtex.com/vtex-rest-api/docs/how-to-add-and-handle-custom-information-in-the-order)

</OverviewCard>

<OverviewCard icon='StoreData'>

## Master Data

- [Use v2 triggers to interact with orders](https://developers.vtex.com/vtex-rest-api/docs/use-master-data-with-orders)

</OverviewCard>
