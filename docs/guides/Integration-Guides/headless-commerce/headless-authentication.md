---
title: "Headless authentication"
slug: "headless-authentication"
hidden: true
createdAt: "2023-01-27T15:04:49.386Z"
---

Building a headless ecommerce means setting up communication between your frontend and VTEX's REST APIs. Each HTTP request sent from your frontend to VTEX must be authenticated with a [user token](https://developers.vtex.com/docs/guides/getting-started-authentication#user-token). The [implementation](#implementation) shown below describes how to obtain this token in your application.

>❗ This feature is currently being tested by a limited number of VTEX accounts. Please do not share this documentation with people outside of your operation.

## Implementation

To ensure a secure shopping experience, shopper authentication for headless VTEX stores must follow a specific flow, as presented in the following:

![headless authentication flow](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Integration-Guides/headless-commerce/headless-authentication_1.png)

1. The shopper authenticates themselves in your frontend via an [OAuth integration](#oauth-log-in).
2. Your frontend [exchanges the OAuth identity provider access token for a VTEX user token](#exchanging-oauth-identity-provider-access-token-for-vtex-user-token).
3. Now, with the [user token](https://developers.vtex.com/docs/guides/getting-started-authentication#user-token) previously obtained, your frontend application can make API requests to VTEX and access all the necessary information to perform actions on behalf of the shopper.

Below you can learn more details on each of these steps.

>❗ Note that, when building a headless store, you are opting to use a frontend application different from VTEX's native frontend. Hence, you must adhere to the guidelines provided below and be aware of your [application's responsibilities](#authentication-responsibilities-of-headless-applications) in order to ensure a smooth and secure shopping experience for your customers.

### OAuth log in

Shopper authentication in your headless store must happen through an external identity provider. To do this, you must [set up an OAuth login integration](https://developers.vtex.com/docs/guides/login-integration-guide-webstore-oauth2).

After you have configured your [OAuth](https://developers.vtex.com/docs/guides/login-integration-guide-webstore-oauth2) connection in the VTEX Admin panel, you can implement the OAuth login on your frontend, according to your store's needs and [responsibilities](#authentication-responsibilities-of-headless-applications).

>⚠️ Make sure that the [OAuth access token](https://developers.vtex.com/docs/guides/login-integration-guide-webstore-oauth2#relevant-requests) has scope `email` (or another value associated with scope `email`).

### Exchanging OAuth identity provider access token for VTEX user token

If you have set up your OAuth integration and implemented login on your frontend, users may be able to authenticate themselves. However, this alone is not sufficient for your frontend to communicate with VTEX REST APIs.

To enable this communication, your frontend application must exchange the [access token](https://developers.vtex.com/docs/guides/login-integration-guide-webstore-oauth2#relevant-requests) from the OAuth login for a VTEX [user token](https://developers.vtex.com/docs/guides/getting-started-authentication#user-token). This can be achieved through the `POST` [Exchange OAuth access token for VTEX credential](https://developers.vtex.com/docs/api-reference/vtex-id-api#post-/api/vtexid/audience/webstore/provider/oauth/exchange) endpoint.

Check out request and response body examples below and refer to the `POST` [Exchange OAuth access token for VTEX credential](https://developers.vtex.com/docs/api-reference/vtex-id-api#post-/api/vtexid/audience/webstore/provider/oauth/exchange) API reference for more details on each field.

#### Request body example

```json
{
  "providerId": "custom-oauth-provider",
  "accessToken": "dsfDShdgfhDFI1NiIsIrtyZCI6IjFBRjI5MUUwRDY0MERENTlEQTkzRTg0REMxNjQyNjA3ODZEQjY3ODAiLCJ0eXAiOiJqd3QifQ.eyJzdWIiOiJ2dGV4YXBwa2V5LXZ0ZXhoZWxwLVdWQ0FCVCIsImFjY291bdg465DATU4GVscCIsImF1MBllbmNlIjoiYWRtaW4iLCJleHAiOjE2Njk3NzA3MzcsInVzZXJJZCI6IjM5MjNhMmUy5khmMTctNGNiYy04YzU3LWQ3OGFkNmUxYTU2NiIsImlhdCI6MTY2OTc0OTEzNywiaXNzIjoidG9rZW4tZW1HgoRlciIsImp0aSI6IjNiNjAxODA2LTExMzEtNDcwYS05MWJjLTVhM2JhOThiYWQyNiJ9.Q7N8MFa1FMJsQUpxBY29oije4aa-654fgjLFLl6LUY3Wei3MRUVUMRQWkey6Kug8iFPonZ1L-PaFmwfzSz3TCQ",
  "duration": 90
}
```

#### Response body example

```json
{
"authToken": "eyJhbGciOiJFUzI1NiIsIrtyZCI6IjFBRjI5MUUwRDY0MERENTlEQTkzRTg0REMxNjQyNjA3ODZEQjY3ODAiLCJ0eXAiOiJqd3QifQ.eyJzdWIiOiJ2dGV4YXBwa2V5LXZ0ZXhoZWxwLVdWQ0FCVCIsImFjY291bnQiOiJwerV4aGVscCIsImF1MBllbmNlIjoiYWRtaW4iLCJleHAiOjE2Njk3NzA3MzcsInVzZXJJZCI6IjM5MjNhMmUy5khmMTctNGNiYy04YzU3LWQ3OGFkNmUxYTU2NiIsImlhdCI6MTY2OTc0OTEzNywiaXNzIjoidG9rZW4tZW1HgoRlciIsImp0aSI6IjNiNjAxODA2LTExMzEtNDcwYS05MWJjLTVhM2JhOThiYWQyNiJ9.Q7N8MFa1FMJsQUpxBY29oije4aa-Jf463lwgLFLl6LUY3Wei3MRUVUMRQWkey6Kug8iFPonZ1L-PaFmwfzSz3TCQ"
}
```

### Making requests to VTEX APIs

Once with a valid VTEX user token, your frontend application can leverage [VTEX APIs](https://developers.vtex.com/docs/api-reference) to manage various commerce capabilities of your store, including product information, shopping cart management, and checkout.

Learn more about [machine authentication in VTEX](https://developers.vtex.com/docs/guides/getting-started-authentication) and [how to use user tokens](https://developers.vtex.com/docs/guides/getting-started-authentication#user-token) to authenticate your requests.

## Authentication responsibilities of headless applications

Since your store is not using VTEX's native frontend to authenticate shoppers, there are some capabilities that your application must be prepared to handle:

- Managing login flow with the external identity provider.
- Making sure that the [OAuth access token](https://developers.vtex.com/docs/guides/login-integration-guide-webstore-oauth2#relevant-requests) has scope `email` (or another value associated with scope `email`).
- Keeping the [OAuth access token](https://developers.vtex.com/docs/guides/login-integration-guide-webstore-oauth2#relevant-requests) in the contexts where it is relevant.
- Refreshing tokens and other information when necessary.
- Keeping track of the expiration time set for the [VTEX user token](https://developers.vtex.com/docs/guides/getting-started-authentication#user-token).
- Requiring new login if it was somehow revoked.
- Repeating the [token exchange](#exchanging-oauth-identity-provider-access-token-for-vtex-user-token) in case the shopper had to log in again.

## Learn more

See these other guides to learn more about building a headless shopping experience using VTEX:

- [Headless commerce overview](https://developers.vtex.com/docs/guides/headless-commerce)
- [Headless catalog and search](https://developers.vtex.com/docs/guides/headless-catalog)
- [Headless cart and checkout](https://developers.vtex.com/docs/guides/headless-cart-and-checkout)
- [Headless profile management and order history](https://developers.vtex.com/docs/guides/headless-profile-management-and-order-history)
