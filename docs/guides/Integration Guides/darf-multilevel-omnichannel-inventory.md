---
title: "Darf Multilevel Omnichannel Inventory"
slug: "darf-multilevel-omnichannel-inventory"
hidden: true
createdAt: "2022-11-18T19:13:29.256Z"
updatedAt: "2022-11-18T19:13:29.256Z"
---

A [marketplace](https://help.vtex.com/pt/tutorial/estrategias-de-marketplace-na-vtex--tutorials_402) is the environment where the product is sold, or the storefront. The [seller](https://help.vtex.com/en/tutorial/estrategias-de-marketplace-na-vtex--tutorials_402#selling-on-marketplaces) owns the product and is responsible for fulfillment. [VTEX promotes digital collaboration](https://vtex.com/us-en/ecommerce-marketplace/) by allowing multiple combinations of architecture between these two entities. One of these combinations is called [Multilevel Omnichannel Inventory](https://help.vtex.com/pt/tutorial/multilevel-omnichannel-inventory--7M1xyCZWUyCB7PcjNtOyw4).

*Multilevel Omnichannel Inventory* is the VTEX setting that allows [franchises](https://help.vtex.com/en/tutorial/o-que-e-conta-franquia--kWQC6RkFSCUFGgY5gSjdl) or [white label sellers](https://help.vtex.com/en/tutorial/white-label-seller--5orlGHyDHGAYciQ64oEgKa)' inventory to be sold in marketplaces to which the main account is connected.

For VTEX sellers, this means being able to sell products from its franchises or white label sellers in a marketplace, without the need to set up the integration with the desired marketplace for all franchise stores, and white label sellers.

For marketplaces, this means selling products from its direct sellers and also physical stores and white label sellers associated with those sellers in a scalable way.

[block:callout]
{
  "type": "warning",
  "body": "To know restrictions around the use of Multilevel Omnichannel Inventory, check out our [Multilevel Omnichannel Inventory Help article](https://help.vtex.com/pt/tutorial/multilevel-omnichannel-inventory--7M1xyCZWUyCB7PcjNtOyw4).",
  "title": "Restrictions of use"
}
[/block]

## Account architecture

When a store sells its products in a marketplace, we have a one-level relationship between seller and marketplace. However, VTEX's architecture allows stores to act as both sellers and marketplaces, expanding the number of possible combinations.

Stores that have white label sellers and franchises are marketplaces to those accounts. But they can also be connected to external marketplaces, becoming sellers themselves. In this case, we have a three level architecture, as illustrated in the image below.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Integration%20Guides/darf-multilevel-omnichannel-inventory-0_31.png)

- **Marketplace (level 1):** storefront where the product is sold and order is placed.
- **Direct seller (level 2):** main account, integrated to the marketplace level 1. Serves as a marketplace for white label sellers, franchise accounts and physical stores connected to it.
- **Franchise accounts/physical stores (level 3):** owns the product, and is responsible for fulfillment. Connected as white label sellers to the main account.

With the Multilevel Omnichannel Inventory setting, all franchise accounts and white label sellers (level 3) are already fully integrated to a store's main account (level 2). This means that when the main account sets up an integration with an external marketplace (level 1), the franchise accounts can be integrated as well, no longer being necessary to manage each franchise individually in order to set up its integration with the marketplace.

[block:callout]
{
  "type": "info",
  "body": "This feature is valid for [VTEX marketplaces](https://help.vtex.com/pt/tutorial/marketplace-strategies-at-vtex--tutorials_402#ser-um-marketplace-vtex), [native connectors](https://help.vtex.com/pt/tutorial/marketplace-strategies-at-vtex--tutorials_402#integrado-a-conector-nativo-vtex) and [certified partners](https://help.vtex.com/pt/tutorial/marketplace-strategies-at-vtex--tutorials_402#integrado-a-conector-certificado-parceiro)."
}
[/block]

## Order flow

The Multilevel Omnichannel Inventory also affects an order's flow. The order flow describes the status, possibilities, and actions throughout the life cycle of an order. With the flow, retailers can also track the mapped order status on the platform. The table below summarizes all types of order flows that VTEX supports.

<table>
    <tr>
        <td><strong>Order source and destination</strong></td>
        <td><strong>Order type and workflow</strong></td>
    </tr>
    <tr>
        <td>VTEX store is the <strong>source</strong> of an order →</td>
        <td><a
                href="https://help.vtex.com/en/tutorial/fluxo-e-status-de-pedidos--tutorials_196#marketplace-flow">Marketplaceorder</a>
            with Checkout Workflow.</td>
    </tr>
    <tr>
        <td>VTEX store is <strong>intermediate</strong> in the order flow →</td>
        <td><a
                href="https://help.vtex.com/en/tutorial/fluxo-e-status-de-pedidos--tutorials_196#chain-flow">Chainorder</a>
            with Chain Workflow.</td>
    </tr>
    <tr>
        <td>VTEX store is the <strong>destination</strong> of an order →</td>
        <td><a
                href="https://help.vtex.com/en/tutorial/fluxo-e-status-de-pedidos--tutorials_196#seller-flow">Sellerorder</a>
            with Fulfillment Workflow.</td>
    </tr>
    <tr>
        <td>VTEX store is both the <strong>source</strong> and the <strong>destination</strong> →</td>
        <td><a
                href="https://help.vtex.com/en/tutorial/fluxo-e-status-de-pedidos--tutorials_196#complete-flow">Completeorder</a>
            flow with Fulfillment workflow.</td>
    </tr>
</table>

The Multilevel Omnichannel Inventory setting allows the entire inventory from a physical store network to be integrated into marketplaces, creating **chain orders**.

Let's break down how chain orders are applied in Multilevel Omnichannel Inventory architecture:

- Order originates in the marketplace (level 1).
- Order goes through an intermediate agent, in this case, the direct sellers (level 2).
- Order reaches its destination, to be fulfilled by the white label sellers (level 3).

Therefore, chain orders in direct seller have characteristics that come from both *marketplaces*, because they take the role of a seller's marketplace, and *sellers*, since they are also sellers of a marketplace.

Check out the order flow for chain orders in the image below:

​
![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Integration%20Guides/darf-multilevel-omnichannel-inventory-1_94.png)
The order flow seen by the level 2 store in a Multilevel Omnichannel Inventory is similar to the marketplace order flow, except for receiving the payment for orders. In the Payment pending stage, instead of the chain receiving payment directly from the gateway, the marketplace informs the chain it has received the payment confirmation.

## Initial setup

The setup for Multilevel Omnichannel Inventory must be made by the marketplace in their VTEX Admin or through REST API. This setup can be made in sellers that are already integrated, or sellers being added for the first time.

To configure Multilevel Omnichannel Inventory via REST API:

1. The marketplace must call the endpoint [Configure Seller Account](https://developers.vtex.com/vtex-rest-api/reference/upsertsellerrequest).

2. Fill the `fulfillmentEndpoint` field with the seller's checkout endpoint, following the example below:

```
https://{{sellerAccount}}.vtexcommercestable.com.br/api/checkout?affiliateid={{affiliateId}}&sc={{salesChannel
```

3. Substitute the placeholders for the following values:

- **sellerAccount**: [account name](https://help.vtex.com/pt/tutorial/o-que-e-account-name--i0mIGLcg3QyEy8OCicEoC) of the seller in VTEX.

- **affiliateId**: the 3-digit [afiliate](https://help.vtex.com/pt/tutorial/o-que-e-afiliado--4bN3e1YarSEammk2yOeMc0) identification code created by the seller. The seller must inform this ID to the marketplace so that the marketplace can complete the configuration process.

- **salesChannel**: Sales channel (or [trade policy](https://help.vtex.com/en/tutorial/como-funciona-uma-politica-comercial--6Xef8PZiFm40kg2STrMkMV#master-data)) associated to the seller account created. The seller must inform this ID to the marketplace so that the marketplace can complete the configuration process.

![Chain Order Flow](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Integration%20Guides/darf-multilevel-omnichannel-inventory-2_119.png)

## API Integration

When using a Multilevel Omnichannel Inventory architecture, the endpoints used in the integration's architecture are the following:

- [Place Order](#place-multilevel-omnichannel-order): create the order in the seller responsible for fulfillment.
- [Marketplace Order Authorization](#marketplace-order-authorization): progressing the order, after the marketplace's authorization.
- [Cancel Order Notification](#cancel-order-notification): route to be notified of the seller's, or of the chain agent's (in this case seller level 2) cancellation.
- [Order Invoice Notification](#order-invoice-notification): route to receive invoice notification from the seller, or of the chain agent's (in this case seller level 2).

Therefore, the flow of the routes follows as the image below shows:

### Place Multilevel Omnichannel Order

Use the request example below to Place Order.

- Method: PUT
- URL: `{host}/api/checkout/pvt/orders?sc={sc}&affiliateId={affiliateId}`

Request example:

```json
{
   "items":[
      {
         "id":"8",
         "quantity":1,
         "seller":"1",
         "price":12
      },
      {
         "id":"36",
         "quantity":1,
         "seller":"1",
         "price":120
      }
   ],
   "clientProfileData":{
      "email":"sicrano@mailinator.com"
   },
   "shippingData":{
      "attachmentId":"shippingData",
      "logisticsInfo":[
         {
            "itemIndex":0,
            "selectedSla":"Retirada (14b25e5)",
            "selectedDeliveryChannel":"pickup-in-point",
            "price":0
         },
         {
            "itemIndex":1,
            "selectedSla":"Normal",
            "selectedDeliveryChannel":"delivery",
            "price":0
         }
      ],
      "selectedAddresses":[
         {
            "addressId":"-4581767308704"
         }
      ]
   },
   "marketplacePaymentValue":1550,
   "marketplaceOrderGroup":"externalMarketplace10",
  "marketplaceServicesEndpoint":"http://service.externalmarketplace.com/api/orders?parameter=value"
}
```

#### Changes in the order's data

The Multilevel Omnichannel Inventory changes and adds fields to the order's data. You can know more about the fields in the [Retrieve user order details](https://developers.vtex.com/vtex-rest-api/reference/userorderdetails) API Reference.

The table below describes the fields that were added or changed in the order's data.

<table>
    <tr>
        <td><strong>Field</strong></td>
        <td><strong>New or Changed?</strong></td>
        <td><strong>Description</strong></td>
    </tr>
    <tr>
        <td>sc</td>
        <td>New</td>
        <td>Path parameter including the sales channel ID.</td>
    </tr>
    <tr>
        <td>marketplaceServicesEndpoint</td>
        <td>New</td>
        <td>Field is added to the orderform. This field should be filled in with the information provided by the
            external marketplace that is placing an order in VTEX.</td>
    </tr>
    <tr>
        <td>marketplaceOrdergroup</td>
        <td>New</td>
        <td>Field is added to the orderform. This field should be filled in with the information provided by the
            external marketplace that is placing an order in VTEX.</td>
    </tr>
    <tr>
        <td>affiliateId</td>
        <td>New</td>
        <td>The <a href="https://help.vtex.com/pt/tutorial/o-que-e-afiliado--4bN3e1YarSEammk2yOeMc0">afiliate</a> identification code created by the seller. The seller must inform this ID to the marketplace so that the marketplace can complete the configuration process.</td>
    </tr>
    <tr>
        <td>marketplacePaymentValue</td>
        <td>New</td>
        <td>Field is added to the orderform.</td>
    </tr>
    <tr>
        <td>transaction</td>
        <td>Changed</td>
        <td>This field no longer is required in the orderform.</td>
    </tr>
    <tr>
        <td>origin</td>
        <td>Changed</td>
        <td>The field 'origin' will come with `chain` as a value, and not `fulfillment` or `marketplace` like before.</td>
    </tr>
    <tr>
        <td>paymentData</td>
        <td>Changed</td>
        <td>The field is no longer required in chained orders.</td>
    </tr>
</table>

### Marketplace Order Authorization

The marketplace must implement the following endpoint to notify the chain order that its progress has been approved:

- Method: POST
- URL: `{host}/api/checkout/pvt/orders/{orderId}/receipts/marketplace-order-authorization`

Request example

```json
{
   "items":[
      {
         "id":"8",
         "quantity":1,
         "seller":"1",
         "price":12
      },
 {
"marketplaceOrderGroup": "847392476",
"authorizationReceipt":  {
        "date": "{date}",
        "receipt": "{receipt}"
    }
}
```

<table>
    <tr>
        <td><strong>Name</strong></td>
        <td><strong>Type</strong></td>
        <td><strong>Mandatory</strong></td>
        <td><strong>Description</strong></td>
    </tr>
    <tr>
        <td>orderId</td>
        <td>String</td>
        <td>Yes</td>
        <td>Path parameter with the Chain order ID.</td>
    </tr>
    <tr>
        <td>items</td>
        <td>array of objects</td>
        <td>Yes</td>
        <td>Array containing the SKUs that are being invoiced.</td>
    </tr>
    <tr>
        <td>id</td>
        <td>string</td>
        <td>Yes</td>
        <td>ID of the SKU being invoiced.</td>
    </tr>
    <tr>
        <td>price</td>
        <td>integer</td>
        <td>Yes</td>
        <td>Total price of the SKU being invoiced in cents. Do not use any decimal separator. For instance, $24.99should
            be represented as 2499.</td>
    </tr>
    <tr>
        <td>seller</td>
        <td>string</td>
        <td>Yes</td>
        <td>Account name of the seller responsible for fulfillment</td>
    </tr>
    <tr>
        <td>quantity</td>
        <td>integer</td>
        <td>Yes</td>
        <td>Quantity currently in inventory of the SKU being invoiced.</td>
    </tr>
    <tr>
        <td>marketplaceOrderGroup</td>
        <td>string</td>
        <td>Yes</td>
        <td>Marketplace order ID or ordergroup</td>
    </tr>
    <tr>
        <td>authorizationReceipt</td>
        <td>Object</td>
        <td>Yes</td>
        <td>Object including date and receipt of authorization</td>
    </tr>
    <tr>
        <td>date</td>
        <td>string</td>
        <td>Yes</td>
        <td>Date of authorization</td>
    </tr>
    <tr>
        <td>receipt</td>
        <td>string</td>
        <td>Yes</td>
        <td>Receipt number</td>
    </tr>
</table>

### Cancel Order Notification

The marketplace must implement the endpoint below, to receive the cancel notification from the VTEX seller.

- Method: POST
- URL: `https://{baseUrldoParceiro}/pvt/orders/order-group/{orderGroup}/notifications/seller-cancellation`

#### Request example

```json
{ 
"id":"sellerOrderCancelled", 
"sellerOrderId": "7908010136043"
}
```

<table>
    <tr>
        <td><strong>Name</strong></td>
        <td><strong>Type</strong></td>
        <td><strong>Mandatory</strong></td>
        <td><strong>Description</strong></td>
    </tr>
    <tr>
        <td>orderGroup</td>
        <td>string</td>
        <td>Yes</td>
        <td>Path parameter including the marketplace order ID or ordergroup.</td>
    </tr>
    <tr>
        <td>id</td>
        <td>string</td>
        <td>Yes</td>
        <td>ID of the canceled order by the seller</td>
    </tr>
    <tr>
        <td>sellerOrderId</td>
        <td>string</td>
        <td>Yes</td>
        <td>Order ID in the VTEX system</td>
    </tr>
</table>

### Order Invoice Notification

The marketplace must implement this endpoint for the chain order to inform it about the order invoice. Check out our [Order Invoice Notification](https://developers.vtex.com/vtex-rest-api/reference/invoicenotification) to know more details.

- Method: POST
- URL: `{marketplaceServiceEndpoint}/api/oms/pvt/orders/{orderId}/invoice`

\[block:callout]
{
"type": "info",
"body": "Note that the path including `/pvt` is usually called if the notification is meant for an internal VTEX endpoint. If calling external agents, substitute the path for `/pub`."
}
\[/block]
Request example:

```json
{
 "invoiceNumber":"7999972",
 "invoiceValue":7450,
 "issuanceDate":"2019-02-07T02:00:00.000Z",
 "invoiceUrl":http://www.invoiceu.rl",
 "invoiceKey":"799",
 "trackingNumber":"9997LUX",
 "trackingUrl":"http://www.trackingu.rl",
 "courier":"All postal codes",
 "items": [
               {
        "id": "1231",
        "price": 7450,
        "quantity": 1
                               }
                        [
}
```

<table>
    <tr>
        <td><strong>Name</strong></td>
        <td><strong>Type</strong></td>
        <td><strong>Mandatory</strong></td>
        <td><strong>Description</strong></td>
    </tr>
    <tr>
        <td>invoiceNumber</td>
        <td>string</td>
        <td>Yes</td>
        <td>Number that identifies the invoice.</td>
    </tr>
    <tr>
        <td>invoiceValue</td>
        <td>string</td>
        <td>Yes</td>
        <td>Total amount being invoiced in cents. Do not use any decimal separator. For instance, $24.99 should be represented as 2499.</td>
    </tr>
    <tr>
        <td>issuanceDate</td>
        <td>string</td>
        <td>Yes</td>
        <td>Issuance date of the invoice.</td>
    </tr>
    <tr>
        <td>invoiceUrl</td>
        <td>string</td>
        <td></td>
        <td>URL of the invoice. Can be used to send the URL of an XML file, for example, which is useful for some integrations.</td>
    </tr>
    <tr>
        <td>trackingNumber</td>
        <td>string</td>
        <td>No</td>
        <td>The number code that identifies the order tracking. This field should only be used when sending the tracking information. When the request is used for sending the invoice, this field should be left empty</td>
    </tr>
    <tr>
        <td>trackingUrl</td>
        <td>string</td>
        <td>No</td>
        <td>The URL used to track the order. This field should only be used when sending the tracking information. When the request is used for sending the invoice, this field should be left empty</td>
    </tr>
    <tr>
        <td>courier</td>
        <td>string</td>
        <td>No</td>
        <td>The name of the carrier responsible for delivering the order. This field should only be used when sending the tracking information. When the request is used for sending the invoice, this field should be left empty</td>
    </tr>
    <tr>
        <td>items</td>
        <td>array of objects</td>
        <td>Yes</td>
        <td>Array containing the SKUs that are being invoiced.</td>
    </tr>
    <tr>
        <td>id</td>
        <td>string</td>
        <td>Yes</td>
        <td>ID of the SKU being invoiced.</td>
    </tr>
    <tr>
        <td>price</td>
        <td>integer</td>
        <td>Yes</td>
        <td>Total price of the SKU being invoiced in cents. Do not use any decimal separator. For instance, $24.99 should be represented as 2499.</td>
    </tr>
    <tr>
        <td>quantity</td>
        <td>integer</td>
        <td>Yes</td>
        <td>Quantity currently in inventory of the SKU being invoiced.</td>
    </tr>
</table>

Response example:

```json
{
"date": "2018-11-21T11:50:09.9994509-02:00",
"orderId": "876053333998-01",
"receipt": "95233cf2078d418ba77155380c18f398"
}
```
