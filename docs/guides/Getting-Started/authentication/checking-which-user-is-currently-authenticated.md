---
title: "Checking which user is currently authenticated"
slug: "checking-which-user-is-currently-authenticated"
hidden: false
createdAt: "2022-08-04T22:00:24.684Z"
updatedAt: "2022-08-04T22:08:52.246Z"
seeAlso:
 - "user-authentication-and-login"
---
When a user logs into your store, cookies that store the authorization token are created. From this moment, any request to VTEX servers will load these cookies automatically, identifying the user responsible for the action.

In many contexts different than API requests to VTEX, it may be necessary to verify that the user is logged in or maybe get something that identifies them, such as email or ID. Cookies also allow this type of action.

However, note that these cookies have the "HTTP Only" and "Secure" options enabled, which means that they are not accessible by any JavaScript method, and will only be sent in secure HTTP requests (i.e., using the HTTPS protocol).

So the verification of the user who is authenticated must happen through the following API endpoint:

```bash
GET
https://{accountName}.{environment}.com.br/api/vtexid/pub/authenticated/user?authToken={VtexIdclientAutCookie}
```

The response will be structured like this:

```json
{
    "userId": "88888888-8888-8888-8888-888888888888",
    "user": "user@mail.com",
    "userType": "F"
}
```

- `userId`: is the user ID within VTEX services.
- `user`: user email.
- `userType`: meant for VTEX internal use.

If the user is not authenticated, the response for this API will be empty (`null` response body), with an HTTP status `200 (OK)` or `401 (Unauthorized)`.