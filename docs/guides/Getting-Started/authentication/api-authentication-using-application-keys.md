---
title: "API authentication using application keys"
slug: "api-authentication-using-api-keys"
hidden: false
createdAt: "2020-01-15T18:58:34.836Z"
updatedAt: "2022-12-13T18:43:56.137Z"
seeAlso:
 - "/docs/guides/app-authentication-using-auth-tokens"
 - "/docs/guides/api-authentication-using-user-tokens"
---

Application keys (`appKey`) are credentials used to authenticate requests to VTEX APIs. Store administrators can create multiple application keys that may be used, for example, for different integrations. Read [Generating and managing application keys](https://help.vtex.com/en/tutorial/api-keys--4bFEmcHXgpNksoePchZyy6) to learn how to create these credentials.

An API key includes specific permissions, based on License Manager [roles](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc) and [resources](https://help.vtex.com/en/tutorial/license-manager-resources--3q6ztrC8YynQf6rdc6euk3) selected when creating or editing the API key. Read [Managing app key permissions](https://help.vtex.com/en/tutorial/api-keys--4bFEmcHXgpNksoePchZyy6#managing-app-key-permissions) for more details.

Each `appKey` you create has an associated `appToken`. The appKey-appToken pair can be used in API requests to authorize interactions with VTEX services if they have [roles](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc) with the required [resources](https://help.vtex.com/en/tutorial/license-manager-resources--3q6ztrC8YynQf6rdc6euk3?&utm_source=autocomplete).

Application keys are usually the best way to authenticate API calls in your integrations or in self-hosted backend requests in general. However, frontend requests should be authenticated with [user tokens](https://developers.vtex.com/docs/guides/api-authentication-using-user-tokens).

>❗ Do not use application keys in your client-side code. This makes your store vulnerable to attacks. Follow the [Best practices for using application keys](https://help.vtex.com/en/tutorial/best-practices-api-keys--7b6nD1VMHa49aI5brlOvJm#never-use-client-side-code-for-integrations).

## Usage

Use the `appKey` and `appToken` credential pair to authenticate API requests by sending their values in these HTTP headers:

| Header key | Value |
| - | - |
| `X-VTEX-API-AppKey` | `{appKey}` |
| `X-VTEX-API-AppToken` | `{appToken}` |

See an example [Get order](https://developers.vtex.com/vtex-rest-api/reference/getorder) request:

```bash
curl --location --request GET 'https://apiexamples.vtexcommercebeta.com.br/api/oms/pvt/orders/:orderId' \
--header 'X-VTEX-API-AppKey: vtexappkey-example-YSWQFZ' \
--header 'X-VTEX-API-AppToken: eyJhbGciOiJFUzI1NiIsImtpZCI6IjA1MTZFN0IwMDNFODMxRTg0QkFDOTg2NzBCNUM2QTRERTlBN0RFNkUiLCJ0eXAiOiJqd3QifQ.eyJzdWIiOiJwZWRyby5jb3N0YUB2dGV4LmNvbS5iciIsImFjY291bnQiOiJhcHBsaWFuY2V0aGVtZSIsImF1ZGllbmNlIjoiYWRtaW4iLCJzZXNzIjoiZjU3YjMyMGItMWE3YS00YzlkLWJkNDMtZTE4NDdhYmE1MTE1IiwiZXhwIjoxNjE2NzY3Mjc4LCJ1c2VySWQiOiJmYjU0MmU1MS01NDg4LTRjMzQtOGQxNy1lZDhmY2Y1OTdhOTQiLCJpYXQiOjE2MwerY2ODA4NzgsImlzcyI6InRva2VuLWVtaXR0ZXIiLCJqdGkiOiJmYTI0YWJiOC03Y2E5LTQ3NjUtYmYzNC1kMmvU5YTgzYjYxZmUifQ.23rn-2dEdAAYXJX2exrxDEdbieyKWsVKABeSUNeFWyhz7xRd7d5EcxwiMLjM3bRaBOKrAA9Op7ocn89c45qQ' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json'
```

>ℹ️️ According to the [W3C definition of Message Headers in HTTP requests](https://www.w3.org/Protocols/rfc2616/rfc2616-sec4.html#sec4.2), header names are case-insensitive. `X-VTEX-API-AppKey`, `x-vtex-api-appkey` or any other variation in the authentication headers will work the same way.
