---
title: "Gift Card Protocol Example"
slug: "lojahyperapharma-uny-giftcard-provider"
excerpt: "lojahyperapharma.uny-giftcard-provider@0.0.8"
hidden: true
createdAt: "2022-07-08T21:18:10.206Z"
updatedAt: "2022-07-28T17:49:10.198Z"
---
A reference app implementing a VTEX IO Gift Card integration service. This app is an example to be followed in order to develop a gift card service integration with VTEX. 

## Testing the app
At first, once you link this application, it's important to know that so as to test it in a store to place an order, for example, it's necessary to register the external provider on the account. By doing that, Gift Card Hub will know how to compose the routes which it's going to send the requests to. This step can be found in the [GraphQL section](#graphql-queries-and-mutations).

Having the app linked, it will have the routes mentioned before exposed. At first, you can test all your routes on Postman, to make sure that they work as you expect it to. After doing that, you can trigger the communication between the Gift Card Hub and your application by simulating a purchase on a store. You'll have to configure your provider on an account so you can use it on your simulation.

> **NOTE**: Some endpoints are only used when the order status changes, such as settlement and cancellation, which means that you need to have permission to use the admin panel to change orders' status.


## Clients
In this example, there are a few clients implemented for you to use.
- `GiftCardHub`: used to connect to the Gift Card Hub to configure or delete a provider on an account;
- `GiftCardProvider`: used to connect to the provider's external API, where it must have methods implemented to handle all the request that the Gift Card Hub might make;
- `VtexCommerce`: basic external client that can be used as the class that can be inherited to develop other clients that connectes to VTEX API. 

## Routes
Gift Card Hub expects the provider's API to be able to handle some endpoints that are related to gift card, transactions, cancellations, settlements, etc. In this example, all the routes are defined on the `service.json` and have their handlers implemented. 
> The base URL that is used is defined when configuring the provider on an account.

## Parsers
As a way to simplify the logic behind the handlers that are implemented in this example, all the code logic that can be necessary to parse the payloads to a specific format is expected to be implemented inside `parsers` directory. This is necessary because both the external provider API and VTEX API expect specific payload formats. Inside the folder, there are two files, `providerToVtex.ts` and `vtexToProvider.ts`.

### VTEX to Provider
In this file, you can define parsers to convert request body formats to the formar that the provider's API expects. In this example, there are some functions implemented, feel free to use them to help developing the integration.

### Provider to VTEX
It's not always that the provider's API have response or request bodies that are aligned with the format that VTEX expects. In this file, you can define parsers to convert them.

## GraphQL queries and mutations

### Getting list of providers configured on an account
There is a GraphQL query that can be used on GraphiQL to check the providers that are configured on the account you're running this application.

To do that, you can use the route that is available to GraphiQL when linking this app and write a query similar to the following one:

```graphql
query {
  getGiftCardProviders{
    serviceUrl
    oauthProvider
    preAuthEnabled
    cancelEnabled
  }
}
```

After doing that, you will receive a response similar to this one:
```json
{
  "data": {
    "getGiftCardProviders": [
      {
        "serviceUrl": "http://api.vtex.com/appliancetheme",
        "oauthProvider": "vtex",
        "preAuthEnabled": true,
        "cancelEnabled": true
      },
      {
        "serviceUrl": "https://fabiana--appliancetheme.myvtex.com/my-provider",
        "oauthProvider": "vtex",
        "preAuthEnabled": true,
        "cancelEnabled": true
      }
    ]
  }
}
```

> **Note**: There will always be a VTEX Gift Card provider configured on any account, because this is the native provider offered by VTEX.

### Using GraphiQL to configure the gift card provider on an account

In this example app, there are also two mutations configured, which are related to adding or deleting a provider from an account.

- Setting a provider
  ```graphql
  mutation ($id: String, $giftCardProvInput: GiftCardProviderInput) {
    setGiftCardProvider (id: $id, giftCardProvInput: $giftCardProvInput){
      serviceUrl
      oauthProvider
      preAuthEnabled
      cancelEnabled
    }
  }
  ```

  Query variables:
  ```json
  {
    "id": "FabianaTest2",
    "giftCardProvInput": {
      "serviceUrl": "https://fabiana--appliancetheme.myvtex.com/my-provider",
      "oauthProvider": "vtex",
      "preAuthEnabled": true,
      "cancelEnabled": true
    }
  }
  ```

- Deleting a provider
  ```graphql
  mutation ($id: String) {
    deleteGiftCardProvider (id: $id){
      serviceUrl
      oauthProvider
      preAuthEnabled
      cancelEnabled
    }
  }
  ```

  Query variables:
  ```json
  {
    "id": "FabianaTest2",
  }
  ```