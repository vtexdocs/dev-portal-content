---
title: "Interacting with Master Data v1 through VTEX IO services"
slug: "interacting-with-master-data-v1-through-vtex-io-services"
hidden: false
createdAt: "2024-06-21T10:45:55.338Z"
updatedAt: "2024-06-21T11:40:35.480Z"
excerpt: "Setting up a service in VTEX IO to interact with Master Data v1."
---

This guide provides step-by-step instructions on how to create a VTEX IO service to interact with [Master Data v1](https://help.vtex.com/en/tutorial/master-data--4otjBnR27u4WUIciQsmkAw). Discover how to effectively leverage Master Data capabilities through your service in the upcoming sections.

## Before you begin

Make sure you meet the technical requirements to complete this project:

* Experience developing in [Typescript](https://www.typescriptlang.org/) language.
* Having [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-install) installed.

## Step 1: Initializing the project

To begin setting up your service to interact with Master Data v1 on VTEX IO, follow these steps to initialize your project using the service-example template:

1. Open the terminal.
2. Type the command `vtex init`.
3. Select the `service-example` template.
4. Enter a folder name or use the default name, which is the same as the selected template.

## Step 2: Setting up policies

Configure permissions for your application to access Master Data by following the steps below:

1. Open the project folder in your preferred code editor.
2. Open the `manifest.json` file located at the root of the project.
3. Add the following structure to the `policies` section:

    ```json
    {
      "name": "outbound-access",
      "attrs": {
        "host": "api.vtex.com",
        "path": "/dataentities/*"
      }
    },
    {
      "name": "ADMIN_DS"
    }
    ```

## Step 3: Creating a client

Create a client class in TypeScript to extend the functionality of `MasterData` from the `@vtex/api` module:

1. Inside the `node` folder, create a `clients` folder if it does not exist.
2. Create a Typescript file in the `clients` folder. In this example, the file will be named `md.ts`.
3. Create a class that extends from the `MasterData` class from the `@vtex/api` module.

   ```typescript
   import { MasterData } from '@vtex/api'
   export default class MD extends MasterData {}
   ```

4. Modify the class to include the constructor and headers:

   In this class, we will call the `constructor` and, within it, the `super` method, passing the `context` and `options` received in the `constructor` class.

   ```typescript
   import { IOContext, InstanceOptions, MasterData } from '@vtex/api'

   export default class MD extends MasterData {
     constructor(context: IOContext, options?: InstanceOptions) {
       super(context, {
         ...options,
         headers: {
           {{app-key}}
           {{app-token}}
         },
       })
     }
   }
   ```

   In this class, we will have access to several methods extended from the **Master Data** class, including:

   * `getDocumentById`
   * `searchDocuments`
   * `scrollDocuments`

5. Add the desired method. The example below uses the `getDocumentById` method:

   ```typescript
   public getDocumentById(
     dataEntity: string,
     id: string,
     fields: string[]
   ): Promise<any> {
     return this.getDocument({ dataEntity, id, fields })
   }
   ```

## Step 4: Registering the Client

After creating our Client class, you need to register it in the `index.ts` file within the same `clients` folder:

1. Open the `index.ts` file in the `clients` folder.
2. Import the new client (e.g., `MD`) and add it to the `Clients` class, as exemplified below:

   ```typescript
   import { IOClients } from '@vtex/api'
   import MD from './md'
   
   // Extend the default IOClients implementation with our own custom clients
   export class Clients extends IOClients {
     public get MD() {
       return this.getOrSet('MD', MD)
     }
   }
   ```

## Step 5: Creating the middleware

Implement a middleware function to handle interactions between your service and Master Data, executing the method we created and returning the response based on the context:

1. Inside the `node` folder, create a `middlewares` folder if it does not exist.
2. Create a file named `masterdataMiddleware.ts` in the `middlewares` folder.
3. Add your TypeScript code to `masterdataMiddleware.ts`.

   Following the example in the previous sections to illustrate this step, in this middleware, we will return the call to the method created to a variable and then add this variable to the context body. The method expects to receive an *entity*, a *document ID*, and an *array* of fields to be returned in the response.

   ```typescript
   export async function masterdataMiddleware(
     ctx: Context,
     next: () => Promise<any>
   ) {
     const {
       clients: { MD },
     } = ctx

     const response = await MD.getDocumentById(
       'CL',
       '0807f150-68bb-11Ec-82ac-12fdbe358f3f',
       ['id', 'email']
     )

     ctx.status = 200

     ctx.body = {
       response,
     }

     await next()
   }
   ```

## Step 6: Configuring the route

Configure a dedicated route in your service that will be accessed through your store's endpoint:

1. Open the `service.json` file in the `node` folder.
2. In the `routes` section, define the `routes` object as shown below. In this example, we will define the `path` as `/_v/md/get-document` and make this route public.

    ```json
    "routes": {
      "masterdata": {
        "path": "/_v/md/get-document",
        "public": true
      }
    }
    ```

3. Open the `index.ts` file in the `node` folder.

   In this file, you will see a new instance of service created. You will register your route within the `routes` object.

4. Register the route  within the `routes` object.

   ```typescript
    masterdata: method({
        GET: [masterdataMiddleware],
    }),
   ```

> The `masterdata` attribute is the route ID created in the `service.json` file.

The `masterdata` attribute receives a function containing an object where we can pass various middleware mappings. In this case, we will use the HTTP method **GET**, which receives an *array* where we must declare the middleware created in previous sections.

## Step 7: Running the project

Finalize setup by linking your project to a development workspace and testing the configured service routes:

1. In the terminal, navigate to the root of the project.
2. Run the command `vtex link`.

   After linking, you should see the following message:

   ```sh
   **info:** *Available service routes: https://{{workspace}}--{{accountName}}.myvtex.com/{{path}}
   ```

3. Access the service route from the previous step in your browser.

   Following the example of a service to retrieve a document, you should see a response with the fields defined in the middleware:

    ```json
    {
      "response": {
        "id": "0807f150-68bb-11Ec-82ac-12fdbe358f3f",
        "email": "john@mail.com"
      }
    }
    ```

## Conclusion

These instructions enable you to configure clients, middleware, and routes to set up a VTEX IO service for interacting with Master Data v1. Note that there are various methods and configurations beyond this guide to further customize and optimize your integration with VTEX IO and Master Data.
