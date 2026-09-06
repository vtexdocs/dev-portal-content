---
title: "PPP versioning"
slug: "ppp-versioning"
excerpt: "Learn how to set the Payment Provider Protocol version used by your payment connector to enable additional features."
hidden: false
createdAt: "2025-12-18T00:00:00.000Z"
updatedAt: "2026-09-04T00:00:00.000Z"
---

The [Payment Provider Protocol](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-protocol) (PPP) is the integration protocol between VTEX and payment processing partners. To enable new features without impacting existing operations, VTEX offers PPP versioning, which gives providers the flexibility to configure their connectors according to the solutions they want to offer.

> ⚠️ This feature is currently in the testing phase (Closed Beta), which means that only select clients can access it. If you'd like to implement it in the future, contact our [Support](https://help.vtex.com/docs/tutorials/opening-tickets-to-vtex-support).

VTEX approves all payment connectors using PPP version `1.0.0`, which corresponds to the standard protocol behavior. Declare the `version` field in the manifest only if you want to adopt a version with additional features.

## Before you begin

Make sure you meet the following requirements:

| **Requirement** | **Description** |
| --- | --- |
| Payment provider integration | You must have a payment connector approved by VTEX and implemented according to the [Payment Provider Protocol](https://developers.vtex.com/docs/api-reference/payment-provider-protocol). |
| Closed Beta access | PPP versioning is restricted to select clients. Contact [VTEX Technical Support](https://help.vtex.com/docs/tutorials/opening-tickets-to-vtex-support) to request access. |
| Version requirements | Check the additional fields required by the version you want to adopt, as described in [Features of PPP versions](#features-of-ppp-versions). Some versions require new fields in the manifest or in specific endpoints. |

## Configuring PPP versioning

To define the PPP version used for payment connector transactions, follow these instructions:

1. Update the connector manifest by adding the `version` field with the desired version number, such as `2.0.0`.

    ```json
    {
    ...
      "version": "2.0.0",
    ...
    }
    ```

2. Open a ticket with [VTEX Technical Support](https://help.vtex.com/docs/tutorials/opening-tickets-to-vtex-support) to request the connector update. In the ticket, include the account name, the connector name, and the PPP version declared in the manifest.

> ℹ️ VTEX applies the new version only after the connector update is processed. Until then, the connector keeps operating on its current version.

To return a connector to the standard PPP behavior, change the `version` field back to `1.0.0` and open a new ticket requesting the connector update.

## Features of PPP versions

The following table describes the additional features available in each PPP version:

| **PPP version** | **Feature** | **Description** |
| --- | --- | --- |
| `1.0.0` | Standard protocol behavior | Default version applied to all approved payment connectors. It requires no additional fields in the manifest. |
| `2.0.0` | [Payment tokenization](https://developers.vtex.com/docs/guides/implementing-payments-tokenization) | Allows you to manage credit card token information, increasing security in the storage and transmission of sensitive payment data. It requires the `cardToken` object in the manifest, as described in [Updating the connector manifest](https://developers.vtex.com/docs/guides/implementing-payments-tokenization#updating-the-connector-manifest). |

## Next steps

- [Implementing payments tokenization](https://developers.vtex.com/docs/guides/implementing-payments-tokenization): Set up the manifest fields and endpoints required by version `2.0.0`.
- [Payment Provider Protocol](https://developers.vtex.com/docs/api-reference/payment-provider-protocol): Check the endpoint reference for your connector.
