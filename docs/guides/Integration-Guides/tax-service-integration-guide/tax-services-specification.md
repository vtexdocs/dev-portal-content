---
title: "Specification"
slug: "tax-services-specification"
hidden: false
createdAt: "2020-09-01T16:35:02.523Z"
updatedAt: "2022-02-11T15:38:54.137Z"
---

In synchronous integration, VTEX’s [Checkout API](https://developers.vtex.com/docs/api-reference/checkout-api) triggers and sends a request to the external tax service API whenever there are changes to a customer’s cart, such as adding or removing items.

To know more about how to implement a client to connect your tax calculation provider to VTEX’s APIs, the [Tax Service recipe](https://developers.vtex.com/docs/guides/tax-services-recipe) and [example](https://developers.vtex.com/docs/guides/tax-services-reference-implementation).

>⚠️ Timeout for the request is five seconds. There is no retry in case of timeout. If the external service that responds to the request times out constantly, the store will not be able to finish the order. If this integration is active, it applies to all stores in that account.

## Tax integration via Checkout API

You must activate the tax integration by configuring the `orderForm`, a object that stores contextual information about the order. This data is essencial to the checkout process of the order.

Check the flow of `orderForm` configuration below:

<img src="https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/tax-services-specification-0.svg"/>

To activate the tax integration, first it is necessary to get the current `orderForm` settings using the [Get `orderForm` configuration](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pvt/configuration/orderForm?endpoint=get-/api/checkout/pvt/configuration/orderForm).

In the request response, the `taxConfiguration` object has the tax information that must be updated. 

```json
  "taxConfiguration": {
        "url": "https://accountname.myvtex.com/tax-service/order-tax",
        "authorizationHeader": "99b9935b048dfd86893d0bf9gas628849",
        ...
    },
  "isMarketplaceResponsibleFoTaxes": false
```

Then, Checkout settings can be updated via [Update orderForm configuration](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pvt/configuration/orderForm?endpoint=post-/api/checkout/pvt/configuration/orderForm) endpoint.

The most important data in the `taxConfiguration` object is the `url`. This is the external API endpoint of the tax tool that the Checkout will query to receive the calculated taxes.

The `authorizationHeader` defines the value that the Checkout will use in the `Authorization` header of calls to the external tax calculation API. This field can be used to define the access credentials for this API.

```json
  "taxConfiguration": {
        "url": "{Tax provider URL}",
        "authorizationHeader": "{Tax provider authorization header}",
        ...
    },
  "isMarketplaceResponsibleFoTaxes": true,
  ...
```

After successfully submitting the request, the Tax API integration becomes active in synchronous mode.

>⚠️ When a purchase is made in a store, the location from which the order is shipped matters for tax calculation purposes. Because of this, when items from [White Label Sellers](https://help.vtex.com/en/tutorial/white-label-seller--5orlGHyDHGAYciQ64oEgKa) are part of an order, tax configuration for the marketplace (`seller 1`) is not taken into account for those items. Each seller must have its own tax service configuration in order for this type of integration function properly.

## Tax calculation request

The tax calculation tool must provide an endpoint that will receive a POST request. In this request, Checkout provides a body in a specific format. This means that either the endpoint must be prepared to receive this body format, or the integration must contain a parser to adapt it to the correct format.

Here is an example of that body sent by Checkout API:

```json
{
     "orderFormId": "e5098ad8c4jk490bb2f6f03400ac1413",
     "salesChannel": "1",
     "items": [
       {
         "id": "0",
         "sku": "26",
         "ean": "12345678909123",
         "refId": null,
         "unitMultiplier": 1,
         "measurementUnit": "un",
         "targetPrice": 8.2,
         "itemPrice": 8.2,
         "quantity": 1,
         "discountPrice": 0,
         "dockId": "1125a08",
         "freightPrice": 0,
         "brandId": "2000002"
       }
     ],
     "totals": [
       {
         "id": "Items",
         "name": "Items Total",
         "value": 820
       },
       {
         "id": "Discounts",
         "name": "Discounts Total",
         "value": 0
       },
       {
         "id": "Shipping",
         "name": "Shipping Total",
         "value": 0
       },
       {
         "id": "Tax",
         "name": "Tax Total",
         "value": 0
       }
     ],
     "clientEmail": "client@email.com",
     "shippingDestination": {
       "country": "BRA",
       "state": "RJ",
       "city": "Rio de Janeiro",
       "neighborhood": "Botafogo",
       "postalCode": "22250-905",
       "street": "Praia Botafogo"
     },
     "clientData": {
       "email": "client@email.com",
       "document": "12345678909",
       "corporateDocument": null,
       "stateInscription": null
     },
     "paymentData": {
       "payments": [
         {
           "paymentSystem": "2",
           "bin": null,
           "referenceValue": 820,
           "value": 820,
           "installments": null
         }
       ]
     }
}
```

This body has eight main fields:

| Field | Type | Description |
| - | - | - |
| `orderFormId` | string | `orderform` ID. |
| `salesChannel` | string | Type of sales channel. |
| `items` | array  | List of objects which are the order products, where `dockId` is a field that refers to its identification on the logistics system that contains information of its address. |
| `totals` | array  | Total amount of the order form, divided into taxes, shipping, discounts, and the items themselves. |
| `clientEmail` | string | Client's email address. |
| `shippingDestination` | object | Shipping information. Mandatory field. |
| `clientData` | object | Information regarding the client that placed the order. |
| `paymentData` | object | Contains an array of payments, where there is information regarding the order payment. |

### Tax provider response to the request

In response to the request sent by Checkout, we expect an array of products, each with its own array of taxes. See the example below:

```json
[
    {
        "id": "0",
        "taxes": [
            {
                "name": "TAX 1",
                "description": "Description 1",
                "value": 3.48
            },
            {
                "name": "TAX 2",
                "description": "Description 2",
                "value": 22
            }
        ]
    }
]
```

| Field | Type | Description |
| - | - | - |
| `id` | string | Request item index, which means the SKU's position on the `items` array sent by the request body. |
| `taxes` | array | List of all the taxes types for an SKU. |
| `name` | string | Tax name that will appear on the checkout. |
| `description` | string | Informative field, which does not appear on the storefront. |
| `value` | number | Absolute numeric value that will be added to the original price. |

In the example above, the only item in the items array has a cost of `10`, and, including the calculated taxes returned by the tax calculation tool, the total value would be `10 + 3.48 + 22 = 35.48`.

>ℹ️ If no taxes apply to the items in the order, the expected response is an empty array (`[]`).

For the Checkout API to understand the request body, the `content-type` must be set to `application/vnd.vtex.checkout.minicart.v1+json`.

#### Jurisdiction fields

If you use [Avalara](https://www.avalara.com/us/en/index.html) as your tax calculation provider, response bodies might also include the following fields, which refer to the different jurisdictions that may apply according to location.

| Field | Type | Description |
| - | - | - |
| `jurisType` | string | Type of jurisdiction that applies to calculation. |
| `jurisCode` | string | Unique code that identifies the appropriate jurisdiction. |
| `jurisName` | string | Name of the jurisdiction that applies to the calculation. |

These fields are also read by Checkout and added to the `priceTag`.

Below is an example for values that may be contained in these fields, and you can [download all of the jurisdictions and respective codes used by Avalara](https://help.avalara.com/Avalara_AvaTax_Update/Download_jurisdiction_codes).

```json
{
  "jurisType": "State",
  "jurisCode": "20",
  "jurisName": "Kansas"
}
```

```html
{
  "html": "<link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css\" integrity=\"sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm\" crossorigin=\"anonymous\">\n<script src=\"https://code.jquery.com/jquery-3.2.1.slim.min.js\" integrity=\"sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN\" crossorigin=\"anonymous\"></script>\n<script src=\"https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js\" integrity=\"sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q\" crossorigin=\"anonymous\"></script>\n<script src=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js\" integrity=\"sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl\" crossorigin=\"anonymous\"></script>\n\n\n<a href=\"tax-service-integration-guide\"<button type=\"button\" class=\"btn btn-outline-secondary\">Back</button></a>\n\n<style></style>"
}
```