---
title: "Headless cart and checkout"
slug: "headless-cart-and-checkout"
hidden: true
createdAt: "2021-03-31T21:20:32.157Z"
updatedAt: "2023-05-29T21:21:53.940Z"
---

A shopper browsing ecommerce products must be able to add items to a shopping cart and then go to checkout to place an order.

In this guide, you can learn about the API endpoints and resources VTEX offers so that you can add shopping cart and checkout functionalities to your headless store.

>ℹ️ To know more about VTEX checkout API and its features, see this [checkout API overview](https://developers.vtex.com/docs/api-reference/checkout-api).

## Shopping cart

Shopping cart information is organized in the form of an [orderForm](https://developers.vtex.com/docs/guides/orderform-fields), which is an object containing all data relevant to the purchase, from the products being bought to shipping and payment information, among other data.

The `orderForm` is a complex data structure with many customization possibilities. You can learn more about its structure with the [orderForm documentation](https://developers.vtex.com/docs/guides/orderform-fields). But the parts essential to placing an order via API can be divided into [items](#items) and [attachments](#attachments).

### Items

Items are the products of a shopping cart. In the `orderForm`, items' information is in the `items` array of object, where each object corresponds to one SKU contained in the cart. See a basic example of a shopping cart containing two units of SKU `123`, to be fulfilled by seller `1`, for a price of $100,00 by unit:

```json
"items": [
    {
        "id": "123",
        "quantity": 2,
        "seller": "1",
        "price": 10000
    }
]
```

The information above is enough to place an order, but there are other possible fields for shopping cart items, many of which are populated by VTEX modules. Learn more about these fields with the [orderForm documentation](https://developers.vtex.com/docs/guides/orderform-fields#items).

### Attachments

Shopping cart attachments are `orderForm` objects containing order information not directly related to the products. Below are some examples of shopping cart attachments. Click the links to learn more details about each of them:

- [clientProfileData](https://developers.vtex.com/docs/guides/orderform-fields#clientprofiledata)
- [shippingData](https://developers.vtex.com/docs/guides/orderform-fields#shippingdata)
- [paymentData](https://developers.vtex.com/docs/guides/orderform-fields#paymentdata)
- [marketingData](https://developers.vtex.com/docs/guides/orderform-fields#marketingdata)

>ℹ️ Note that some attachments may contain arrays of objects in which each object corresponds respectively to an item of the [items](#items) array. An example is [shippingData.logisticsInfo](https://developers.vtex.com/docs/guides/orderform-fields#shippingdata).

## Placing orders

There are two ways of placing orders with VTEX APIs:

- [Place new order](#place-new-order): manage shopping cart information in your frontend and then use one API request to send all order information to VTEX.
- [Place order from existing cart](#place-order-from-existing-cart): manage shopping cart information in the VTEX platform throughout the shopping experience, then place an order from that data using just the cart ID.

### Place new order

To place an order from scratch, meaning with no shopping cart data previously registered to the VTEX platform, use the [Place order API request](https://developers.vtex.com/docs/api-reference/checkout-api#put-/api/checkout/pub/orders).

For a step by step guide of this method, see the tutorial [Create a regular order from an existing cart](https://developers.vtex.com/docs/guides/create-a-regular-order-using-the-checkout-api). But keep in mind that the `orderForm` is not limited to the information exemplified in this tutorial. You may send other data fields, as described in the [orderForm fields documentation](https://developers.vtex.com/docs/guides/orderform-fields).

### Place order from existing cart

VTEX also makes available shopping cart endpoints, with which you can use the VTEX platform to manage [orderForm](#shopping-cart) information and then [place an order providing only the shopping cart ID](https://developers.vtex.com/vtex-rest-api/reference/placeorderfromexistingorderform).

These endpoints may be used to perform tasks such as adding products to a cart or associating shipping information with the order.

See below the list of endpoints you can use to use this order-placing method.

- Manage cart items
    - [POST - Cart Simulation](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForms/simulation)
    - [GET - Get current or create a new cart](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/orderForm)
    - [GET - Get cart information by ID](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/orderForm/-orderFormId-)
    - [POST - Remove all items](https://developers.vtex.com/vtex-rest-api/reference/removeallitems)
    - [POST - Update cart items](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/items/update)
    - [POST - Add cart items](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/items)
    - [PUT - Change price](https://developers.vtex.com/docs/api-reference/checkout-api#put-/api/checkout/pub/orderForm/-orderFormId-/items/-itemIndex-/price)
    - [GET - Cart installments](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/orderForm/-orderFormId-/installments)
-  Manage cart attachments
    - [GET - Get client profile by email](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/profiles)
    - [POST - Add client profile](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/attachments/clientProfileData)
    - [GET - Remove all personal data](https://developers.vtex.com/docs/api-reference/checkout-api#get-/checkout/changeToAnonymousUser/-orderFormId-)
    - [PATCH - Ignore profile data](https://developers.vtex.com/docs/api-reference/checkout-api#patch-/api/checkout/pub/orderForm/-orderFormId-/profile)
    - [POST - Add shipping address and select delivery option](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/attachments/shippingData)
    - [POST - Add client preferences](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/attachments/clientPreferencesData)
    - [POST - Add marketing data](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/attachments/marketingData)
    - [POST - Add payment data](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/attachments/paymentData)
    - [POST - Add merchant context data](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/attachments/merchantContextData)
    - [POST - Add coupons to the cart](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/coupons)
- Place order
    - [Place order from existing cart](https://developers.vtex.com/vtex-rest-api/reference/placeorderfromexistingorderform)

#### Shopping flow

When a shopper goes to your store, you must make sure you have an `orderForm` for them. Meaning they must have a shopping cart available for them to shop.

You can [Create a new cart](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/orderForm), and you will get an `orderFormId` in the response. If your headless storefront is not browser-based (e.g., native app), it is important that you save this ID and use it to manage the cart's information with the requests above. Otherwise, VTEX cookies will automatically manage this information in the shopper's browser.

If the shopper leaves the store, make sure you keep the `orderFormId` so you can retrieve their previously abandoned cart with the [Get cart information by ID API request](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/orderForm/-orderFormId-).

Throughout the shopping experience, use the requests listed above to assemble your desired shopping experience.

And once your customer goes to checkout and wishes to place the order, use the [Place order from existing cart endpoint](https://developers.vtex.com/vtex-rest-api/reference/placeorderfromexistingorderform)

### Which order placing method should you use?

The [place new order](#place-new-order) method of placing orders may seem more straightforward, but it may also raise the complexity of your application since your frontend must manage all shopping cart data to correctly assemble the [orderForm](#shopping-cart).

Also, since the [place new order](#place-new-order) method does not send shopping cart information to VTEX before shoppers place their orders, you may be unable to use some commerce features offered by VTEX.

Because of this, the [place order from existing cart](#place-order-from-existing-cart) method is best in most cases. Use [place new order](#place-new-order) if your operation has specific requirements, such as limiting the number of HTTP requests sent from your frontend.

## After placing an order

After placing an order with either of the methods presented above, you will receive an `orderId` and `transactionId` in the response body, as well as some validation cookies. Your integration must use these IDs and cookies to complete the purchase process within five minutes. This means [sending payment information](#sending-payment-information), then [requesting order processing](#request-order-processing).

>❗Failing to perform these steps within five minutes will cause the order to be automatically canceled and tagged `incomplete`.

### Send payment information

You can send the payment information to VTEX using one of these requests:

- [Send payment information API request (public)](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/pub/transactions/-transactionId-/payments)
- [Send payment information API request (private)](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/pvt/transactions/-transactionId-/payments).

The body of the request used in this step is based in the order's `paymentData` attachment. You can get this data from the response of the [order placement](#placing-orders) request.

Learn more about these API requests:

- [Send payment information](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/pub/transactions/-transactionId-/payments)
- [Send payment information with a saved credit card](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/pvt/transactions/-transactionId-/payments)

>❗ Make sure that all value-related fields match the information sent when [placing the order](#placing-orders).

### Request order processing

Finally, you must request the processing of the order with the [Process order API request](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/gatewayCallback/-orderGroup-).

At this point, if everything is ok with the payment, the order should be placed. Otherwise, you should get a `status 500` error.

>⚠️ Be aware that this process uses the gateway connectors configured in your VTEX environment. Be careful to avoid any unwanted charges or unexpected payment denials.

### Checking the result

Once you have successfully placed an order, sent payment information, and requested order processing, you will be able to see the order in the [order management module](https://help.vtex.com/en/tutorial/orders-list--tutorials_200#) in VTEX Admin.

 You can also use the API requests [Get order](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/oms/pvt/orders/-orderId-) and [List orders](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/oms/pvt/orders) for this purpose.

## Checkout interface

When a shopper goes to checkout at your store, there are some tasks that your frontend must be able to handle. See to implement these in the sections below.

### Order details

Order details filled by shoppers at checkout, such as their profile information or shipping address, are [attachments](#attachments) of the [shopping cart](#shopping-cart).

This means you must handle this information in a way compatible with the order placement method of your choice, see the corresponding section to learn how to do it:

- [Place new order](#place-new-order)
- [Place order from existing cart](#attachments)

### Address autofill

You can implement an address autofill feature, with the following endpoint:

- [Get address by postal code](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/postal-code/-countryCode-/-postalCode-)

### Pickup points

As mentioned above, shipping information is added to the order in the form of [orderForm attachments](#order-details). However, for your customer to be able to choose pickup points close to their location, you can fetch this information using the following API endpoint:

- [List pickup points by location](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/pickup-points)

### reCAPTCHA

VTEX stores have access to [reCAPTCHA integration](https://help.vtex.com/en/tutorial/using-recaptcha-at-checkout--18Te3oDd7f4qcjKu9jhNzP) to improve checkout security.

>ℹ️ Learn more about [reCAPTCHA for VTEX stores](https://help.vtex.com/en/tutorial/using-recaptcha-at-checkout--18Te3oDd7f4qcjKu9jhNzP).

If you activate reCAPTCHA for your store, you must make sure that your frontend is prepared to display and handle reCAPTCHA. Otherwise, it will not be able to place orders. Learn how to implement this in your frontend with the [reCAPTCHA integration guide](https://developers.vtex.com/docs/guides/recaptcha).
