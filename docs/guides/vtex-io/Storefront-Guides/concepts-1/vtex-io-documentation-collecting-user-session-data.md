---
title: "Collecting user session data"
slug: "vtex-io-documentation-collecting-user-session-data"
hidden: false
createdAt: "2022-04-27T13:50:39.981Z"
updatedAt: "2022-12-13T20:17:44.566Z"
---

VTEX tracks users' sessions within apps by storing session information in a namespace. Each app has its own namespace, and only the app can modify its session properties. For example, the `vtex.search-session` app manages the `search` namespace.

This guide explains how to detect session changes in a specific namespace and respond to them programmatically.

> ℹ️ Learn more about the [Session manager](https://help.vtex.com/tutorial/using-session-manager-to-track-browsing-sessions-in-vtex-stores--1pA0tqsD4BFnJYhQ7ORQBd) and check the [Session manager API reference](https://developers.vtex.com/docs/api-reference/session-manager-api#overview). For a practical use case, refer to the [Cart cleanup guide](https://developers.vtex.com/docs/guides/vtex-io-documentation-cleaning-cart-data-on-log-out).

## Session Manager API overview

To view a store's current session data and structure, open your browser and navigate to:

```
https://{workspace}–{accountName}.myvtex.com/api/sessions?items=*
```

> ⚠️ Only use `items=*` during development. Never use it in production, as it retrieves all session data. For production, retrieve specific session data by specifying the required namespace and properties (e.g., `items=authentication.storeUserEmail,checkout.orderFormId`).

## Before you begin

Before starting, ensure you have the following:

- [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference): Install and configure the VTEX IO CLI.
- Existing app: If you are building a new app, run `vtex init` and select `service-example` to create a new app using the [node builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-node-builder). Make sure the app vendor is set to the appropriate account.

## Instructions

### Step 1 - Configuring the `vtex.session` builder

1. Open your app's `manifest.json` file and add `vtex.session` under the `builders` section:

      ```json manifest.json
      "builders": {
          "node": "7.x",
          "docs: "0.x",
          "vtex.session": "0.x"
      },
      ```

2. In the root directory of your project, create a folder named `vtex.session` and add the `configuration.json` to it. This file defines the session behavior for your app.
3. Inside `configuration.json`, define the session configuration using the following structure:
      
      ```json configuration.json
      {
          "APP-NAME": {
              "input": {
                  "NAMESPACE": ["VALUE"]
              },
              "output": {
                  "NAMESPACE": ["VALUE"]
              }
          }
      }
      ```
      
| Parameter   | Description                                                                                      |
|-------------|--------------------------------------------------------------------------------------------------|
| `APP-NAME`  | App's name without the `vendor` prefix. For example, `session-watcher-demo`.                    |
| `input`     | Object containing the key-value pairs corresponding to session changes you want to monitor.           |
| `output`    |  Object containing the key-value pairs for the session changes you want to apply.             |

#### Example

In the following example, the app listens for changes in the `authentication` namespace to retrieve the user's email (`storeUserEmail`). It also monitors the `checkout` namespace to track the `orderFormId`. The output stores a property called `demo` in the `public` namespace.

```json
{
    "session-watcher-demo": {
        "input": {
            "authentication": ["storeUserEmail"],
            "checkout": ["orderFormId]
        },
        "output": {
            "public": ["demo"]
        }
    }
} 
```

### Step 2 - Setting up the `transform` handler

The `vtex.session` builder detects changes in the `input` values of the `configuration.json` file and sends a `POST` request to the public endpoint (`/_v/APP-NAME/session/transform`) whenever a change occurs. All values listed under `input` are sent in the request, even if not all values have changed.

To set up this endpoint, take the following steps:

1. Open the `./node/services.json` file and add a route containing `path` and `public` under the `routes` property. For example:
      
      ```json services.json
      "routes": {
          "clearCart": {
              "path": "/_v/session-watcher-demo/session/transform",
              "public": true
          }
      }
      ```

2. Create the `node/resolvers/index.ts` file and define the handler function for processing session changes. This function will respond with the expected output defined in the `configuration.json`. Take the following example and note the handler receives a `Context` that gives access to the request body. The handle should respond as a JSON with the object expected on the `output` definition.

      ```ts node/resolvers/index.ts mark=6,17:23,25:26
      /* eslint-disable no-console */
      import { json } from 'co-body'
      
      export const resolvers = {
        Routes: {
          clearCart: async (ctx: Context) => {
            const { req } = ctx
      
            const body: any = await json(req)
            const email = body?.authentication?.storeUserEmail?.value ?? null
      
            console.log('clearCart =>', body)
      
            ctx.set('Content-Type', 'application/json')
            ctx.set('Cache-Control', 'no-cache, no-store')
      
            const res = {
              public: {
                demo: {
                  value: email ? 'User Authenticated' : 'User not authenticated',
                },
              },
            }
      
            ctx.response.body = res
            ctx.response.status = 200
          },
        },
      }
      ```
   
4. In the `./node/index.ts` file, import the handler function file ( `node/reseolvers/index.ts`) and load it to the Service.

      ```ts node/index.ts
      import { resolvers } from ‘./resolvers’
      …
      // Export a service that defines route handlers and client options.
      export default new Service{{
          clients,
          routes: resolvers.Routes,
      })
      ```

### Step 3 - Testing your changes

1. Link your app to a development workspace by running `vtex link`.
2. Monitor the terminal for logs indicating the session changes. Once a user logs in or out, you should see logs like `clearCart =>` with the body of the request.

      ![Terminal screenshot](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-collecting-user-session-data-2.png)

You can also check the session data changes by accessing the following URL:

```
https://{workspace}–{accountName}.myvtex.com/api/sessions?items=public.demo
```

The response might look like this:

```json
{
   "id": "cca40248-a3f9-4a60-baf1-b67de92cd8a",
   "namespaces": {
      "public": {
         "demo": {
            "Value": "User Authenticated"
         }
      }
   }
}
```

> The `vtex.session` builder may take a few minutes to initialize after linking the app. If logs don’t appear immediately, please wait a few minutes.

For a complete example, [download the code](https://drive.google.com/file/d/1ISNE6MhYz5pQEWmqjOmfpsUJ7ApBrwXw/view?usp=sharing).
