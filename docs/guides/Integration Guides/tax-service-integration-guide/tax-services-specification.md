---
title: "Specification"
slug: "tax-services-specification"
hidden: false
createdAt: "2020-09-01T16:35:02.523Z"
updatedAt: "2022-02-11T15:38:54.137Z"
---
Below, we are going to go over tax service integration works, and if you want to know more about how to implement a client to connect your tax calculation provider to VTEX’s APIs, this [recipe](https://developers.vtex.com/vtex-developer-docs/docs/tax-services-recipe) and [example](https://developers.vtex.com/vtex-developer-docs/docs/tax-services-reference-implementation) might help you.

# How it works

In synchronous integration, VTEX’s Checkout API triggers and sends a request to the external tax service API whenever there are changes to a customer’s cart, such as adding or removing items.

[block:callout]
{
  "type": "warning",
  "body": "- Timeout for the request is five seconds.\n- There is no retry in case of timeout.\n- If the external service that responds to the request times out constantly, the store will not be able to finish the order.\n- If this integration is active, it applies to all stores in that account.",
  "title": "When using Tax Service integration, keep in mind that:"
}
[/block]
## Checkout Configuration

Synchronous tax integration can be activated or deactivated through a request to the Checkout Configuration API.

<img src="https://appliancetheme.vtexassets.com/assets/app/src/tax-protocol-image-2___28abb75b71aba103910c818a4fd037a5.svg"></img>

First, it is necessary to GET the current `orderForm` settings from this endpoint:

`https://{accountName}.{environment}.com.br/api/checkout/pvt/configuration/orderForm`

Then, Checkout settings can be updated via a POST call to the same endpoint. The full request body can be found in the [Update orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/updateorderformconfiguration), as well as more details on that API. Here we will focus on the `taxConfiguration` object, which defines the External Tax Service settings:

```json
  "taxConfiguration": {
        "url": "https://accountname.myvtex.com/tax-service/order-tax",
        "authorizationHeader": "99b9935b048dfd86893d0bf9gas628849",
    }
```

The most important data in this object is the `url`. This is the endpoint URL that the Checkout will query to receive the calculated taxes. In other words, this is the external API endpoint of the tax tool.

The `authorizationHeader` defines the value that the Checkout will use in the `Authorization` header of calls to the external tax calculation API. This field can be used to define the access credentials for this API.

Once the POST for the Checkout Configuration API has finished processing the request with this data, its synchronous integration with the Tax API is activated.
[block:callout]
{
  "type": "warning",
  "body": "When a purchase is made in a store, the location from which the order is shipped matters for tax calculation purposes. Because of this, when items from [White Label Sellers](https://help.vtex.com/pt/tutorial/definicoes-de-conta-franquia-e-seller-white-label--5orlGHyDHGAYciQ64oEgKa#) are part of an order, tax configuration for the marketplace (seller 1) is not taken into account for those items. Each seller must have its own tax service configuration in order for this type of integration function properly."
}
[/block]
## Tax calculation request

The tax calculation tool must provide an endpoint that will receive a POST request. In this request, Checkout provides a body in a specific format. This means that either the endpoint must be prepared to receive this body format, or the integration must contain a parser to adapt it to the correct format.

Let’s see an example of that body sent by Checkout:

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

- `orderFormId`: *string* related to the order form ID;

- `salesChannel`: type of sales channel;

- `items`: an *array* that contains objects which are the order products, where **dockId** is a field that refers to its identification on the logistics system that contains information of its address;

- `totals`: an *array* with the total amount of the order form, divided into taxes, shipping, discounts, and the items themselves;

- `clientEmail`: *string* that contains the client's email;

- `shippingDestination`: *object* with shipping information, it's a mandatory field;

- `clientData`: *object* that contains information regarding the client that did the order;

- `paymentData`: *object* that contains an *array* of payments, where there is information regarding the payment methods, etc.

## Tax provider response to the request

In response to the request sent by Checkout, we expect an array of products, each with its own array of taxes. See the example below:

```json
{
    "itemTaxResponse": [
            {
            "id": "0",
            "taxes": [
              {
                "name": "TAX 1",
                "description": "",
                "value": 3.48
              },
              {
                "name": "TAX 2",
                "description": "",
                "value": 22
              }
            ]
          }
        ],
    "hooks": [
        {
          "major": 1,
          "url": "http://master--bufferin.myvtex.com/avalara/checkout/salesinvoice-tax"
        }
    ]
}
```

- `itemTaxResponse` is an array of objects that corresponds to all the tax information that is applied to the different items sent to the tax provider. The main fields of those objects are described below:

- `id` is the request item index, which means the SKU position on the items array sent by the requisition body;

- `taxes` is an array that contains all the taxes types for an SKU;

- `name` is the tax name that will appear on the checkout;

- `description` is an informative field. It will not appear on the storefront;

- `value` is the absolute value that will be added to the original price;

- `hooks` should be an empty array, but any entry on the array corresponds to an URL that will be called when an order has its status changed. Usually, the relevant status change to listen to is “invoiced”. This URL needs to be prepared to receive the order id and should just respond to an HTTP 200 status.

In the example above, the only item in the items array has a cost of `10`, and, including the calculated taxes returned by the tax calculation tool, the total value would be `10 + 3.48 + 22 = 35.48`.

[block:callout]
{
  "type": "info",
  "body": "If no taxes apply to the items in the order, the expected response is an empty array (`[]`)."
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "For the Checkout API to understand the request body, the content-type must be set to `application/vnd.vtex.checkout.minicart.v1+json`"
}
[/block]

### Jurisdiction fields

If you use Avalara as your tax calculation provider, response bodies might also include the following fields, which refer to the different jurisdictions that may apply according to location.

- `jurisType`: Type of jurisdiction that applies to calculation.
- `jurisCode`: Unique code that identifies the appropriate jurisdiction.
- `jurisName`: Name of the Jurisdiction that applies to the calculation.

These fields are also read by Checkout and added to the `priceTag`.

Below is an example for values that may be contained in these fields, and you can download all of the jurisdictions and respective codes used by Avalara [here](https://help.avalara.com/Avalara_AvaTax_Update/Download_jurisdiction_codes).

```json
{
“jurisType”: “State”,
“jurisCode”: “20”,
“jurisName”: “Kansas”
}
```


[block:html]
{
  "html": "<link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css\" integrity=\"sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm\" crossorigin=\"anonymous\">\n<script src=\"https://code.jquery.com/jquery-3.2.1.slim.min.js\" integrity=\"sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN\" crossorigin=\"anonymous\"></script>\n<script src=\"https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js\" integrity=\"sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q\" crossorigin=\"anonymous\"></script>\n<script src=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js\" integrity=\"sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl\" crossorigin=\"anonymous\"></script>\n\n\n<a href=\"tax-service-integration-guide\"<button type=\"button\" class=\"btn btn-outline-secondary\">Back</button></a>\n\n<style></style>"
}
[/block]