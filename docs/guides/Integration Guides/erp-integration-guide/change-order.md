---
title: "Change order"
slug: "change-order"
hidden: false
createdAt: "2022-04-06T22:24:27.302Z"
updatedAt: "2022-04-13T17:36:48.363Z"
---
Change order is a feature that allows your store to modify the items or prices of an order. With this feature, the store can handle eventual changes in orders motivated by customer mistakes, product unavailability, and the inclusion of discounts, among other things. Learn more about how it works and its restrictions in the article [Changing items from a completed order](https://help.vtex.com/en/tutorial/changing-items-from-a-complete-order--tutorials_190#).
[block:callout]
{
  "type": "info",
  "body": "Learn more about [Order replacement](https://help.vtex.com/en/tutorial/order-replacement--2IK9mwQjBKseQmE8K8saO8#) and how to enable your customers to easily request order changes."
}
[/block]

## Implementation

The [Register change on order](https://developers.vtex.com/vtex-rest-api/reference/registerchange) endpoint in the Orders API allows you to create a discount, change an item or increase the price of an order.
[block:callout]
{
  "type": "warning",
  "body": "When removing or adding items to an order, the inventory of the affected SKUs is not updated automatically - you should update it [using the Logistics API](https://developers.vtex.com/vtex-rest-api/reference/updateinventorybyskuandwarehouse)."
}
[/block]
Changes made this way can be confirmed by the `changesAttachment` field in the response of the [Get order](https://developers.vtex.com/vtex-rest-api/reference/getorder) endpoint. Alternatively, you may search for the order in the *Orders > Orders management > All orders* section of your Admin panel and see the item change history in the order details.
[block:callout]
{
  "type": "danger",
  "body": "Increasing the price of an order is only available for credit card purchases. The connector must also be able to handle purchases without the CVV, as well as duplicated sequences."
}
[/block]

### Errors

See below what API errors can be returned when attempting to [change an order via API](https://developers.vtex.com/vtex-rest-api/reference/registerchange) and how to avoid or work around them.

#### Request errors

These errors happen when there are one or more errors in the information sent in the request.

<table>
    <td><b> Error</b></td>
    <td><b> Description</b></td>
    <tr>
        <td><code>The change value needs to be greater or equal than zero</code></td>
        <td><code>discountValue</code> or <code>incrementValue</code> is smaller than 0.</td>
    </tr>
    <tr>
        <td><code>Invalid change for order</code></td>
        <td>All of these conditions are true:- <code>incrementValue</code> is equal to <code>discountValue</code>.-
            <code>itemsAdded</code> is empty.- <code>itemsRemoved</code> is empty.</td>
    </tr>
    <tr>
        <td><code>Invalid id for item</code></td>
        <td>The request body contains either an <code>itemsAdded</code> or <code>itemsRemoved</code> object, that has
            anempty <code>id</code>.</td>
    </tr>
    <tr>
        <td><code>Field reason not set</code></td>
        <td>Empty <code>reason</code> field.</td>
    </tr>
</table>

#### Restriction errors

These are errors that are returned when the request is correct but the order cannot be modified due to [order change restrictions](https://help.vtex.com/en/tutorial/changing-items-from-a-complete-order--tutorials_190#restrictions).

<table>
    <td><b> Error</b></td>
    <td><b> Description</b></td>
    <tr>
        <td><code>Só é permitido registrar mudanças (change) quando o pedido estiver em manuseio: status = handling, waiting for fulfillment or ready for invoicing</code>
        </td>
        <td>The fulfillment order is not in a status that allows changes (<code>handling</code>,
            <code>waiting for fulfillment</code> and <code>ready-for-invoice</code>).</td>
    </tr>
    <tr>
        <td><code>Não é permitido fazer changes em pedidos de cadeia</code></td>
        <td>The order has a <code>chain</code> origin.</td>
    </tr>
    <tr>
        <td><code>Só é permitido registrar uma mudança (change) quando o pedido estiver com o pagamento aprovado - status = payment-approved</code>
        </td>
        <td>The marketplace order is not on the status <code>payment-approved</code>.</td>
    </tr>
    <tr>
        <td><code>The value of the change exceed the order's price</code></td>
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
        <td><code>Max allowed changes for order exceeded: {0}</code></td>
        <td>More than 50 registered change requests for a single order.</td>
    </tr>
    <tr>
        <td><code>404 Not Found</code></td>
        <td>At least one of these conditions is true:- Removed item does not exist in the order.- Added item does not
            exist in the catalog.</td>
    </tr>
    <tr>
        <td><code>Invalid quantity to remove from item {0}</code></td>
        <td>An item’s quantity would be reduced to less than 0 after the change.</td>
    </tr>
    <tr>
        <td><code>It's not allowed to make changes in orders without a credit card payment, promissory card, cash or credit control</code></td>
        <td>All of these conditions are true:- Attempt to increase order price.- Payment method does not support value
            change.- Payment method is not credit card payment, promissory card, cash or credit control.Consult with
            your payment gateway to see which methods allow for order value change.</td>
    </tr>
    <tr>
        <td><code>Change cannot be done. Possible reason: settlement directly done by API</code></td>
        <td>All of these conditions are true:- Attempt to reduce order price.- Payment method does not support value
            change.Consult with your payment gateway to see which methods allow for order value change.</td>
    </tr>
    <tr>
        <td><code>The value of the change exceed the order's price</code></td>
        <td><code>discountValue</code> is greater than the amount allowed for the order transaction.</td>
    </tr>
    <tr>
        <td><code>500 Internal Server Error</code></td>
        <td>There is an issue with the payment gateway.</td>
    </tr>
</table>
