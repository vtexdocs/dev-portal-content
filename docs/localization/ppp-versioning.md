---
title: "PPP Versioning"
slug: "ppp-versioning"
hidden: false
createdAt: "2025-12-01T00:00:00.00Z"
---

The [Payment Provider Protocol (PPP)](https://help.vtex.com/docs/tutorials/payment-provider-protocol) is the integration protocol between VTEX and payment processing partners. To enable new features without impacting existing operations, VTEX offers PPP versioning, giving providers flexibility to configure their connectors according to the solutions they want to offer.

> ⚠️ This feature is currently in the testing phase (Closed Beta), which means that only select clients can access it. If you'd like to implement it in the future, contact our [Support](https://support.vtex.com/hc/en-us/).

## Configuring PPP Versioning

Follow the steps below to define the PPP version used for payment connector transactions:

1. Update the connector manifest by adding the `version` field with the desired version number (example: `2.0.0`).
2. Ask [VTEX Technical Support](https://help.vtex.com/docs/tutorials/opening-tickets-to-vtex-support) to update the manifest on VTEX.

> ⚠️ Before updating the manifest to a new version of PPP, check the additional requirements for that version. Some versions may require new fields in specific endpoints to support extra features.

Example manifest configured for version `2.0.0`:

```json
{
…
  "version": "2.0.0",
…
}
```

> ⚠️ All payment connectors are automatically approved by VTEX using PPP version `1.0.0`. If the payment provider isn't interested in offering additional features, there's no need to include the `version` field in the manifest. If the connector has already been updated (for example, to version `2.0.0`) and the provider wants to return to the standard PPP behavior, change the `version` field back to `1.0.0` and ask VTEX Technical Support for a new connector update.

## Configuring PPP Versioning

The table below shows the additional features available in each PPP version configured in the payment connector:

| **PPP versioning** | **Feature** | **Description** |
| --- | --- | --- |
| 2.0.0 | [Payment tokenization](TBD) | Allows you to manage credit card token information, increasing security in the storage and transmission of sensitive payment data. |
