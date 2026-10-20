---
title: "Payments Gateway error codes"
slug: "payments-gateway-error-codes"
hidden: false
createdAt: "2026-10-13T00:00:00.000Z"
updatedAt: "2026-10-13T00:00:00.000Z"
excerpt: "Reference of error codes returned by the Payments Gateway API, including HTTP status codes, the error response body, and how to handle each case."
---

This guide explains how to interpret errors returned by the [Payments Gateway API](https://developers.vtex.com/docs/api-reference/payments-gateway-api) and what your integration should do in each case.

>ℹ️ The scenarios described here are the most common ones, and this content is reviewed regularly as the platform evolves. Some responses may vary depending on the payment provider, connector, or operation. If you receive an error that isn't described here, check the `error.message` field for details, or see [Getting help](#getting-help).

Payment errors can reach your integration in two ways:

- **Directly**, when your integration calls Payments Gateway API endpoints, such as transactions, payments, settlements, refunds, and cancellations. The routes are available with the equivalent prefixes `/api/pvt/...` and `/api/payments/pvt/...`.
- **Indirectly through Checkout**, when the Checkout converts a payment failure into a Checkout error. In this case, see [Checkout error codes](https://developers.vtex.com/docs/guides/checkout-error-codes). The most common payment-related Checkout codes are listed in [Related Checkout error codes](#related-checkout-error-codes).

## How to read a payment error

Every error response has two independent pieces of information:

| Information | Where it is | What it tells you |
| --- | --- | --- |
| HTTP status code | Response status line | The broad category of the failure, such as an invalid request (`4xx`), a rate limit (`429`), or an internal failure (`500`). |
| `error.code` | Response body and `x-vtex-error-code` header | The specific reason for the failure, when one is available. |

These two values are separate and must be evaluated independently. A numeric similarity between them means nothing. For example:

- An HTTP status `429 Too Many Requests` response doesn't have an `error.code`. It's a plain-text throttling response.
- The error code `1429` is returned with HTTP status `400 Bad Request`, not `429`.

Always evaluate the HTTP status code first, and then use `error.code` and `error.message` to identify the specific cause.

## Error response format

When the Payments Gateway returns an error with a JSON body, the body has the following format:

```json
{
  "error": {
    "code": "1419",
    "message": "This transaction must have in Approved status.",
    "exception": null
  }
}
```

| Field | Type | Description |
| --- | --- | --- |
| `error` | object | Object containing the error details. |
| `error.code` | string | VTEX error code. Although the value is numeric, it's returned as a string. This is not the acquirer code and not the HTTP status code. See [Error codes](#error-codes). |
| `error.message` | string | Technical message in English describing the error. It often includes IDs and values from the request, such as the expected and received values. The text can change over time, so use it for logging and troubleshooting, not for exact string matching. |
| `error.exception` | null | Reserved for internal VTEX debugging. For integrations, it's always `null`. |

### Error headers

Error responses with this format also include the error information in the response headers, so you can handle the error without parsing the body:

| Header | Content |
| --- | --- |
| `x-vtex-error-code` | Same value as `error.code`, URL-encoded. |
| `x-vtex-error-message` | Same value as `error.message`, URL-encoded and truncated to 2048 characters. |

### Generic error code `1`

The `error.code` value `"1"` means the error wasn't mapped to a specific code. It's a generic value shared by different scenarios, so it doesn't identify a cause by itself. It usually appears in these cases:

- **HTTP status `500`**: an unexpected failure, such as an infrastructure failure or an operation timeout. The `error.message` contains the original error description.
- **HTTP status `401` or `403`**: authentication and authorization errors may return `"1"` instead of a specific code.

When you receive `"code": "1"`, use the HTTP status code to decide what to do, log the full `error.message`, and don't map `"1"` to a single meaning in your integration.

## HTTP status codes

The following HTTP status codes are returned by the Payments Gateway API in production:

| Status code | Meaning | Recommended action |
| --- | --- | --- |
| `200 OK` | The request was processed. For asynchronous payment methods, such as bank invoices, redirects, and wallets, the transaction may still be pending. | Check the returned transaction or payment status. See [Asynchronous payment failures](#asynchronous-payment-failures). |
| `400 Bad Request` | The request is invalid or the operation isn't allowed in the current state of the transaction or payment. | Check `error.code` and `error.message`, and fix the request before sending it again. See [Error codes](#error-codes). |
| `401 Unauthorized` | The credentials are missing or invalid. The body may contain `"code": "1"`. | Check the `X-VTEX-API-AppKey` and `X-VTEX-API-AppToken` headers or the user token. See [Authentication overview](https://developers.vtex.com/docs/guides/authentication-overview). |
| `403 Forbidden` | The credentials don't have access to the route or to the transaction. The body may contain `"code": "1"` or be empty. See [Responses without the error body](#responses-without-the-error-body). | Check whether the API key or user has the [License Manager resources](https://help.vtex.com/en/tutorial/license-manager-resources--3q6ztrC8YynQf6rdc6euk3) required by the endpoint, and whether the transaction belongs to the account making the request. |
| `404 Not Found` | The requested resource, such as a transaction or payment, wasn't found. | Check the IDs and the account name used in the request. |
| `405 Method Not Allowed` | The HTTP method isn't supported by the route. | Check the method in the [API reference](https://developers.vtex.com/docs/api-reference/payments-gateway-api). |
| `429 Too Many Requests` | The request was throttled because the rate limit was exceeded. | Wait for the time indicated in the `Retry-After` header before trying again. See [Rate limiting](#rate-limiting). |
| `500 Internal Server Error` | An unexpected internal error occurred. The body usually contains `"code": "1"` or a code in the `15xx` range. | Retry with exponential backoff. Before retrying operations that move money, check the transaction status. If the error persists, see [Getting help](#getting-help). |

## Responses without the error body

Some responses don't use the JSON error format described above. Make sure your integration handles responses with a plain-text or empty body.

| Scenario | HTTP status | Body |
| --- | --- | --- |
| General rate limit | `429` | Plain text starting with `gateway: max usage by`, with a `Retry-After` header. There's no `error.code`. |
| Too many retries in payment provider callbacks | `429` | Plain text `Too Many Requests`. There's no `error.code`. |
| Payment provider callback with an invalid signature | `403` | Empty. |
| Refund request (`POST /api/pvt/transactions/{transactionId}/refunding-request`) made by an account that doesn't own the transaction | `403` | Empty. The error description is sent in the HTTP reason phrase. |

>⚠️ Parse the response body as JSON only when the `Content-Type` header is `application/json`.

## Rate limiting

When your integration exceeds the request limit, the Payments Gateway returns HTTP status `429 Too Many Requests` with a plain-text body and a `Retry-After` header with the number of seconds to wait. Read operations, such as transaction queries, are the most frequently throttled.

```http
HTTP/1.1 429 Too Many Requests
Retry-After: 30

gateway: max usage by ...
```

To handle rate limits:

1. Read the `Retry-After` header and wait at least that many seconds before retrying.
2. If the header isn't present, use exponential backoff with jitter, for example, waiting 1, 2, 4, and 8 seconds between attempts.
3. Avoid polling transaction data in short intervals. Distribute batch operations over time instead of sending them in bursts.

>ℹ️ The error code `1429` is a different mechanism. It's returned with HTTP status `400` when the request rate for card tokenization is exceeded. See [Request validation errors](#request-validation-errors).

## Error codes

The tables below list the codes returned in the `error.code` field for synchronous requests. Unless stated otherwise, these codes are returned with HTTP status `400 Bad Request`.

### Transaction and payment lifecycle errors

| Error code | Meaning | Recommended action |
| --- | --- | --- |
| `1403` | The transaction couldn't be authorized because there are unauthorized payments or payments still being authorized. | Check the status of each payment in the transaction. |
| `1404` | The acquirer or issuer denied the transaction. This code is also returned when a cancellation fails in the payment connector. | Don't repeat the same attempt. Ask the shopper to use another payment method. |
| `1405` | The anti-fraud provider rejected the transaction, or the approval confirmation failed. | Check `error.message` and the anti-fraud analysis of the transaction. |
| `1408` | The cancellation wasn't completed because not all payments were canceled. | Check the payments and send the cancellation request again. |
| `1409` | The transaction can't be settled. For example, the transaction isn't approved, was already settled, has a zero value without previous settlements, or the connector refused the settlement. | Check the transaction status and the remaining value before settling. |
| `1410` | The settlement was blocked because the anti-fraud provider rejected the transaction. | Don't settle the transaction. Cancel it instead. |
| `1411` | A technical failure occurred in the communication with the acquirer. Unlike `1404`, this isn't a business denial. | Retry the request. If the error persists, contact the payment provider. |
| `1414` | The transaction was canceled by the anti-fraud validation or pre-analysis. | Check `error.message` to identify the rule that canceled the transaction. |
| `1415` | The requested transaction status change isn't allowed by the transaction workflow. | Check the current transaction status before the operation. |
| `1417` | One or more payments couldn't be refunded. | Check the payments listed in `error.message`. |
| `1418` | The transaction can't be canceled because it already has settlements. | Request a refund instead of a cancellation. |
| `1420` | The requested payment status change isn't allowed by the payment workflow. | Check the current payment status before the operation. |
| `1425` | The payment cancellation failed in the payment connector. | Check the payment status. If the cancellation keeps failing, contact the payment provider. |

### Request validation errors

| Error code | Meaning | Recommended action |
| --- | --- | --- |
| `1401` | Required data is missing from the request. | Check the identifiers and the request body. |
| `1402` | A parameter is invalid, is out of the allowed range, or refers to a resource that wasn't found. | Check `error.message`, which usually includes the expected and received values. |
| `1419` | The request is invalid for the current scenario, for example, the transaction status doesn't allow the operation or a business field is invalid. | Check `error.message` for the specific scenario. |
| `1422` | Another operation is being processed for the same transaction. | Retry with exponential backoff. |
| `1423` | The account or user doesn't have access to the transaction or route. | Check the credentials used in the request. In refund requests, this case returns an empty `403` response. |
| `1426` | The payout split was already executed. | Treat it as already completed. No action needed. |
| `1428` | The original `paymentRecipients` are missing from the split request. | Send the original payment recipients. |
| `1429` | The request rate for card tokenization was exceeded. This code is returned with HTTP status `400`, not `429`. | Reduce the request rate. |
| `1430` | The seller and payment pair doesn't exist in the original payment recipients. | Check the `sellerId` and `paymentId` values. |
| `1431` | The sum of the partial settlement values is inconsistent. | Recalculate the values for each recipient. |
| `1433` | A precondition for the operation wasn't met. | Check `error.message`. |
| `1434` | The operation requires the transaction to be locked. | Follow the standard flow for the operation. |
| `1435` | A resource required by the operation couldn't be loaded. | Retry the request. |

## Error codes by endpoint

The table below lists the error codes most commonly returned by each endpoint. All endpoints can also return `401`, `403`, and `429` responses.

| Endpoint | HTTP status | Error codes |
| --- | --- | --- |
| `POST /api/pvt/transactions` | `400` | `1402` |
| `POST /api/pvt/transactions/{transactionId}/payments` | `400`, `500` | `1419`, `1402` |
| `POST /api/pvt/transactions/{transactionId}/additional-data` | `400`, `500` | `1419`, `1402` |
| `POST /api/pvt/transactions/{transactionId}/authorization-request` | `400`, `500` | `1403`, `1404`, `1405`, `1414`, `1419`, `1402` |
| `POST /api/pvt/transactions/{transactionId}/settlement-request` | `400`, `500` | `1409`, `1402`, `1401`, `1410`, `1422` |
| `POST /api/pvt/transactions/{transactionId}/refunding-request` | `400`, `500`, `403` without body | `1402`, `1415`, `1417`, `1422` |
| `POST /api/pvt/transactions/{transactionId}/cancellation-request` | `400`, `500` | `1418`, `1402`, `1419`, `1408`, `1422` |
| `GET /api/pvt/transactions/{transactionId}` and `GET /api/pvt/transactions/{transactionId}/payments` | `400`, `403`, `404`, `429`, `500` | `1402`, `1401`. Responses `401` and `403` may return `"1"`. |
| `POST /api/pvt/payments/{paymentSystemId}/sessions` and card tokenization | `400` | `1402`, `1429` |

## Acquirer and issuer codes

The `error.code` field always contains a VTEX code, never the original code from the acquirer or issuer. To find out why a payment was denied by the acquirer, check the transaction details in the VTEX Admin, where the original code and message returned by the provider are recorded, or contact the payment provider.

## Asynchronous payment failures

Payment methods with asynchronous confirmation, such as bank invoices, redirects, and wallets, return HTTP status `200 OK` with the transaction pending. If the payment fails later, the failure isn't returned as an HTTP error. Instead, it appears in the transaction status.

For these payment methods, monitor the transaction status instead of relying only on the HTTP response of the request.

## Related Checkout error codes

When a payment fails during the purchase flow, the error usually reaches the shopper or your integration as a Checkout error. These are the payment-related codes from the [Checkout error codes](https://developers.vtex.com/docs/guides/checkout-error-codes) guide:

| Error code | Message | Meaning |
| --- | --- | --- |
| **CHK002** | "The endpoint to gateway has not been provided" | Gateway authentication error. |
| **CHK004** | "There is no active transaction for current payment" | Error creating and activating payment transaction. |
| **CHK007** | "There isn't any payment system available" | There are no payment methods available. |
| **CHK0012** | "A communication error with gateway has occurred and the payment data for transaction {0} not successfully received" | There was a communication error with the gateway, and the payment data for transaction {0} was not correctly received. |
| **CHK0016** | "Payment value does not match with reference value" | Payment value does not match the reference value. |
| **CHK0019** | "Please select the desired number of installments" | Unable to determine the number of installments for the payment method. |
| **CHK0044** | "A communication error with installments has occurred" | Unable to get purchase installment options. |
| **CHK0076** | "A communication error with payment system has occurred" | There was a communication error to obtain payment data. |
| **CHK0080** | "Maximum amount of denied transactions reached. Please, try again in 24 hours." | Maximum number of denied transactions reached. Please try again in 24 hours. |
| **CHK0115** | "Current transaction is inactive and cannot be processed" | The current transaction is inactive and cannot be processed. |
| **CHK0237** | "Inconsistency detected in order {0}, transaction {1}" | There are inconsistencies between the receipts and the operations carried out with the gateway. |
| **CHK0265** | "A communication error with gateway has occurred" | There was a communication error with the Payment Gateway. |

>ℹ️ Gift card errors, such as `CHK0021`, `CHK0114`, and `CHK0133`, are also listed in the [Checkout error codes](https://developers.vtex.com/docs/guides/checkout-error-codes) guide.

## Best practices for handling payment errors

- **Decide on retries by HTTP status.** Retry `429` and `500` responses with backoff. Don't retry `400` responses without changing the request, except for `1411`, `1422`, and `1435`, which indicate temporary conditions.
- **Check the transaction status before retrying.** After a timeout or `500` response on an operation that moves money, such as authorization, settlement, or refund, query the transaction first. The operation may have been completed even if your integration didn't receive the response.
- **Read errors from the headers when the body is unavailable.** Use the `x-vtex-error-code` and `x-vtex-error-message` headers, and handle plain-text and empty bodies.
- **Log enough context.** Store the endpoint, HTTP status code, `error.code`, `error.message`, transaction ID, and timestamp for every failed request.
- **Don't show raw error messages to shoppers.** Map errors to user-friendly messages in your interface and keep technical details in your logs.

## Getting help

If an error persists, especially `500` responses, open a ticket with [VTEX Support](https://help.vtex.com/en/support) and include:

- Account name.
- Transaction ID and payment ID, when available.
- Endpoint and HTTP method.
- Request timestamp, including the time zone.
- HTTP status code and full response body, or the `x-vtex-error-code` and `x-vtex-error-message` headers.
