---
title: "External seller connector"
slug: "external-seller-integration-connector"
hidden: false
createdAt: "2020-09-01T13:47:40.310Z"
updatedAt: "2022-09-30T16:51:08.972Z"
---
The seller integration flow comprises eight different API requests. Four of these are calls that the seller should make to the marketplace. The other four are requests that the marketplace will need to make to the seller. So, for these, you will need to implement endpoints that are prepared to receive specific request bodies and respond with specific objects.

In the table below, you will find every API request needed for each step of the integration. Each one of them links to their specific API Reference documentation, where you can find the request URLs, methods, headers, the explanation of every field, and examples of requests and responses.

## Seller integration requests flow

| Step | API Request | Request Target |
|---|---|---|
| [Catalog Notification](#catalog-notification) | <span class="api pg-type type-post">post</span><a href="https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog_system/pvt/skuseller/changenotification/-skuId-">Change Notification</a>| ➡ Marketplace |
| [Catalog Registration](#catalog-registration) | <span class="api pg-type type-put">put</span><a href="https://developers.vtex.com/docs/guides/marketplace-api#manage-suggestions">Send SKU Suggestion</a> | ➡ Marketplace |
| [Catalog and Storefront Update](#catalog-update) | <span class="api pg-type type-post">post</span><a href="https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-seller-fulfillment#post-/pvt/orderForms/simulationn">Fulfillment Simulation</a>  | ⬅ Seller |
| [Order Placement](#order-placement) | <span class="api pg-type type-post">post</span><a href="https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-seller-fulfillment#post-/pvt/orders">Order Placement</a>  | ⬅ Seller |
| [Order Dispatching](#order-dispatching) | <span class="api pg-type type-post">post</span><a href="https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-seller-fulfillment#post-/pvt/orders/-sellerOrderId-/fulfill">Authorize Fulfillment</a>  | ⬅ Seller |
| [Order Invoicing and Tracking](#order-invoicing) | <span class="api pg-type type-post">post</span><a href="https://developers.vtex.com/docs/api-reference/orders-api#post-/api/oms/pvt/orders/-orderId-/invoice">Order Invoice Notification</a>  | ➡ Marketplace |
| [Cancellation by the Marketplace](#cancellation-by-the-marketplace) | <span class="api pg-type type-post">post</span><a href="https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-seller-fulfillment#post-/pvt/orders/-orderId-/cancel">Marketplace Order Cancellation</a> | ⬅ Seller |
| [Cancellation by the Seller](#cancellation-by-the-seller) | <span class="api pg-type type-post">post</span><a href="https://developers.vtex.com/docs/api-reference/marketplace-protocol#post-/pvt/orders/-marketplaceOrderId-/cancel">Cancel Order</a>  | ➡ Marketplace |
| [Order invoicing](#order-invoicing)                   | <span class="api pg-type type-post">post</span><a href="https://developers.vtex.com/docs/api-reference/marketplace-protocol#post-/pvt/orders/-marketplaceOrderId-/invoice">Send invoice</a>                     | ➡ Marketplace  |
| [Send tracking information](#order-tracking)       | <span class="api pg-type type-post">post</span><a href="https://developers.vtex.com/docs/api-reference/marketplace-protocol#post-/pvt/orders/-marketplaceOrderId-/invoice/-invoiceNumber-">Send tracking information</a>     | ➡ Marketplace  |
| [Update tracking status](#order-tracking)          | <span class="api pg-type type-post">post</span><a href="https://developers.vtex.com/docs/api-reference/marketplace-protocol#post-/pvt/orders/-marketplaceOrderId-/invoice/-invoiceNumber-/tracking">Update tracking status</a>         | ➡ Marketplace  |

>ℹ️ To help you test the integration requests and see in practice how they behave, we've assembled a Postman API Collection with all eight requests listed in this guide, including the necessary URLs, methods, headers, and example request bodies.\n\n[![Run in Postman](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Integration-Guides/external-seller-integration-guide/button_32.svg)](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/external-seller-integration-connector-0.png)

Let’s walk through each of the steps in the integration.

## Catalog notification

The seller is responsible for suggesting new SKUs to be sold in the marketplace, as well as notifying the marketplace about updates to SKUs that already exist. Both scenarios begin with a catalog notification.
To send this notification, the seller must call the `[POST ChangeNotification](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog_system/pvt/skuseller/changenotification/-skuId-)` endpoint provided by the marketplace.

Use the **Change Notification API** to notify the marketplace about changes in the **catalog information** of a SKU, such as:

- Name  
- Description  
- Images  
- EAN  
- Specifications

[block:callout]
{
  "type": "info",
  "body": "For price and inventory change notification, please see the [Catalog Update](#catalog-update) section."
}
[/block]

If the request is properly authenticated and formatted, there are two possible responses:

- **200 OK**: The SKU already exists in the marketplace. The seller should proceed to update its catalog information.
- **404 Not Found**: `"Seller StockKeepingUnit not found for this seller id"`  
  This means the SKU does not yet exist in the marketplace. The seller must first register the SKU offer before it can be updated.

The “status 404” response means that the SKU does not yet exist in the marketplace. In this case, in order to push the SKU offer to the marketplace, the seller should register the seller.

The “status 200” response means that the SKU informed in the request already exists in the seller. In this case, the seller should *update* the SKU information.

## Catalog registration

When the marketplace responds to the Change Notification request with status 404, it means that the SKU informed by the seller does not exist in the marketplace’s catalog. In this case, the seller should send an SKU offer to the marketplace.

[block:callout]
{
  "type": "info",
  "body": "The catalog is owned by the marketplace, and the seller has no direct access to it. This is why every SKU is sent as an offer, which needs to be approved by the marketplace in order to become an SKU actually registered in the marketplace’s catalog."
}
[/block]

The SKU offer is sent through the <span class="pg-type type-put">put</span><span class="api"><a href="https://developers.vtex.com/docs/guides/marketplace-api#manage-suggestions">Send SKU Suggestion</a></span> API request. In this request, the seller informs mandatory information about the SKU, such as the product and SKU name, the seller ID, and the image URL.

[block:callout]
{
  "type": "warning",
  "body": "Don’t forget that, for the Save Suggestion request to work, the marketplace must have created the proper brands and categories in their account. This should be done in the setup phase of the integration."
}
[/block]

Besides sending new SKU offers to the marketplace, the seller can update offers that have already been sent and have not yet been approved by the marketplace. To do this, you should make the same request used to create a new offer. In this case, the offer information will be replaced by the new one.
[block:callout]
{
  "type": "warning",
  "body": "An offer update only works if the original offer hasn’t yet been approved or disapproved by the marketplace. An approved offer ceases do exist, and the SKU registration that comes from it can only be edited by the marketplace."
}
[/block]

## Catalog update

To notify the marketplace of price and inventory changes, the seller must call the following endpoints:

- [Notify marketplace of price update](https://developers.vtex.com/docs/api-reference/marketplace-apis#post-/notificator/-sellerId-/changenotification/-skuId-/price)  
- [Notify marketplace of inventory update](https://developers.vtex.com/docs/api-reference/marketplace-apis#post-/notificator/-sellerId-/changenotification/-skuId-/inventory)

After these notifications, the marketplace will reach out to the seller to retrieve the latest SKU information.

### Endpoint implementation

The endpoint that the marketplace will call is the <span class="pg-type type-post">post</span><span class="api"><a href="https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-seller-fulfillment#post-/pvt/orderForms/simulation">Fulfillment Simulation</a></span> endpoint. The marketplace will send an object containing an array of items. The seller must use this list to get the updated information about the referred SKUs and send them back to the marketplace, following the response format explained in the API Reference.

Be mindful to add `/api` in your endpoint's base url for the call to function properly.

[block:callout]
{
  "type": "warning",
  "body": "This route directly impacts the marketplace checkout flow and is essential to the functioning of the integration. Because of that, it needs to have high performance and availability."
}
[/block]

[block:callout]
{
  "type": "warning",
  "body": "The maximum time that VTEX marketplaces wait for a response from the fulfillment endpoint is 2.5 seconds. After that, the product will be considered unavailable or inactive."
}
[/block]

## Storefront update

During the order flow, the marketplace storefront needs to be constantly fetching the updated price and inventory of each SKU in the cart. This is essential to guarantee that the customer will always be presented with the most updated information possible.

As in the [catalog update](#catalog-update) step, this information is provided by the seller through the <span class="pg-type type-post">post</span><span class="api"><a href="https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-seller-fulfillment#post-/pvt/orderForms/simulation">Fulfillment Simulation</a></span> endpoint. As in that step, the same request format should be expected and the same response format should be returned.

When the Fulfillment Simulation call is applied in the Storefront simulation scenario,  the request from VTEX does not send the paramenters `country` and `postalCode`.

## Seller processing payments

If the seller is processing payments, once the [necessary configurations](https://developers.vtex.com/vtex-rest-api/docs/external-seller-processing-payments) are set up, the seller must send their VTEX account name to the marketplace.

You can find your account name in your VTEX environment by accessing **Account Settings > Account Management > Account**, and looking for the `Account Name` field.

This information will be added in the `merchantName` field in the [Storefront Update](https://developers.vtex.com/docs/guides/external-seller-integration-connector#storefront-update) and [Order Placement](https://developers.vtex.com/docs/guides/external-seller-integration-connector#order-placement) steps of the integration guide. This is the field that confirms that payments will be done on the seller's side:

`"merchantName": "sellerAccountName",`

## Order placement

Once the customer finishes their checkout, the marketplace needs to let the seller know there is a newly placed order.

### Endpoint implementation

The marketplace notifies the seller about a new order through the <span class="pg-type type-post">post</span><span class="api"><a href="https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-seller-fulfillment#post-/pvt/orders">Order Placement</a></span> endpoint, which needs to be implemented by the seller.

The marketplace will send information such as the items contained in the cart, the client’s profile data, the shipping data, and the payment data. With that, the seller will be able to create the order in their own store.

## Order dispatching

After the payment is finished and approved, the marketplace sends a request to the seller to notify it that the fulfillment process can be started.

### Endpoint implementation

This notification is done through a request to the <span class="pg-type type-post">post</span><span class="api"><a href="https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-seller-fulfillment#post-/pvt/orders/-sellerOrderId-/fulfill">Authorize Fulfillment</a></span> endpoint, which needs to be implemented by the seller.

The body of this request contains only one information: the `marketplaceOrderId`, which identifies the order in the marketplace. The seller should use this ID to trigger the fulfillment process.

## Order invoicing

Once the fulfillment process is triggered and the invoice is issued by the seller, the invoice data must be sent to the marketplace. The seller sends this information through the <span class="pg-type type-post">post</span><span class="api"><a href="https://developers.vtex.com/docs/api-reference/orders-api#post-/api/oms/pvt/orders/-orderId-/invoice">Order Invoice Notification</a></span> request.

## Order tracking

The same endpoint called by the seller to send the invoice is used to send the order tracking information, which holds the following fields:

- Carrier
- Tracking identifier
- Tracking URL

In this case, the <span class="pg-type type-post">post</span><span class="api"><a href="https://developers.vtex.com/docs/api-reference/orders-api#post-/api/oms/pvt/orders/-orderId-/invoice">Order Invoice Notification</a></span> should happen once the seller delivers the package to the carrier and receives the tracking data from it.

## Cancellation by the marketplace

Order cancellations are never wanted, but they happen in every store. So the seller must be ready to receive order cancellation requests from the marketplace. For that, you will need to implement the last endpoint in this integration guide.

### Endpoint implementation

The <span class="pg-type type-post">post</span><span class="api"><a href="https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-seller-fulfillment#post-/pvt/orders/-orderId-/cancel">Marketplace Order Cancellation</a></span> endpoint  must be implemented on the seller's side. This call should be made twice: once for the *Evaluate cancellation request* scenario, and a second time to *Confirm cancellation* or *Refuse cancellation*

For the seller to:

- **Evaluate a cancellation request:** it is possible to send an empty body as a response to the cancellation request, meaning that the seller is evaluating whether to proceed with the cancellation or not.
- **Confirm the cancellation request:** it is possible to confirm the order cancellation by the marketplace by responding to the call with a body including only one information: the `marketplaceOrderId`, which identifies the order in the marketplace. The seller should use this ID to trigger the cancellation of the corresponding order. The seller should then respond with the same `marketplaceOrderId` and also with the `orderId`, which identifies the order in the seller, the date and time of the notification receipt, and a protocol code that confirms the receipt of the request (which may have the value `null`).
- **Refuse a cancellation request:** it is possible to to [send the Invoice](https://developers.vtex.com/docs/api-reference/marketplace-protocol#post-/pvt/orders/-marketplaceOrderId-/invoice), meaning that the cancellation has been denied, and the flow continues to the [Order Invoicing](https://developers.vtex.com/docs/guides/external-seller-integration-connector#order-invoicing) step, and the ones that follow it.

## Cancellation by the seller

On certain occasions, the seller may also need to cancel the order itself. This might happen, for example, if there’s a problem with the order that prevents the seller from fulfilling it. In this case, the seller must call the <span class="pg-type type-post">post</span><span class="api"><a href="https://developers.vtex.com/docs/api-reference/marketplace-protocol#post-/pvt/orders/-marketplaceOrderId-/cancel">Cancel Order</a></span> endpoint.

> ⚠️ If the order status is `Invoiced`, the order can only be canceled if—before using the Cancel Order endpoint—the seller sends a return invoice.\n\nTo do this, you must use the Order Invoice Notification endpoint, explained in the [Order invoicing](https://developers.vtex.com/docs/guides/external-seller-integration-connector#order-invoicing) session. To inform the system that you are sending a return invoice, you must use the value input for the field type of the request body.\n\nAfter doing this, you will be able to send a cancellation request for the invoiced order, by using the endpoint referenced below.

## Setting payment conditions

---

After building the endpoints listed in this guide and preparing your integration to send the requests expected by the marketplace, there is only one final configuration step before the VTEX marketplace can receive SKU offers from the external seller.
