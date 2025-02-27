---
title: "VTEX ID API: New endpoints for token renewal"
slug: "2025-03-14-vtex-id-api-new-endpoints-for-token-renewal"
hidden: false
type: "added"
createdAt: "2025-03-14T00:00:00.219Z"
excerpt: "VTEX ID API now allows you to renew API tokens with new secure endpoints."
---

We have introduced two new endpoints to the VTEX ID API to allow merchants to securely renew API tokens: `PATCH` [Initiate token renewal](https://developers.vtex.com/docs/api-reference/vtex-id-api#patch-/api/vtexid/apikey/-apiKey-/apitoken/renew) and `PATCH` [Complete token renewal](https://developers.vtex.com/docs/api-reference/vtex-id-api#patch-/api/vtexid/apikey/-apiKey-/apitoken/finish-renewal). This two-step renewal process ensures better security while maintaining service continuity.

## What has changed?

Previously, the new [API Keys experience](https://help.vtex.com/en/tutorial/api-keys--4bFEmcHXgpNksoePchZyy6) only allowed [token renewal via Admin interface](https://help.vtex.com/en/tutorial/renewing-api-tokens--7r4AzptYjXErGHadg9LnJ3). Now, there are two API endpoints dedicated to renewing tokens:

| Endpoint | Description |
| - | - |
| `PATCH` [Initiate token renewal](https://developers.vtex.com/docs/api-reference/vtex-id-api#patch-/api/vtexid/apikey/-apiKey-/apitoken/renew) | Starts the API token renewal process by generating a new token while keeping the current token active. This ensures a smooth transition without service disruption. The previous token and the new token are both valid until the renewal process is completed by making a request to `PATCH` [Complete token renewal](https://developers.vtex.com/docs/api-reference/vtex-id-api#patch-/api/vtexid/apikey/-apiKey-/apitoken/finish-renewal). |
| `PATCH` [Complete token renewal](https://developers.vtex.com/docs/api-reference/vtex-id-api#patch-/api/vtexid/apikey/-apiKey-/apitoken/finish-renewal) | Finalizes the API token renewal process, deactivating the old token. After this step, the old token can no longer be used, ensuring security by enforcing a controlled rotation. |

Any user or [application key](https://developers.vtex.com/docs/guides/authentication-overview#application-keys) must have the *Renew API Token* [License Manager resource](https://help.vtex.com/en/tutorial/license-manager-resources--3q6ztrC8YynQf6rdc6euk3) to be able to successfully run these requests. Otherwise, they will receive a status code `403` error.
