---
title: "Order modifications"
slug: "order-modifications"
hidden: false
createdAt: "2022-04-06T22:24:27.302Z"
updatedAt: "2022-04-13T17:36:48.363Z"
---

Order modification is a feature that allows your store to modify the items or prices of an order. With this feature, the store can handle potential changes in orders due to customer mistakes, product unavailability, and the inclusion of discounts, among other reasons. Learn more about how it works and its restrictions in the article [Changing items from a completed order](https://help.vtex.com/en/tutorial/changing-items-from-a-complete-order--tutorials_190).

> ℹ️ We recommend that you use the [Create order modifications](https://developers.vtex.com/docs/api-reference/orders-api#patch-/api/order-system/orders/-changeOrderId-/changes) endpoint to modify an order.

>⚠️ The [Order modifications](https://developers.vtex.com/docs/api-reference/orders-api#patch-/api/order-system/orders/-changeOrderId-/changes) feature is not applicable to the Catalog API - Seller Portal.

> Learn more about [Order replacement](https://help.vtex.com/en/tutorial/order-replacement--2IK9mwQjBKseQmE8K8saO8) and how to enable your customers to request order changes.

## Implementation

The [Register modifications on order](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/oms/pvt/orders/-orderId-/changes) endpoint in the Orders API allows you to create a discount, change an item, or increase the price of an order.

>⚠️ When removing or adding items to an order, the inventory of the affected SKUs is not updated automatically. You should update it [using the Logistics API](https://developers.vtex.com/docs/api-reference/logistics-api#put-/logistics/pvt/inventory/skus/-skuId-/warehouses/-warehouseId-).

Modifications made this way can be confirmed using the `changesAttachment` field in the response of the [Get order](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/oms/pvt/orders/-orderId-) endpoint. Alternatively, you may search for the order in the **Orders > Orders management > All orders** section of your Admin panel and see the item modification history in the order details.

>❗ Increasing the price of an order is only available for credit card purchases. The connector must also be able to handle purchases without the CVV, as well as duplicate sequences.

### Errors in Change v1

See below which API errors can be returned when attempting to [modify an order via Change v1 API](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/oms/pvt/orders/-orderId-/changes) and how to avoid or work around them.

#### Request errors

These errors happen when there are one or more errors in the information sent in the request.

| Error | Description |
|-------|-------------|
| `The modification value needs to be greater or equal than zero` | `discountValue` or `incrementValue` is less than 0. |
| `Invalid modification for order` | All of these conditions are true: <br> - `incrementValue` is equal to `discountValue`. <br> - `itemsAdded` is empty. <br> - `itemsRemoved` is empty. |
| `Invalid id for item` | The request body contains either an `itemsAdded` or `itemsRemoved` object that has an empty `id`. |
| `Field reason not set` | Empty `reason` field. |

#### Restriction errors

These are errors returned when the request is correct but the order cannot be modified due to [order change restrictions](https://help.vtex.com/en/tutorial/changing-items-from-a-complete-order--tutorials_190#restrictions).

| Error | Description |
|-------|-------------|
| `It is only allowed to register an order modification when the order is in handling: status = handling, waiting for fulfillment or ready for invoicing` | The fulfillment order is not in a status that allows changes (`handling`, `waiting for fulfillment` and `ready-for-invoice`). |
| `It is not allowed to make modifications to chain orders` | The order has a `chain` origin. |
| `It is only allowed to register a modification in the order when the payment is approved - status = payment-approved` | The marketplace order is not in the status `payment-approved`. |
| `The value of the modification exceeds the order's price` | `discountValue` is greater than the total order price. |
| `Impossible cancel order {0} - Payment not found` | Order is complete, but transaction `id` is empty or null. |
| `Workflow not found for order {0}` | Order has an empty or null `workflowInstanceId`. |
| `Max allowed modifications for order exceeded: {0}` | More than 50 registered modification requests for a single order. |
| `404 Not Found` | At least one of these conditions is true: <br> - The removed item does not exist in the order. <br> - The added item does not exist in the catalog. |
| `Invalid quantity to remove from item {0}` | An item's quantity would be reduced to less than 0 after the modification. |
| `It's not allowed to make modifications in orders without a credit card payment, promissory card, cash, or credit control` | All of these conditions are true: <br> - An attempt to increase order price was made. <br> - The payment method does not support value changes. <br> - The payment method is not credit card payment, promissory card, cash, or credit control. Consult with your payment gateway to see which methods allow for order value changes. |
| `Modification cannot be done. Possible reason: settlement directly done by API` | All of these conditions are true: <br> - An attempt to reduce order price. <br> - The payment method does not support value modifications. Consult with your payment gateway to see which methods allow for order value modifications. |
| `The value of the modification exceeds the order's price` | `discountValue` is greater than the amount allowed for the order transaction. |
| `500 Internal Server Error` | There is an issue with the payment gateway. |

### Errors in Change v2

See below which API errors can be returned when attempting to [modify an order via Change v2 API](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/oms/pvt/orders/-orderId-/changes) and how to avoid or work around them.

#### Errors with exception codes

| Error code | Error message | Description |
|------------|---------------|-------------|
| `CHK0022` | `Invalid id for item.` | The item `id` is not valid or does not exist. |
| `CHK0023` | `Invalid quantity for item.` | The item `quantity` is not allowed (e.g., less than 1). |
| `CHK0034` | `The value of the change exceed the order's price.` | The modification value is greater than the total order price. |
| `CHK0095` | `Changes in chain orders are not allowed.` | Chain orders do not support modifications. |
| `CHK0096` | `Change cannot be done. Possible reason: settlement directly done by API.` | The change operation is not allowed, possibly due to a direct settlement. |
| `CHK0098` | `The change value needs to be greater or equal than zero.` | The value for the change operation must not be negative. |
| `CHK0124` | `Invalid change for order.` | The requested modification is not valid for the current order state or data. |
| `CHK0196` | `Cannot cancel order {0} - Payment not found.` | The order cannot be canceled because no payment was found. |
| `CHK0199` | `OrderGroup {0} not found.` | The order group does not exist. |
| `CHK0201` | `Order {0} not found.` | The order does not exist. |
| `CHK0229` | `Workflow not found for order {0}.` | No workflow was found for the order. |
| `CHK0289` | `Change order request {0} not found.` | The modification order request does not exist. |
| `CHK00342` | `Change order cannot increase the value for this payment method.` | Increasing the order value is not allowed for the selected payment method. |
| `SalesOrderSystem008` | `Cannot Change Cancelled Order.` | Changes cannot be made to orders that have already been canceled. |
| `SalesOrderSystem010` | `It's not possible to remove the item of ID {0} from the original order. Validate your {1} operation items IDs.` | The specified item `id` cannot be removed from the original order. Please verify the `id` in your operation. |
| `SalesOrderSystem011` | `It's not possible to remove more than {0} quantities of the item of ID {1} from the original order. Validate your items quantities at Remove or Replace From operations.` | The `quantity` being removed exceeds the `quantity` available in the order. |
| `SalesOrderSystem012` | `The logistics information couldn't be determined for the item due to the presence of multiple options.` | The order contains multiple logistics options, so the system cannot infer which one to use. |
| `SalesOrderSystem013` | `The logistics information provided was not found on the order.` | The logistics details given do not match any information in the order. |
| `SalesOrderSystem014` | `Change In Progress.` | A change operation is currently in progress for this order. |
| `SalesOrderSystem015` | `A Change V1 has already been applied to this order. Orders can only contain one Change Order version at a time.` | Only one type of order change (v1 or v2) can be applied. A v1 change already exists. |
| `SalesOrderSystem016` | `Cannot Retry Change.` | The change operation cannot be retried. |
| `SalesOrderSystem017` | `Change process was automatically canceled after failed retries.` | The modification was canceled by the system after several failed attempts. |
| `SalesOrderSystem018` | `Unable to communicate with Participants Client.` | The system could not reach the Participants Client service. |
| `SalesOrderSystem019` | `Cannot Update Change Order Settings.` | Settings are being updated by another request. Please try again later. |
| `SalesOrderSystem026` | `Unable to match an item to the information provided. Try providing the item's uniqueId for identification.` | The item could not be identified with the given data. Try using the item's `uniqueId`. |
| `SalesOrderSystem027` | `Change Settings Not Found.` | Change order settings could not be found for this configuration. |
| `SalesOrderSystem029` | `Cannot Add New Products At Change Order When Order Has Multiple Address.` | New products cannot be added to orders with multiple delivery addresses. |
| `SalesOrderSystem035` | `The {0} is not a valid Agreement Type.` | The agreement type is not recognized or supported. |
| `SalesOrderSystem045` | `Invalid address.` | The address is invalid. |
| `SalesOrderSystem046` | `The order change is not allowed after the item invoice has been issued.` | The order modification is not allowed after the item invoice has been issued. |
| `SalesOrderSystem047` | `The address change is not allowed.` | The address modification is not allowed. |
| `SalesOrderSystem048` | `The address change is not allowed when there are packages associated.` | The address modification is not allowed when there are packages associated. |
| `SalesOrderSystem051` | `Change order not allowed with tax hub and multiple delivery docks.` | Order modification is not allowed with tax hub and multiple delivery docks. |
| `SalesOrderSystem055` | `Item modification is not allowed when the measurement unit differs from the original.` | Item modification is not allowed when the measurement unit differs from the original. |
