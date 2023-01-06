---
title: "Add and handle custom information in the order"
slug: "add-and-handle-custom-information-in-the-order"
hidden: false
createdAt: "2022-07-25T16:59:55.570Z"
updatedAt: "2022-10-20T17:35:29.973Z"
---
When the end customer enters the checkout process at a VTEX store, all order information is organized within fields of the `orderForm` object.

However, some stores have the need to request customer data that is not part of the orderForm's default set of objects. For example: gender, cell phone number, age, etc.

To include them, you must use the `customData` field in the `orderForm`. The purpose of this field is to be populated with custom information needed for the specific operation of the store.

To work with this field, you must use VTEX’s Checkout API. Three steps are required:

1. [Creating apps and fields through the configuration request](#creating-apps-and-fields-through-the-configuration-request).

2. [Using the API to record/update/query the data (via `orderForm` and `placeOrder`)](#using-the-api-to-recordupdatequery-the-data).

3. [Finding the desired data in the created order](#finding-the-desired-data-in-the-created-order).

## Creating apps and fields through the configuration request

Before populating the `customData` field, you need to use the [Update orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/updateorderformconfiguration) call to create an app. This app will contain custom fields that will be populated during checkout.
[block:callout]
{
  "type": "warning",
  "body": "The **Update orderForm configuration** defines settings that apply to all `orderForms` generated in your account. This means that, from the moment you add an app through it, all the store’s orders will contain the extra fields defined in that app. To create an app and its fields, this call only needs to happen once."
}
[/block]
Here is an example of an `app` object sent in the body of the request **Update orderForm configuration**:
[block:code]
{
  "codes": [
    {
      "code": "\"apps\": [\n       {\n            \"id\":\"profile\",\n            \"fields\":\n            [\n                \"age\",\n                \"gender\"\n            ]\n        },\n        {\n            \"id\":\"address\",\n            \"fields\":\n            [\n                \"phone2\"\n            ]\n        }\n]",
      "language": "json"
    }
  ]
}
[/block]
In this case, two applications will be created, which function as groups of fields: one with ID `profile` and one with ID `address`.

The __profile__ app has two fields:
- `age`
- `gender`

The __address__ app has only one field:
- `phone2`


## Using the API to record/update/query the data

After creating the fields, we need to save the data in them. This can be done using one of the following calls: [Set single custom field value](https://developers.vtex.com/vtex-rest-api/reference/setsinglecustomfieldvalue) or [Set multiple custom field values](https://developers.vtex.com/vtex-rest-api/reference/setmultiplecustomfieldvalues).

Through these calls, you inform the ID of the app you want to change (in the URL), as well as the names of the fields and the values you want to save in each of these fields (in the body).

See below an example of the JSON that we must pass in the body of this call:
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"expectedOrderFormSections\":\n  [\n    \"items\",\n    \"gifts\",\n    \"totalizers\",\n    \"clientProfileData\",\n    \"shippingData\",\n    \"paymentData\",\n    \"sellers\",\n    \"messages\",\n    \"marketingData\",\n    \"clientPreferencesData\",\n    \"storePreferencesData\",\n    \"customData\"\n  ],\n  \"value\":{{appFieldValue}}\n}",
      "language": "json"
    }
  ]
}
[/block]
In the URL of the call, you must pass the following parameters:
- `{orderFormId}`: ID of the orderForm that will receive the new custom field values.
- `{appId}`: ID of the app created with the configuration API.
- `{appFieldName}`: Name of the app's field created through the Update orderForm Configuration endpoint. In the example of the fields created in the previous call, it could be `age`, `gender` or `phone2`.

In the body you must pass the `{{appFieldValue}}`, which is the value to be sent.

## Finding the desired data in the created order

Finally, it is necessary to implement access to the data saved in the orderForm’s extra fields. To do this, use the [Get Order API](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/oms/pvt/orders/-orderId-), appending the order ID to the URL.

The fields and their respective values will be inside the `customData` object.
[block:callout]
{
  "type": "warning",
  "body": "To remove an app field, access the [Remove single custom field value](https://developers.vtex.com/vtex-rest-api/reference/removesinglecustomfieldvalue) endpoint."
}
[/block]
