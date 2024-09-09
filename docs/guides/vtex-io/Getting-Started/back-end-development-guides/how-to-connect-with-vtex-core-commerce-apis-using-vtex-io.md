---
title: "Connecting to VTEX Core Commerce APIs"
slug: "how-to-connect-with-vtex-core-commerce-apis-using-vtex-io"
excerpt: "Learn how to enable seamless HTTP communication with VTEX Core Commerce APIs within your VTEX IO app."
hidden: false
createdAt: "2020-10-08T02:47:14.995Z"
updatedAt: "2021-03-25T14:40:29.493Z"
---

VTEX IO apps are designed designed to seamlessly interface with [VTEX Core Commerce APIs](https://developers.vtex.com/docs/api-reference). These APIs provide a set of functionalities and data access points for managing and interacting with the VTEX ecommerce platform, enabling developers to perform various operations, such as managing orders, products, and customer data.

In this guide, you will learn how to create a custom client that can handle HTTP requests to these VTEX Core Commerce APIs, allowing your application to retrieve and manipulate data within the VTEX ecosystem.

## Before you begin

Ensure a smooth development process by having the following prerequisites in place:

- **VTEX IO Development Workspace:** Set up your VTEX IO environment by following the steps outlined in [Creating a Development Workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace).
- **TypeScript Familiarity:** Acquire a basic understanding of TypeScript, as we'll be using the `node` [Builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-builders) for TypeScript development. For details, refer to [Typescript's Official Documentation](https://www.typescriptlang.org/docs/).
- **Understanding of Clients:** Clients play a crucial role in facilitating interactions between your application and both external and internal services. Learn more about [Clients](https://developers.vtex.com/docs/guides/vtex-io-documentation-clients).

## Instructions

### Step 1 - Setting up your VTEX IO app

1. Start a new VTEX IO app using the `node` builder and open the project using your preferred code editor.
2. Install the `@vtex/api` package by running the following command:

   ```sh
   yarn add @vtex/api
   ```

4. Update the app's `manifest.json` to include the appropriate `outbound-access` policy for the requested URL. Here's a hypothetical example:
    
    ```json manifest.json mark=13:21
    {
      "name": "your-app",
      "version": "1.0.0",
      "scripts": {
        // ...
      },
      "dependencies": {
        // ...
      },
      "builders": {
        // ...
      },
      "policies": [
        {
          "name": "outbound-access",
          "attrs": {
            "host": "{{account}}.vtexcommercestable.com.br",
            "path": "/api/checkout/pub/orderForm/*"
          }
        }
      ]
    }
    ```
    
### Step 2 - Creating a Client for connecting to VTEX Core Commerce APIs

1. Create a TypeScript file for your Client in the `node/clients` directory. Choose a name that easily identifies your Client (e.g., `myClient.ts`).
2. Create a client that represents the module you want to access. It will be a class that extends `JanusClient`.
   
    ```ts ./node/clients/myClient.ts mark=2,4:8
    import type { InstanceOptions, IOContext } from ‘@’vtex/api’
    import { JanusClient } from ‘@vtex/api’
    
    export default class MyClient extends JanusClient {
        constructor(context: IOContext, options?: InstanceOptions) {
            super(context, { …options })
        }
    }
    ```

3. In the constructor, set the `VtexIdclientAutCookie` header with the required token for authorization. Use `ctx.authToken` for the app's token, or `ctx.vtex.storeUserAuthToken` or `ctx.vtex.adminUserAuthToken` for requests from VTEX Admin or VTEX Storefront, respectively. Refer to [App authentication using auth tokens
](https://developers.vtex.com/docs/guides/app-authentication-using-auth-tokens) for more information.

    ```ts ./node/clients/myClient.ts mark=10
    import type { InstanceOptions, IOContext } from ‘@’vtex/api’
    import { JanusClient } from ‘@vtex/api’
    
    export default class MyClient extends JanusClient {
        constructor(context: IOContext, options?: InstanceOptions) {
           super(ctx, {
            ...options,
            headers: {
              Accept: 'application/json',
              VtexIdclientAutCookie: ctx.storeUserAuthToken,
              'x-vtex-user-agent': ctx.userAgent,
              ...options?.headers,
            },
          })
        }
    }
    ```
    
    > Ensure to export the Client from its module using either [default or named export](https://medium.com/@etherealm/named-export-vs-default-export-in-es6-affb483a0910).
    
### Step 3 - Implementing the Client methods

In your Client TypeScript file, implement the desired methods using the [`HttpClient`](https://developers.vtex.com/docs/guides/vtex-io-documentation-how-to-create-and-use-clients#httpclient-methods) for targeted HTTP calls.
   
  ```ts ./node/clients/myClient.ts mark=17:23
  import type { InstanceOptions, IOContext } from ‘@’vtex/api’
  import { JanusClient } from ‘@vtex/api’
  
  export default class MyClient extends JanusClient {
      constructor(context: IOContext, options?: InstanceOptions) {
         super(ctx, {
          ...options,
          headers: {
            Accept: 'application/json',
            VtexIdclientAutCookie: ctx.storeUserAuthToken,
            'x-vtex-user-agent': ctx.userAgent,
            ...options?.headers,
          },
        })
      }

      public newOrderForm = (orderFormId?: string) => {
        return this.http
          .postRaw<OrderForm>(this.routes.orderForm(orderFormId), undefined, {
            metric: 'checkout-newOrderForm',
          })
          .catch(statusToError) as Promise<IOResponse<OrderForm>>
      }
      
      private get routes() {
        const base = '/api/checkout/pub'
    
        return {
          orderForm: (orderFormId?: string) =>
            `${base}/orderForm/${orderFormId ?? ''}`
        }
      }

  }
  ```
  
    In the provided example, the `newOrderForm` method is implemented to make HTTP requests using `this.http`. It facilitates the creation of a new order form by sending a POST request (`postRaw`) to the specified endpoint. The method includes additional configurations such as defining the metric for tracking and handling potential errors in the response.

### Step 4 - Exporting custom clients

Now that you've created your custom Client, organize and export it for use in your VTEX IO service. Follow these steps:

1. Create an `index.ts` file in the `node/clients` folder.
2. Inside the `index.ts` file, import the custom client you created in the previous step. For example:

    ```ts
    import MyClient from "./myClient.ts";
    ```

3. Define a class called `Clients` that extends `IOClients`. This class is used to organize and configure your custom Clients. Within the Clients class, declare a `get` property for each of your custom Clients. This property allows you to access a specific Client by name. In our example, we've created a client named `myClient` that uses the `MyClient` class.

    ```ts
    import { IOClients } from "@vtex/api";
    import MyClient from "./myClient.ts";

    export class Clients extends IOClients {
      public get status() {
        return this.getOrSet("myClient", MyClient);
      }
    }
    ```

Now that you have developed and exported your custom Client to communicate with the desired service, your Clients can be accessed and used within your VTEX IO service to perform various tasks. Learn how to use clients effectively in the [Using Node Clients](https://developers.vtex.com/docs/guides/using-node-clients) guide.

## Key considerations

- **GraphQL apps:** Some Core Commerce modules already feature a GraphQL app that abstracts their endpoints. Check if the desired data is available via one of our GraphQL apps. Utilize the [GraphQL IDE](https://developers.vtex.com/docs/guides/graphql-ide) app on the Admin for exploration.
- **Authentication:** IO apps do not require an appKey/appToken pair to make requests to VTEX Core Commerce APIs. Every app has its own rotating token that can be used on the app's code. In scenarios where using the app's token is not ideal (e.g., authorization depends on the calling user), opt to use the user's token instead, using  `ctx.vtex.storeUserAuthToken` or `ctx.vtex.adminUserAuthToken`. Refer to [Authentication](https://developers.vtex.com/docs/guides/authentication) for more information.

## Example

- [CheckoutClient](https://github.com/vtex-apps/store-graphql/blob/master/node/clients/checkout.ts)
