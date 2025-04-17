---
title: "Refresh token flow for headless implementations"
slug: "refresh-token-flow-for-headless-implementations"
hidden: false
excerpt: "Learn how to implement refresh token in headless stores."
createdAt: "2025-04-04T22:18:24.684Z"
updatedAt: "2025-04-16T22:08:16.684Z"
---

The refresh token flow is a security mechanism in authentication systems that allows clients to obtain new access tokens without requiring users to reauthenticate.

This guide explains how to implement the refresh token flow in [headless](https://developers.vtex.com/docs/guides/headless-commerce) scenarios using native VTEX Login.

## Authentication tokens

The refresh token flow operates with two types of tokens:

* **Access token (`VtexIdclientAutCookie_{{accountName}}`)**: Short-lived token (24h), the primary credential used to authenticate API requests. It has a short expiration time to minimize security risks.
* **Refresh token (`vid_rt`)**: Token with configurable expiration, always with a longer duration when compared to the access token (1, 7, or 30 days). Used to renew access tokens.

>ℹ️ Contact VTEX [Support](https://support.vtex.com/hc/en-us/requests) to request the refresh token activation and expiration time configuration.

## Refresh token flow

When the access token expires, but the refresh token is still valid, the client must use the refresh token to request a new access token via a dedicated renewal endpoint. The refresh process also returns a new refresh token, which replaces the previous one.

The following diagram illustrates the complete refresh token lifecycle, showing how authentication and token renewal work over time.

```mermaid
sequenceDiagram
participant User as User's Browser
participant VTEXID as VTEX ID

User->>VTEXID: 1. Login
VTEXID-->>User: 2. Cookie: Access token X <br> Cookie: Refresh token A

Note over User,VTEXID: 29 days later

User->>VTEXID: 3. Reauthenticate with Refresh token A
VTEXID-->>User: 4. Cookie: Access token Y<br> Cookie: Refresh token B
```

The following steps detail the refresh token flow shown in the diagram:

1. **Login**

   The user initiates authentication by logging into the system. VTEX ID processes the login request.

2. **VTEX ID responds with tokens**

   If authentication is successful, VTEX ID issues:

     * Access token
     * Refresh token

   These tokens are stored in cookies during the user's browser session.

3. **Reauthentication after access token expiration**

   After 24 hours, the access token expires. If the refresh token is still valid, the client can automatically obtain a new access token without any additional interaction.

   For example, if the refresh token has a 30-day lifespan and the user attempts to log in 29 days after their last authentication, the user’s browser sends the refresh token to VTEX ID to obtain a new access token. However, once the 30-day period ends, the refresh token expires, and the user must log in again to generate new access and refresh tokens.

   This happens automatically when stores use [Store Framework](https://developers.vtex.com/docs/guides/store-framework) or [Legacy CMS Portal](https://help.vtex.com/en/tracks/cms--2YcpgIljVaLVQYMzxQbc3z/1oN446gRGcR2s70RvBCAmj). For [headless](https://developers.vtex.com/docs/guides/headless-commerce) stores, it needs to be manually implemented following the instructions on this guide.

1. **VTEX ID issues new tokens**

   VTEX ID validates the refresh token and, if it's still valid:

     * Issues a new access token
     * Provides a new refresh token

   These new tokens replace the old ones in the browser.

This cycle repeats until the refresh token expires, ensuring uninterrupted user authentication.

## Implementing the refresh token flow

To implement the refresh token flow in headless stores, use the VTEX ID API endpoints described in the following sections.

### 1. Starting authentication

Initiate the authentication flow and obtain an `authenticationToken` by sending a `GET` request to the [Start authentication](https://developers.vtex.com/docs/api-reference/vtex-id-api#get-/api/vtexid/pub/authentication/start) endpoint.

**Request:**

```curl
curl --location 'https://{{storeDomain}}/api/vtexid/pub/authentication/start?scope={{accountName}}&fingerprint={{fingerprint}} \
```

#### **Response body example:**

```json
{
  "authenticationToken": "C17BCD635B637E66BF2BBE07CEED0B1B7425387FB8D6E42FE68EBCE7A49193F2",
  "oauthProviders": [
    {
      "providerName": "Google",
      "className": "google-plus",
      "expectedContext": []
    },
    {
      "providerName": "Facebook",
      "className": "facebook",
      "expectedContext": []
    }
  ],
  "showClassicAuthentication": true,
  "showAccessKeyAuthentication": true,
  "showPasskeyAuthentication": false,
  "authCookie": null,
  "isAuthenticated": false,
  "selectedProvider": null,
  "samlProviders": []
}
```

### 2. Continuing authentication

After starting the authentication process, the next step is to proceed with the login method configured for the store. VTEX ID supports multiple login providers, including:

* Access key (login code sent by email)
* Email and password
* Social logins (Google, Facebook)
* Custom OAuth providers

Each store can enable one or more of these options, and all of which follow the same general flow at this stage: the client uses the `authenticationToken` from the previous step to complete the login process.

If the store uses **access key** as the login method, you must send a login code to the user's email using a `POST` request to the [Send access key](https://developers.vtex.com/docs/api-reference/vtex-id-api#post-/api/vtexid/pub/authentication/accesskey/send) endpoint.

**Example request for access key login:**

```curl
curl --location --request POST 'https://{{storeDomain}}/api/vtexid/pub/authentication/accesskey/send?email={{userEmail}}' \
--header 'Cookie: _vss={{authenticationToken}}'
```

The expected response is an empty `200 OK`, and the user will instantly receive an email with the access code.

### 3. Validating the session

Once the user has provided their credentials or login code — depending on the login provider configured for the store — you must validate the session to complete authentication and receive the access and refresh tokens.

For the access key method, use the received access key and the user email to validate the session via a `POST` request to the [Validate session](https://developers.vtex.com/docs/api-reference/vtex-id-api#post-/api/vtexid/pub/authentication/accesskey/validate) endpoint. The request is structured as follows:

**Request:**

```json
curl --location 'https://{{storeDomain}}/api/vtexid/pub/authentication/accesskey/validate' \
--header 'Cookie: _vss={{authenticationToken}} \
--form 'accesskey="{{accessKey}}"' \
--form 'login="{{userEmail}}"'
```

**Response body example:**

```json
{
  "authStatus": "Success",
  "promptMFA": false,
  "lastAttemptAvailable": null,
  "clientToken": null,
  "authCookie": {
    "Name": "VtexIdclientAutCookie_{{accountName}}",
    "Value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
  },
  "accountAuthCookie": {
    "Name": "VtexIdclientAutCookie_{{accountId}}",
    "Value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
  },
  "expiresIn": 86399,
  "userId": "1f6c17e5-06f9-44a9-a459-b3686e03fa9d",
  "phoneNumber": null,
  "scope": null
}
```

The response headers will set a `vid_rt` cookie, which contains the refresh token value, as illustrated below:

| Set-Cookie | `vid_rt=QiEOQKuzdRjukvSnsn7F8h1wwkrqq8wWlkk7bXA5LSbTHkbKbYEfDJ7MGb6_pllGWd1VQ-JxQI7UDLvYrCUH9o7i1rOSeSG8zJewZw; expires=Thu, 27 Mar 2025 10:22:49 GMT; domain={{storeDomain}}; path=/api/vtexid/refreshtoken/webstore; secure; samesite=strict; httponly` |
| - | - |

### 4. Refreshing the token

Finally, use the obtained refresh token to request a new access token via a `POST` request to the [Refresh token](https://developers.vtex.com/docs/api-reference/vtex-id-api#post-/api/vtexid/refreshtoken/webstore) endpoint.

**Request:**

```curl
curl --location --request POST 'https://{{storeDomain}}/api/vtexid/refreshtoken/webstore' \
--header 'Host: {{storeDomain}}' \
--header 'Content-Type: application/json;charset=UTF-8' \
--header 'Cookie: vid_rt={{vid_rt}};
VtexIdclientAutCookie_{{accountId}}={{VtexIdclientAutCookie_accountId}}; VtexIdclientAutCookie_{{accountName}}={{VtexIdclientAutCookie_accountName}}' \
--data-raw '{
    "fingerprint": "a1b2c3d4e5f6"
}'
```

**Response body example:**

```json
{
    "status": "Success",
    "userId": "1f6c17e5-06f9-44a9-a459-b3686e03fa9d",
    "refreshAfter": "2025-03-26T02:53:39+00:00"
}
```

The response cookies provide valid values for:

* `vid_rt`
* `VtexIdclientAutCookie_{{accountId}}`
* `VtexIdclientAutCookie_{{accountName}}`
