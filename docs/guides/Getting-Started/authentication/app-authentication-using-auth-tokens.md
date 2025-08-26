---
title: "App authentication using auth tokens"
slug: "app-authentication-using-auth-tokens"
hidden: false
createdAt: "2020-01-15T18:58:34.836Z"
updatedAt: "2022-12-13T18:43:56.137Z"
seeAlso:
 - "/docs/guides/api-authentication-using-user-tokens"
---

When working on VTEX IO apps, you generally won't have to make direct requests to VTEX APIs. This is because VTEX IO already provides convenient access to VTEX APIs through pre-defined [clients](https://developers.vtex.com/docs/guides/vtex-io-documentation-clients). Hence, using application keys within your app will often be unnecessary. When necessary, the recommended approach involves employing authentication tokens.

We recommend using the VTEX IO [clients package](https://github.com/vtex/io-clients) when possible. In this context, every client method accepts an optional argument called `authMethod`, which receives one of three authentication options, indicating which token will be used in this request.

The tokens are available via the VTEX IO context and are associated with different permissions.

You can import the context in your app as in the following: `import { IOContext } as ctx from '@vtex/api'.` See the table below to learn about each token.

| Token | `authMethod` | Via context | Description | Permissions |
|---|---|---|---|---|
| App authentication token (default) | `AUTH_TOKEN` | `ctx.authToken` | Every VTEX IO app has its own temporary authentication token. We recommend you avoid using this app token whenever user tokens are available. | Permissions declared in the  [policies](https://developers.vtex.com/docs/guides/vtex-io-documentation-policies) in your app's [manifest](https://developers.vtex.com/docs/guides/vtex-io-documentation-manifest). In this file, developers must declare precisely what actions are allowed for the app they are building. |
| Store user token | `STORE_TOKEN` | `ctx.storeUserAuthToken` | [User token](https://developers.vtex.com/docs/guides/api-authentication-using-user-tokens) with store scope. | Shopper permissions. |
| Admin user token | `ADMIN_TOKEN` | `ctx.adminUserAuthToken` | [User token](https://developers.vtex.com/docs/guides/api-authentication-using-user-tokens) with Admin scope. | Administrative permissions as defined by [License Manager roles](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc) associated with the logged in user. |

If your project requires features not provided by the available [clients](https://developers.vtex.com/docs/guides/vtex-io-documentation-clients), we recommend creating your own clients following the same authentication logic.

> ❗ Authenticate your apps' actions with user tokens whenever possible. Currently, app authentication tokens are not subject to [License Manager permissions](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc). We recommend that you consider this when defining your app's architecture and configuring [policies](https://developers.vtex.com/docs/guides/vtex-io-documentation-policies).

## Usage examples

Below we show examples of how to use each token type in a client’s definition.

### App authentication token

Use the app's `authToken` when the operations are not linked to any user. In this case, you define the permission level with [policies](https://developers.vtex.com/docs/guides/vtex-io-documentation-policies) in the app's [`manifest.json` file](https://developers.vtex.com/docs/guides/vtex-io-documentation-manifest).

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

When the app's focus is on the **store browsing** experience, it is recommended to use `storeUserAuthToken` whenever possible. This way, the app's permissions are limited to the **shopper** user's permissions in the account.

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

When the app's focus is on the **Admin** experience, it is recommended to use `adminUserAuthToken` whenever possible. This way, the app's permissions are limited to the **Admin** user's permissions in the account.

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
