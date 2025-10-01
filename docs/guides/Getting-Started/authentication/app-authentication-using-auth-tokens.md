---
title: "App authentication using auth tokens"
slug: "app-authentication-using-auth-tokens"
excerpt: "Learn how to use app auth tokens in each context"
hidden: false
createdAt: "2020-01-15T18:58:34.836Z"
updatedAt: "2025-08-26T14:20:00.000Z"
seeAlso:
 - "/docs/guides/api-authentication-using-user-tokens"
---

When working on VTEX IO apps, you generally don't make direct requests to VTEX APIs. This is because VTEX IO already provides convenient access to VTEX APIs through predefined [clients](https://developers.vtex.com/docs/guides/vtex-io-documentation-clients). Therefore, using application keys within your app is often unnecessary. If you need to use them, the recommended approach is using authentication tokens.

We recommend using the VTEX IO [clients package](https://github.com/vtex/io-clients) when possible. With this package, every [client method](https://developers.vtex.com/docs/guides/vtex-io-documentation-how-to-create-and-use-clients#step-3-implementing-client-methods) has an optional argument called `authMethod`, which accepts one of three authentication options, each indicating which token to use for the request.

The tokens are available via the VTEX IO context and are associated with different permissions.

You can import the context in your app as follows: `import { IOContext } as ctx from '@vtex/api'`. See the table below to learn about each token.

| Token | `authMethod` | Via context | Description | Permissions |
|---|---|---|---|---|
| App authentication token (default) | `AUTH_TOKEN` | `ctx.authToken` | Every VTEX IO app has its own temporary authentication token. We recommend avoiding the use of this app token whenever user tokens are available. | Permissions declared in the [policies](https://developers.vtex.com/docs/guides/vtex-io-documentation-policies) defined in the app's [manifest](https://developers.vtex.com/docs/guides/vtex-io-documentation-manifest), where developers must declare precisely what actions are allowed for the app they are building. |
| Store user token | `STORE_TOKEN` | `ctx.storeUserAuthToken` | [User token](https://developers.vtex.com/docs/guides/api-authentication-using-user-tokens) with store scope. | Shopper permissions. |
| Admin user token | `ADMIN_TOKEN` | `ctx.adminUserAuthToken` | [User token](https://developers.vtex.com/docs/guides/api-authentication-using-user-tokens) with Admin scope. | Administrative permissions as defined by [License Manager roles](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc) associated with the current logged-in user. |

If your project requires features not provided by the available [clients](https://developers.vtex.com/docs/guides/vtex-io-documentation-clients), we recommend creating your own clients following the same authentication logic.

> ❗ Authenticate app actions with user tokens whenever possible. Currently, app authentication tokens are not subject to [License Manager permissions](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc). We recommend considering this when defining app architecture and configuring [policies](https://developers.vtex.com/docs/guides/vtex-io-documentation-policies).

## Usage examples

Below are examples of how to use each token type in a [client definition](https://developers.vtex.com/docs/guides/vtex-io-documentation-how-to-create-and-use-clients#step-2-creating-a-custom-client).

### App authentication token

Use the app `authToken` when operations are not linked to a user. In this case, the permission level is defined by [policies](https://developers.vtex.com/docs/guides/vtex-io-documentation-policies) in the app [`manifest.json` file](https://developers.vtex.com/docs/guides/vtex-io-documentation-manifest).

```ts
export class OmsClient extends JanusClient {
 constructor(ctx: IOContext, options?: InstanceOptions) {
   super(ctx, {
     ...options,
     headers: {
       ...options?.headers,
       VtexIdclientAutCookie: ctx.authToken,
     },
   })
 }
}
```

### Store user token

When the app is focused on **store browsing** experience, use `storeUserAuthToken` whenever possible. This way, app permissions will be limited to **shopper** user permissions in the account.

```ts
export class OmsClient extends JanusClient {
 constructor(ctx: IOContext, options?: InstanceOptions) {
   super(ctx, {
     ...options,
     headers: {
       ...options?.headers,
       VtexIdclientAutCookie: ctx.storeUserAuthToken,
     },
   })
 }
}
```

### Admin user token

When the app is focused on **Admin** experience, use `adminUserAuthToken` whenever possible. This way, app permissions will be limited to **Admin** user permissions in the account.

```ts
export class OmsClient extends JanusClient {
 constructor(ctx: IOContext, options?: InstanceOptions) {
   super(ctx, {
     ...options,
     headers: {
       ...options?.headers,
       VtexIdclientAutCookie: ctx.adminUserAuthToken,
     },
   })
 }
}
```
