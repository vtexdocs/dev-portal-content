---
title: "Order modifications"
slug: "order-modifications"
hidden: false
createdAt: "2022-04-06T22:24:27.302Z"
updatedAt: "2022-04-13T17:36:48.363Z"
---

Order modification is a feature that allows your store to modify the items or prices of an order. With this feature, the store can handle potential changes in orders due to customer mistakes, product unavailability, and the inclusion of discounts, among other reasons. Learn more about how it works and its restrictions in the article [Changing items from a completed order](https://help.vtex.com/en/tutorial/changing-items-from-a-complete-order--tutorials_190).

> ℹ️ We recommend you use the [Create order modifications](https://developers.vtex.com/docs/api-reference/orders-api#patch-/api/order-system/orders/-changeOrderId-/changes) endpoint to modify an order.

>⚠️ The [Order modifications](https://developers.vtex.com/docs/api-reference/orders-api#patch-/api/order-system/orders/-changeOrderId-/changes) feature isn't applicable to the Catalog API - Seller Portal.

> Learn more about [Order replacement](https://help.vtex.com/en/tutorial/order-replacement--2IK9mwQjBKseQmE8K8saO8) and how to enable your customers to request order changes.

## Implementation

The [Register modifications on order](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/oms/pvt/orders/-orderId-/changes) endpoint in the Orders API allows you to create a discount, change an item or increase the price of an order.

>⚠️ When removing or adding items to an order, the inventory of the affected SKUs is not updated automatically; you should update it [using the Logistics API](https://developers.vtex.com/docs/api-reference/logistics-api#put-/logistics/pvt/inventory/skus/-skuId-/warehouses/-warehouseId-).

Modifications made this way can be confirmed by the `changesAttachment` field in the response of the [Get order](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/oms/pvt/orders/-orderId-) endpoint. Alternatively, you may search for the order in the **Orders > Orders management > All orders** section of your Admin panel and see the item modification history in the order details.

>❗ Increasing the price of an order is only available for credit card purchases. The connector must also be able to handle purchases without the CVV, as well as duplicated sequences.

### Errors in Change v1

See below which API errors can be returned when attempting to [modify an order via Change v1 API](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/oms/pvt/orders/-orderId-/changes) and how to avoid or work around them.

#### Request errors

These errors happen when there are one or more errors in the information sent in the request.

<table>
    <td><strong> Error</strong></td>
    <td><strong> Description</strong></td>
    <tr>
        <td><code>The modification value needs to be greater or equal than zero</code></td>
        <td><code>discountValue</code> or <code>incrementValue</code> is smaller than 0.</td>
    </tr>
    <tr>
        <td><code>Invalid modification for order</code></td>
        <td>All of these conditions are true:- <code>incrementValue</code> is equal to <code>discountValue</code>.- <code>itemsAdded</code> is empty.- <code>itemsRemoved</code> is empty.</td>
    </tr>
    <tr>
        <td><code>Invalid id for item</code></td>
        <td>The request body contains either an <code>itemsAdded</code> or <code>itemsRemoved</code> object, that has an empty <code>id</code>.</td>
    </tr>
    <tr>
        <td><code>Field reason not set</code></td>
        <td>Empty <code>reason</code> field.</td>
    </tr>
</table>

#### Restriction errors

These are errors that are returned when the request is correct but the order cannot be modified due to [order change restrictions](https://help.vtex.com/en/tutorial/changing-items-from-a-complete-order--tutorials_190#restrictions).

<table>
    <td><strong> Error</strong></td>
    <td><strong> Description</strong></td>
    <tr>
        <td><code>It is only allowed to register an order modification when the order is in handling: status = handling, waiting for fulfillment or ready for invoicing</code></td>
        <td>The fulfillment order is not in a status that allows changes (<code>handling</code>, <code>waiting for fulfillment</code> and <code>ready-for-invoice</code>).</td>
    </tr>
    <tr>
        <td><code>It is not allowed to make modifications to chain orders</code></td>
        <td>The order has a <code>chain</code> origin.</td>
    </tr>
    <tr>
        <td><code>It is only allowed to register a modification in the order when the payment is approved - status = payment-approved</code></td>
        <td>The marketplace order is not on the status <code>payment-approved</code>.</td>
    </tr>
    <tr>
        <td><code>The value of the modification exceeds the order's price</code></td>
        <td><code>discountValue</code> is greater than the total order price.</td>
    </tr>
    <tr>
        <td><code>Impossible cancel order {0} - Payment not found</code></td>
        <td>Order is complete, but transaction <code>id</code> is empty or null.</td>
    </tr>
    <tr>
        <td><code>Workflow not found for order {0}</code></td>
        <td>Order has <code>workflowInstanceId</code> empty or null.</td>
    </tr>
    <tr>
        <td><code>Max allowed modifications for order exceeded: {0}</code></td>
        <td>More than 50 registered modifications requests for a single order.</td>
    </tr>
    <tr>
        <td><code>404 Not Found</code></td>
        <td>At least one of these conditions is true:- Removed item does not exist in the order.- Added item does not exist in the catalog.</td>
    </tr>
    <tr>
        <td><code>Invalid quantity to remove from item {0}</code></td>
        <td>An item’s quantity would be reduced to less than 0 after the modification.</td>
    </tr>
    <tr>
        <td><code>It's not allowed to make modifications in orders without a credit card payment, promissory card, cash or credit control</code></td>
        <td>All of these conditions are true:- Attempt to increase order price.- Payment method does not support value change.- Payment method is not credit card payment, promissory card, cash or credit control.Consult with your payment gateway to see which methods allow for order value change.</td>
    </tr>
    <tr>
        <td><code>Modification cannot be done. Possible reason: settlement directly done by API</code></td>
        <td>All of these conditions are true:- Attempt to reduce order price.- Payment method does not support value modification. Consult with your payment gateway to see which methods allow for order value modification.</td>
    </tr>
    <tr>
        <td><code>The value of the modification exceeds the order's price</code></td>
        <td><code>discountValue</code> is greater than the amount allowed for the order transaction.</td>
    </tr>
    <tr>
        <td><code>500 Internal Server Error</code></td>
        <td>There is an issue with the payment gateway.</td>
    </tr>
</table>

### Errors in Change v2

See below which API errors can be returned when attempting to [modify an order via Change v2 API](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/oms/pvt/orders/-orderId-/changes) and how to avoid or work around them.

#### Errors with exception codes

<table>
    <td><strong> Error code</strong></td>
    <td><strong> Error message</strong></td>
    <td><strong> Description</strong></td>
    <tr>
        <td><code>CHK0022</code></td>
        <td><code>Invalid id for item.</code></td>
        <td>The item <code>id</code> is not valid or does not exist.</td>
    </tr>
    <tr>
        <td><code>CHK0023</code></td>
        <td><code>Invalid quantity for item.</code></td>
        <td>The item <code>quantity</code> is not allowed (e.g., less than 1).</td>
    </tr>
    <tr>
        <td><code>CHK0034</code></td>
        <td><code>The value of the change exceed the order's price.</code></td>
        <td>The modification value is greater than the total order price.</td>
    </tr>
    <tr>
        <td><code>CHK0095</code></td>
        <td><code>Changes in chain orders are not allowed.</code></td>
        <td>Chain orders do not support modifications.</td>
    </tr>
    <tr>
        <td><code>CHK0096</code></td>
        <td><code>Change cannot be done. Possible reason: settlement directly done by API.</code></td>
        <td>The change operation is not allowed, possibly due to a direct settlement.</td>
    </tr>
    <tr>
        <td><code>CHK0098</code></td>
        <td><code>The change value needs to be greater or equal than zero.</code></td>
        <td>The value for the change operation must not be negative.</td>
    </tr>
    <tr>
        <td><code>CHK0124</code></td>
        <td><code>Invalid change for order.</code></td>
        <td>The requested modification is not valid for the current order state or data.</td>
    </tr>
    <tr>
        <td><code>CHK0196</code></td>
        <td><code>Cannot cancel order {0} - Payment not found.</code></td>
        <td>The order cannot be canceled because no payment was found.</td>
    </tr>
    <tr>
        <td><code>CHK0199</code></td>
        <td><code>OrderGroup {0} not found.</code></td>
        <td>The order group does not exist.</td>
    </tr>
    <tr>
        <td><code>CHK0201</code></td>
        <td><code>Order {0} not found.</code></td>
        <td>The order does not exist.</td>
    </tr>
    <tr>
        <td><code>CHK0229</code></td>
        <td><code>Workflow not found for order {0}.</code></td>
        <td>No workflow was found for the order.</td>
    </tr>
    <tr>
        <td><code>CHK0289</code></td>
        <td><code>Change order request {0} not found.</code></td>
        <td>The modification order request does not exist.</td>
    </tr>
    <tr>
        <td><code>CHK00342</code></td>
        <td><code>Change order cannot increase the value for this payment method.</code></td>
        <td>Increasing the order value is not allowed for the selected payment method.</td>
    </tr>
    <tr>
        <td><code>SalesOrderSystem010</code></td>
        <td><code>It's not possible to remove the item of ID {0} from the original order. Validate your {1} operation items IDs.</code></td>
        <td>The specified item <code>id</code> cannot be removed from the original order. Please verify the <code>id</code> in your operation.</td>
    </tr>
    <tr>
        <td><code>SalesOrderSystem011</code></td>
        <td><code>It's not possible to remove more than {0} quantities of the item of ID {1} from the original order. Validate your items quantities at Remove or Replace From operations.</code></td>
        <td>The <code>quantity</code> being removed exceeds the <code>quantity</code> available in the order.</td>
    </tr>
    <tr>
        <td><code>SalesOrderSystem012</code></td>
        <td><code>The logistics information couldn't be determined for the item due to the presence of multiple options.</code></td>
        <td>The order contains multiple logistics options, so the system cannot infer which one to use.</td>
    </tr>
    <tr>
        <td><code>SalesOrderSystem013</code></td>
        <td><code>The logistics information provided was not found on the order.</code></td>
        <td>The logistics details given do not match any information on the order.</td>
    </tr>
    <tr>
        <td><code>SalesOrderSystem015</code></td>
        <td><code>A Change V1 has already been applied to this order. Orders can only contain one Change Order version at a time.</code></td>
        <td>Only one type of order change (v1 or v2) can be applied; a v1 change already exists.</td>
    </tr>
    <tr>
        <td><code>SalesOrderSystem017</code></td>
        <td><code>Change process was automatically canceled after failed retries.</code></td>
        <td>The modification was canceled by the system after several failed attempts.</td>
    </tr>
    <tr>
        <td><code>SalesOrderSystem018</code></td>
        <td><code>Unable to communicate with Participants Client.</code></td>
        <td>The system could not reach the Participants Client service.</td>
    </tr>
    <tr>
        <td><code>SalesOrderSystem026</code></td>
        <td><code>Unable to match an item to the information provided. Try providing the item's uniqueId for identification.</code></td>
        <td>The item could not be identified with the given data. Try using the item's <code>uniqueId</code>.</td>
    </tr>
    <tr>
        <td><code>SalesOrderSystem035</code></td>
        <td><code>The {0} is not a valid Agreement Type.</code></td>
        <td>The agreement type is not recognized or supported.</td>
    </tr>
    <tr>
        <td><code>SalesOrderSystem045</code></td>
        <td><code>Invalid address.</code></td>
        <td>The address is invalid.</td>
    </tr>
    <tr>
        <td><code>SalesOrderSystem046</code></td>
        <td><code>The order change is not allowed after the item invoice has been issued.</code></td>
        <td>The order modification is not allowed after the item invoice has been issued.</td>
    </tr>
    <tr>
        <td><code>SalesOrderSystem047</code></td>
        <td><code>The address change is not allowed.</code></td>
        <td>The address modification is not allowed.</td>
    </tr>
    <tr>
        <td><code>SalesOrderSystem048</code></td>
        <td><code>The address change is not allowed when there are packages associated.</code></td>
        <td>The address change is not allowed when there are packages associated.</td>
    </tr>
    <tr>
        <td><code>SalesOrderSystem051</code></td>
        <td><code>Change order not allowed with tax hub and multiple delivery docks.</code></td>
        <td>Order modification is not allowed with tax hub and multiple delivery docks.</td>
    </tr>
    <tr>
        <td><code>SalesOrderSystem055</code></td>
        <td><code>Item modification is not allowed when the measurement unit differs from the original.</code></td>
        <td>Item modification is not allowed when the measurement unit differs from the original.</td>
    </tr>
</table>
