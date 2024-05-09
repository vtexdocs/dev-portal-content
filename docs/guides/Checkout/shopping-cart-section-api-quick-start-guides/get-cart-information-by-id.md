---
title: "Get cart information by ID"
slug: "get-cart-information-by-id"
hidden: false
createdAt: "2022-10-07T17:07:32.040Z"
updatedAt: "2022-11-17T12:27:47.716Z"
---

The shopping cart is where the information on the products chosen by the customer while browsing a store is gathered. This data may include item prices, shipping value, payment, and delivery methods, among others.

This guide will describe how to access information for a specific shopping cart by its identification code (`orderFormId`).

## Getting shopping cart ID

The first step is to get the `orderFormId` of the shopping cart you want to check. You can obtain this information through the [Get current or create a new cart](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/orderForm) endpoint. The response body of this request will provide the `orderFormId` of your current cart or, if desired, a new empty cart. See more information at [Get current or create a new cart Guide](https://developers.vtex.com/docs/guides/create-a-new-cart).

>⚠️ The `orderFormId` information to be used on VTEX APIs must be obtained only from the [Get current or create a new cart Guide](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/orderForm) endpoint. This value cannot be obtained from the Cookies via JavaScript implementation.

If you only intend to perform test operations (e.g. in Postman), you can use the following procedure:

1. Access the website where a shopping cart is open (the order has not already been concluded).
2. Go to the **Dev. Tools** screen (press the `F12` key).
3. Click the **Application** tab, and under **Cookies**, click the name of the site's URL.
4. In the table, locate the line `checkout.vtex.com` and record the value `_ofid=`. This is the `orderFormId` of the current shopping cart.

![orderFormId Dev Tools](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/get-cart-information-by-id-0.png)

## Accessing shopping cart information

With the `orderFormId` information available, you must use the [Get cart information by ID](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/orderForm/-orderFormId-) endpoint to send the following information through the URL:

- **Path param**: `orderFormId` value.
- **Query param**: `refreshOutdatedData`. You can set up this query as `false` or `true` to define whether some cart information can be updated by the [Update cart items](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/items/update) endpoint.

See a URL example below:

`https://{accountname}.{environment.com.br}/api/checkout/pub/orderForm/ede846222cd44046ba6c638442c3505a?refreshOutdatedData=true`

After sending the request, the endpoint will return the response body containing the shopping cart information, as shown in the example below:

```json
{
    "orderFormId": "ede846222cd44046ba6c638442c3505a",
    "salesChannel": "1",
    "loggedIn": false,
    "isCheckedIn": false,
    "storeId": null,
    "checkedInPickupPointId": null,
    "allowManualPrice": false,
    "canEditData": true,
    "userProfileId": null,
    "userType": null,
    "ignoreProfileData": false,
    "value": 0,
    "messages": [],
    "items": [],
    "selectableGifts": [],
    "totalizers": [],
    "shippingData": null,
    "clientProfileData": {
        "email": null,
        "firstName": null,
        "lastName": null,
        "document": null,
        "documentType": null,
        "phone": null,
        "corporateName": null,
        "tradeName": null,
        "corporateDocument": null,
        "stateInscription": null,
        "corporatePhone": null,
        "isCorporate": false,
        "profileCompleteOnLoading": null,
        "profileErrorOnLoading": null,
        "customerClass": null
    },
...
```

> ℹ️ For more information about the meaning of each of the fields available in the shopping cart, access the [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) overview.

## Error code

The following error may appear as a message in the response body.

### 404 - Not Found

- `Message error example: "The requested URL was not found on the server"`: Check that the URL data is correct.

```html
<body>
	<h1>404 Not Found</h1>
	<p>The requested URL was not found on this server.</p>
</body>
```
