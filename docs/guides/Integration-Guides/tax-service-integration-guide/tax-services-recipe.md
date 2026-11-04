---
title: "Recipe"
slug: "tax-services-recipe"
hidden: false
createdAt: "2020-09-01T16:36:08.632Z"
updatedAt: "2026-10-27T12:00:00.000Z"
excerpt: "Learn how to build a tax service app with clients, routes, and parsers that connect VTEX Checkout to an external tax provider."
---
## Clients

Clients are an abstraction for implementing connections to VTEX APIs or external ones that are agnostic to the purpose of the application you are developing. So, the methods of a client class expect some parameters that are necessary for some calls to the API, such as a body to a `POST` request.

### Developing clients on a tax service

Regarding the purpose of a tax service integration, there are some connections to be implemented to establish the [tax calculation flow](https://developers.vtex.com/docs/guides/tax-services-overview):

- To the [Checkout API](https://developers.vtex.com/docs/api-reference/checkout-api), to do the `orderForm` configuration.
- To the external tax provider API, to calculate any taxes related to the items of a cart.

### Example of implementation

This [tax protocol example](https://github.com/vtex-apps/tax-protocol-example) is one way you can implement your clients. More details below:

- `Checkout`: used to configure the tax service in the Checkout;

- `Logistics`: it has a single method that can be used to fetch information about docks, using its id;

- `TaxProvider`: used to connect with the provider's external API;

- `Checkout`: Configures the tax service in Checkout.
- `Logistics`: Fetches dock information by ID through a single method.
- `TaxProvider`: Connects to the provider's external API.
- `VtexCommerce`: Defines a basic external client that other clients inherit to connect to the VTEX API.

## Routes

Routes are the endpoints that will be defined on the `service.json` file and need to have handlers to deal with the requests that are coming through those routes.

### Necessary routes

When implementing a tax integration app, there are three types of operations that the application needs to handle defining routes and using handlers:

- Configure the tax integration by changing the order form configuration - activate or deactivate.

> ℹ️ Private route that configures the tax service for a specific account.

- Simulate the taxes to be applied to a cart and return this information to the Checkout in a specific format.

> ℹ️ This route will be the one that is going to be registered on the Order Form Configuration.

- Commit the order taxes based on a logic regarding the order status changing

> ℹ️ It's the same route that is on the `hooks` object on the provider's response to the Checkout API after calculating the taxes.

The simulate and commit routes work only after you configure the tax service in your account with the configuration route. To set up the routes:

1. Define the routes in the `service.json` file.
2. Create handlers for those routes.
3. Use the handlers on the `node/index.ts` file.

## Parsers

To simplify the logic behind the handlers required when developing an integration with a tax service, the entire code that parses payloads into a specific format can be implemented as a parser. This is necessary because both the external provider API and the Checkout API require specific payload formats.

There are many ways to do it, but this documentation focuses on how it was implemented in the Tax Protocol Example on GitHub.

### Parsing data from VTEX to provider

The external provider API will receive a POST request with a specifically formatted body from Checkout. In case the provider expects a different format, one can implement the logic inside a function that parses the information.

### Parsing data from provider to VTEX

Considering the response the provider returns to the VTEX Checkout API, it's also possible to implement a parser to format the payload as checkout expects.

Besides the `taxes` array, this payload can include an optional `fees` array for each item, used for charges that aren't taxes, such as regulatory or commercial fees. Learn more in [Item fees](https://developers.vtex.com/docs/guides/tax-services-specification#item-fees).
