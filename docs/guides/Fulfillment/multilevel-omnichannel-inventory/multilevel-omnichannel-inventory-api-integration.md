---
title: "Multilevel omnichannel inventory API integration"
slug: "multilevel-omnichannel-inventory-api-integration"
hidden: false
createdAt: "2022-11-18T18:48:14.043Z"
updatedAt: "2022-11-18T18:53:14.127Z"
---

>⚠️ The [Multilevel Omnichannel Inventory (MOI)](https://developers.vtex.com/docs/guides/multilevel-omnichannel-inventory) feature has been discontinued for integrations with external marketplaces. Now, MOI is available only for integrations between VTEX marketplaces and sellers. We recommend reviewing your integration strategies to align with the currently supported functionalities. For more information, please contact [VTEX support](https://help.vtex.com/en/support).

Marketplaces following the [External Marketplace protocol](https://developers.vtex.com/docs/guides/external-marketplace-integration-guide) can also make the [Multilevel Omnichannel Inventory](https://developers.vtex.com/docs/guides/multilevel-omnichannel-inventory) setting available for VTEX sellers connected to it. This allows for more fulfillment options by VTEX sellers, since they can connect their franchise accounts' inventories as fulfillment options. You can learn more about the benefits and restrictions of implementing this feature in our [Multilevel Omnichannel Inventory Help article](https://help.vtex.com/pt/tutorial/multilevel-omnichannel-inventory--7M1xyCZWUyCB7PcjNtOyw4).

External marketplaces and connectors should follow this article's instructions to configure Multilevel Omnichannel Inventory in their marketplace architecture with VTEX.

>ℹ️ Before you begin, make sure that the necessary [settings](https://developers.vtex.com/docs/guides/multilevel-omnichannel-inventory#setup-for-vtex-marketplaces) are made in the connected VTEX account, so the feature is fully operational.

## API integration overview

When using a [Multilevel Omnichannel Inventory](https://developers.vtex.com/docs/guides/multilevel-omnichannel-inventory) architecture, the endpoints used in the integration's architecture are the following:

* [Place Order](#place-multilevel-omnichannel-order): create the order in the seller responsible for fulfillment.
* [Marketplace Order Authorization](#marketplace-order-authorization): progressing the order, after the marketplace's authorization.
* [Cancel Order Notification](#cancel-order-notification): route to be notified of the seller's, or of the chain agent's (in this case seller level 2) cancellation.
* [Order Invoice Notification](#order-invoice-notification): route to receive invoice notification from the seller, or of the chain agent's (in this case seller level 2).

Therefore, the flow of the routes follows the image below:

![chain-orders-order-flow](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/multilevel-omnichannel-inventory-1.png)

## Place Multilevel Omnichannel Order

Use the request example below to Place Order.

* Method: PUT
* URL: `{host}/api/checkout/pvt/orders?sc={sc}&affiliateId={affiliateId}`

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

### Changes in the order's data

The Multilevel Omnichannel Inventory changes and adds fields to the order's data. You can know more about the fields in the [Retrieve user order details](https://developers.vtex.com/vtex-rest-api/reference/userorderdetails) API Reference.

The table below describes the fields that were added or changed in the order's data.

| Field                        | New or Changed? | Description                                                                                                                         |
|------------------------------|------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| sc                           | New              | Path parameter including the sales channel ID.                                                                                      |
| marketplaceServicesEndpoint  | New              | Field is added to the orderform. This field should be filled in with the information provided by the external marketplace that is placing an order in VTEX.                                      |
| marketplaceOrdergroup         | New              | Field is added to the orderform. This field should be filled in with the information provided by the external marketplace that is placing an order in VTEX.                                      |
| affiliateId                  | New              | The [afiliate](https://help.vtex.com/pt/tutorial/o-que-e-afiliado--4bN3e1YarSEammk2yOeMc0) identification code created by the seller. The seller must inform this ID to the marketplace so that the marketplace can complete the configuration process. |
| marketplacePaymentValue       | New              | Field is added to the orderform.                                                                                                    |
| transaction                  | Changed          | This field no longer is required in the orderform.                                                                                 |
| origin                       | Changed          | The field 'origin' will come with `chain` as a value, and not `fulfillment` or `marketplace` like before.                           |
| paymentData                  | Changed          | The field is no longer required in chained orders.                                                                                  |

## Marketplace Order Authorization

The marketplace must implement the following endpoint to notify the chain order that its progress has been approved:

* Method: POST
* URL: `{host}/api/checkout/pvt/orders/{orderId}/receipts/marketplace-order-authorization`

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
   ],
   "marketplaceOrderGroup": "847392476",
   "authorizationReceipt":  {
        "date": "{date}",
        "receipt": "{receipt}"
    }
}
```

| Name                   | Type              | Mandatory | Description                                            |
|------------------------|-------------------|-----------|--------------------------------------------------------|
| orderId                | String            | Yes       | Path parameter with the Chain order ID.                |
| items                  | Array of objects  | Yes       | Array containing the SKUs that are being invoiced.    |
| id                     | String            | Yes       | ID of the SKU being invoiced.                           |
| price                  | Integer           | Yes       | Total price of the SKU being invoiced in cents. Do not use any decimal separator. For instance, $24.99 should be represented as 2499. |
| seller                 | String            | Yes       | Account name of the seller responsible for fulfillment |
| quantity               | Integer           | Yes       | Quantity currently in inventory of the SKU being invoiced. |
| marketplaceOrderGroup  | String            | Yes       | Marketplace order ID or order group                    |
| authorizationReceipt   | Object            | Yes       | Object including date and receipt of authorization    |
| date                   | String            | Yes       | Date of authorization                                  |
| receipt                | String            | Yes       | Receipt number                                         |

## Cancel Order Notification

The marketplace must implement the endpoint below, to receive the cancel notification from the VTEX seller.

* Method: POST
* URL: `https://{baseUrldoParceiro}/pvt/orders/order-group/{orderGroup}/notifications/seller-cancellation`

### Request example

```json
{ 
    "id":"sellerOrderCancelled", 
    "sellerOrderId": "7908010136043"
}
```

| Name           | Type   | Mandatory | Description                                   |
|----------------|--------|-----------|-----------------------------------------------|
| orderGroup     | String | Yes       | Path parameter including the marketplace order ID or order group. |
| id             | String | Yes       | ID of the canceled order by the seller.       |
| sellerOrderId  | String | Yes       | Order ID in the VTEX system.                  |

## Order Invoice Notification

The marketplace must implement this endpoint for the chain order to inform it about the order invoice. Check out our [Order Invoice Notification](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/oms/pvt/orders/-orderId-/invoice) to know more details.

* Method: POST
* URL: `{marketplaceServiceEndpoint}/api/oms/pvt/orders/{orderId}/invoice`

>ℹ️ Note that the path including `/pvt` is usually called if the notification is meant for an internal VTEX endpoint. If calling external agents, substitute the path for `/pub`.

Request example:

```json
{
 "invoiceNumber":"7999972",
 "invoiceValue":7450,
 "issuanceDate":"2019-02-07T02:00:00.000Z",
 "invoiceUrl":"http://www.invoiceu.rl",
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
   ]
}
```

| Name              | Type              | Mandatory | Description                                                                                                 |
|-------------------|-------------------|-----------|-------------------------------------------------------------------------------------------------------------|
| invoiceNumber     | String            | Yes       | Number that identifies the invoice.                                                                         |
| invoiceValue      | String            | Yes       | Total amount being invoiced in cents. Do not use any decimal separator. For instance, $24.99 should be represented as 2499.                                            |
| issuanceDate      | String            | Yes       | Issuance date of the invoice.                                                                                |
| invoiceUrl        | String            |           | URL of the invoice. Can be used to send the URL of an XML file, for example, which is useful for some integrations.                                                   |
| trackingNumber    | String            | No        | The number code that identifies the order tracking. This field should only be used when sending the tracking information. When the request is used for sending the invoice, this field should be left empty. |
| trackingUrl       | String            | No        | The URL used to track the order. This field should only be used when sending the tracking information. When the request is used for sending the invoice, this field should be left empty.                   |
| courier           | String            | No        | The name of the carrier responsible for delivering the order. This field should only be used when sending the tracking information. When the request is used for sending the invoice, this field should be left empty.                   |
| items             | Array of objects  | Yes       | Array containing the SKUs that are being invoiced.                                                           |
| id                | String            | Yes       | ID of the SKU being invoiced.                                                                                |
| price             | Integer           | Yes       | Total price of the SKU being invoiced in cents. Do not use any decimal separator. For instance, $24.99 should be represented as 2499.                                            |
| quantity          | Integer           | Yes       | Quantity currently in inventory of the SKU being invoiced.                                                 |

Response example:

```json
{
    "date": "2018-11-21T11:50:09.9994509-02:00",
    "orderId": "876053333998-01",
    "receipt": "95233cf2078d418ba77155380c18f398"
}
```

## Next steps

Checkout the [Change chain orders in external marketplaces](https://developers.vtex.com/docs/guides/change-orders-multilevel-omnichannel-inventory-external-marketplaces) article to learn how to implement more complex change order scenarios.
