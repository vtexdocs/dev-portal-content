---
title: "Using and creating clients"
slug: "how-to-use-and-create-clients-on-vtex-io"
hidden: true
createdAt: "2020-10-08T12:52:54.752Z"
updatedAt: "2021-03-25T14:39:10.125Z"
---
## Introduction
Clients, on VTEX IO, are **abstractions to other services**. We tackle complexities when setting up an HTTP client, for example, so you can focus on the real value of your software. Whenever you need to setup a connection with an **external API** or another **VTEX service**, you should create a *client*! Some standard clients are already baked into VTEX IO, check them [here](https://github.com/vtex/node-vtex-api/blob/ccf4d8f8d3208007c4bfd558baf979df8d825af8/src/clients/IOClients.ts).

> Leave the burden with us!

**These are some of the features built in our clients infrastructure:**

- Cache *(you can use disk on in-memory cache easily)*
- Native metrics support
- Retry and timeout options
- Billing tracking *(you can easily charge who uses your app)*
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2e85738-clients.png",
        "clients.png",
        1120,
        700,
        "#c7c8c8"
      ]
    }
  ]
}
[/block]
Before talking about *how we create clients*, let’s *recap* how we use them. If you are familiar with IO services, you already know that your implementation **exports functions** that receive a ***context*** object. These functions can be a **resolver function to a GraphQL field**, a **middleware to an HTTP server** or an **event handler**, and, in all of them, you receive a `ctx`*(or however you wanna call it)* object of type `[Context](https://github.com/vtex/node-vtex-api/blob/master/src/service/worker/runtime/typings.ts)`, and it is inside of `ctx.clients` where you’ll find each client.

[block:code]
{
  "codes": [
    {
      "code": "export const authorize = async (ctx: Context) {\n    const { clients: { licenseManager } } = ctx\n    ...\n    const data = await licenseManager.canAccessResource(/*...*/)\n}",
      "language": "typescript",
      "name": "using-clients.ts"
    }
  ]
}
[/block]
## How to create clients and how do they look?

The `[@vtex/api](https://github.com/vtex/node-vtex-api/)` SDK provides a structured way to create clients, and the first thing to do is **identify the type of communication you want to implement.** As of now, we support these out of the box:

[block:parameters]
{
  "data": {
    "h-0": "Type",
    "h-1": "Use case",
    "0-0": "AppClient",
    "1-0": "AppGraphQLClient",
    "2-0": "ExternalClient",
    "3-0": "JanusClient",
    "4-0": "InfraClient",
    "0-1": "Communication with other IO Services via plain-old HTTP calls",
    "1-1": "Communication with other IO GraphQL services",
    "2-1": "Communication with external API’s",
    "3-1": "Communication with VTEX Core Commerce API’s through Janus Router",
    "4-1": "Communication with VTEX IO Infra services"
  },
  "cols": 2,
  "rows": 5
}
[/block]
> When using clients, don’t forget to add the appropriate policies on your manifest.json. Incorrect policies may result in request blocking.

After finding the *base* client you are looking for, you need to implement a **Typescript class that extends the type of this base client**. You may place them wherever you want, but we advise you to put them on `node/clients`.

Let’s take a look on the anatomy of an *ExternalClient* to the *Github API*:

`node/clients/github.ts`
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/fadfbf9-client.png",
        "client.png",
        3933,
        6560,
        "#5f6061"
      ],
      "caption": ""
    }
  ]
}
[/block]
**Reference** 

1. Look, it’s one of the types from the **table above**.
2. Take a look [here](https://github.com/vtex/node-vtex-api/blob/4f17dba5d750dae6603c606187c888fbd91fd18c/src/HttpClient/typings.ts#L58) to check everything you can configure.
3. Read more about **app’s pricing** [here](https://help.vtex.com/tutorial/app-pricing-options--2ZKBKxLe08Q6seA6sCi6o2).
4. There are a lot of other methods available, you can check them on [**HttpClient**].(https://github.com/vtex/node-vtex-api/blob/master/src/HttpClient/HttpClient.ts)

> You’re free to add data handling logic inside your client’s methods (i.e: mapping fields, or filtering data), but be careful to not lose track of the client’s responsabilities!

## Ok, now what?

After you’ve learned how to create **great clients**, it’s time to **ship them**, so you may **use it on your implementations**. It’s easy as well!

> If you want to jump to an example, check how the StatusClient is setup on service-example.

**Let’s suppose you’ve created the Github client** we’ve described above!

1. Make sure you’ve **exported** the *client* from its module. *(Either [default or named export](https://medium.com/@etherealm/named-export-vs-default-export-in-es6-affb483a0910))*
2. Create a `node/clients/index.ts` file.
3. Paste the following snippet on it. *(If you’ve used named export on Step 2, change the import clause)*


[block:code]
{
  "codes": [
    {
      "code": "import { IOClients } from '@vtex/api'\nimport GithubClient from './github.ts'\n\nexport class Clients extends IOClients {\n  public get status() {\n    return this.getOrSet('github', GithubClient)\n  }\n}",
      "language": "typescript",
      "name": "clients-index.ts"
    }
  ]
}
[/block]
1 - Now, **import the Clients class** on `node/index.ts` (the service *entrypoint*).

2 - Create or edit a `clients` object of type `ClientsConfig<Clients>` *(from @vtex/api)* like so:
[block:code]
{
  "codes": [
    {
      "code": "    const clients: ClientsConfig<Clients> = {\n      implementation: Clients,\n      options: {\n        default: {\n          retries: 2,\n          timeout: 2000,\n        },\n      },\n    }",
      "language": "typescript",
      "name": "clients-config.ts"
    }
  ]
}
[/block]
3 - Use the `clients` variable on the **Service** exported:
[block:code]
{
  "codes": [
    {
      "code": "export default new Service<Clients, State>({\n  clients,\n  routes: {\n    ...\n  },\n})",
      "language": "typescript",
      "name": "service.ts"
    }
  ]
}
[/block]
**Optional:** Place this **type declaration** on the same `node/index.ts` file. It helps you type the implementation functions.

[block:code]
{
  "codes": [
    {
      "code": "declare global {\n  type Context = ServiceContext<Clients, State>\n}",
      "language": "typescript"
    }
  ]
}
[/block]
**That’s it** ✨! Now you can, on your functions, **access your client** from the `ctx`.

[block:code]
{
  "codes": [
    {
      "code": "export const authorize = async (ctx: Context) {\n    const { clients: { github } } = ctx\n    ...\n    const data = await github.getUser(/*...*/)\n}",
      "language": "typescript"
    }
  ]
}
[/block]
## Want to dive deeper?

If you didn’t find what you were looking for here, try **learning by example**. We are already doing some advanced thing on our default clients, like **file upload**, **use of disk cache** and more: 

- [AppsClient](https://github.com/vtex/node-vtex-api/blob/master/src/clients/infra/Apps.ts)