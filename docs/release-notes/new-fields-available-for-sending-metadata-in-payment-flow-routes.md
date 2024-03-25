---
title: "New fields available for sending metadata in payment flow routes"
slug: "new-fields-available-for-sending-metadata-in-payment-flow-routes"
type: "added"
excerpt: "Two new fields available in Payment Provider Protocol endpoints."
createdAt: "2024-03-25T00:00:00.000Z"
updatedAt: "2024-03-25T00:01:00.000Z"
---

Two new fields are now available in [Payment Provider Protocol API](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#overview) requests.


## What has changed?

The `metadataFields` and `connectorMetadata` were added to the [Payment Provider Protocol API](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#overview) endpoints to allow the provider to send metadata information in payment transactions carried out at the VTEX gateway.

The following endpoints have been updated to add these parameters:

- `metadataFields`: [List Payment Provider Manifest](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#get-/manifest)
- `connectorMetadata`: [Create Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments), [Cancel Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/cancellations), [Settle Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/settlements), [Refund Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/refunds) and [Inbound Request (BETA)](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/inbound/-action-).



## What needs to be done?

To use metadata in the provider's payment transactions, follow the steps below:

1. Update the provider manifest to include the `metadataFields` array and forward it to VTEX. This array must contain a maximum of 3 strings, each with a maximum length of 20 characters, which will represent the names of the metadata fields to be sent by the provider. See an example below:

```json
...
"metadataFields": [
        "MetadataName1",
        "MetadataName2"
    ]
...
```

2. Add the `connectorMetadata` array to the request body of the following endpoints ([Create Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments), [Cancel Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/cancellations), [Settle Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/settlements), [Refund Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/refunds) and [Inbound Request (BETA)](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/inbound/-action-)). The array must contain the following information:

    - `name`: string that identifies the name of the metadata field inserted in the provider manifest (maximum limit of 20 characters).
    - `value`: string containing the metadata (maximum limit of 200 characters).

See an example below:

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
    },
]
...
```

3. After sending one of the endpoint requests from the previous step, the response body will return the payment and metadata information, indicating that they were stored in the VTEX gateway. See an example of the response body from the [Refund Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/refunds) endpoint.


```json
{
    "paymentId": "F5C2A4E21D3B4E09B7E871F5B6BC9F91",
    "refundId": "2EA324981E7E4BCC9F9D7B46874C2594",
    "value": 57,
    "code": null,
    "message": "Successfully refunded",
    "requestId": "LB4E40D3B4G07B7B871F5B4BC3F31",
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
