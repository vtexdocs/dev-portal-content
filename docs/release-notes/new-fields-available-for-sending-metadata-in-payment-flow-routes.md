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

See where each field was added:

| Field   | Endpoints    |
| ---------- | ---------- |
| `metadataFields`       | <ul><li><a href="https://developers.vtex.com/docs/api-reference/payment-provider-protocol#get-/manifest">List Payment Provider Manifest</a></li></ul>     |
| `connectorMetadata`       | <ul><li><a href="https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments">Create Payment</a></li><li><a href="https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/cancellations">Cancel Payment</a></li><li><a href="https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/settlements">Settle Payment</a></li><li><a href="https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/refunds">Refund Payment</a></li><li><a href="https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments/-paymentId-/inbound/-action-">Inbound Request (BETA)</a></li></ul>      |

## What needs to be done?

To check the steps required to insert metadata into your transactions, access [Metadata information in payment transactions](https://developers.vtex.com/docs/guides/metadata-information-in-payment-transactions).