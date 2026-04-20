---
title: "Updated vtexvault.com route for Send Payments request"
slug: "2026-04-20-updated-vtexvaultcom-route-for-send-payments-request"
hidden: false
type: "improved"
createdAt: "2026-04-20T12:00:00.000Z"
excerpt: "The vtexvault.com route for sending payment information has changed to use the account name in the subdomain. Update your integration by July 21, 2026."
---

The route for sending payment information via `vtexvault.com` has been updated. All integrations that have already adopted the route announced in the [Mandatory migration to vtexvault.com for "Send Payments" request](https://developers.vtex.com/updates/release-notes/2025-10-28-mandatory-migration-to-vtexvault-com-for-send-payments-request) release note must be updated to use the new route format.

## What has changed?

The [previous release note](https://developers.vtex.com/updates/release-notes/2025-10-28-mandatory-migration-to-vtexvault-com-for-send-payments-request) introduced the `vtexvault.com` domain for sending payment information, using the account name as a query parameter:

`https://api.vtexvault.com/api/payments/transactions/{transactionId}/payments?an={accountName}`

The route has been updated so the account name is now part of the subdomain, as in the example:

`https://{accountName}.vtexvault.com/api/payments/transactions/{transactionId}/payments`

> ⚠️ After **July 21, 2026**, if you send payment data to any route other than `http://{accountName}.vtexvault.com/api/payments/transactions/{transactionId}/payments`, the system will block the request, return a `404 - Not Found` status code, and interrupt the purchase order flow.


## What needs to be done?

Update your payment integration to use the new route format before **July 21, 2026**:

| **Method** | **From** | **To** |
|-----------|----------|----------|
| **POST** | `https://api.vtexvault.com/api/payments/transactions/{transactionId}/payments?an={accountName}` | `https:/{accountName}.vtexvault.com/api/payments/transactions/{transactionId}/payments` |


> ⚠️ If you have not yet migrated from the legacy routes (`myvtex.com`, `vtexcommercestable.com.br`, `vtexpayments.com.br`), migrate directly to the route `https:/{accountName}.vtexvault.com/api/payments/transactions/{transactionId}/payments` before **July 21, 2026**. For the full list of deprecated routes, refer to the [original release note](https://developers.vtex.com/updates/release-notes/2025-10-28-mandatory-migration-to-vtexvault-com-for-send-payments-request).

> ℹ️ The [endpoint](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/payments/transactions/-transactionId-/payments) behavior remains the same: a successful request returns an empty body with status code `201 - Created`. If your implementation relies on payment details in the response, call the [Get payment details](https://developers.vtex.com/docs/api-reference/payments-gateway-api#get-/api/pvt/transactions/-transactionId-/payments/-paymentId-) endpoint after sending the payment.
