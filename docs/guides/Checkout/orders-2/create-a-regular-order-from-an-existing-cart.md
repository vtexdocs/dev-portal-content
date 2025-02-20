---
title: "Create a regular order from an existing cart"
slug: "create-a-regular-order-from-an-existing-cart"
hidden: false
createdAt: ""
updatedAt: ""
---
The shopping cart is where the information of the products chosen by the customer while browsing a store is gathered. This data may include item prices, shipping value, payment, and delivery methods, among others.

This guide will describe how to create an order from an existing shopping cart by the API.

> ℹ️ To place an order from a new cart, access the [Create a regular order using the Checkout API](https://developers.vtex.com/docs/guides/create-a-regular-order-using-the-checkout-api).

> ✅ Try the interactive version of this article by accessing this [link](https://developers.vtex.com/docs/guides/creating-a-regular-order-from-an-existing-cart). Code will be highlighted and focused for your convenience.

## Getting shopping cart information

The first step is to get the `orderFormId` of the shopping cart you want to create an order. For more information, access the [Get cart information by ID](https://developers.vtex.com/docs/guides/get-cart-information-by-id) guide.

## Placing order from an existing cart

To create an order via a specific shopping cart, you need to use the [Place order from an existing cart](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/transaction) endpoint. In this request, you must send the `orderFormId` through the URL address, as shown by the example below:

`https://{accountName}.{environment.com.br}/api/checkout/pub/orderForm/ede846222cd44046ba6c638442c3505a/transaction`

Additionally, you need to send the request body containing the following information:

- `referenceId`: ID of the orderForm corresponding to the cart in which the order will be created (`orderFormId`).
- `savePersonalData`: This parameter should be set as `true` if the shopper’s data provided during checkout should be saved for future reference. The default value is `true`.
- `optinNewsLetter`: this parameter should be set as "true" if the shopper opted to receive the newsletter. Default value is `false`.
- `value`: total value of the order without separating cents. For example, $24.99 is represented by `2499`.
- `referenceValue`: reference value of the order for calculating interest (if applicable). It can be equal to the total value and does not separate cents. For example, $24.99 is represented by `2499`.
- `interestValue`: interest rate to be used in case it applies.

See a request body example below:

```json
{
  "referenceId": "ede846222cd44046ba6c638442c3505a",
  "savePersonalData": false,
  "optinNewsLetter": false,
  "value": 3500,
  "referenceValue":3500,
  "interestValue": 0
}
```

After sending the request, the endpoint will return the response body containing all information of a regular order. The example below shows only some of the data returned in this request:

```json
{
    "id": null,
    "merchantTransactions": [],
    "receiverUri": null,
    "gatewayCallbackTemplatePath": null,
    "orderGroup": null,
    "orderFormId": "ec00bf808e9f474ea8476681ba37ee2e",
    "salesChannel": "1",
    "loggedIn": true,
    "isCheckedIn": false,
    "storeId": null,
    "checkedInPickupPointId": null,
    "allowManualPrice": true,
    "canEditData": true,
    "userProfileId": "b2632321b-43326-4893-bfe3-bd922dsgdf4af",
    "userType": null,
    "ignoreProfileData": false,
    "value": 310,
    "messages": [ ],
    "items": [
        {
            "uniqueId": "CG5652A26705E4026B30E343FF061E26",
            "id": "29",
            "productId": "18",
            "productRefId": null,
            "refId": "456",
            "ean": null,
            "name": "Real coin",
            "skuName": "Real coin",
            "modalType": null,
            "parentItemIndex": null,
            "parentAssemblyBinding": null,
            "assemblies": [],
            "priceValidUntil": "2024-02-06T19:41:02Z",
            "tax": 0,
            "taxCode":"54WC8ZN6K8",
            "price": 100,
            "listPrice": 100,
            "manualPrice": null,
            "manualPriceAppliedBy": null,
            "sellingPrice": 100,
            "rewardValue": 0,
            "isGift": false,
            "additionalInfo": {
                "dimension": null,
                "brandName": "Brand name",
                "brandId": "2000000",
                "offeringInfo": null,
                "offeringType": null,
                "offeringTypeId": null
            },
            "preSaleDate": null,
            "productCategoryIds": "/1/",
            "productCategories": {
                "1": "Category"
            },
            "quantity": 2,
            "seller": "1",
            "sellerChain": [
                "1"
            ],
...
    "shippingData": {
        "address": {
            "addressType": "residential",
            "receiverName": "R S",
            "addressId": "5431864143",
            "isDisposable": true,
            "postalCode": "12200-000",
            "city": "São Paulo",
            "state": "SP",
            "country": "BRA",
            "street": "Rua Teste",
            "number": "0",
            "neighborhood": "Conjunto Residencial Teste",
            "complement": null,
            "reference": null,
            "geoCoordinates": [
                -45.00000000000000,
                -23.00000000000
            ]
        },
        "logisticsInfo": [
            {
                "itemIndex": 0,
                "selectedSla": "Normal",
                "selectedDeliveryChannel": "delivery",
                "addressId": "5431864143",
                "slas": [
                    {
                        "id": "Normal",
                        "deliveryChannel": "delivery",
                        "name": "Normal",
                        "deliveryIds": [
                            {
                                "courierId": "1",
                                "warehouseId": "1_1",
                                "dockId": "1",
                                "courierName": "Transportadora",
                                "quantity": 2,
                                "kitItemDetails": []
                            }
                        ],
                        "shippingEstimate": "3bd",
                        "shippingEstimateDate": null,
                        "lockTTL": null,
                        "availableDeliveryWindows": [],
                        "deliveryWindow": null,
...
```

> ℹ️ For more information about the meaning of each of the fields available in the shopping cart, access the [orderForm guide](https://developers.vtex.com/docs/guides/orderform-fields).

> ⚠️ After creating an order using this procedure, you have 5 (five) minutes to [send payment information](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/pub/transactions/-transactionId-/payments) and then [request order processing](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/gatewayCallback/-orderGroup-). Otherwise, the order is automatically canceled and tagged `incomplete`.

## Error codes

The following errors may appear as a message in the response body.

### 400 - Bad Request

- `Message error example (code ORD002): "Invalid order form"`: the `orderFormId` information is not valid.

```json
{
    "fields": {},
    "error": {
        "code": "ORD002",
        "message": "Invalid order form",
        "exception": null
    },
    "operationId": "f01ef909-8b81-4ffd-a91d-82be680d60ff"
}
```

- `Message error example (code CHK0016): "Payment value does not match with reference value"`: the fields `value` and `referenceValue` have different values even without the use of interest in the payment. Modify the values used or check if the interest rate is applicable to this order.

```json
{
    "fields": {},
    "error": {
        "code": "CHK0016",
        "message": "Payment value does not match with reference value",
        "exception": null
    },
    "operationId": "6a080d5f-6911-4469-a661-312e93c23419"
}
```

### 404 - Not Found

- `Message error example: "The requested URL was not found on the server"`: check that the URL data is correct.

```html
<body>
 <h1>404 Not Found</h1>
 <p>The requested URL was not found on this server.</p>
</body>
```

### 500 - Internal Server Error

- `Message error example (code ORD005): "The purchase cannot be done without items"`: this message will appear when the shopping cart (orderFormId) informed in the request does not have any item, making it impossible to create an order.

```json
{
    "fields": {},
    "error": {
        "code": "ORD005",
        "message": "The purchase cannot be done without items",
        "exception": null
    },
    "operationId": "673771c0-f5ba-4fa6-800d-bea836c51f93"
}
```
