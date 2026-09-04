---
title: "Metadata information in payment transactions"
slug: "metadata-information-in-payment-transactions"
excerpt: "Learn how a payment provider stores custom metadata in the VTEX payment gateway using the Payment Provider Protocol."
hidden: false
createdAt: "2024-04-16T00:00:00.691Z"
updatedAt: "2026-09-04T00:00:00.000Z"
---

Payment providers can use [Payment Provider Protocol](https://developers.vtex.com/docs/api-reference/payment-provider-protocol) (PPP) endpoints to record additional information they consider essential for processing a transaction. This information can include data related to orders or other platform modules, payment identifiers created by the provider, and internal operation logs.

To use this feature, declare the metadata fields in the provider manifest and return their values in the PPP endpoint responses.

## Before you begin

Make sure you meet the following requirements:

| Requirement | Description |
| ----------- | ----------- |
| Payment provider integration | You must have a payment provider implemented according to the [Payment Provider Protocol](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-protocol). |
| Manifest endpoint | Your provider must expose the [List Payment Provider Manifest](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#get-/manifest) endpoint, as VTEX reads the metadata field names from it. |
| Field planning | Define which metadata fields you need in advance, respecting the limits described in [Metadata field limits](#metadata-field-limits). |

## Metadata field limits

The following table describes the limits that apply to metadata fields:

| Item | Limit |
| ---- | ----- |
| Number of fields declared in `metadataFields` | Maximum of 3 strings |
| Length of each name in `metadataFields` | Maximum of 20 characters |
| Length of `connectorMetadata[].name` | Maximum of 20 characters |
| Length of `connectorMetadata[].value` | Maximum of 200 characters |

> ⚠️ Validate these limits in your integration before sending the data to VTEX. The PPP schema documents the limits as descriptions, so they aren't enforced by schema validation.

## Adding metadata information to your payment transactions

To use metadata in your payment transactions, follow these instructions:

1. Update the provider manifest to include the `metadataFields` array, which declares the names of the metadata fields your provider sends to VTEX.

    ```json
    ...
    "metadataFields": [
        "MetadataName1",
        "MetadataName2"
    ]
    ...
    ```

2. Return the `connectorMetadata` array in the response body of the endpoints where you want to record metadata:

    - [Create payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments)
    - [Cancel payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/cancellations)
    - [Settle payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/settlements)
    - [Refund payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/refunds)
    - [Inbound request (BETA)](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/inbound/-action-)

    Each item of the array must contain the following required fields:

    | Field | Type | Description |
    | ----- | ---- | ----------- |
    | `name` | string | Name of the metadata field, which must match one of the names declared in the `metadataFields` array of the provider manifest. Limited to 20 characters. |
    | `value` | string | Content of the metadata to be stored in the payment gateway. Limited to 200 characters. |

    See the following example of a `connectorMetadata` array:

    ```json
    ...
    "connectorMetadata": [
        {
            "name": "MetadataName1",
            "value": "MetadataValue1"
        },
        {
            "name": "MetadataName2",
            "value": "MetadataValue2"
        }
    ]
    ...
    ```

When VTEX receives your response, it stores the metadata in the payment gateway. The following example shows the response body of the [Refund payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/refunds) endpoint returning the payment and metadata information.

```json
{
    "paymentId": "F5C1A4E20D3B4E07B7E871F5B5BC9F91",
    "refundId": "2EA354989E7E4BBC9F9D7B66674C2574",
    "value": 57,
    "code": null,
    "message": "Successfully refunded",
    "requestId": "LA4E20D3B4E07B7E871F5B5BC9F91",
    "connectorMetadata": [
        {
            "name": "MetadataName1",
            "value": "MetadataValue1"
        },
        {
            "name": "MetadataName2",
            "value": "MetadataValue2"
        }
    ]
}
```

## Retrieving stored metadata

The `connectorMetadata` array is also part of the request schema of the [Create payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments), [Cancel payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/cancellations), [Settle payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/settlements), [Refund payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/refunds), and [Inbound request (BETA)](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/inbound/-action-) endpoints. This means the metadata stored for a payment can be sent back to your provider in the requests VTEX makes for subsequent operations on that payment.

> ℹ️ The [Payments Gateway API](https://developers.vtex.com/docs/api-reference/payments-gateway-api) doesn't expose an endpoint for reading `connectorMetadata`. Metadata is available to your provider through the PPP request and response bodies described in this article.

## Next steps

- [Payment Provider Protocol](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-protocol): Learn about the endpoints your provider must implement.
- [Payment provider homologation](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-homologation): Test and validate your provider before going live.
- [Implementing a payment provider](https://developers.vtex.com/docs/guides/payments-integration-implementing-a-payment-provider): See the full integration flow.
