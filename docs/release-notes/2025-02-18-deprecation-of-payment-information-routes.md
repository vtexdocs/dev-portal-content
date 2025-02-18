---
title: "Payments Gateway API: Deprecation of payment information routes"
slug: "2025-02-18-deprecation-of-payment-information-routes"
type: improved
excerpt: "Two routes used to send payment information will be deprecated."
createdAt: "2025-02-18T00:00:00.000Z"
updatedAt: ""
hidden: false
---
To improve payment information management in the VTEX Payments Gateway API, the following routes will be deprecated on **April 1, 2025**:

|  METHOD  |                                                    ROUTES                                                    |
| :------: | :----------------------------------------------------------------------------------------------------------: |
| `POST` | `https://{accountName}.vtexcommercestable.com.br/api/payments/pub/transactions/{{transactionId}}/payments` |
| `POST` | `https://{accountName}.vtexcommercestable.com.br/api/payments/pvt/transactions/{{transactionId}}/payments` |

## What has changed?

Previously, merchants could use one of the following endpoints to forward payment information to VTEX:

|  METHOD  |                                                                                                                            ROUTES                                                                                                                            |
| :------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| `POST` |   [2.1 Send payments information public](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/pub/transactions/-transactionId-/payments) `https://{accountName}.vtexpayments.com.br/api/pub/transactions/{transactionId}/payments`   |
| `POST` | [2.2 Send payments with saved credit card](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/pvt/transactions/-transactionId-/payments) `https://{accountName}.vtexpayments.com.br/api/pvt/transactions/{transactionId}/payments` |
| `POST` |                                                                         `https://{accountName}.vtexcommercestable.com.br/api/payments/pub/transactions/{transactionId}/payments`                                                                         |
| `POST` |                                                                         `https://{accountName}.vtexcommercestable.com.br/api/payments/pvt/transactions/{transactionId}/payments`                                                                         |

From **April 1, 2025**, the VTEX Payments Gateway API will only accept requests made through the endpoints [2.1 Send payments information public](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/pub/transactions/-transactionId-/payments) and [2.2 Send payments with saved credit card](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/pvt/transactions/-transactionId-/payments).

> ⚠️ Requests made via deprecated routes will be blocked, preventing the creation of the payment transaction and interrupting the purchase order flow. In this scenario, the message with status code 403 will be displayed.

## What needs to be done?

Check whether any of your account's payment integrations are using the deprecated routes and make the following adjustments before **April 1, 2025**, if necessary:

|                                                     FROM                                                     |                                                                                                                              TO                                                                                                                              |
| :----------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| `https://{accountName}.vtexcommercestable.com.br/api/payments/pub/transactions/{{transactionId}}/payments` |   [2.1 Send payments information public](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/pub/transactions/-transactionId-/payments) `https://{accountName}.vtexpayments.com.br/api/pub/transactions/{transactionId}/payments`   |
| `https://{accountName}.vtexcommercestable.com.br/api/payments/pvt/transactions/{transactionId}/payments` | [2.2 Send payments with saved credit card](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/pvt/transactions/-transactionId-/payments) `https://{accountName}.vtexpayments.com.br/api/pvt/transactions/{transactionId}/payments` |
