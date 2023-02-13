---
title: "Headless authentication"
slug: "headless-authentication"
hidden: true
createdAt: "2023-01-27T15:04:49.386Z"
---

Building a headless ecommerce means setting up communication between your frontend and VTEX's REST APIs. Each HTTP request sent from your frontend to VTEX must be authenticated with a [user token](https://developers.vtex.com/docs/guides/getting-started-authentication#user-token). The [implementation](#implementation) shown below describes how to obtain this token in your application.

>❗ This feature is currently being tested by a limited number of VTEX accounts. Please do not share this documentation with people outside of your operation.

## Implementation

This is the flow of shopper authentication for headless VTEX stores:

![headless authentication flow](./headless-authentication_1.png)

1. The shopper authenticates themselves in your frontend via an [OAuth integration](#oauth-log-in).
2. Your frontend [exchanges the OAuth identity provider access token for a VTEX user token](#exchanging-oauth-identity-provider-access-token-for-vtex-user-token).
3. Now you can make requests from your frontend to VTEX APIs using the obtained [user token](https://developers.vtex.com/docs/guides/getting-started-authentication#user-token).

Below you can learn more details on each of these steps.

>❗ If you are building a headless store, it means you are using a frontend application different from VTEX's native frontend. Because of this, it is important to follow the instructions provided below and be aware of your [application's responsibilities](#authentication-responsibilities-of-headless-applications).

### OAuth log in

Shopper authentication in your headless store must happen through an external identity provider. To do this, you must [set up an OAuth login integration](https://developers.vtex.com/docs/guides/login-integration-guide-webstore-oauth2).

After you have configured your [OAuth](https://developers.vtex.com/docs/guides/login-integration-guide-webstore-oauth2) connection in the VTEX Admin panel, you can implement the OAuth login on your frontend, according to your store's needs and [responsibilities](#authentication-responsibilities-of-headless-applications).

>⚠️ Make sure that the [OAuth access token](https://developers.vtex.com/docs/guides/login-integration-guide-webstore-oauth2#relevant-requests) has scope `email` (or another value associated with scope `email`).

### Exchanging OAuth identity provider access token for VTEX user token

If you have set up your OAuth integration and implemented login on your frontend, users may be able to authenticate themselves, but this is still not enough for your frontend to communicate with VTEX REST APIs.

To be able to do this, your frontend must exchange the [access token](https://developers.vtex.com/docs/guides/login-integration-guide-webstore-oauth2#relevant-requests) from the OAuth login for a VTEX [user token](https://developers.vtex.com/docs/guides/getting-started-authentication#user-token) via the [Exchange OAuth access token for VTEX credential API request](https://developers.vtex.com/docs/api-reference/vtex-id-api#post-/vtexid/audience/webstore/provider/oauth/exchange). See an example below:

Endpoint:

```
POST
https://{accountName}.{environment}.com.br/vtexid/audience/webstore/provider/oauth/exchange
```

Request body:

```
{
  "providerId": "GoogleID",
  "accessToken": "dsfDShdgfhDFI1NiIsIrtyZCI6IjFBRjI5MUUwRDY0MERENTlEQTkzRTg0REMxNjQyNjA3ODZEQjY3ODAiLCJ0eXAiOiJqd3QifQ.eyJzdWIiOiJ2dGV4YXBwa2V5LXZ0ZXhoZWxwLVdWQ0FCVCIsImFjY291bdg465DATU4GVscCIsImF1MBllbmNlIjoiYWRtaW4iLCJleHAiOjE2Njk3NzA3MzcsInVzZXJJZCI6IjM5MjNhMmUy5khmMTctNGNiYy04YzU3LWQ3OGFkNmUxYTU2NiIsImlhdCI6MTY2OTc0OTEzNywiaXNzIjoidG9rZW4tZW1HgoRlciIsImp0aSI6IjNiNjAxODA2LTExMzEtNDcwYS05MWJjLTVhM2JhOThiYWQyNiJ9.Q7N8MFa1FMJsQUpxBY29oije4aa-654fgjLFLl6LUY3Wei3MRUVUMRQWkey6Kug8iFPonZ1L-PaFmwfzSz3TCQ",
  "duration": 90
}
```

- `providerId` - Identity provider ID as configured in the [OAuth integration setup](#oauth-log-in).
- `accessToken` - Access token that gets to your frontend as a result of a successful [OAuth login](https://developers.vtex.com/docs/guides/login-integration-guide-webstore-oauth2#relevant-requests).
- `duration` - Duration of the [VTEX user token](https://developers.vtex.com/docs/guides/getting-started-authentication#user-token) that will be returned. This field is optional and the default is 60.

Response body:

```
{
"authToken": "eyJhbGciOiJFUzI1NiIsIrtyZCI6IjFBRjI5MUUwRDY0MERENTlEQTkzRTg0REMxNjQyNjA3ODZEQjY3ODAiLCJ0eXAiOiJqd3QifQ.eyJzdWIiOiJ2dGV4YXBwa2V5LXZ0ZXhoZWxwLVdWQ0FCVCIsImFjY291bnQiOiJwerV4aGVscCIsImF1MBllbmNlIjoiYWRtaW4iLCJleHAiOjE2Njk3NzA3MzcsInVzZXJJZCI6IjM5MjNhMmUy5khmMTctNGNiYy04YzU3LWQ3OGFkNmUxYTU2NiIsImlhdCI6MTY2OTc0OTEzNywiaXNzIjoidG9rZW4tZW1HgoRlciIsImp0aSI6IjNiNjAxODA2LTExMzEtNDcwYS05MWJjLTVhM2JhOThiYWQyNiJ9.Q7N8MFa1FMJsQUpxBY29oije4aa-Jf463lwgLFLl6LUY3Wei3MRUVUMRQWkey6Kug8iFPonZ1L-PaFmwfzSz3TCQ"
}
```

- `authToken` - [User token](https://developers.vtex.com/docs/guides/getting-started-authentication#user-token) that can be used to [authenticate API requests](#making-requests-to-vtex-apis).

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
