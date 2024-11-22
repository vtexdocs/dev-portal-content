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

To check the authenticated user, send a request to the indicated API endpoint, replacing `VtexIdclientAutCookie` with the user's authorization token.

<CH.Code>

```bash Request
GET
https://{accountName}.{environment}.com.br/api/vtexid/pub/authenticated/user?authToken={VtexIdclientAutCookie}
```

---

```json 200-Response
{
    "userId": "88888888-8888-8888-8888-888888888888",
    "user": "user@mail.com",
    "userType": "F"
}
```

</CH.Code>

---

### Analyzing the API response

#### Authenticated user

If the user is authenticated, the API will return a JSON object with the following structure:

- `userId`: The unique user ID within VTEX services.
- `user`: The user's email address.
- `userType`: Internal VTEX user type identifier (for VTEX use only).

<CH.Code>

```json Request
```

---

```json 200-Response mark=2:4
```
</CH.Code>

---

#### Non-authenticated user

If the user is not authenticated, the response body will be empty (`null`), and the HTTP status will be either `200 (OK)` or `401 (Unauthorized)`.

<CH.Code>

```json Request
```

---

```json 200-Response
 null
```
</CH.Code>


</CH.Scrollycoding>
