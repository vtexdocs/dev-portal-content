---
title: "Custom Auto Capture Feature"
slug: "custom-auto-capture-feature"
hidden: false
createdAt: "2021-12-17T11:45:14.279Z"
updatedAt: "2021-12-17T11:49:15.923Z"
---

Merchants need flexibility when receiving their payments according to the characteristics and restrictions of their business.

The VTEX platform allows payment providers to implement a feature that gives merchants the possibility to set a custom delay interval for automatic payment capture.
[block:callout]
{
  "type": "warning",
  "body": "If you noticed that the fields indicated in this article are not available to your connector, please submit a request to VTEX to update the connector."
}
[/block]

## Setting up Custom Auto Capture

To manage which auto-capture options are available in the connector, the payment provider has access to two fields:

1. **useAutoSettleOptions**: provides options of capture for merchants. This field must be set to “true” in the provider’s connector to allow merchants to access the **Payment capture** field in the VTEX Admin.

The **Payment capture** field is composed of the following options:

  - **Use Behavior Recommended By The Payment Processor**: Capture is not automatic; it is scheduled according to the period specified by the acquirer. The acquirer indicates whether the payment has been authorized and can determine or recommend a number of days for the capture upon payment authorization. (This is the platform's default behavior).
  - **Automatic Capture Immediately After Payment Authorization**: Capture is automatically performed right after payment authorization, even if the transaction includes an anti-fraud analysis.
  - **Automatic Capture Immediately After Anti-fraud Analysis**: Capture is automatically performed right after payment authorization and anti-fraud analysis. If you select this behavior and do not have anti-fraud analysis, the system will perform the payment capture as in *Automatic Capture Immediately After Payment Authorization*.
  - **Scheduled: Schedules The Automatic Capture**: By selecting this option, the field **Scheduled time frame in hours for automatic capture** will be displayed, and it must be completed with the period in which the automatic capture will take place. This period must be in accordance with the limits allowed by the payment provider.
  - **Deactivated: Not Automatically Captured**: Capture takes place only when the order is invoiced. If you select this behavior, it is important to pay attention to the invoicing time, as invoicing can exceed the capture time agreed with the payment provider and lead to the cancellation of the transaction.

[block:callout]
{
  "type": "warning",
  "body": "Enable the `useAutoSettleOptions` will override any other behavior available for the  `earlySecurityCapture`."
}
[/block]

2. **autoSettleDelay**: provides a customized capture option for merchants based on hourly intervals. The “minimum” and “maximum” interval values must be defined by the provider in their manifest.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@readme-docs/docs/guides/Integration%20Guides/payments-integration-guide/efb0672-autoSettleDelay_illustration_36.JPG)
When the `useAutoSettleOptions` field is enabled in the provider’s connector (set to “true”) and the `autoSettleDelay` field is set in the provider’s manifest, the **“Scheduled: Schedules The Automatic Capture”** option will be available in the **Payment capture** field when configuring a gateway on the VTEX Admin.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@readme-docs/docs/guides/Integration%20Guides/payments-integration-guide/210021b-payment_capture_installation_39.JPG)
After selecting this option, a new field **“Scheduled time frame in hours for automatic capture”** will be displayed. This field is used by the merchant to set the capture time.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@readme-docs/docs/guides/Integration%20Guides/payments-integration-guide/94f24fc-schedule_time_installation_42.JPG)

[block:callout]
{
  "type": "warning",
  "body": "The merchant can set the capture time only within the range set by the payment provider within their manifest. Its value must be set by the merchant in whole hours (decimals are not allowed)."
}
[/block]
