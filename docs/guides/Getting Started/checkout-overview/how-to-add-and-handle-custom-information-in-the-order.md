---
title: "How to add and handle custom information in the order (B2B)"
slug: "how-to-add-and-handle-custom-information-in-the-order"
hidden: false
createdAt: "2022-07-25T16:59:55.570Z"
updatedAt: "2022-07-25T18:09:05.590Z"
---
When the end customer enters the checkout process at a VTEX store, all order information is organized within fields of the `orderForm` object.

However, in B2B transactions, whose sale context is more complex, the store usually needs to add extra information such as order type and purchase order number.

To include them, you must use the `customData` field in the `orderForm`. The purpose of this field is to be populated with custom information needed for the specific operation of the store.

To work with this field, you must use VTEX’s Checkout API. Three steps are required:

1. [Creating apps and fields through the configuration request](https://developers.vtex.com/vtex-rest-api/docs/how-to-add-and-handle-customized-information-to-the-order#creating-apps-and-fields-through-the-configuration-request).
2. [Using the API to record/update/query the data (via `orderForm` and `placeOrder`)](https://developers.vtex.com/vtex-rest-api/docs/how-to-add-and-handle-customized-information-to-the-order#use-the-api-to-recordupdatequery-the-data).
3. [Finding the desired data in the created order](https://developers.vtex.com/vtex-rest-api/docs/how-to-add-and-handle-customized-information-to-the-order#find-the-desired-data-in-the-created-order).

# Creating apps and fields through the configuration request

Before populating the `customData` field, you need to use the [Update orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/updateorderformconfiguration) call to create an app. This app will contain custom fields that will be populated during checkout.
[block:callout]
{
  "type": "warning",
  "body": "The **Update orderForm configuration** defines settings that apply to all `orderForms` generated in your account. This means that, from the moment you add an app through it, all the store’s orders will contain the extra fields defined in that app. To create an app and its fields, this call only needs to happen once."
}
[/block]
Here is an example of an `app` object sent in the body of the request Update orderForm configuration:
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/46ebe0b-Configuration_request.PNG",
        "Configuration request.PNG",
        729,
        230,
        "#2e303b"
      ]
    }
  ]
}
[/block]
With this object in the body, the request will create an app whose ID will be `cart-b2b-context` and which will contain two fields: `order-type` and `po-number`.

If the call is successful (answer `200 OK`), the orderForm of your store's orders will now contain these two new fields.


# Using the API to record/update/query the data

After creating the fields, we need to save the data in them. This can be done with a single call: [Set multiple custom field values](https://developers.vtex.com/reference/custom-data#setmultiplecustomfieldvalues).

Through this call, you inform the ID of the app you want to change (in the URL), as well as the names of the fields and the values you want to save in each of these fields (in the body).

Using our previous example, we could make the following request:

- **URL**: `https://{accountName}.myvtex.com.br/api/checkout/pub/orderForm/{orderFormId}/customData/cart-b2b-context`

- **Body information**:
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/275702b-Configuration_request_2.PNG",
        "Configuration request_2.PNG",
        729,
        114,
        "#33353f"
      ]
    }
  ]
}
[/block]
In this example, we are populating the new extra fields of the `orderForm` identified in the URL by `{orderFormId}`.

# Finding the desired data in the created order

Finally, it is necessary to implement access to the data saved in the orderForm’s extra fields. To do this, use the [Get Order API](https://developers.vtex.com/reference/orders#getorder), appending the order ID to the URL.

The fields and their respective values will be inside the `customData` object.