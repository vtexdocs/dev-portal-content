---
title: "Recipe"
slug: "tax-services-recipe"
hidden: false
createdAt: "2020-09-01T16:36:08.632Z"
updatedAt: "2021-02-09T15:24:50.558Z"
---
## Clients

Clients are an abstraction for implementing connections to VTEX APIs or external ones that are agnostic to the purpose of the application you are developing. So, the methods of a client class expect some parameters that are necessary for some calls to the API, such as a body to a `POST` request.

### Developing clients on a tax service

Regarding the purpose of a tax service integration, there are some connections to be implemented:

- To the [Checkout API](), to do the `orderForm` configuration.
- To the Tax Provider API, to calculate any taxes related to the items of a cart.

### Example of implementation

This [tax protocol example](https://github.com/vtex-apps/tax-protocol-example) is one way you can implement your clients. More details below:

- `Checkout`: used to configure the tax service in the Checkout;

- `Logistics`: it has a single method that can be used to fetch information about docks, using its id;

- `TaxProvider`: used to connect with the provider's external API;

- `VtexCommerce`: a basic external client that can be used as the class that can be inherited to develop other clients that connect to VTEX API.

## Routes

Routes are the endpoints that will be defined on the `service.json` file and need to have handlers to deal with the requests that are coming through those routes.

### Necessary routes

When implementing a tax integration app, there are three types of operations that the application needs to handle defining routes and using handlers:

- Configure the tax integration by changing the order form configuration - activate or deactivate.

> Private route that configures the tax service for a specific account.

- Simulate the taxes to be applied to a cart and return this information to the Checkout in a specific format.

> This route will be the one that is going to be registered on the Order Form Configuration.

- Commit the order taxes based on a logic regarding the order status changing

> It's the same route that is on the `hooks` object on the provider's response to the Checkout API after calculating the taxes.

It is important to emphasize that, for the last two routes to work, you must have the tax service configured in your account. This can be done by using the first endpoint described above. Basically, in this step, one is going to:

1. Define the routes in the `service.json` file;
2. Create handlers for those routes;
3. Use the handlers on the `node/index.ts` file.

## Parsers

As a way to simplify the logic behind the handlers that need to exist when developing integration with a tax service, the entire code logic needed to parse the payloads to a specific format can be implemented as a parser. This can be necessary because both the external provider API and Checkout API expect specific payload formats.

There are a lot of ways of doing it, but this documentation focuses on how it was made in the Tax Protocol Example that you can find on Github.

### Parsing data from VTEX to provider

The external provider API will receive a POST request with a specifically formatted body from Checkout. In case the provider expects a different format, one can implement the logic inside a function that parses the information.

### Parsing data from provider to VTEX

Considering the request done by the provider to the VTEX Checkout API, it is also possible to implement a parser in order to put the payload in the format that the checkout expects.

[block:html]
{
  "html": "<link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css\" integrity=\"sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm\" crossorigin=\"anonymous\">\n<script src=\"https://code.jquery.com/jquery-3.2.1.slim.min.js\" integrity=\"sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN\" crossorigin=\"anonymous\"></script>\n<script src=\"https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js\" integrity=\"sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q\" crossorigin=\"anonymous\"></script>\n<script src=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js\" integrity=\"sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl\" crossorigin=\"anonymous\"></script>\n\n\n<a href=\"tax-service-integration-guide\"<button type=\"button\" class=\"btn btn-outline-secondary\">Back</button></a>\n\n<style></style>"
}
[/block]
