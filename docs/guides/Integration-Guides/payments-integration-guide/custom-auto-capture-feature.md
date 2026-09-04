---
title: "Custom Auto Capture Feature"
slug: "custom-auto-capture-feature"
excerpt: "Learn how payment providers enable custom automatic capture (settlement) in the connector manifest and how merchants schedule the settlement time frame in the VTEX Admin."
hidden: false
createdAt: "2021-12-17T11:45:14.279Z"
updatedAt: "2026-08-25T00:00:00.000Z"
---

Merchants need flexibility to receive payments according to the characteristics and restrictions of their business. VTEX allows payment providers to offer merchants a custom delay interval for automatic payment settlement.

Setting up this feature involves two roles:

- **Payment providers** declare support for the feature in the connector manifest and define the range of delays merchants can choose from.
- **Merchants** select the settlement behavior for that provider in the VTEX Admin.

> ℹ️ VTEX [replaced the term capture with settlement](https://help.vtex.com/en/announcements/2022-06-30-replacing-the-term-capture-for-settlement-in-the-payments-documentation) throughout the Payments documentation. Some identifiers keep the previous term, such as `usesEarlySecurityCapture`.

## Before you start

Check the following requirements according to your role:

- **Payment providers:** your connector must be integrated through the [Payment Provider Protocol](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-protocol), so that you can edit the manifest returned by the [Get manifest](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#get-/manifest) endpoint. For connectors built as VTEX IO apps, edit the `manifest.json` file of the app, as described in [Payment Provider Framework](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-framework).
- **Merchants:** the payment provider must already be registered in your store, as described in [Registering gateway affiliations](https://help.vtex.com/en/docs/tutorials/registering-gateway-affiliations).

> ⚠️ If the fields described in this guide are unavailable for your connector, [open a ticket to VTEX support](https://help.vtex.com/en/docs/tutorials/opening-tickets-to-vtex-support) requesting the connector update.

## Provider setup

To control which settlement options merchants can use, declare the following fields in the connector manifest:

| Field | Type | Description |
| ----- | ---- | ----------- |
| `usesAutoSettleOptions` | Boolean | When set to `true`, the **Payment settlement** field becomes available to merchants in the provider configuration in the VTEX Admin. When set to `false` or omitted, the VTEX Admin doesn't display this field. |
| `autoSettleDelay` | Object | Range of delays merchants can schedule, declared with the `minimum` and `maximum` properties. Both properties are required, and their values are strings expressed in whole hours. |

The following example declares a provider that accepts scheduled settlement between 0 and 720 hours:

```json
{
  "paymentMethods": [
    {
      "name": "Visa",
      "allowsSplit": "onAuthorize"
    }
  ],
  "usesAutoSettleOptions": true,
  "autoSettleDelay": {
    "minimum": "0",
    "maximum": "720"
  }
}
```

> ⚠️ Declare `minimum` and `maximum` as strings representing whole hours, as decimals are not allowed. Declaring them as numbers makes the manifest validation fail.

> ⚠️ Enabling `usesAutoSettleOptions` overrides any behavior set for the `usesEarlySecurityCapture` field.

### Relationship with the authorization response

The manifest defines the range merchants can choose from, while the authorization response of the [Create payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments) endpoint defines the delay applied to an individual payment. These fields use different units:

| Field | Where it is declared | Unit |
| ----- | -------------------- | ---- |
| `autoSettleDelay` | Connector manifest | Whole hours, as a string |
| `delayToAutoSettle` | Authorization response | Seconds, limited to `604800` (7 days) |
| `delayToAutoSettleAfterAntifraud` | Authorization response | Seconds |

When the merchant schedules a time frame in the VTEX Admin, that value takes precedence over the `delayToAutoSettle` value returned in the authorization response.

## Merchant configuration

1. In the VTEX Admin, go to **Store Settings > Payments > Providers**, or type **Providers** in the search bar at the top of the page.
2. Select the payment provider you want to configure.
3. In the **Automatic settlement** field, select one of the following options:

| Option | Behavior |
| ------ | -------- |
| **Use behavior recommended by the payment processor** | Settlement is not automatic. It follows the period specified by the acquirer, which indicates whether the payment was authorized and can recommend a number of days for settlement. This is the default behavior of the platform. |
| **Automatic capture after payment authorization** | Settlement happens right after payment authorization, even if the transaction includes an anti-fraud analysis. |
| **Automatic capture after anti-fraud analysis** | Settlement happens after payment authorization and anti-fraud analysis. Without an anti-fraud analysis, the platform settles the payment right after authorization. |
| **Disabled** | Settlement happens only when the order is invoiced. Consider your invoicing time, because it can exceed the settlement time agreed with the payment provider and lead to the cancellation of the transaction. |
| **Scheduled: Schedules the automatic capture** | Settlement happens after the time frame you define, within the range declared by the payment provider. |

![Payment settlement field in the provider configuration in the VTEX Admin, displaying the available automatic settlement options.](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/custom-auto-capture-feature-0.JPG)

4. If you select **Scheduled: Schedules the automatic capture**, fill in the **Scheduled time frame in hours for automatic capture** field with the period the platform must wait before settling the payment.

![Scheduled time frame in hours for automatic settlement field, displayed after selecting the scheduled option.](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/custom-auto-capture-feature-2.JPG)

5. Save the configuration.

> ⚠️ Set the time frame in whole hours and within the range declared by the payment provider in the manifest. Decimals are not allowed.


## Learn more

- [Payment Provider Framework](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-framework)
- [Payment Provider Protocol](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-protocol)
- [Configuring maximum automatic payment settlement time frame](https://help.vtex.com/en/docs/tutorials/configuring-maximum-automatic-payment-settlement-time-frame)
