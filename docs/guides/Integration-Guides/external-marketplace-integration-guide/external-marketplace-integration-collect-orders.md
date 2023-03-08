---
title: "New Order Integration"
slug: "external-marketplace-integration-collect-orders"
hidden: false
createdAt: "2021-09-02T20:44:52.943Z"
updatedAt: "2022-06-10T16:10:11.654Z"
---

>⚠️ If you used our previous method for integrating orders, you can still find their documentation in [Order Logs](https://developers.vtex.com/docs/guides/deprecated-order-logs) and [How to collect orders from sales channels](https://developers.vtex.com/docs/guides/deprecated-how-to-collect-orders-from-sales-channels). The previous method, however, will not be maintained. If you are integrating orders for the first time, we recommend you use the instructions in this article.

## Authentication/authorization
When sending a request to our APIs, you must inform in the headers a X-VTEX-API-AppKey + X-VTEX-API-AppToken pair or a VtexIdclientAutCookie (the connector’s app token, if using our [App Template](https://developers.vtex.com/docs/guides/external-marketplace-integration-app-template)) that has access to the specified account.


## API Reference: New order Integration

Use the request example below to Place an order. The description and requirement of each of the fields present in the request body are found in our [API Reference](https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-marketplace-orders#post-/api/order-integration/orders).

It’s important to note that although some fields are optional in our API, depending on the order's country of origin or trade policy, they may be mandatory for Checkout/Fulfillment. In such cases, when trying to process the order, we will return the validation error in question to the connector, as well as other possible errors and success notifications.


```json
{
    "marketplaceOrderId": string,
    "connectorName": string,
    "connectorEndpoint": string,
		"marketplaceOrderStatus": string,
    "marketplacePaymentValue": int,
		"marketplaceInterestValue": int,
		"priceDivergenceAllowanceRate": decimal,
		"allowFranchises": bool,
		"pickupAccountName": string,
    "items": [
        {
            "id": string,
            "price": int,
            "quantity": int
        }
    ],
    "clientProfileData": {
        "email": string,
        "firstName": string,
        "lastName": string,
        "phone": string,
        "document": string,
        "corporateDocument": string,
        "corporatePhone": string,
        "corporateName": string,
        "tradeName": string,
        "stateInscription": string
    },
    "shippingData": {
        "logisticsInfo": [
            {
                "price": int,
                "selectedDeliveryChannel": string,
								"selectedSla": string,
                "lockTTL": string,
                "shippingEstimate": string,
								"deliveryIds": [
                    {
                        "warehouseId": string
                    }
                ]
            }
        ],
        "selectedAddresses": [
            {
                "addressType": string,
								"addressId": string,
                "receiverName": string,
                "postalCode": string,
                "city": string,
                "state": string,
                "country": string,
                "street": string,
                "number": string,
                "neighborhood": string,
								"complement": string,
								"geoCoordinates": {
								    "latitude": double,
										"longitude": double
								}
            }
        ],
        "isFob": bool,
        "isMarketplaceFulfillment": bool,
				"trackingHints": [
					{
						"trackingId": string,
						"courierName": string,
						"trackingUrl": string,
						"trackingLabel": string
					}
				]
    },
    "invoiceData": {
        "userPaymentInfo": {
            "paymentMethods": string[]
        }
    },
    "customData": {
        "customApps": [
            {
                "id": string,
                "major": int,
                "fields": {
                    string: string
                }
            }
        ]
    },
		"taxData": [
			{
				"skuId": string,
				"value": int
			}	
		],
		"openTextField": string
}
```

### Response Notifications
To receive notifications from our service, the connector must implement some API routes in the base endpoint informed in connectorEndpoint (be in the request or the App Template).
Order Processing Result

 Notifications with the orders processing result are sent through the following request: POST {connectorEndpoint}/order-integration/notification/processing-result?an={accountName}. The body is the same as described here.


#### Response Body
All API responses and order notifications from our service return the same data contract, as detailed bellow:

```json
{
		"accountName": string,
    "success": bool,
    "flow": string,
    "operationId": string,
    "marketplaceOrderId": string,
		"code": string,
		"message": string,
    "errors": 
    [
        {
            "source": string,
            "code": string,
            "description": string
        }
    ],
    "fields": {
           "mainOrderId": string,
					 "franchiseOrderId": string
    }
}
```

Some fields can return as null in some cases, such as accountName, marketplaceOrderId and operationId, for example.

#### Response Codes

|  Code  |                                                                                                                                                                    Description                                                                                                                                                                    |
|:------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| SOI001 | The order was integrated into VTEX successfully                                                                                                                                                                                                                                                                                                   |
| SOI002 | The order was approved in VTEX successfully                                                                                                                                                                                                                                                                                                       |
| SOI003 | The order was successfully enqueued in our service for processing                                                                                                                                                                                                                                                                                 |
| EOI000 | An unknown error occurred when processing the order, and in this case, the solution would be contacting VTEX for support                                                                                                                                                                                                                          |
| EOI001 | An unmapped error occurred when processing the order, and more details about the error can be found in the response error list                                                                                                                                                                                                                    |
| EOI002 | There are no SLAs or items available to fulfill this order. That is: the item(s) can be without stock, inactive in the catalog or not included in connector’s trade policy; the SLA/pickup point chosen in the order is not available or doesn’t have stock for the order’s items; or there aren’t any SLAs available at all to fulfill the order |
| EOI003 | The order total payment value differs from what is expected by the seller, and they do not have Order Authorization rules set up to deal with price divergence                                                                                                                                                                                    |
| EOI004 | This order's cart is invalid. That can mean that either the item(s) in it don’t exist in VTEX catalog or the order's data doesn’t comply with the store configuration (for example, the minimum total value or quantity of items set by the seller was not reached in the order)                                                                  |
| EOI005 | A validation error occurred while trying to process the order. That is, some field/value sent in the order’s contract is invalid and not filled according to our’s or Checkout/Fulfillment’s documentation                                                                                                                                        |
| EOI006 | An unexpected error occurred in one of VTEX's internal services. Please try to send the request again later, as it’s possible one of our services is going through instabilities                                                                                                                                                                  |
| EOI007 | The order specified already exists in VTEX and we are not able to create duplicated orders                                                                                                                                                                                                                                                        |
| EOI008 | The order cannot be approved because it’s not integrated in VTEX yet                                                                                                                                                                                                                                                                              |
| EOI009 | This order is out of the valid status to approve, such as canceled, for example                                                                                                                                                                                                                                                                   |
| EOI010 | The request to our API timed out, meaning we exceeded the response time limit                                                                                                                                                                                                                                                                     |
| EOI011 | The order was integrated with a price divergence, and we cannot approve it yet because we are waiting for the seller's manual authorization before proceeding                                                                                                                                                                                     |

#### Order Notification Results
    - Error
        - EOI000 - Unknown error
        - EOI001 - Unmapped error
        - EOI002 - SLA not available
        - EOI003 - Price divergence
        - EOI004 - Invalid cart
        - EOI005 - Validation error
        - EOI006 - VTEX unexpected error
        - EOI007 - Duplicated order
    - Success
        - SOI001 - Order integrated


## Scenario 1: new order, with pending payment

To integrate orders with pending payment, you just need to set the marketplaceOrderStatus field to NEW in the [New Order Integration](https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-marketplace-orders#post-/api/order-integration/orders) request.


### Response

```json
{
    "marketplaceOrderId": null,
    "accountName": "connections",
    "code": "SOI003",
    "flow": "PlaceOrder",
    "success": true,
    "operationId": null,
    "errors": null,
    "fields": null,
    "message": "Order successfully enqueued"
}
```


### Notification

```json
{
  "marketplaceOrderId": "123456789",
  "accountName": "connections",
  "code": "SOI001",
  "flow": "PlaceOrder",
  "success": true,
  "operationId": "a1a0e124-6cfc-404e-a8c5-95f5a494dc86",
  "errors": null,
  "fields": {
    "mainOrderId": "MKP-123456789",
    "franchiseOrderId": null
  },
  "message": "Order integrated successfully"
}
```

## Scenario 2: Approved order, with approved payment
To integrate orders with approved payment (automatically approving them afterwards) you just need to set the `marketplaceOrderStatus` field to `approved` in the [New Order Integration](https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-marketplace-orders#post-/api/order-integration/orders) API request.


### Response

```json
{
    "marketplaceOrderId": null,
    "accountName": "connections",
    "code": "SOI003",
    "flow": "PlaceOrder",
    "success": true,
    "operationId": null,
    "errors": null,
    "fields": null,
    "message": "Order successfully enqueued"
}
```

### Notification

**Integration:**

```json
{
  "marketplaceOrderId": "123456789",
  "accountName": "connections",
  "code": "SOI001",
  "flow": "PlaceOrder",
  "success": true,
  "operationId": "8cd93fe7-db90-4e1b-b55f-890a61e72bad",
  "errors": null,
  "fields": {
    "mainOrderId": "MKP-123456789",
    "franchiseOrderId": null
  },
  "message": "Order integrated successfully"
}
```

**Approval:**

```json
{
  "marketplaceOrderId": "123456789",
  "accountName": "connections",
  "code": "SOI002",
  "flow": "ApproveOrder",
  "success": true,
  "operationId": "8cd93fe7-db90-4e1b-b55f-890a61e72bad",
  "errors": null,
  "fields": {
    "mainOrderId": "MKP-123456789",
    "franchiseOrderId": null
  },
  "message": "Order approved successfully"
}
```


## Scenario 3: order with interest

To integrate orders with additional interest values, you need to fill in the marketplaceInterestValue field, with the desired amount in the [New Order Integration](https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-marketplace-orders#post-/api/order-integration/orders) API request.


### Response

```json
{
    "marketplaceOrderId": null,
    "accountName": "connections",
    "code": "SOI003",
    "flow": "PlaceOrder",
    "success": true,
    "operationId": null,
    "errors": null,
    "fields": null,
    "message": "Order successfully enqueued"
}
```

### Notification

```json
{
  "marketplaceOrderId": "123456789",
  "accountName": "connections",
  "code": "SOI001",
  "flow": "PlaceOrder",
  "success": true,
  "operationId": "7425f2ef-0849-4b73-94c7-355982119e51",
  "errors": null,
  "fields": {
    "mainOrderId": "MKP-123456789",
    "franchiseOrderId": null
  },
  "message": "Order integrated successfully"
}
```

## Scenario 4: Order with discounts 

To integrate orders with discounts, you need to apply the discount directly in the order in the[New Order Integration](https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-marketplace-orders#post-/api/order-integration/orders) API request, before sending it to our service. This means:

- If shipping costs $10 for a SKU, but the marketplace is offering a 10% discount on it, the `price` in `logisticsInfo` should be $9 (in integer format, 900).
- If the SKU is priced at $100, and the marketplace is offering a 10% discount on it, the `price` of the SKU in `items` should be $90 (in integer format, 9000).  
- And when the marketplace is offering a discount applied to all shipping or all SKUs in the order, this value should be split between the items, for example:  
  - SKU 1 price: $10, SKU 2 price: $40. Marketplace discount: $10. SKU 1 final `price` in `items` should be $5 (in integer format, 500) and SKU 2 final `price` should be $35 (in integer format, 3500).

### Response

```json
{
    "marketplaceOrderId": null,
    "accountName": "connections",
    "code": "SOI003",
    "flow": "PlaceOrder",
    "success": true,
    "operationId": null,
    "errors": null,
    "fields": null,
    "message": "Order successfully enqueued"
}
```

### Notification

```json
{
  "marketplaceOrderId": "123456789",
  "accountName": "connections",
  "code": "SOI001",
  "flow": "PlaceOrder",
  "success": true,
  "operationId": "9e396ae7-1e76-4915-b1ba-adb860e177bd",
  "errors": null,
  "fields": {
    "mainOrderId": "MKP-123456789",
    "franchiseOrderId": null
  },
  "message": "Order integrated successfully"
}
```

## Scenario 5: Order delivered by the seller 

To input an order delivered by the seller, you must do the following in the[New Order Integration](https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-marketplace-orders#post-/api/order-integration/orders) API request:
- Fill the `selectedDeliveryChannel` field with the value `delivery`.  
- Fill the `selectedSla` field with the name of the seller’s SLA selected to deliver this order. In this case, this field can also be left empty, and Fulfillment’s service will choose an available SLA automatically, if there’s any.

### Response

```json
{
    "marketplaceOrderId": null,
    "accountName": "connections",
    "code": "SOI003",
    "flow": "PlaceOrder",
    "success": true,
    "operationId": null,
    "errors": null,
    "fields": null,
    "message": "Order successfully enqueued"
}
```

### Notification

```json
{
  "marketplaceOrderId": "123456789",
  "accountName": "grocery1",
  "code": "SOI001",
  "flow": "PlaceOrder",
  "success": true,
  "operationId": "e30cf30c-7b89-4a04-aa20-eb3d116e2ac7",
  "errors": null,
  "fields": {
    "mainOrderId": "MKP-123456789",
    "franchiseOrderId": null
  },
  "message": "Order integrated successfully"
}
```

## Scenario 6: Order delivered by seller’s franchise (Multilevel Omnichannel Inventory)

To input an order delivered by a seller’s franchise, to allow the Multilevel Omnichannel Inventory feature, in the [New Order Integration](https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-marketplace-orders#post-/api/order-integration/orders) API request, you must do the following:

- Fill the `selectedDeliveryChannel` field with the value `delivery`;
- Fill the `selectedSla` field with the name of the seller’s SLA selected to deliver this order;
- Set the `allowFranchises` field to `true`.

### Response

```json
{
    "marketplaceOrderId": null,
    "accountName": "connections",
    "code": "SOI003",
    "flow": "PlaceOrder",
    "success": true,
    "operationId": null,
    "errors": null,
    "fields": null,
    "message": "Order successfully enqueued"
}
```

### Notification

```json
{
  "marketplaceOrderId": "123456789",
  "accountName": "connections",
  "code": "SOI001",
  "flow": "PlaceOrder",
  "success": true,
  "operationId": "e1d447aa-c885-4b03-97c4-ddf20090a3c3",
  "errors": null,
  "fields": {
    "mainOrderId": "MKP-123456789-01",
    "franchiseOrderId": "MKT-MKP-123456789-01"
  },
  "message": "Order integrated successfully"
}
```

## Scenario 7: Order delivered by the marketplace (with stock in the seller) 

To input an order delivered by the marketplace with the stock in the seller, in the [New Order Integration](https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-marketplace-orders#post-/api/order-integration/orders) API request, you must do the following:

- Fill the `selectedDeliveryChannel` field with the value `delivery`.  
- Don’t fill the `selectedSla` field.  
- Set the `isFob` field to `true`.  
- Set the `isMarketplaceFulfillment` to false.  
 
### Response

```json
{
    "marketplaceOrderId": null,
    "accountName": "connections",
    "code": "SOI003",
    "flow": "PlaceOrder",
    "success": true,
    "operationId": null,
    "errors": null,
    "fields": null,
    "message": "Order successfully enqueued"
}
```

### Notification

```json
{
  "marketplaceOrderId": "123456789",
  "accountName": "connections",
  "code": "SOI001",
  "flow": "PlaceOrder",
  "success": true,
  "operationId": "94c3242a-74b9-4261-9820-8e26bb73dbbd",
  "errors": null,
  "fields": {
    "mainOrderId": "MKP-123456789",
    "franchiseOrderId": null
  },
  "message": "Order integrated successfully"
}
```

## Scenario 8: Order delivered by the marketplace (with stock in the marketplace)

To input an order delivered by and with the stock in the marketplace, in the [New Order Integration](https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-marketplace-orders#post-/api/order-integration/orders) API request, you must do the following:

- Fill the `selectedDeliveryChannel` field with the value `delivery`;
- Don’t fill the `selectedSla` field;
- Set the `isFob` field to `true`;
- Set the `isMarketplaceFulfillment` to `true`;
- Fill the `warehouseId` within the `deliveryIds` field with the id of the warehouse set by the seller to handle orders from the marketplace.

### Response

```json
{
    "marketplaceOrderId": null,
    "accountName": "connections",
    "code": "SOI003",
    "flow": "PlaceOrder",
    "success": true,
    "operationId": null,
    "errors": null,
    "fields": null,
    "message": "Order successfully enqueued"
}
```

### Notification

```json
{
  "marketplaceOrderId": "123456789",
  "accountName": "grocery1",
  "code": "SOI001",
  "flow": "PlaceOrder",
  "success": true,
  "operationId": "42ca5760-e229-49b1-a731-73bebd0c48a0",
  "errors": null,
  "fields": {
    "mainOrderId": "MKP-123456789",
    "franchiseOrderId": null
  },
  "message": "Order integrated successfully"
}
```

## Scenario 9: Order with pickup-in-point

To input a pickup-in-point order, where the customer’ll be responsible for retrieving the products in a specified store, you must do the following in the [New Order Integration](https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-marketplace-orders#post-/api/order-integration/orders) API request:

- Fill the `selectedDeliveryChannel` field with the value `pickup-in-point`.  
- Fill the `selectedAddresses` list with the pickup point address, instead of the customers’s, specifying:
    - In the `addressType` field the value `pickup`.  
    - In the `addressId` field the pickup point’s ID in VTEX’s logistics system.
- Fill the `geoCoordinates` field with the geo coordinates from the pickup address.  
- The `isFob` field cannot be set to `true` if the order’s delivery type is pickup-in-point.  
- The `selectedSla` should be left empty for `pickup-in-point` orders as well.

### Response

```json
{
    "marketplaceOrderId": null,
    "accountName": "connections",
    "code": "SOI003",
    "flow": "PlaceOrder",
    "success": true,
    "operationId": null,
    "errors": null,
    "fields": null,
    "message": "Order successfully enqueued"
}
```

### Notification

```json
{
  "marketplaceOrderId": "123456789",
  "accountName": "connections",
  "code": "SOI001",
  "flow": "PlaceOrder",
  "success": true,
  "operationId": "b830df0e-3377-4b44-9601-85ecfd848b41",
  "errors": null,
  "fields": {
    "mainOrderId": "MKP-123456789",
    "franchiseOrderId": null
  },
  "message": "Order integrated successfully"
}
```


## Scenario 10: Order with a franchise pickup-in-point (Multilevel Omnichannel Inventory)

To input a franchise pickup-in-point order, where the customer’ll be responsible for retrieving the products in a specified seller’s franchise store, you must do the following in the [New Order Integration](https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-marketplace-orders#post-/api/order-integration/orders) API request:

- Fill the `selectedDeliveryChannel` field with the value `pickup-in-point`.  
- Fill the `selectedAddresses` list with the pickup point address, instead of the customers’s, specifying:
    - In the `addressType` field the value `pickup`.  
    - In the `addressId` field the pickup point’s ID in VTEX’s logistics system.
- Set the `allowFranchises` field to `true`.  
- Fill the `pickupAccountName` field, indicating from which account name the pickup point selected in the order is from, even if it’s from the main account.
- Fill the `geoCoordinates` field with the geo coordinates from the pickup address.  
- The `isFob` field cannot be set to true if the order’s delivery type is pickup-in-point.  
- The `selectedSla` should be left empty for `pickup-in-point` orders as well.


### Response

```json
{
    "marketplaceOrderId": null,
    "accountName": "connections",
    "code": "SOI003",
    "flow": "PlaceOrder",
    "success": true,
    "operationId": null,
    "errors": null,
    "fields": null,
    "message": "Order successfully enqueued"
}
```

### Notification

```json
{
  "marketplaceOrderId": "123456789",
  "accountName": "connections",
  "code": "SOI001",
  "flow": "PlaceOrder",
  "success": true,
  "operationId": "c1f00956-801c-4ab5-b343-b05c1d33863e",
  "errors": null,
  "fields": {
    "mainOrderId": "MKP-123456789-01",
    "franchiseOrderId": "MKT-MKP-123456789-01"
  },
  "message": "Order integrated successfully"
}
```


## Scenario 11: Order with taxes
To integrate orders with additional taxes values, in the [New Order Integration](https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-marketplace-orders#post-/api/order-integration/orders) API request, you need to fill in the taxData field, a list containing all taxes, one per SKU. If you don’t have the value individually by SKU, you can add only one item in the list, using one SKU ID from the order and adding all the taxes in field value.


### Response

```json
{
    "marketplaceOrderId": null,
    "accountName": "connections",
    "code": "SOI003",
    "flow": "PlaceOrder",
    "success": true,
    "operationId": null,
    "errors": null,
    "fields": null,
    "message": "Order successfully enqueued"
}
```

### Notification

```json
{
  "marketplaceOrderId": "123456789",
  "accountName": "connections",
  "code": "SOI001",
  "flow": "PlaceOrder",
  "success": true,
  "operationId": "7425f2ef-0849-4b73-94c7-355982119e51",
  "errors": null,
  "fields": {
    "mainOrderId": "MKP-123456789",
    "franchiseOrderId": null
  },
  "message": "Order integrated successfully"
}
```


## Scenario 12: Order with tracking hints
To integrate orders with label information, in the [New Order Integration](https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-marketplace-orders#post-/api/order-integration/orders) API request, you need to fill in the trackingHints field, a list containing all infos related to order label.


### Response

```json
{
    "marketplaceOrderId": null,
    "accountName": "connections",
    "code": "SOI003",
    "flow": "PlaceOrder",
    "success": true,
    "operationId": null,
    "errors": null,
    "fields": null,
    "message": "Order successfully enqueued"
}
```

### Notification

```json
{
  "marketplaceOrderId": "123456789",
  "accountName": "connections",
  "code": "SOI001",
  "flow": "PlaceOrder",
  "success": true,
  "operationId": "7425f2ef-0849-4b73-94c7-355982119e51",
  "errors": null,
  "fields": {
    "mainOrderId": "MKP-123456789",
    "franchiseOrderId": null
  },
  "message": "Order integrated successfully"
}
```