---
title: "Checking authenticated users via authorization cookies"
slug: "checking-which-user-is-currently-authenticated"
excerpt: Learn how to check which user is currently authenticated in your store using their authentication token and VTEX APIs.
hidden: false
createdAt: "2022-08-04T22:00:24.684Z"
updatedAt: "2022-08-04T22:08:52.246Z"
seeAlso:
 - "/docs/guides/api-authentication-using-user-tokens"
---

In this guide, you will learn how to verify if a user is currently authenticated in your store using their authentication token stored in cookies. Additionally, you will learn how to retrieve identifying information, such as their user ID and email, using VTEX's API.

## Authentication cookies overview

When a user logs into your store, cookies are created to store the authorization token. From that point onward, these cookies are automatically included in all requests to VTEX servers, enabling the system to identify the user performing the action.

In situations other than API requests to VTEX, you may need to check whether the user is logged in or retrieve identifying information, such as their email or user ID. These actions can also be accomplished using the authentication cookies.

> Note that these cookies have the `HTTP Only` and `Secure` options enabled. This means they cannot be accessed via JavaScript and will only be sent over secure HTTPS requests.

## Instructions

<CH.Scrollycoding>

### Sending the request to verify user authentication

To check the authenticated user, send a request to the `POST` [Check authenticated user](https://developers.vtex.com/docs/api-reference/vtex-id-api#post-/api/vtexid/credential/validate) endpoint, replacing the example account name, API key / token pair and user token.

<CH.Code>

```curl Request
curl --request post \
	--url 'https://apiexamples.vtexcommercestable.com.br/api/vtexid/credential/validate?an=exampleAccount' \
	--header 'Accept: application/json' \
	--header 'Content-Type: application/json' \
	--header 'X-VTEX-API-AppKey: 123' \
	--header 'X-VTEX-API-AppToken: 123' \
	--data '{"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"}'
```

---

```json 200-Response
{
  "authStatus": "Success",
  "id": "1f6c17e5-06f9-44a9-a459-b3686e03fa9d",
  "user": "john@mail.com",
  "account": "apiexamples",
  "audience": "admin",
  "tokenType": "user"
}
```

</CH.Code>

---

### Analyzing the API response

#### Authenticated user

If the user is authenticated, the API will return a JSON object with the following structure:

- `authStatus`: The authentication status (e.g., `Success`).
- `id`: The unique user ID within VTEX services.
- `user`: The user's email address.
- `account`: The account name associated with the request.
- `audience`: The audience scope of the token (e.g., `admin`).
- `tokenType`: The type of token used for authentication (e.g., `user`).

<CH.Code>

```json Request
```

---

```json 200-Response mark=2:7
```
</CH.Code>

</CH.Scrollycoding>

#### Non-authenticated user

If the user is not authenticated, the HTTP status will be `401 (Unauthorized)`.
