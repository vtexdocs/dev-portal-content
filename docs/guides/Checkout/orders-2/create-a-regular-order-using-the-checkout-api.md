---
title: "Create a regular order using the Checkout API"
slug: "create-a-regular-order-using-the-checkout-api"
hidden: false
createdAt: "2021-10-25T23:13:41.287Z"
updatedAt: "2022-10-27T18:56:50.737Z"
---
There are different ways of using VTEX APIs to handle shopping carts and checkout in order to place orders. For instance, you can use API requests to [create](https://developers.vtex.com/vtex-rest-api/reference/createanewcart) and [manage](https://developers.vtex.com/vtex-rest-api/reference/cart-attachments) shopping carts on the VTEX platform, so as to place an order from that information later, or directly place an order with a single request containing all cart data.
[block:callout]
{
  "type": "info",
  "body": "The main data structure used in VTEX Checkout is the `orderForm`. It contains every piece of information pertinent to a shopping cart, including logistics, payment, products and customer profile, for instance. Learn more in the [orderForm documentation.](https://developers.vtex.com/vtex-rest-api/reference/orderform-fields)"
}
[/block]
For this tutorial, we chose one of the more objective ways to understand and use our APIs to place a regular order (placed, paid, and delivered under the liability of a single account). To do this, we will follow these steps:

1. [Simulate a cart](doc:create-a-regular-order-using-the-checkout-api#1-simulate-a-cart);
    Find out what delivery and payment options are available.

2. [Check if the customer already exists in your database](doc:create-a-regular-order-using-the-checkout-api#2-check-if-a-customer-already-exists-in-your-database);
    An order needs the shopper’s email address to be placed.

3. [Assemble a cart](doc:create-a-regular-order-using-the-checkout-api#3-assemble-a-cart);
    Put together all order information in the correct format.

4. [Place the order](doc:create-a-regular-order-using-the-checkout-api#4-place-the-order);
    Creating the order on the VTEX platform.

5. [Send payment information](doc:create-a-regular-order-using-the-checkout-api#5-send-payment-information);
    Let VTEX know you have information to resolve payment.

6. [Request order processing](doc:create-a-regular-order-using-the-checkout-api#6-request-order-processing).
    The payments module can now process the transaction.

And by the end of this process you may [check the result.](doc:create-a-regular-order-using-the-checkout-api#checking-the-result)
[block:callout]
{
  "type": "warning",
  "body": "For any authentication required by the APIs presented in this tutorial, you must provide a valid `appToken` and `appKey` registered in the **License Manager** module of your account and empowered with enough permissions. Learn more in this article about [Roles.](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc#)"
}
[/block]

## 1. Simulate a cart

The very first thing that you should do is to check if your store is able to fulfill the cart. A simulation request is how your system will know which delivery and payment options are available for a given combination of items in a cart.

In order to do so, use the [Cart simulation](https://developers.vtex.com/vtex-rest-api/reference/cartsimulation) API request.

From the response content, you will be mostly using the information in `items`, `logisticsInfo` and `paymentData`. More information about each of them will be provided in the next steps.

## 2. Check if a customer already exists in your database

Whenever you attempt to place an order, you must provide an email address to identify the shopper. Typically, once an order gets successfully placed, the provided email address is assigned to a client profile on your store.

Therefore, it is a good idea to verify if a given email address is already linked to a customer of yours, so you can avoid any permission issues and retrieve any stored information.

To check an email address for existing profiles, just send use the [Get client by email](https://developers.vtex.com/vtex-rest-api/reference/cart-attachments#getclientprofilebyemail) API request.

If the response to this request returns any content, it means that you already have this customer’s information on your store’s data base. In this case, you can use that information in the next steps without having to ask the shopper to provide it to you again.

## 3. Assemble a cart

Assembling a cart from an API point of view means getting all order information into the appropriate data structure, the [orderForm](https://developers.vtex.com/vtex-rest-api/reference/orderform-fields).

An [orderForm](https://developers.vtex.com/vtex-rest-api/reference/orderform-fields) may include many elements, but for a simple order, we can focus on the main five. The overall structure will be similar to this:

```json
"items": [],
"clientProfileData": {},
"shippingData": {
    "address": {},
    "logisticsInfo": []
},
"paymentData": {}
```

[block:callout]
{
  "type": "info",
  "body": "Note that we are assembling this data structure to be sent as the request body in the next step. Below, we discuss these sections briefly, but you can learn more about each field in the [Place order API request documentation.](https://developers.vtex.com/vtex-rest-api/reference/order-placement-1#placeorder)"
}
[/block]

### items

This is the core of your order, an array that contains all data pertinent to the SKUs being purchased.

Obtain the necessary information from the `items` array in the cart simulation response from the first step of this tutorial.

Then, build a block with the following structure:

```json
"items": [
    {
        "id": "1",
        "quantity": 1,
        "seller": "1",
        "price": 10000
    }
]
```

[block:callout]
{
  "type": "info",
  "body": "For this example, we are considering a single item in the cart. To learn more and explore more complex examples see the [Place order API request documentation.](https://developers.vtex.com/vtex-rest-api/reference/order-placement-1#placeorder)"
}
[/block]

### clientProfileData

This object contains information about the shopper. Consider this format for new customers willing to create an account:

```json
"clientProfileData": {
    "email": "email@domain.com",
    "firstName": "Testing",
    "lastName": "VTEX",
    "document": "078051120",
    "documentType": "ssn",
    "phone": "1234567890",
    "corporateName": null,
    "tradeName": null,
    "corporateDocument": null,
    "stateInscription": null,
    "corporatePhone": null,
    "isCorporate": false
}
```

For [customers already in your database](doc:create-a-regular-order-using-the-checkout-api#2-check-if-a-customer-already-exists-in-your-database), sending only the email address is enough to register the order to the shopper’s existing account.

```json
"clientProfileData": {
    "email": "email@domain.com"
}
```

>❗ If the shopper exists in you database but is not logged in, sending other profile information along with the email will cause the platform to fail placing the order. This happens because this action is interpreted as an attempt to edit profile data, which is not possible unless the customer is logged in to the store.

### shippingData.address

This object contains shipping address information.

```json
"shippingData": {
    "address": {
        "addressType": "residential",
        "receiverName": "Testing VTEX",
        "postalCode": "33301",
        "city": "Fort Lauderdale",
        "state": "FL",
        "country": "USA",
        "street": "110 East Broward Blvd",
        "number": null,
        "neighborhood": null,
        "complement": "Suite 1700",
        "reference": null,
        "geoCoordinates": []
    }
}
```

For [customers already in your data base](doc:create-a-regular-order-using-the-checkout-api#2-check-if-a-customer-already-exists-in-your-database), it is enough to send this object only with an `addressId`, which you may get from [step two](doc:create-a-regular-order-using-the-checkout-api#2-check-if-a-customer-already-exists-in-your-database).

```json
"shippingAddress": {
    "address": {
        "addressId": "666c2e830bd9474ab6f6cc53fb6dd2d2"
    }
}
```

### shippingData.logisticsInfo

This is an array that contains logistics information for each item in the `items` array, including the selected delivery option and freight cost.

```json
"shippingData": {
    "logisticsInfo": [
        {
        "itemIndex": 0,
        "selectedSla": "Regular",
        "price": 100
        }
    ]
}
```

The `selectedSla` field indicates the selected delivery option. You can choose an `id` value, from among the options in the `slas` array obtained in the [Cart simulation step](doc:create-a-regular-order-using-the-checkout-api#1-simulate-a-cart). The corresponding `price` can also be found in the simulation response data, in the same object.

The `logisticsInfo` array should contain a number of objects equal to the number of objects in the `items` array. The `itemIndex` of a `logisticsInfo` object indicates to which item of the array `items` that information is referring. The object referring to the first item in `items` will contain an `itemIndex` of `0` and so on.
[block:callout]
{
  "type": "info",
  "body": "For this example, we are considering a single item in the cart. To learn more and explore more complex examples see the [Place order API request documentation.](https://developers.vtex.com/vtex-rest-api/reference/order-placement-1#placeorder)"
}
[/block]

### paymentData

This object informs the payment method and installment options (if available) selected for the order.

```json
"paymentData": {
    "payments": [
        {
        "paymentSystem": "1",
        "referenceValue": 10100,
        "value": 10100,
        "installments": 1
        }
    ]
}
```

Note that the `value` field corresponds to the full value to be payed by the shopper, whereas the `referenceValue` is the base number over which interests apply. If no interest apply to the order, they should be equal.
[block:callout]
{
  "type": "info",
  "body": "For this example, we are considering a single payment method, with a single installment and no interest. To learn more and explore more complex examples see the [Place order API request documentation.](https://developers.vtex.com/vtex-rest-api/reference/order-placement-1#placeorder)"
}
[/block]
Use the options and information from the [simulation](doc:create-a-regular-order-using-the-checkout-api#1-simulate-a-cart) response data to assemble your own `paymentData`.

## 4. Place the order

When you are done consolidating all of your shopping cart information, your `orderForm` should look something like this:

```json
{
    "items": [
        {
            "id": "1",
            "quantity": 1,
            "seller": "1",
            "price": 10000
        }
    ],
    "clientProfileData": {
        "email": "email@domain.com",
        "firstName": "Testing",
        "lastName": "VTEX",
        "document": "078051120",
        "documentType": "ssn",
        "phone": "1234567890",
        "corporateName": null,
        "tradeName": null,
        "corporateDocument": null,
        "stateInscription": null,
        "corporatePhone": null,
        "isCorporate": false
    },
    "shippingData": {
        "address": {
            "addressType": "residential",
            "receiverName": "Testing VTEX",
            "postalCode": "33301",
            "city": "Fort Lauderdale",
            "state": "FL",
            "country": "USA",
            "street": "110 East Broward Blvd",
            "number": null,
            "neighborhood": null,
            "complement": "Suite 1700",
            "reference": null,
            "geoCoordinates": []
        },
        "logisticsInfo": [
            {
            "itemIndex": 0,
            "selectedSla": "Regular",
            "price": 100            
            }
        ]
    },
    "paymentData": {
        "payments": [
            {
            "paymentSystem": "1",
            "referenceValue": 10100,
            "value": 10100,
            "installments": 1
            }
        ]
    }
}
```

Or, for a returning customer, it may be something like this:

```json
{
    "items": [
        {
            "id": "1",
            "quantity": 1,
            "seller": "1",
            "price": 10000
        }
    ],
    "clientProfileData": {
        "email": "email@domain.com"
    },
    "shippingData": {
        "address": {
            “addressId”: "666c2e830bd9474ab6f6cc53fb6dd2d2"
        },
        "logisticsInfo": [
            {
            "itemIndex": 0,
            "selectedSla": "Regular",
            "price": 100
            }
        ]
    },
    "paymentData": {
        "payments": [
            {
            "paymentSystem": "1",
            "referenceValue": 10100,
            "value": 10100,
            "installments": 1
            }
        ]
    }
}
```

If the delivery method is pickup point, add the information <code>"selectedDeliveryChannel": "pickup-in-point"</code>, as in the example below:"

```json
{
   "logisticsInfo": [
            {
            "itemIndex": 0,
            "selectedSla": "Regular",
            "price": 100,
            "selectedDeliveryChannel": "pickup-in-point"
            }
        ]
    }
```

[block:callout]
{
  "type": "info",
  "body": "This exemplifies a fairly simple fictitious shopping cart. The `orderForm` is actually highly customizable. Learn more about all possibilities in the [Place order API request documentation.](https://developers.vtex.com/vtex-rest-api/reference/order-placement-1#placeorder)"
}
[/block]
This `orderForm` can now be sent as the body in the [Place order API request.](https://developers.vtex.com/vtex-rest-api/reference/placeorder)

If you get a status `201 Created` response, take note of four pieces of information from its response content:

- `orderId`: ID of the order within VTEX’s Order Management System (OMS). You can find an  `orderId` in each object in the `orders` array.
- `transactionId`: ID of the transaction, which can be found in the objects contained in the `transactionData.merchantTransactions` array.
- `addressId`: if you're going to use the same address for shipping and billing, get this ID from the `orders[].shippingData.address` object.
- `Vtex_CHKO_Auth`: authentication cookie that is sent with the response.

>❗ Starting from the placing of the order, you have five minutes to complete the payment process. Otherwise, the order is automatically canceled and tagged `incomplete`.

## 5. Send payment information

With the `orderId` and `transactionId` values in hand, you must now inform VTEX of the payment data that should be used to resolve the order payment. To do this, use the [Send payment information API request](https://developers.vtex.com/vtex-rest-api/reference/2sendpaymentspublic). Note that there is also an alternative [private request for sending payment information](https://developers.vtex.com/vtex-rest-api/reference/2sendpaymentswithsavedcreditcard), that can be used to send saved credit card data.

The information you send in this step’s request body should be based on the `paymentData` section of your `orderForm`.

For most cases, it will look like the following:

```json
[
    {
        "paymentSystem": 1,
        "paymentSystemName": "American Express",
        "group": "creditCardPaymentGroup",
        "installments": 1,
        "installmentsInterestRate": 0,
        "installmentsValue": 10100,
        "value": 10100,
        "referenceValue": 10100,
        "fields": 
        {
            "holderName": "Testing VTEX",
            "cardNumber": "4444 3333 2222 1111",
            "validationCode": "1234",
            "dueDate": "10/20",
            "addressId": "666c2e830bd9474ab6f6cc53fb6dd2d2"
        },
        "transaction": {
            "id": "123456789abcdefgh",
            "merchantName": "MyStore"
        },
        "currencyCode": "USD"
    }
]
```

[block:callout]
{
  "type": "info",
  "body": "In the `fields` object, you can send an `addressId` to use an existing address or a new `address` object."
}
[/block]

>❗ Make sure that all value-related fields match the information sent in [step four](doc:create-a-regular-order-using-the-checkout-api#4-place-the-order), when placing the order.

## 6. Request order processing

Finally, you must request the processing of the order with the [Process order API request](https://developers.vtex.com/vtex-rest-api/reference/processorder).

At this point, if everything is ok with the payment, the order should be placed. Otherwise, you should get a `status 500` error.
[block:callout]
{
  "type": "warning",
  "body": "Be aware that this process uses the gateway connectors configured in your VTEX environment. Be careful to avoid any unwanted charges or unexpected payment denials."
}
[/block]

## Checking the result

You should be able to verify your order was in fact placed in the [Order management module](https://help.vtex.com/en/tutorial/orders-list--tutorials_200#) in VTEX Admin.

You can also use the API requests [Get order](https://developers.vtex.com/vtex-rest-api/reference/getorder) and [List orders](https://developers.vtex.com/vtex-rest-api/reference/listorders) for this purpose.
