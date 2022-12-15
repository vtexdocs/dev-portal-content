---
title: "API Integration"
slug: "api-integration"
hidden: false
createdAt: "2022-11-18T18:48:14.043Z"
updatedAt: "2022-11-18T18:53:14.127Z"
---
When using a Multilevel Omnichannel Inventory architecture, the endpoints used in the integration's architecture are the following:


* [Place Order](#place-multilevel-omnichannel-order): create the order in the seller responsible for fulfillment.
* [Marketplace Order Authorization](#marketplace-order-authorization): progressing the order, after the marketplace's authorization.
* [Cancel Order Notification](#cancel-order-notification): route to be notified of the seller's, or of the chain agent's (in this case seller level 2) cancellation.
* [Order Invoice Notification](#order-invoice-notification): route to receive invoice notification from the seller, or of the chain agent's (in this case seller level 2).

Therefore, the flow of the routes follows as the image below shows:




## Place Multilevel Omnichannel Order

Use the request example below to Place Order. 

* Method: PUT
* URL: `{host}/api/checkout/pvt/orders?sc={sc}&affiliateId={affiliateId}`

Request example:


```
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


<table>
  <tr>
   <td><strong>Field</strong>
   </td>
   <td><strong>New or Changed?</strong>
   </td>
   <td><strong>Description</strong>
   </td>
  </tr>
  <tr>
   <td>sc
   </td>
   <td>New
   </td>
   <td>Path parameter including the sales channel ID.
   </td>
  </tr>
  <tr>
   <td>marketplaceServicesEndpoint
   </td>
   <td>New
   </td>
   <td>Field is added to the orderform. This field should be filled in with the information provided by the external marketplace that is placing an order in VTEX.
   </td>
  </tr>
  <tr>
   <td>marketplaceOrdergroup
   </td>
   <td>New
   </td>
   <td>Field is added to the orderform. This field should be filled in with the information provided by the external marketplace that is placing an order in VTEX.
   </td>
  </tr>
  <tr>
   <td>affiliateId
   </td>
   <td>New
   </td>
   <td>The <a href="https://help.vtex.com/pt/tutorial/o-que-e-afiliado--4bN3e1YarSEammk2yOeMc0">afiliate</a> identification code created by the seller. The seller must inform this ID to the marketplace so that the marketplace can complete the configuration process.
   </td>
  </tr>
  <tr>
   <td>marketplacePaymentValue
   </td>
   <td>New
   </td>
   <td>Field is added to the orderform.
   </td>
  </tr>
  <tr>
   <td>transaction
   </td>
   <td>Changed
   </td>
   <td>This field no longer is required in the orderform.
   </td>
  </tr>
  <tr>
   <td>origin
   </td>
   <td>Changed
   </td>
   <td>The field 'origin' will come with `chain` as a value, and not `fulfillment` or `marketplace` like before.
   </td>
  </tr>
  <tr>
   <td>paymentData
   </td>
   <td>Changed
   </td>
   <td>The field is no longer required in chained orders.
   </td>
  </tr>
</table>



## Marketplace Order Authorization

The marketplace must implement the following endpoint to notify the chain order that its progress has been approved:



* Method: POST
* URL: `{host}/api/checkout/pvt/orders/{orderId}/receipts/marketplace-order-authorization`

Request example


```
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
   <td><strong>Name</strong>
   </td>
   <td><strong>Type</strong>
   </td>
   <td><strong>Mandatory</strong>
   </td>
   <td><strong>Description</strong>
   </td>
  </tr>
  <tr>
   <td>orderId
   </td>
   <td>String
   </td>
   <td>Yes
   </td>
   <td>Path parameter with the Chain order ID.
   </td>
  </tr>
  <tr>
   <td>items
   </td>
   <td>array of objects
   </td>
   <td>Yes
   </td>
   <td>Array containing the SKUs that are being invoiced.
   </td>
  </tr>
  <tr>
   <td>id
   </td>
   <td>string
   </td>
   <td>Yes
   </td>
   <td>ID of the SKU being invoiced.
   </td>
  </tr>
  <tr>
   <td>price
   </td>
   <td>integer
   </td>
   <td>Yes
   </td>
   <td>Total price of the SKU being invoiced in cents. Do not use any decimal separator. For instance, $24.99 should be represented as 2499.
   </td>
  </tr>
  <tr>
   <td>seller
   </td>
   <td>string
   </td>
   <td>Yes
   </td>
   <td>Account name of the seller responsible for fulfillment
   </td>
  </tr>
  <tr>
   <td>quantity
   </td>
   <td>integer
   </td>
   <td>Yes
   </td>
   <td>Quantity currently in inventory of the SKU being invoiced.
   </td>
  </tr>
  <tr>
   <td>marketplaceOrderGroup
   </td>
   <td>string
   </td>
   <td>Yes
   </td>
   <td>Marketplace order ID or ordergroup
   </td>
  </tr>
  <tr>
   <td>authorizationReceipt
   </td>
   <td>Object
   </td>
   <td>Yes
   </td>
   <td>Object including date and receipt of authorization
   </td>
  </tr>
  <tr>
   <td>date
   </td>
   <td>string
   </td>
   <td>Yes
   </td>
   <td>Date of authorization
   </td>
  </tr>
  <tr>
   <td>receipt
   </td>
   <td>string
   </td>
   <td>Yes
   </td>
   <td>Receipt number
   </td>
  </tr>
</table>



## Cancel Order Notification

The marketplace must implement the endpoint below, to receive the cancel notification from the VTEX seller.



* Method: POST
* URL: `https://{baseUrldoParceiro}/pvt/orders/order-group/{orderGroup}/notifications/seller-cancellation`


### Request example


```
{ 
"id":"sellerOrderCancelled", 
"sellerOrderId": "7908010136043"
}
```



<table>
  <tr>
   <td><strong>Name</strong>
   </td>
   <td><strong>Type</strong>
   </td>
   <td><strong>Mandatory</strong>
   </td>
   <td><strong>Description</strong>
   </td>
  </tr>
  <tr>
   <td>orderGroup
   </td>
   <td>string
   </td>
   <td>Yes
   </td>
   <td>Path parameter including the marketplace order ID or ordergroup.
   </td>
  </tr>
  <tr>
   <td>id
   </td>
   <td>string
   </td>
   <td>Yes
   </td>
   <td>ID of the canceled order by the seller
   </td>
  </tr>
  <tr>
   <td>sellerOrderId
   </td>
   <td>string
   </td>
   <td>Yes
   </td>
   <td>Order ID in the VTEX system
   </td>
  </tr>
</table>



## Order Invoice Notification

The marketplace must implement this endpoint for the chain order to inform it about the order invoice. Check out our [Order Invoice Notification](https://developers.vtex.com/vtex-rest-api/reference/invoicenotification) to know more details.



* Method: POST
* URL: `{marketplaceServiceEndpoint}/api/oms/pvt/orders/{orderId}/invoice` 


[block:callout]
{
  "type": "info",
  "body": "Note that the path including `/pvt` is usually called if the notification is meant for an internal VTEX endpoint. If calling external agents, substitute the path for `/pub`."
}
[/block]
Request example:


```
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
   <td><strong>Name</strong>
   </td>
   <td><strong>Type</strong>
   </td>
   <td><strong>Mandatory</strong>
   </td>
   <td><strong>Description</strong>
   </td>
  </tr>
  <tr>
   <td>invoiceNumber
   </td>
   <td>string
   </td>
   <td>Yes
   </td>
   <td>Number that identifies the invoice.
   </td>
  </tr>
  <tr>
   <td>invoiceValue
   </td>
   <td>string
   </td>
   <td>Yes
   </td>
   <td>Total amount being invoiced in cents. Do not use any decimal separator. For instance, $24.99 should be represented as 2499.
   </td>
  </tr>
  <tr>
   <td>issuanceDate
   </td>
   <td>string
   </td>
   <td>Yes
   </td>
   <td>Issuance date of the invoice.
   </td>
  </tr>
  <tr>
   <td>invoiceUrl
   </td>
   <td>string
   </td>
   <td>
   </td>
   <td>URL of the invoice. Can be used to send the URL of an XML file, for example, which is useful for some integrations.
   </td>
  </tr>
  <tr>
   <td>trackingNumber
   </td>
   <td>string
   </td>
   <td>No
   </td>
   <td>The number code that identifies the order tracking. This field should only be used when sending the tracking information. When the request is used for sending the invoice, this field should be left empty
   </td>
  </tr>
  <tr>
   <td>trackingUrl
   </td>
   <td>string
   </td>
   <td>No
   </td>
   <td>The URL used to track the order. This field should only be used when sending the tracking information. When the request is used for sending the invoice, this field should be left empty
   </td>
  </tr>
  <tr>
   <td>courier
   </td>
   <td>string
   </td>
   <td>No
   </td>
   <td>The name of the carrier responsible for delivering the order. This field should only be used when sending the tracking information. When the request is used for sending the invoice, this field should be left empty
   </td>
  </tr>
  <tr>
   <td>items
   </td>
   <td>array of objects
   </td>
   <td>Yes
   </td>
   <td>Array containing the SKUs that are being invoiced.
   </td>
  </tr>
  <tr>
   <td>id
   </td>
   <td>string
   </td>
   <td>Yes
   </td>
   <td>ID of the SKU being invoiced.
   </td>
  </tr>
  <tr>
   <td>price
   </td>
   <td>integer
   </td>
   <td>Yes
   </td>
   <td>Total price of the SKU being invoiced in cents. Do not use any decimal separator. For instance, $24.99 should be represented as 2499.
   </td>
  </tr>
  <tr>
   <td>quantity
   </td>
   <td>integer
   </td>
   <td>Yes
   </td>
   <td>Quantity currently in inventory of the SKU being invoiced.
   </td>
  </tr>
</table>


Response example:


```
{
"date": "2018-11-21T11:50:09.9994509-02:00",
"orderId": "876053333998-01",
"receipt": "95233cf2078d418ba77155380c18f398"
}
```