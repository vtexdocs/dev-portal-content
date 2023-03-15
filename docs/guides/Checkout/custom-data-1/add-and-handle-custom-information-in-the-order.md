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

Before populating the `customData` field, you need to use the [Update orderForm configuration](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pvt/configuration/orderForm) request to create an app. This app will contain custom fields that will be populated during checkout.

>⚠️ The **Update orderForm configuration** defines settings that apply to all `orderForms` generated in your account. This means that, from the moment you add an app through it, all the store’s orders will contain the extra fields defined in that app. To create an app and its fields, this call only needs to happen once. For more information, access the [Update an account’s orderForm configuration developers guide](https://developers.vtex.com/docs/guides/update-an-account-orderform-configuration).

See below a request body example of the **Updater orderForm configuration** endpoint containing an `apps` object:

```json
...
"apps": [
        {
            "fields": [
                  "gender",
                  "age"
            ],
            "id": "profile",
            "major": 1
        },
        {
            "fields": [
                  "street"
            ],
            "id": "address",
            "major": 1
        }
  ]
...
```

In this case, two applications will be created, which function as groups of fields: one with ID `profile` and one with ID `address`.

The __profile__ app has two fields:
- `gender`
- `age`

The __address__ app has only one field:
- `street`


## Using the API to record/update/query the data

After creating the fields, we need to save the data in them. This can be done using one of the following requests: [Set single custom field value](https://developers.vtex.com/docs/api-reference/checkout-api#put-/api/checkout/pub/orderForm/-orderFormId-/customData/-appId-/-appFieldName-) or [Set multiple custom field values](https://developers.vtex.com/docs/api-reference/checkout-api#put-/api/checkout/pub/orderForm/-orderFormId-/customData/-appId-).

### **Set single custom field value**

To update a value of a specific custom field, you can use this endpoint by sending the value to be updated (`appFieldValue`) through the request body. The following information must be sent as path parameters in the URL:

- `orderFormId`: ID of the orderForm that will receive the new custom field values.
- `appId`: ID of the app created through the Update orderForm Configuration endpoint.
- `appFieldName`: name of the app's field created through the Update orderForm Configuration endpoint.

See a URL and request body example below:

URl: `https://{accountName}.{environment}.com.br/api/checkout/pub/orderForm/ede846222cd44046ba6c638442c3505a/customData/address/street`

```json
{
  "value": "Bourbon Street"
}
```

### **Set multiple custom field values**

To update values of multiple custom fields at the same time, you can use this endpoint by sending all the values and their respective fields to be updated in the request body (`appFieldValue` and `appFieldName`). The following information must be sent as path parameters in the URL:

- `orderFormId`: ID of the orderForm that will receive the new custom field values.
- `appId`: ID of the app created through the Update orderForm Configuration endpoint.

See a URL and request body example below:

URl: `https://{accountName}.{environment}.com.br/api/checkout/pub/orderForm/ede846222cd44046ba6c638442c3505a/customData/address`

```json
{
  "street": "Bourbon Street",
  "number": "78",
  "postalCode": "11554"
}
```

After choosing one of the methods and sending the URL request, the terminal will return the response body containing the updated custom data information, as shown in the example below:

```json
...
"customData": {
        "customApps": [
            {
                "fields": {
                      "street": "Bourbon Street",
                      "number": "78",
                      "postalCode": "11554"
                },
                "id": "address",
                "major": 1
            }
        ]
    },
...
```

## Finding the desired data in the created order

Finally, it is necessary to implement access to the data saved in the orderForm’s extra fields. To do this, use the [Get Order API](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/oms/pvt/orders/-orderId-), appending the order ID to the URL.

The fields and their respective values will be inside the `customData` object.

## Remove single custom field value

To remove the value of a specific custom field, you can use the [Remove single custom field value](https://developers.vtex.com/docs/api-reference/checkout-api#delete-/api/checkout/pub/orderForm/-orderFormId-/customData/-appId-/-appFieldName-) endpoint by sending the following information as path parameters in the URL:

- `orderFormId`: ID of the orderForm where the custom field value will be deleted.
- `appId`: ID of the app created through the Update orderForm Configuration endpoint.
- `appFieldName`: name of the app's field created through the Update orderForm Configuration endpoint and which will be deleted.

See a URL and request body example below:

`https://{accountName}.{environment}.com.br/api/checkout/pub/orderForm/ede846222cd44046ba6c638442c3505a/customData/address/street`

## Error codes

The following errors may appear as a message in the response body.

### Set single custom field value and Set multiple custom field values endpoints

### 400 - Bad Request

- `Message error example (code ORD002): "Invalid order form"`: this message indicates that the `orderFormId` used in the request does not exist or is incorrect.

```json
{
    "fields": {},
    "error": {
        "code": "ORD002",
        "message": "Invalid order form",
        "exception": null
    },
    "operationId": "f2b8107f-e5d5-4b7c-b719-344d1b05d1fa"
}
```

- `Message error example (code CHK0121): "Invalid app fields"`: this message indicates that the `value` was not sent in this request.

```json
{
    "fields": {},
    "error": {
        "code": "CHK0121",
        "message": "Invalid app fields",
        "exception": null
    },
    "operationId": "62cf897f-2025-4304-8e25-2104b58d416d"
}
```

### 404 - Not found

- `Message error example (code CHK0090): "App id not found"`: this message indicates that the `appId` parameter used in the request does not exist or is incorrect.

```json
{
    "fields": {},
    "error": {
        "code": "CHK0090",
        "message": "App id not found",
        "exception": null
    },
    "operationId": "0926942a-769b-45ec-a7c3-3d733ed76a46"
}
```

- `Message error example (code CHK0091): "App key not found for id profile"`: this message indicates that the `appFieldName` parameter used in the request does not exist or is incorrect. This message code is applicable only for the **Set single custom field value** endpoint.

```json
{
    "fields": {},
    "error": {
        "code": "CHK0091",
        "message": "App key not found for id profile",
        "exception": null
    },
    "operationId": "6e8191fb-4f2a-41c8-8155-92d2595a96b3"
}
```

**Update orderForm configuration endpoint:**

### 400 - Bad Request

- `Message error example (code CHK0288): "Invalid configuration"`: this message indicates that the mandatory parameters (`paymentConfiguration`, `requiresAuthenticationForPreAuthorizedPaymentOption` and `minimumQuantityAccumulatedForItems`) was not sent in this request.

```json
{
    "fields": {},
    "error": {
        "code": "CHK0288",
        "message": "Invalid configuration",
        "exception": null
    },
    "operationId": "f2b8107f-e5d5-4b7c-b719-344d1b05d1fa"
}
