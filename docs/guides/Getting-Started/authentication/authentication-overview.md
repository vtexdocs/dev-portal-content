---
title: "Authentication overview"
slug: "authentication-overview"
hidden: false
createdAt: "2020-01-15T18:58:34.836Z"
updatedAt: "2022-12-13T18:43:56.137Z"
---
In this article, you can learn about all authentication aspects relevant to developers building integrations with VTEX:

- [Machine authentication](#machine-authentication)
- [Single Sign On integrations](#single-sign-on-integrations)
- [Shopper authentication for B2B stores](#shopper-authentication-for-b2b-stores)

> ℹ️️ See this related content:
> 
> - Authorization: [Users](https://help.vtex.com/en/subcategory/users--63DHe3VQEEE6Uuua8gIs2M), [Roles](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc) and [License Manager Resources](https://help.vtex.com/en/tutorial/license-manager-resources--3q6ztrC8YynQf6rdc6euk3)
> 
> - Accounting: [Audit](https://help.vtex.com/en/tutorial/searching-for-events-on-audit--5RXf9WJ5YLFBcS8q8KcxTA)

## Machine authentication

There are different contexts in which machine authentication is required in the regular functioning of a VTEX store. Because of that, there are different ways this is done. Below are some example use cases and details about machine authentication methods.

| **Use case** | **Indicated authentication methods** |
| ----- | ----- |
| Backend VTEX IO app | [User token](#user-token) via VTEX IO context, or, if needed, [app authentication token](#app-authentication) via VTEX IO context |
| Frontend VTEX IO app | [User token](#user-token) via VTEX IO context |
| Self-hosted backend request to VTEX APIs | [Application keys](#application-keys) |
| Self-hosted frontend request to VTEX APIs | [User token](#user-token) |

> ℹ️️ The authentication methods in the table above are indicated but are not the only alternative for these use cases. Learn more about each method and how to use them below.

### Application keys

Application keys (`appKey`) are credentials used to authenticate requests to VTEX APIs. Store administrators can create multiple application keys that may be used, for example, for different integrations.

You can [manage permissions for any given application key](https://help.vtex.com/en/tutorial/application-keys--2iffYzlvvz4BDMr6WGUtet) with License Manager [roles](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc) and [resources](https://help.vtex.com/en/tutorial/license-manager-resources--3q6ztrC8YynQf6rdc6euk3).

Application keys are usually the best way to authenticate API calls in your integrations. However, there are some VETX API endpoints that do not allow this mode of authentication. Authenticate those with [user tokens](#user-token).

>❗ [Do not use application keys in your client-side code](https://help.vtex.com/en/tutorial/best-practices-application-keys--7b6nD1VMHa49aI5brlOvJm#never-use-client-side-code-for-integrations). This makes your store vulnerable to attacks.

Below you can learn more about how to authenticate API requests in this way. Still, we recommend reading these other articles to develop secure API integrations:
- [Generating and managing application keys](https://help.vtex.com/en/tutorial/application-keys--2iffYzlvvz4BDMr6WGUtet)
- [Best practices for using application keys](https://help.vtex.com/en/tutorial/best-practices-application-keys--7b6nD1VMHa49aI5brlOvJm)

#### Authenticating requests with application keys

Each `appKey` you create has an associated `appToken`. Use this credential pair to authenticate API requests by sending their values in these HTTP headers:

| **Header key** | **Value** |
|---------------------|-------------|
| `X-VTEX-API-AppKey` | `{appKey}` |
| `X-VTEX-API-AppToken` | `{appToken}` |

See an example [Get order](https://developers.vtex.com/vtex-rest-api/reference/getorder) request:

```curl
curl --location --request GET 'https://apiexamples.vtexcommercebeta.com.br/api/oms/pvt/orders/:orderId' \
--header 'X-VTEX-API-AppKey: vtexappkey-example-YSWQFZ' \
--header 'X-VTEX-API-AppToken: eyJhbGciOiJFUzI1NiIsImtpZCI6IjA1MTZFN0IwMDNFODMxRTg0QkFDOTg2NzBCNUM2QTRERTlBN0RFNkUiLCJ0eXAiOiJqd3QifQ.eyJzdWIiOiJwZWRyby5jb3N0YUB2dGV4LmNvbS5iciIsImFjY291bnQiOiJhcHBsaWFuY2V0aGVtZSIsImF1ZGllbmNlIjoiYWRtaW4iLCJzZXNzIjoiZjU3YjMyMGItMWE3YS00YzlkLWJkNDMtZTE4NDdhYmE1MTE1IiwiZXhwIjoxNjE2NzY3Mjc4LCJ1c2VySWQiOiJmYjU0MmU1MS01NDg4LTRjMzQtOGQxNy1lZDhmY2Y1OTdhOTQiLCJpYXQiOjE2MwerY2ODA4NzgsImlzcyI6InRva2VuLWVtaXR0ZXIiLCJqdGkiOiJmYTI0YWJiOC03Y2E5LTQ3NjUtYmYzNC1kMmvU5YTgzYjYxZmUifQ.23rn-2dEdAAYXJX2exrxDEdbieyKWsVKABeSUNeFWyhz7xRd7d5EcxwiMLjM3bRaBOKrAA9Op7ocn89c45qQ' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json'
```

> ℹ️️ According to the [W3C definition of Message Headers in HTTP requests](https://www.w3.org/Protocols/rfc2616/rfc2616-sec4.html#sec4.2), header names are case-insensitive. `X-VTEX-API-AppKey`, `x-vtex-api-appkey` or any other variation in the authentication headers will work the same way.

### User token

Whenever a user successfully logs in to your VTEX store, VTEX ID generates a [JWT](https://en.wikipedia.org/wiki/JSON_Web_Token) user token and sets it as the `VtexIdclientAutCookie` cookie.

For a period of 24 hours after its creation, the user token can be used to authenticate requests to VTEX APIs. To do this, send it as a header named `VtexIdclientAutCookie`.

User tokens allow for actions limited to their scope, which is defined according to the user who logged in:
- **Shopper -** Shoppers' tokens have permission to perform actions related to the shopping experience, such as viewing active products' information, placing orders, and viewing information of orders made under that same shopper profile. This token scope does not allow users to access the VTEX Admin panel or change logistics settings, for example.
- **Admin -** Administrative users' tokens allow for actions based on [License Manager roles](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc) attributed to them. This may include access to different Admin panel pages or the ability to edit different configurations, for example.

As described above, user tokens and associated permissions are tied to the user who logged in. However, they are not store-exclusive. This means, for example, that administrative users with access to different accounts can perform actions in all of those stores with the same token.

Developers working with VTEX may generate authentication tokens without having to simulate login. This can be useful to run tests or even to generate tokens programmatically if your integration depends on an API that can not be authenticated with [application keys](#application-keys). There are two methods you can use:
- [VTEX IO CLI](#generating-tokens-with-the-vtex-io-cli)
- [VTEX ID API](#generate-token-with-the-vtex-id-api)

#### Generating tokens with the VTEX IO CLI

1. Make sure you have the [VTEX IO CLI installed](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-install).
2. Log in to VTEX by running this command on your terminal:
    ```
    vtex login {accountName}
    ```
3. Once you are logged in to your VTEX account, run this command:
    ```
    vtex local token
    ```

With this, the CLI will generate a valid user token associated with your profile print it to your terminal and also copy it to your clipboard.

#### Generating tokens with the VTEX ID API

To do this, use the [Generate authentication token endpoint](https://developers.vtex.com/vtex-rest-api/reference/generateauthenticationtoken).

> ⚠️ Note that the token generated by this API endpoint is not actually a user token since it is not tied to a user profile but to an [application key](#application-key). This token's permissions are the same as [defined to the credential pair](https://help.vtex.com/en/tutorial/application-keys--2iffYzlvvz4BDMr6WGUtet#managing-app-key-permissions). However, you can use this token to authenticate API requests in the same way as a user token: as the `VtexIdclientAutCookie` header.

### App authentication

In general, when developing [VTEX IO apps](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-a-vtex-app), you will not need to send requests to VTEX APIs because these platform features are available through [clients](https://developers.vtex.com/docs/guides/vtex-io-documentation-clients). Hence, you will most likely not need to use [application keys](#application-keys) in your app.

#### Authenticating VTEX IO client operations

We recommend using the VTEX IO [clients package](https://github.com/vtex/io-clients) when possible. In this context, every client method accepts an optional argument called `authMethod`, which receives one of three authentication options, indicating which token will be used in this request:

| **`authMethod`** | Description |
|----|----|
| `AUTH_TOKEN` | App authentication token (default) |
| `STORE_TOKEN` | Store user token |
| `ADMIN_TOKEN` | Admin user token |

> ⚠️ If your project requires features not provided by these, it is a good idea to create your own clients following the same authentication logic.

The tokens shown above are available via the VTEX IO context and are associated with different permissions. See the table below to learn about each token.

> ℹ️️ You can import the context in your app as in the following: `import { IOContext } as ctx from '@vtex/api'`

| **Token**                | **`authMethod`** | **Via context**         | **Description**                                                                                                                              | **Permissions**                                                                                                                                                                                                                                                                                                                          |
|--------------------------|------------------|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| App authentication token | `AUTH_TOKEN`     | `ctx.authToken`          | Every VTEX IO app has its own rotating authentication token. We recommend you avoid using this app token whenever user tokens are available. | Developers must declare precisely what actions are allowed for the app they are building. You must do this by editing the [policies](https://developers.vtex.com/docs/guides/vtex-io-documentation-policies) in your app's [manifest](https://developers.vtex.com/docs/guides/vtex-io-documentation-manifest). |
| Store user token         | `STORE_TOKEN`    | `ctx.storeUserAuthToken` | [User token](#user-token) with store scope.                                                                                                  | Shopper permissions.                                                                                                                                                                                                                                                                                                                     |
| Admin user token         | `ADMIN_TOKEN`    | `ctx.adminUserAuthToken` | [User token](#user-token) with Admin scope.                                                                                                  | Administrative permissions as defined by [License Manager roles](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc) associated with the logged in user.                                                                                                                                                                    |
>❗ Authenticate your apps' actions with user tokens whenever possible. Currently, app authentication tokens are not subject to [License Manager permissions](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc). We recommend that you consider this when defining your app's architecture and configuring [policies](https://developers.vtex.com/docs/guides/vtex-io-documentation-policies).

## Single sign on integrations

VTEX allows stores to integrate with external identity providers to provide single sign on (SSO) experiences to shoppers and Administrative users. You can learn more about this in the article [Login (SSO)](https://developers.vtex.com/vtex-rest-api/docs/login-integration-guide) and below you can find more information on these and other SSO use cases:

- [Store SSO with OAuth 2.0](https://developers.vtex.com/docs/guides/login-integration-guide-webstore-oauth2)
- [Admin SSO with SAML 2.0](https://developers.vtex.com/docs/guides/login-integration-guide-admin-saml2)
- [Use your VTEX account as an OAuth provider](https://developers.vtex.com/docs/apps/vtex.oauth-provider-admin@2.x)
- [Unifying login for different accounts](https://developers.vtex.com/vtex-rest-api/docs/unifying-login-for-different-accounts)

## Shopper authentication for B2B stores

VTEX stores have access to different B2B solutions. See the articles below to learn more about authentication in the context of these different solutions:
- **B2B Suite** - [Storefront permissions](https://developers.vtex.com/docs/guides/vtex-storefront-permissions)
- **Legacy B2B solution** - [Configuring a B2B environment](https://developers.vtex.com/docs/guides/vtex-io-documentation-configuring-a-b2b-environment)
