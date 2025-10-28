---
title: 'Mandatory migration to vtexvault.com for "Send Payments" request'
slug: "2025-10-28-mandatory-migration-to-vtexvault-com-for-send-payments-request"
hidden: false
type: "improved"
createdAt: "2025-10-28T00:00:00.219Z"
updatedAt: "2025-10-28T00:00:00.219Z"
excerpt: "The current routes for sending payment information will be replaced with the new route vtexvault.com."
tags:
    - Payments
---

To enhance payment data security, all payment information will now be received exclusively through a new dedicated route on VTEX.

## What has changed?

Previously, merchants could use routes containing the `myvtex.com`, `vtexcommercestable.com.br`, `vtexpayments.com.br` domains or personalized client hosts (example: `{accountname}.com`) to forward payment information to VTEX.

Example:

`https://{accountName}.vtexpayments.com.br/api/pvt/transactions/{transactionId}/payments`

After **January 31, 2026**, it will be mandatory to send all payment information to VTEX using the `vtexvault.com` domain, where the account name is sent as a query parameter:

`https://api.vtexvault.com/api/payments/transactions/{transactionId}/payments?an={accountName}`

> ⚠️ If you send payment data to any route other than `https://api.vtexvault.com/api/payments/transactions/{transactionId}/payments?an={accountName}`, the system will block the request, return a `404 - Not Found` status code, and interrupt the purchase order flow.

> ℹ️ We renamed the endpoint [2.1 Send payments information public](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/pub/transactions/-transactionId-/payments) to "**Send payments information**" and updated its path route. We will also deprecate the [2.2 Send payments with saved credit card](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/pvt/transactions/-transactionId-/payments) endpoint.

## What needs to be done?

Check if any of the payment integrations in your account are using the deprecated routes and make the following adjustment before **January 31, 2026**, if necessary:

| **Method** | **From** |
|-----------|----------|
| **POST** | <ul><li>`https://{accountName}.myvtex.com/api/pub/transactions/{transactionId}/payments`</li><li>`https://{accountName}.vtexcommercestable.com.br/api/pub/transactions/{transactionId}/payments`</li><li>`https://{accountName}.vtexpayments.com.br/api/pub/transactions/{transactionId}/payments`</li></ul> |
| **POST** | <ul><li>`https://{accountName}.myvtex.com/api/pvt/transactions/{transactionId}/payments`</li><li>`https://{accountName}.vtexcommercestable.com.br/api/pvt/transactions/{transactionId}/payments`</li><li>`https://{accountName}.vtexpayments.com.br/api/pvt/transactions/{transactionId}/payments`</li></ul> |
| **POST** | <ul><li>`https://{accountName}.myvtex.com/api/payments/pub/transactions/{transactionId}/payments`</li><li>`https://{accountName}.vtexcommercestable.com.br/api/payments/pub/transactions/{transactionId}/payments`</li><li>`https://{accountName}.vtexpayments.com.br/api/payments/pub/transactions/{transactionId}/payments`</li></ul> |
| **POST** | <ul><li>`https://{accountName}.myvtex.com/api/payments/pvt/transactions/{transactionId}/payments`</li><li>`https://{accountName}.vtexcommercestable.com.br/api/payments/pvt/transactions/{transactionId}/payments`</li><li>`https://{accountName}.vtexpayments.com.br/api/payments/pvt/transactions/{transactionId}/payments`</li></ul> |

| **Method** | **To** |
|-----------|----------|
| **POST** | `https://api.vtexvault.com/api/payments/transactions/{transactionId}/payments?an={accountName}` |

When the new route successfully sends payment information, it returns an empty body with the status code `201 - Created`. Unlike the two routes below, it doesn’t return payment details. If your current implementation relies on the returned information, you must call the [Get payment details](https://developers.vtex.com/docs/api-reference/payments-gateway-api#get-/api/pvt/transactions/-transactionId-/payments/-paymentId-) route after migration to retrieve it:

- **GET**: `https://{accountName}.vtexcommercestable.com.br/api/pvt/transactions/{transactionId}/payments`
- **GET**: `https://{accountName}.vtexcommercestable.com.br/api/payments/pvt/transactions/{transactionId}/payments`
