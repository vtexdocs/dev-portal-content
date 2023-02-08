---
title: "Headless authentication"
slug: "headless-authentication"
hidden: true
createdAt: "2023-01-27T15:04:49.386Z"
---

Building a headless ecommerce means setting up communication between your frontend and VTEX's REST APIs. Each HTTP request sent from your frontend to VTEX must be authenticated with a [user token](https://developers.vtex.com/docs/guides/getting-started-authentication#user-token). The [implementation](#implementation) shown below describes how to obtain this token in your frontend.

>❗ This feature is currently being tested by a limited number of VTEX accounts. Please do not share this documentation with people outside of your operation.

## Implementation

This is the flow of shopper authentication for headless VTEX stores:

![headless authentication flow](./headless-authentication_1.png)

1. The shopper authenticates themselves in your frontend via an [OAuth integration](#oauth-log-in).
2. Your frontend [exchanges the OAuth identity provider access token for a VTEX user token](#exchanging-oauth-identity-provider-access-token-for-vtex-user-token).
3. Now you can make requests from your frontend to VTEX APIs using the obtained [user token](https://developers.vtex.com/docs/guides/getting-started-authentication#user-token).

Below you can learn more details on each of these steps.

### OAuth log in

Shopper authentication in your headless store must happen through an external identity provider. To do this, you must [set up an OAuth login integration](https://developers.vtex.com/docs/guides/login-integration-guide-webstore-oauth2).

After you have configured your [OAuth](https://developers.vtex.com/docs/guides/login-integration-guide-webstore-oauth2) connection in the VTEX Admin panel, you can implement the OAuth login on your frontend.

### Exchanging OAuth identity provider access token for VTEX user token

If you have set up your OAuth integration and implemented login on your frontend, users may be able to authenticate themselves, but this is still not enough for your frontend to communicate with VTEX REST APIs.

To be able to do this, your frontend must exchange the [access token](https://developers.vtex.com/docs/guides/login-integration-guide-webstore-oauth2#relevant-requests) from the OAuth login for a VTEX user token via the [Exchange OAuth access token for VTEX credential API request](https://developers.vtex.com/docs/api-reference/vtex-id-api#post-/vtexid/audience/webstore/provider/oauth/exchange). See an example below:

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

- `providerId` must be the same as configured in the [OAuth integration](#oauth-log-in).

Response body:
```
{
"authToken": "eyJhbGciOiJFUzI1NiIsIrtyZCI6IjFBRjI5MUUwRDY0MERENTlEQTkzRTg0REMxNjQyNjA3ODZEQjY3ODAiLCJ0eXAiOiJqd3QifQ.eyJzdWIiOiJ2dGV4YXBwa2V5LXZ0ZXhoZWxwLVdWQ0FCVCIsImFjY291bnQiOiJwerV4aGVscCIsImF1MBllbmNlIjoiYWRtaW4iLCJleHAiOjE2Njk3NzA3MzcsInVzZXJJZCI6IjM5MjNhMmUy5khmMTctNGNiYy04YzU3LWQ3OGFkNmUxYTU2NiIsImlhdCI6MTY2OTc0OTEzNywiaXNzIjoidG9rZW4tZW1HgoRlciIsImp0aSI6IjNiNjAxODA2LTExMzEtNDcwYS05MWJjLTVhM2JhOThiYWQyNiJ9.Q7N8MFa1FMJsQUpxBY29oije4aa-Jf463lwgLFLl6LUY3Wei3MRUVUMRQWkey6Kug8iFPonZ1L-PaFmwfzSz3TCQ"
}
```

### Making requests to VTEX APIs

Once your frontend has a VTEX user token, it can now use [VTEX APIs](https://developers.vtex.com/docs/api-reference) to manage your store's commerce capabilities, such as product information, shopping cart and checkout.

Learn more about [machine authentication in VTEX](https://developers.vtex.com/docs/guides/getting-started-authentication) and [user tokens](https://developers.vtex.com/docs/guides/getting-started-authentication#user-token).