---
title: "Connecting to VTEX Core Commerce APIs"
slug: "how-to-connect-with-vtex-core-commerce-apis-using-vtex-io"
hidden: false
createdAt: "2020-10-08T02:47:14.995Z"
updatedAt: "2021-03-25T14:40:29.493Z"
---
## Context
A VTEX IO app is a first-class citizen to connect with VTEX Core Commerce API's ([https://developers.vtex.com/docs/api-reference](https://developers.vtex.com/docs/api-reference)), and it's very easy to create integrations with our modules.
[block:callout]
{
  "type": "info",
  "body": "The Client you need may already be implemented on `@vtex/clients`. Check it out on [https://github.com/vtex/commerce-io-clients](https://github.com/vtex/commerce-io-clients/blob/master/src/clients/catalog.ts)"
}
[/block]


## Steps

1. On your app, create a *Client* that represents the module you want to access. It will be a class that **extends JanusClient.** 
2. On the constructor, setup the `VtexIdclientAutCookie` header with the **token you want to use to authorize the request.** Use `ctx.authToken` to use the app's token. You may also use `ctx.vtex.storeUserAuthToken` or `ctx.vtex.adminUserAuthToken` to use the requester's token, for request incoming from the VTEX Admin or VTEX Storefront. You can also pass that on each specific call.
3. On each method, make the HTTP call using `this.http` using the **path of the service** you want to access. (e.g: `/api/billing/company`)
4. On the app's `manifest.json`, add the appropriate `outbound-access` policy to the URL you are requesting. (example [here](https://github.com/vtex-apps/store-graphql/blob/684dcbbbd6e9cdbd121afd7802200856cb952d2b/manifest.json#L107))
5. That's it. Now, finish the Client's setup according to the documentation, and you may now use it on our code.

## Keep In Mind 👀

### GraphQL Apps

- Some of our Core Commerce Modules already have a GraphQL app that abstracts their endpoints, so it's important to check if the data you want to access is already exported via one of our GraphQL apps. You can check that on the **GraphQL IDE** app on your admin's (`vtex install vtex.admin-graphql-ide` if you can't see it)

### Authentication

- IO Apps **don't need appKey/appToken** to make requests to VTEX APIs, thus it's not necessary to ask the merchant to create this pair. Every app will have it's own rotating token that can be used on the app's code.
- In some cases, it's not ideal to use the app's token (e.g: the authorization is important and depends on the calling user), and you can use the **user's token instead**, using  `ctx.vtex.storeUserAuthToken` or `ctx.vtex.adminUserAuthToken`.

### Some examples

- CheckoutClient - [https://github.com/vtex-apps/store-graphql/blob/master/node/clients/checkout.ts](https://github.com/vtex-apps/store-graphql/blob/master/node/clients/checkout.ts)