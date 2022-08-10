---
title: "Creating customizable fields in the cart with Checkout API"
slug: "customizable-fields-with-checkout-api"
hidden: false
createdAt: "2021-03-26T15:43:44.040Z"
updatedAt: "2022-06-27T17:49:35.410Z"
---
During the checkout process, some stores have the need to request customer data that is not part of the orderForm's default set of objects. For example: gender, cell phone number, age etc.

To do this, you can use both Custom Data calls: one to create extra fields in the orderForm and the other to set the value of each of these fields.

This data will be available within the Order, in the _orders_ APIs (Orders management).

[See here the Custom Data API full documentation.](https://developers.vtex.com/vtex-rest-api/reference/setmultiplecustomfieldvalues)

## Creating customizable fields

To create custom fields in the orderForm, use the call below:

&bull; URL: `https://{{AccountName}}.vtexcommercestable.com.br/api/checkout/pvt/configuration/orderForm`

&bull; Method: `POST`

See below an example of the JSON that we must pass in the body of this call.

```json
{
	"paymentConfiguration": 
	{
		"requiresAuthenticationForPreAuthorizedPaymentOption": false
	},
	"minimumQuantityAccumulatedForItems": 1,
	"decimalDigitsPrecision": 2,
	"minimumValueAccumulated": 0,
	"apps": 
	[
		{
			"id":"profile",
			"fields":
			[
				"age",
				"gender"
			]
		},
		{
			"id":"address",
			"fields":
			[
				"phone2"
			]
		}
	]
}
```

The `apps` object is what defines the customizable fields that will be inserted into the store's orderForm.

When we make the call by passing the sample body above, two applications will be created, which function as groups of fields: one with ID `profile` and one with ID `address`.

In the __profile__ app, we have two fields:
- `age`
- `gender`

In the __address__ app, we will have one field:
- `phone2`

## Defining the value of customizable fields

Once the fields are created with the call explained above, you can also send values to them using the API.

To do this, use the call below:

&bull; URL: `https://{{AccountName}}.vtexcommercestable.com.br/api/checkout/pub/orderForm/{{orderFormId}}/customData/{{appName}}/{{appFieldName}}`

&bull; Method: `PUT`

See below an example of the JSON that we must pass in the body of this call.

```json
{
  "expectedOrderFormSections":
  [
    "items",
    "gifts",
    "totalizers",
    "clientProfileData",
    "shippingData",
    "paymentData",
    "sellers",
    "messages",
    "marketingData",
    "clientPreferencesData",
    "storePreferencesData",
    "customData"
  ],
  "value":{{appFieldValue}}
}
```

In the URL of the call, you must pass the following parameters:
- `{{orderFormId}}`: ID of the orderForm to which the values will be sent.
- `{{appName}}`: name of the app (that is, of the group of fields defined in the previous call) where the values will be sent.
- `{{appFieldName}}`: name of the field for which to set the value. In the example of the fields created in the previous call, it could be `age`, `gender` or `phone2`.

In the body you must pass the `{{appFieldValue}}`, which is the value to be sent.