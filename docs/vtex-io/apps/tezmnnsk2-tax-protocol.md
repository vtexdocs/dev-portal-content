---
title: "Tax Protocol Example"
slug: "tezmnnsk2-tax-protocol"
excerpt: "tezmnnsk2.tax-protocol@0.3.1"
hidden: true
createdAt: "2022-07-22T17:52:36.340Z"
updatedAt: "2022-08-02T18:28:35.708Z"
---
A reference app implementing a VTEX IO Tax Protocol service.

## Uses
This app is an example to be followed in order to develop a tax service integration with VTEX. 

## Clients
In this example, there are a few clients implemented for you to use.
- `Catalog`: can be used to retrieve information regarding produts, in case of needing more data besides those that come on the tax payload
- `Checkout`: used to configure the tax service in the Checkout
- `Logistics`: it has a single method that can be used to fetch information about docks.
- `TaxProvider`: used to connect with the provider's external API.
- `VtexCommerce`: basic external client that can be used as the class that can be inherited to develop other clients that connectes to VTEX API. 

## Parsers
As a way to simplify the logic behind the handlers that are implemented in this example, all the code logic that can be necessary to parse the payloads to a specific format is expected to be implemented inside `parsers` directory. This is necessary because both the external provider API and VTEX API expect specific payload formats. Inside the folder, there are two files, `providerToVtex.ts` and `vtexToProvider.ts`.

### VTEX to Provider
The provider API will receive a HTTP post request with a well-defined body from the checkout. In case of it expecting a different format, one can implement the loginc inside `vtexToProvider` function. 

An example of the body sent in the checkout post request is:
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

### Provider to VTEX
Considering the request done by the provider to the VTEX Checkout API, it's also possible to implement a parser in order to put the payload in the format that the checkout expects. One can find an example of the expected format:

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
          "url": "https://master--bufferin.myvtex.com/app/tax-provider/oms/invoice"
        }
    ]
}
```

## GraphQL queries and mutations
Both have resolvers that can be tested on GraphiQL. They use the `Checkout` client in order to do POST or GET HTTP requests regarding the Order Form Configuration.

### `getTaxConfiguration` query
Responsible to fetch information regarding the Tax Configuration of an account, its resolver makes a GET request to `Checkout` and get the Order Form configuration.

### `setTaxConfiguration` mutation
It expects a parameter, which can be `activate` or `deactivate` and it does a POST HTTP request to set the Tax Configuration on the Order Form Configuration. In order to do so, it uses a `Checkout` client. 

Having it ready is useful for those integration that need a admin panel to configure the tax service, since it's possible to use React Hooks in order to call the mutation.

## Using GraphiQL to configure the tax service on an account

In order to test the integration, it's necessary configure the integration on desired account. In order to do so, you can use the GraphiQL route that is available when linking the application to write the necessary mutation.

Below you can find a mutation example that can be used to configure the tax integration. It's been written and executed on the GraphiQL route that is available when linking the app.

```graphql
mutation setConfiguration ($operation: String) {
  setTaxConfiguration(operation: $operation) {
    taxConfiguration {
      allowExecutionAfterErrors
      authorizationHeader
      integratedAuthentication
      url
    }
  }
}
```
> Note: `$operation` is a query variable that is configured on the GraphiQL, the GraphQL IDE.

You can find an image of GraphiQL below:

![image](https://user-images.githubusercontent.com/19495917/89305970-a9ea1800-d645-11ea-9131-cab6efd34cf8.png)


## Routes
There are two main routes in this example and they are mainly using mocked values so as to simulate their functions.

It is important to emphasize that for the first two endpoints to work, you **must** have the tax service configured in your account, which can be done by using GraphiQL, as it was explained in the previous step.

- `taxSimulation`: responsible for simulating a Checkout request for tax calculation.
- `orderInvoice`: public route to send the taxes.

## Testing the example app

After having the integration properly configured, you can test those routes using this [Postman collection](https://www.getpostman.com/collections/3b2ee13b0cbba50e0809).

> **Attention!** The authorization header that it's present in the Postman collection is a mocked value to be correctly validated by the handlers. This value is defined in the `utils/constants.ts` file and it's used to configure the tax service when calling the `settings` endpoint.


**Upcoming documentation:**

 - [Fixing problem with dependency](https://github.com/vtex-apps/tax-protocol-example/pull/9)