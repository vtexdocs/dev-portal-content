---
title: "Service Example"
slug: "cea-minha-cea-services"
excerpt: "cea.minha-cea-services@0.1.2"
hidden: true
createdAt: "2022-08-03T15:04:36.241Z"
updatedAt: "2022-08-04T19:54:05.666Z"
---
A reference app implementing a VTEX IO service using the `dotnet` builder.

We're using the [Vtex.Api](https://github.com/vtex/dotnet-builder/tree/master/dotnet-vtex-api) library in order to get context information so we can setup a HttpClient to communicate with Core Commerce Apis.

We're also using [Refit](https://github.com/reactiveui/refit) as an automatic rest library to further simplify the api calls.

[NUnit](https://nunit.org) and [Moq](https://github.com/moq/moq) are being used for unit testing.

## Table of Contents
1. [Getting Started](#getting-started)
2. [Project Structure](#project-structure)
3. [The Manifest and Service Files](#the-manifest-and-service-files)
4. [The Routes Controller](#the-routes-controller)
5. [Connecting to VTEX Core Commerce APIs](#connecting-to-vtex-core-commerce-apis)


## Getting Started
<a name="getting-started"></a>
First of all you need an up and running VTEX IO environment, and you can use the toolbelt for that: [Toolbelt Reference](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-vtex-io-cli-installation-and-command-reference)

To begin testing this reference app, you need to be logged in on a VTEX environment:
```bash
$ vtex login accountName
```

The next step is setting up a workspace
```bash
$ vtex use workspaceName
```

Then you can `link` your app to your environment:

```bash
$ vtex link
```

Your app should be running and the available service routes will pop up on the console, like this:
```bash
09:47:31.145 - info: Available service routes:
https://sandboxbrdev.myvtex.com/_v/dotnet-example/health
https://sandboxbrdev.myvtex.com/_v/dotnet-example/taggedProduct/{id}
09:47:31.322 - info: App running 
```
## Project Structure

The `dotnet` folder contains a class library project **DotNetService.csproj** which is responsible for handling the routes and events configured in the `service.json` file.

Please keep in note that (at the time of this writing) the `dotnet` builder supports `netcoreapp3.0`, as in **.NET Core 3.0**. Further versions of the .NET Framework may be supported by future versions of the builder.

The project is structured as follows:

| Folder | Description |
| ------ | ----------- |
| Clients | Configures clients in order to facilitate external communication to other services.
| Controllers | Handles incoming requests and sends responses back to callers. Please note that in the IO environment, routing is explicitly declared in the service.json file and is not handled by the controllers themselves.
| Data | Contains all data repositories and their functions (such as CRUD operations)
| Models | Contains all business models and their domain logic. 
| Services | Services are in charge of orchestrating business logic by retrieving data from repositories and delegating calls to the models. Again, for the sake of simplicity this folder is being used for both domain services and application services in this reference app, but each app can make this distinction accordingly.
| Tests | All unit/integration tests go here.
| Utils | This folder is used for extension methods, exception handlers, and all generic purpose functions.

Its goal is to be a simplified but well-structured project that may serve as a model to develop IO services using C# and .NET Core frameworks.

## The Manifest and Service Files

To enable your service you need to change the `manifest.json` file in a few parts:
- First, we must add `dotnet` to the list of `builders`:
```json
"builders": {
  "dotnet": "2.x"
}
```
- To be able to make outgoing requests, we need to change the `policies` section. In this case, we're enabling access to the catalog api in the VTEX Core Commerce APIs:
```json
"policies": [
  {
    "name": "outbound-access",
    "attrs": {
      "host": "{{account}}.vtexcommercestable.com.br",
      "path": "/api/catalog/*"
    }
  }
]
```
For more information about the manifest file, please check the [Manifest](https://developers.vtex.com/vtex-developer-docs/docs/manifest) section from VTEX IO Documentation.

The `service.json` file on the other hand contains all the routes and parameters that allow the service to run, such as the stack (dotnet in this case) or how much memory it's allowed to use.

```json
{
  "stack": "dotnet",
  "memory": 256,
  "timeout": 20,
  "routes": {
    "HealthCheck": {
      "path": "/_v/dotnet-example/health",
      "public": true
    },
    "GetTaggedProduct": {
      "path": "/_v/dotnet-example/taggedProduct/:id",
      "public": true
    }
  }
}
```

In this example we're creating two routes: One is a simple health check, and the other returns products with "auto-generated" search tags. To further look into routing you can check the [Routes](https://developers.vtex.com/vtex-developer-docs/docs/routes) section from VTEX IO Documentation.

## The Routes Controller

The **RoutesController** acts as a handler for configured routes in `service.json`, so in this example we're going to create two methods to handle the **HealthCheck** and **GetTaggedProduct** routes.

```c#
[HttpGet]
public async Task<IActionResult> GetTaggedProduct(int id)
{
    if (id <= 0) return BadRequest("The required 'id' parameter must be a non-zero positive integer.");
    return Ok(await _productService.GetTaggedProduct(id));
}

[HttpGet]
public IActionResult HealthCheck()
{
    return Ok();
}
```

Please note that there's no point in decorating this method with the `Route` attribute, since routing is being taken care of already. Furthermore, the name of the method must match the route name in `service.json`.

## Connecting to VTEX Core Commerce APIs

As mentioned before, project uses Refit to make handling http requests easier and more streamlined. In **Clients/VtexHttpClient.cs** we set everything up to make requests to the core commerce platform, such as including default headers, setting the base uri and so on.

In this case we're using the catalog api to retrieve product information, but feel free to explore everything the platform has to offer: [Api Reference](https://developers.vtex.com/vtex-developer-docs/reference/get-to-know-vtex-apis)

In the **IProductRepository** interface we declare the endpoint signature and let Refit do its magic:

```c#
[Get("/api/catalog/pvt/product/{productId}")]
Task<Product> GetProduct(int productId);
```

Adding a refit client is just as simple (use the **StartupExtender** for that):

```c#
services.AddRefitClient<IProductRepository>().ConfigureHttpClient(VtexHttpClient.Configure);
```

Speaking of which, the `StartupExtender` class is used to build on top of the default Startup process enveloped by the `dotnet` builder. Exceptionally, its namespace must be `Vtex`or it won't work. 

## Contributing
At last but not least, please feel free to contribute and discuss about this service template.