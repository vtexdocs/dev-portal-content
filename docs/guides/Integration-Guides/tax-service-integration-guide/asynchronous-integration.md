---
title: "Tax service asynchronous integration"
slug: "asynchronous-integration"
hidden: true
createdAt: "2021-02-24T13:33:21.352Z"
updatedAt: "2021-02-24T14:39:42.422Z"
---
If you use synchronous tax service integration, you might find some limitations:

- Timeout for the request is five seconds.
- There is no retry in case of timeout.
- If the external service that responds to the request times out constantly, the store will not be able to finish the order.
- If this integration is active, it applies to all stores in that account.

> ⚠️ For stores in which there are often up to hundreds of items in a cart, like some B2B operations, this flow can become inefficient and expensive. In this case, consider using asynchronous integration.

## Asynchronous integration

Asynchronous integration is an alternative that offers a better user experience, as it ensures that the flow will always have the taxes at the right time, although it depends directly on the resilience of third parties.

By definition, this type of integration allows other processes to move forward while it waits for a response from the tax engine. Thus, the system will not respond with a timeout even if it takes more than 5 seconds to respond.

Instead of calling the external tax service API for each item added to the cart, asynchronous integration will send just one request resulting in  less data being processed, and thus checkout becomes faster and more efficient. That request can be triggered, for instance, by an event in the checkout UI.

### Implementing asynchronous integration

To use asynchronous integration, Checkout can not be configured to handle the External Tax Services. This configuration should only be done for synchronous integration. To use asynchronous integration, make sure that the response from the [Checkout Configuration API](https://developers.vtex.com/reference/configuration) has the `taxConfiguration` object with the value `null`. If not, use the Checkout Configuration UPDATE request to make it `null`.

The asynchronous call to the tax engine does not require any configuration. It must be implemented by the store, as described in this [recipe](https://developers.vtex.com/docs/guides/tax-services-recipe). It is usually triggered by an event or button in the checkout UI.

To query the tax engine, the implementation must follow this flow:

- Get the orderForm.
- Calculate taxes (or get calculation from the external provider).
- Submit response with taxes.

#### Getting the orderForm

To obtain the orderForm, the implementation must use the following request:

- __Method__: `GET`
- __URL__: `https://{accountName}.{environment}.com.br/api/checkout/pub/orderForm/{orderFormId}?disableAutoCompletion=true`
[block:callout]
{
  "type": "info",
  "body": "The `disableAutoCompletion=true` parameter is necessary to ensure that the requested orderForm won’t be recalculated but delivered exactly as it was at the time of the request."
}
[/block]

> ⚠️ Although the route is public (`/pub`), it is necessary to use credentials (`appKey` and `appToken`) with permission to access the cart data to obtain the unmasked data.

#### Calculating taxes and sending the response

Having obtained the `orderForm`, the implementation must calculate the appropriate taxes, or get the appropriate calculations from the external provider, and send the following information in the response:

- `itemTaxResponse`: an array of items (SKUs), each containing an array of applicable taxes.
- `miniCartRequest`: an object containing the items, delivery address, buyer data, orderForm ID, and trade policy of the cart receiving the taxes.

Taxes should be sent to the following endpoint:

- __Method__: `POST`
- __URL__: `https://{accountName}.vtexcommercestable.com.br/api/checkout/pvt/orderForms/taxes`

Below is an example body.

This request requires the `appKey` and `appToken` credentials.

```json
{
    "itemTaxResponse": [
        {
            "sku": "8",
            "taxes": [
                {
                    "name": "Tax1",
                    "value": 1.28
                },
                {
                    "name": "Tax2",
                    "value": 7.91
                }
            ]
        },
        {
            "sku": "33",  // SKU id
            "taxes": [
                {
                    "name": "Tax1",   // name you want to use for the tax
                    "value": 3.98
                }
            ]
        }
    ],
    "miniCartRequest": {
        "orderFormId": "9c7aad42ee2d4a37a23478a9d5cb6f30",
        "salesChannel": "1",
        "items": [
            {
                "sku": 8,
                "ean": null,
                "refId": "1111A",
                "unitMultiplier": 1,
                "measurementUnit": "un",
                "targetPrice": 80,   // price
                "itemPrice": 240,    // total price (price * qty * unitMultiplier)
                "discountPrice": 0,  // item discounts
                "freightPrice": 0.9, // item’s freight price
                "quantity": 3,
                "dockId": "1",
                "brandId": 2000000
            },
            {
                "sku": 33,
                "ean": null,
                "refId": "1111B",
                "unitMultiplier": 1,
                "measurementUnit": "un",
                "targetPrice": 20,
                "itemPrice": 40,
                "discountPrice": 0,
                "freightPrice": 0.6,
                "quantity": 2,
                "dockId": "1",
                "brandId": 2000000
            }
        ],
        "shippingDestination": {     // required!
            "country": "BRA",
            "state": "RJ",
            "city": "Rio de Janeiro",
            "neighborhood": "Botafogo",
            "postalCode": "22250-040",
            "street": "Praia de Botafogo"
        },
        "clientData": {
            "email": "email@gmail.com.br",
            "document": "01234567890",
            "corporateDocument": null
        }
    }
}
```

#### Validating taxes

Note that the tax engine response includes, in addition to the taxes, the minicart that was used for the calculation. So, VTEX is able to guarantee that the calculated tax is consistent with the cart that is completing the purchase. This happens through the following algorithm:

- When the system receives the response from the tax provider, it gets the minicart that was used to calculate the taxes.
- The system generates a token for this minicart and saves it in the cart.
- When the purchase is concluded, the token is sent to the seller, who checks whether it matches the cart that is completing the purchase.
- If it is the same token, the purchase is completed, with the tax applied. If the tokens do not match, the purchase is denied.
- If the purchase is denied, there will be a 500 error in the request `/transaction`: “The order cannot be created. Please try again."

[block:callout]
{
  "type": "info",
  "body": "The implementer is responsible for the minicart. Note that it is crucial for validating taxes, so there must be an exact match with the customer's current cart."
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "If the system takes too long to apply the tax, you can create an order without taxes."
}
[/block]

> ⚠️ If the system takes too long to review the tax after changes to the cart, it will not be possible to complete the order.

#### Example of order object

Finally, see an example of an order object at VTEX after taxes are applied. Note that they have been included in the `totals` array.

```json
{
  "emailTracked": "0df1ee8d7f58474782c3750e2f42e4ed@ct.vtex.com.br",
  "approvedBy": null,
  "cancelledBy": null,
  "cancelReason": null,
  "handlingData": null,
  "orderId": "v3613574JRSA-01",
  "sequence": "3613574",
  "marketplaceOrderId": "",
  "marketplaceServicesEndpoint": "http://oms.vtexinternal.com.br/api/oms?an=mystore",
  "sellerOrderId": "00-v3613574JRSA-01",
  "origin": "Marketplace",
  "affiliateId": "",
  "salesChannel": "1",
  "merchantName": null,
  "status": "ready-for-handling",
  "statusDescription": "Pronto para o manuseio",
  "value": 598095,
  "creationDate": "2020-05-26T17:37:56.2353707+00:00",
  "lastChange": "2020-05-26T17:39:24.4238867+00:00",
  "orderGroup": null,
  "totals": [
    {
      "id": "Items",
      "name": "Total de los items",
      "value": 656890
    },
    {
      "id": "Discounts",
      "name": "Total de descuentos",
      "value": 0
    },
    {
      "id": "Shipping",
      "name": "Costo total del envío",
      "value": 0
    },
    {
      "id": "Tax",
      "name": "Costo total del cambio",
      "value": 0
    },
    {
      "id": "CustomTax",
      "name": "FI_ SOCIOS PREMIUM ",
      "value": 297
    },
    {
      "id": "CustomTax",
      "name": "VI_P 3X2_BEBIDAS   ",
      "value": 400
    }
  ],
  "items": [
    {
      "uniqueId": "892FF75C59301ACE8CBE75BA7P0E1BE9",
      "id": "4321",
      "productId": "1234",
      "ean": "9974111597732",
      "lockId": "00-v3612391AKPI-01",
      "itemAttachment": {
        "content": {},
        "name": null
      },
      "attachments": [],
      "quantity": 1,
      "seller": "1",
      "name": "My Product",
      "refId": "11570114019",
      "price": 5750,
      "listPrice": null,
      "manualPrice": null,
      "priceTags": [],
      "imageUrl": "https://mystore.vteximg.com.br/arquivos/ids/521666-55-55/myproduct-12-U-1-2256.jpg?v=536862711303520990",
      "detailUrl": "/my-product/p",
      "components": [],
      "bundleItems": [],
      "params": [],
      "offerings": [],
      "sellerSku": "2511",
      "priceValidUntil": null,
      "commission": 0,
      "tax": 0,
      "preSaleDate": null,
      "additionalInfo": {
        "brandName": "BRAND",
        "brandId": "1190",
        "categoriesIds": "/1/29/201/",
        "categories": [
          {
            "id": 201,
            "name": "Category1"
          },
          {
            "id": 29,
            "name": "Category2"
          },
          {
            "id": 1,
            "name": "Category3"
          }
        ],
        "productClusterId": "1171,1401,2643,2832,4121,4318,4342",
        "commercialConditionId": "1",
        "dimension": {
          "cubicweight": 0.0002,
          "height": 1,
          "length": 1,
          "weight": 1,
          "width": 1
        },
        "offeringInfo": null,
        "offeringType": null,
        "offeringTypeId": null
      },
      "measurementUnit": "un",
      "unitMultiplier": 1,
      "sellingPrice": 5750,
      "isGift": false,
      "shippingPrice": null,
      "rewardValue": 0,
      "freightCommission": 0,
      "priceDefinitions": null,
      "taxCode": null,
      "parentItemIndex": null,
      "parentAssemblyBinding": null,
      "callCenterOperator": null,
      "serialNumbers": null,
      "assemblies": [],
      "costPrice": null
    }
  ],
  "marketplaceItems": [],
  "clientProfileData": {
    "id": "clientProfileData",
    "email": "email@gmail.com",
    "firstName": "John",
    "lastName": "Doe",
    "documentType": "DNI",
    "document": "12345678",
    "phone": "+55012345678",
    "corporateName": null,
    "tradeName": null,
    "corporateDocument": null,
    "stateInscription": null,
    "corporatePhone": null,
    "isCorporate": false,
    "userProfileId": "1c87654df-f25c-49jf-9e9f-4839c00009a6",
    "customerClass": null
  },
  "giftRegistryData": null,
  "marketingData": null,
  "ratesAndBenefitsData": {
    "id": "ratesAndBenefitsData",
    "rateAndBenefitsIdentifiers": [
      {
        "description": "christmas2020",
        "featured": true,
        "id": "011p7fbc-2129-424e-b45e-4b53fa8d4805",
        "name": "christmas2020",
        "matchedParameters": {
          "productCluster@CatalogSystem": "4848|inclusive"
        },
        "additionalInfo": null
      }
    ]
  },
  "shippingData": {
  ...
  },
  "paymentData": {
  ...
  },
  "packageAttachment": {
    "packages": []
  },
  "sellers": [
    {
      "id": "1",
      "name": "My Store",
      "logo": "",
      "fulfillmentEndpoint": "http://fulfillment.vtexcommerce.com.br/api/fulfillment?sc=1&an=mystore"
    }
  ],
  "callCenterOperatorData": null,
  "followUpEmail": "email@vtex.com",
  "lastMessage": null,
  "hostname": "storehostname",
  "invoiceData": null,
  "changesAttachment": null,
  "openTextField": null,
  "roundingError": 0,
  "orderFormId": "48x123e0baff36718d0nc81e56cec29c",
  "commercialConditionData": null,
  "isCompleted": true,
  "customData": null,
  "storePreferencesData": {
    "countryCode": "ARG",
    "currencyCode": "ARS",
    "currencyFormatInfo": {
      "CurrencyDecimalDigits": 2,
      "CurrencyDecimalSeparator": ",",
      "CurrencyGroupSeparator": ".",
      "CurrencyGroupSize": 3,
      "StartsWithCurrencySymbol": true
    },
    "currencyLocale": 11274,
    "currencySymbol": "$",
    "timeZone": "Argentina Standard Time"
  },
  "allowCancellation": false,
  "allowEdition": false,
  "isCheckedIn": false,
  "marketplace": {
    "baseURL": "http://oms.vtexinternal.com.br/api/oms?an=mystore",
    "isCertified": null,
    "name": "mystore"
  },
  "authorizedDate": "2020-05-26T17:38:10.2154236+00:00",
  "invoicedDate": null,
  "itemMetadata": null,
  "subscriptionData": null,
  "taxData": null,
  "checkedInPickupPointId": null,
  "cancellationData": null
}
```

[block:html]
{
  "html": "<link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css\" integrity=\"sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm\" crossorigin=\"anonymous\">\n<script src=\"https://code.jquery.com/jquery-3.2.1.slim.min.js\" integrity=\"sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN\" crossorigin=\"anonymous\"></script>\n<script src=\"https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js\" integrity=\"sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q\" crossorigin=\"anonymous\"></script>\n<script src=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js\" integrity=\"sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl\" crossorigin=\"anonymous\"></script>\n\n\n<a href=\"tax-service-integration-guide\"<button type=\"button\" class=\"btn btn-outline-secondary\">Back</button></a>\n\n<style></style>"
}
[/block]
