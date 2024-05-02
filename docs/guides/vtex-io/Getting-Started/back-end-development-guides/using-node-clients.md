---
title: "Using Node Clients"
slug: "using-node-clients"
excerpt: "Learn how to use Clients in your VTEX IO app for interaction with both internal and external services."
hidden: false
createdAt: "2022-02-16T13:52:17.234Z"
updatedAt: "2022-12-13T20:17:43.979Z"
---

In VTEX IO Services, Node [Clients](https://developers.vtex.com/docs/guides/vtex-io-documentation-clients) are powerful tools that enable you to seamlessly interact with both internal and external services. These clients play a crucial role in tasks such as making API requests, fetching data, and performing various operations within your VTEX IO apps. This guide will walk you through the effective utilization of Node Clients.

For this guide, note that VTEX IO Services exports functions that receive a `context` object. These functions can be resolver functions for GraphQL fields, middlewares for an HTTP server, or event handlers. In all cases, the Service receives a `ctx` object of type [`Context`](https://github.com/vtex/node-vtex-api/blob/master/src/service/worker/runtime/typings.ts), and it is within `ctx.clients` where you will find your Clients.

## Before you begin

Before diving into using Clients within your VTEX IO app, ensure you have the following prerequisites in place:

- **VTEX IO development workspace:** Ensure you have a VTEX IO development workspace set up. For more information, refer to [Creating a Development workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace).
- **TypeScript Familiarity:** This guide assumes you have a basic understanding of TypeScript, as we'll be using the `node` [Builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-builders) to develop with TypeScript. For more information, refer to [Typescript's official documentation](https://www.typescriptlang.org/docs/).
- **Understanding of Clients:** Clients play a crucial role in facilitating interactions between your application and both external and internal services. For more information, refer to [Clients](https://developers.vtex.com/docs/guides/vtex-io-documentation-clients).

## Using native `@vtex/api` Clients

1. Start a new VTEX IO app using the `node` builder and open the project using your preferred code editor.
2. Open the terminal and change to your app's `node` folder.
3. Install the `@vtex/api` package by running the following command:

   ```sh
   yarn add @vtex/api
   ```

4. In your app's handlers and middlewares, access the desired Clients via the `ctx` object. Here's an example of accessing the `@vtex/api` native `licenseManager` Client:

    ```ts
    export const authorize = async (ctx: Context) {
        const { clients: { licenseManager } } = ctx
        ...
        const data = await licenseManager.canAccessResource(/*...*/)
    }
    ```

## Using native `@vtex/clients` Clients

The [`@vtex/clients`](https://github.com/vtex/io-clients) package exports Clients, Client Factories and TypeScript typings that help you connect a VTEX IO app with VTEX Core Commerce modules.

1. Start a new VTEX IO app using the `node` builder and open the project using your preferred code editor.
2. Open the terminal and change to your app's `node` folder.
3. Install the `@vtex/api` package by running the following command:

   ```sh
   yarn add @vtex/api
   ```

4. Install the `@vtex/clients` package by running the following command:

   ```sh
   yarn add @vtex/clients
   ```

5. Check the list of VTEX IO Clients available in the `@vtex/clients` package. Refer to [List of native Clients](https://developers.vtex.com/docs/guides/vtex-io-documentation-clients#list-of-native-clients) and choose whether to use a Factory or an individual Client based on your requirements.

<details>
<summary>Using individual Clients</summary>

1. Create a `node/clients/index.ts` file and import the desired Client.

    ```ts
    import { Catalog } from '@vtex/clients'
    ```

2. In `node/clients/index.ts`, define a class called `Clients` that extends `IOClients`. This class is used to organize and configure your custom Clients. Within the Clients class, declare a `get` property for each of your custom Clients. This property allows you to access a specific Client by name. In our example, we've created a client named `catalog` that uses the `Catalog` class.

    ```ts
    import { IOClients } from "@vtex/api";
    import { Catalog } from '@vtex/clients'

    export class Clients extends IOClients {
        public get catalog() {
            return this.getOrSet('catalog', Catalog)
        }
    }
    ```

3. In your app's handlers and middlewares, access the desired Clients via the `ctx` object. Here's an example of accessing the `catalog` client and its `getSkuById` method:

    ```ts
    ctx.clients.catalog.getSkuById(...)
    ```

</details>

<details>
<summary>Using Client Factories</summary>

1. Create a `node/clients/index.ts` file and import the desired factory. For example:

    ```ts
    import { masterDataFor } from '@vtex/clients'
    ```

2. Follow the instructions for each factory, using its methods to create a Client class. Refer to [Creating a Master Data CRUD app](https://developers.vtex.com/docs/guides/create-master-data-crud-app) for more information on how to use the Master Data factory.
3. In `node/clients/index.ts`, define a class called `Clients` that extends `IOClients`. This class is used to organize and configure your custom Clients. Within the Clients class, declare a `get` property for each of your custom Clients. This property allows you to access a specific Client by name. In our example, we've created a client named `books` that uses the `BooksClient` class.

    ```ts
    import { IOClients } from "@vtex/api";
    const BooksClient = masterDataFor<MyBookType>('books')

    export class Clients extends IOClients {
        public get books() {
            return this.getOrSet('books', BooksClient)
        }
    }
    ```

4. In your app's handlers and middlewares, access the desired Clients via the `ctx` object. Check the following example where we access the `books` client and its `save` method:

    ```ts
    ctx.clients.books.save({ name: 'Example Book' })
    ```

</details>

## Using custom Clients

If you have developed custom Clients for a specific need, take the following steps to use them in your VTEX IO app.

> For a practical example, you can refer to how the `StatusClient` is set up in the [`service-example`](https://github.com/vtex-apps/service-example).

1. After completing the steps in the [Developing custom Clients](https://developers.vtex.com/docs/guides/vtex-io-documentation-how-to-create-and-use-clients) guide, import the `Clients` class to the `node/index.ts` file.

   ```ts
   import { Clients } from "./clients";
   ```

2. Create or edit the `clients` object of type `ClientsConfig<Clients>` from `@vtex/api`. This code sets up the configuration for Clients available in `ctx.clients`. It specifies an `implementation` property as `Clients`, which points to the custom Clients imported in the previous step, providing access to your custom Clients and their functionality.

   ```ts
   import type { ClientsConfig } from "@vtex/api";

   const clients: ClientsConfig<Clients> = {
     implementation: Clients,
     options: {
       default: {
         retries: 2,
         timeout: 2000,
       },
     },
   };
   ```

   Note that inside the `options` property, there's a `default` key with default Client options. These options include specifying the number of retries and the timeout for HTTP requests. See the [Options](#options) table for more options. All IO Clients will be initialized with these options unless otherwise specified.

3. (Optional) In the `node/index.ts` file, consider adding a type declaration to improve type safety and code clarity. This declaration helps you define the `Context` type, which is based on `ServiceContext<Clients, State>`.

   ```ts
   import type { ServiceContext } from "@vtex/api";

   declare global {
     type Context = ServiceContext<Clients, State>;
   }
   ```

4. In the `node/index.ts` file, export a new Service that defines route handlers and client options.

   ```ts
   export default new Service<Clients, State>({
    clients,
    routes: {
       ...
    },
   })
   ```

   > For more information on how to set up routes, refer to the [Routes](https://developers.vtex.com/docs/guides/service-path-patterns) guide.

5. Now, in your app's handlers and middlewares, use the `clients` object from the `ctx` to access your custom Client. Check the following example where we access the custom `github` Client in the `authorize` function.

   ```ts
   export const authorize = async (ctx: Context) {
       const { clients: { github } } = ctx
       ...
       const data = await github.getUser(/*...*/)
   }
   ```

### Options

The table below provides a detailed description of the available options for configuring your custom Client:

| Option                          | Description                                                                         |
| ------------------------------- | ----------------------------------------------------------------------------------- |
| `authType`                      | Specifies the authentication type.                                                  |
| `timeout`                       | Sets the request timeout duration in milliseconds.                                  |
| `memoryCache`                   | Configures a memory cache layer for caching data.                                   |
| `diskCache`                     | Configures a disk cache layer for caching data.                                     |
| `baseURL`                       | Defines the base URL for making requests.                                           |
| `retries`                       | Specifies the number of times a request should be retried in case of failure.       |
| `exponentialTimeoutCoefficient` | Configures the coefficient for exponential timeout backoff strategy.                |
| `initialBackoffDelay`           | Sets the initial delay before starting exponential backoff retries in milliseconds. |
| `exponentialBackoffCoefficient` | Configures the coefficient for exponential backoff retries.                         |
| `metrics`                       | Specifies an object for accumulating metrics related to requests.                   |
| `concurrency`                   | Defines the maximum number of concurrent requests.                                  |
| `headers`                       | Sets default headers to be sent with every request.                                 |
| `params`                        | Sets default query string parameters to be sent with every request.                 |
| `middlewares`                   | Configures an array of middleware functions for request processing.                 |
| `verbose`                       | Enables or disables verbose logging for requests and responses.                     |
| `name`                          | Defines a custom name for the instance.                                             |
| `serverTimings`                 | Sets server timings for measuring request and response times.                       |
| `httpsAgent`                    | Configures the HTTPS agent for making requests over SSL/TLS.                        |
